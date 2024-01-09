# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2024 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from wulfric.geometry import absolute_to_relative

from magnopy.spinham.hamiltonian import SpinHamiltonian


def vector_to_angles(vector):
    if np.allclose(vector / np.linalg.norm(vector), [0.0, 0.0, 1.0]):
        return 0, np.pi / 2
    if np.allclose(vector / np.linalg.norm(vector), [0.0, 0.0, -1.0]):
        return np.pi, np.pi / 2

    theta = np.dot(vector, [0, 0, 1])
    theta /= np.linalg.norm(vector)
    theta = np.arccos(theta)
    vector = np.array([vector[0], vector[1], 0])
    phi = np.dot(vector, [1, 0, 0])
    phi /= np.linalg.norm(vector)
    phi = np.arccos(phi)
    return theta, phi


class Energy(SpinHamiltonian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cone_axis = None
        self._spiral_vector = None
        self.mu_b = 5.7883818060e-2  # Bohr magneton in meV/T

    def copy(self):
        from copy import deepcopy

        return deepcopy(self)

    @property
    def spiral_vector(self):
        return self._spiral_vector

    @spiral_vector.setter
    def spiral_vector(self, value):
        self._spiral_vector = np.array(value) @ self.reciprocal_cell

    def __call__(
        self,
        Q=((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        H=(0, 0, 0),
        phase=(0, 0, 0),
        spiral_vector=(0, 0, 0),
    ):
        if spiral_vector is not None:
            self.spiral_vector = spiral_vector
        return self.exchange() + self.zeeman(H, Q, phase)

    def exchange(self):
        r"""
        Compute exchange energy
        """

        return (
            self.exchange_smooth()
            + self.is_r_lattice_vector(self.spiral_vector) * self.exchange_G()
            + self.is_r_lattice_vector(2 * self.spiral_vector) * self.exchange_G_half()
        )

    def exchange_smooth(self):
        energy = 0
        for atom1, atom2, (i, j, k), J in self:
            theta_a, phi_a = vector_to_angles(atom1.spin_vector)
            theta_b, phi_b = vector_to_angles(atom2.spin_vector)
            S_a = atom1.spin if not self.spin_normalized else 1
            S_b = atom2.spin if not self.spin_normalized else 1
            J_nn = J.zz
            J_minus = (J.xy - J.yx) / 2
            J_plus = (J.xx + J.yy) / 2
            d = (i, j, k) @ self.cell

            energy += (
                self.factor
                * S_a
                * S_b
                * (
                    J_nn * np.cos(theta_a) * np.cos(theta_b)
                    + np.sin(theta_a)
                    * np.sin(theta_b)
                    * (
                        J_plus * np.cos(self.spiral_vector @ d + phi_b - phi_a)
                        + J_minus * np.sin(self.spiral_vector @ d + phi_b - phi_a)
                    )
                )
            )
        return energy

    def exchange_G(self):
        energy = 0
        for atom1, atom2, (i, j, k), J in self:
            theta_a, phi_a = vector_to_angles(atom1.spin_vector)
            theta_b, phi_b = vector_to_angles(atom2.spin_vector)
            S_a = atom1.spin if not self.spin_normalized else 1
            S_b = atom2.spin if not self.spin_normalized else 1
            J_un = J.xz
            J_vn = J.yz
            J_nu = J.zx
            J_nv = J.zy

            d = (i, j, k) @ self.cell

            energy += (
                self.factor
                * S_a
                * S_b
                * (
                    np.sin(theta_a)
                    * np.cos(theta_b)
                    * (J_un * np.cos(phi_a) + J_vn * np.sin(phi_a))
                    + np.cos(theta_a)
                    * np.sin(theta_b)
                    * (
                        J_nu * np.cos(phi_b + self.spiral_vector @ d)
                        + J_nv * np.sin(phi_b + self.spiral_vector @ d)
                    )
                )
            )
        return energy

    def exchange_G_half(self):
        energy = 0
        for atom1, atom2, (i, j, k), J in self:
            theta_a, phi_a = vector_to_angles(atom1.spin_vector)
            theta_b, phi_b = vector_to_angles(atom2.spin_vector)
            S_a = atom1.spin if not self.spin_normalized else 1
            S_b = atom2.spin if not self.spin_normalized else 1
            J_minus = (J.xx - J.yy) / 2
            J_plus = (J.xy + J.yx) / 2
            d = (i, j, k) @ self.cell

            energy += (
                self.factor
                * S_a
                * S_b
                * (
                    np.sin(theta_a)
                    * np.sin(theta_b)
                    * (
                        J_minus * np.cos(self.spiral_vector @ d + phi_b + phi_a)
                        + J_plus * np.sin(self.spiral_vector @ d + phi_b + phi_a)
                    )
                )
            )
        return energy

    def is_r_lattice_vector(self, Q, eps=1e-3):
        r"""
        Check whether the Q is the lattice vector.

        Parameters
        ----------
        Q : (3,) |array-like|_
            Vector to be checked.
        eps : float
            Tolerance for the check.
        """

        Q = np.array(Q)
        Q = absolute_to_relative(Q, self.reciprocal_cell)
        return int(np.allclose(Q, np.round(Q, 0), atol=eps))

    def zeeman(self, H, Q, phase):
        r"""
        Compute Zeeman energy

        Parameters
        ----------
        H : (3,) |array-like|_
            External magnetic field vector amplitudes in units of Tesla:
            :math:`H^u, H^v, H^n`.
        Q : (3,3) |array-like|_
            External magnetic field vector periods, relative to the
            reciprocal lattice vectors. Rows are the vectors, columns are
            the components.
        phase : (3,) |array-like|_
            Phase of the external magnetic field.
        """
        H = np.array(H)
        Q = np.array(Q)
        phase = np.array(phase)
        return (
            self.zeeman_u(Q[0], H[0], phase[0])
            + self.zeeman_v(Q[1], H[1], phase[1])
            + self.zeeman_n(Q[2], H[2], phase[2])
        )

    def zeeman_n(self, Q, H, phase):
        r"""
        Compute Zeeman energy along the n axis

        Parameters
        ----------
        Q : (3,) |array-like|_
            External magnetic field vector periods, relative to the
            reciprocal lattice vectors.
        H : float
            Amplitude of the external magnetic field vector in units of Tesla.
        phase : float
            Phase of the external magnetic field in radians.
        """
        Q = np.array(Q) @ self.reciprocal_cell
        energy = 0
        for atom in self.magnetic_atoms:
            r_a = atom.position @ self.cell
            S_a = atom.spin if not self.spin_normalized else 1
            theta_a, _ = vector_to_angles(atom.spin_vector)

            energy += S_a * (
                H
                * self.is_r_lattice_vector(Q)
                * np.cos(theta_a)
                * np.cos(phase + Q @ r_a)
            )
        return energy * self.mu_b

    def zeeman_u(self, Q, H, phase):
        r"""
        Compute Zeeman energy along the u axis

        Parameters
        ----------
        Q : (3,) |array-like|_
            External magnetic field vector periods, relative to the
            reciprocal lattice vectors.
        H : float
            Amplitude of the external magnetic field vector in units of Tesla.
        phase : float
            Phase of the external magnetic field in radians.
        """
        Q = np.array(Q) @ self.reciprocal_cell
        energy = 0
        for atom in self.magnetic_atoms:
            r_a = atom.position @ self.cell
            S_a = atom.spin if not self.spin_normalized else 1
            phi_au = Q @ r_a + phase

            theta_a, phi_a = vector_to_angles(atom.spin_vector)

            energy += S_a * (
                H
                * np.sin(theta_a)
                * (
                    self.is_r_lattice_vector(Q + self.spiral_vector)
                    * np.cos(phi_au + phi_a)
                    + self.is_r_lattice_vector(Q - self.spiral_vector)
                    * np.cos(phi_au - phi_a)
                )
                / 2
            )
            return energy * self.mu_b

    def zeeman_v(self, Q, H, phase):
        r"""
        Compute Zeeman energy along the u axis

        Parameters
        ----------
        Q : (3,) |array-like|_
            External magnetic field vector periods, relative to the
            reciprocal lattice vectors.
        H : float
            Amplitude of the external magnetic field vector in units of Tesla.
        phase : float
            Phase of the external magnetic field in radians.
        """
        Q = np.array(Q) @ self.reciprocal_cell
        energy = 0
        for atom in self.magnetic_atoms:
            r_a = atom.position @ self.cell
            S_a = atom.spin if not self.spin_normalized else 1
            phi_av = Q @ r_a + phase

            theta_a, phi_a = vector_to_angles(atom.spin_vector)

            energy += S_a * (
                H
                * np.sin(theta_a)
                * (
                    self.is_r_lattice_vector(Q + self.spiral_vector)
                    * np.sin(phi_av + phi_a)
                    - self.is_r_lattice_vector(Q - self.spiral_vector)
                    * np.sin(phi_av - phi_a)
                )
                / 2
            )
        return energy * self.mu_b
