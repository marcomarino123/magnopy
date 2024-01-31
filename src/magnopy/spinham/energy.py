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
from wulfric import TORADIANS, absolute_to_relative

from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.units import MILLI_ELECTRON_VOLT, MU_BOHR, TESLA

__all__ = ["Energy"]


def _find_minimum(C, b):
    R"""

    Parameters
    ==========
    C : (...,3,3) |array-like|_
    b : (...,3) |array-like|_

    Returns
    =======
    alpha : (...) :numpy:`ndarray`
        In radians.
    beta : (...) :numpy:`ndarray`
        In radians.
    """

    if np.allclose(np.zeros(C), C):
        pass

    eigval, eigvec = np.linalg.eig(C)

    betas = np.einsum("...i,...ji->...j", b, eigvec)

    raise NotImplementedError


def _check_input_shape(angle1, angle2, I, in_degrees=True):
    R"""
    Check that input values are consistent with each other and
    with amount of atoms in unit cell.

    Parameters
    ==========
    angle1 : (I, ...) or (...) |array-like|_
        Polar angle or array of polar angles. See notes below for correct shape.
    angle2 : (I, ...) or (...) |array-like|_
        Azimuthal angle or array of azimuthal angles. See notes below for correct shape.
    I : int
        Amount of atoms in unit cell.
    in_degrees : bool, default True
        Whether angles are given in degrees or radians.

    Notes
    =====
    Shape of ``angle1`` always has to match the shape of ``angle2``.

    * If ``I = 1``
      Allows you to pass n-dimensional array of different configurations.
    * If ``I > 1``
      For both arrays first index is running over atoms in unit cell
      (i.e. ``angle1.shape[0] == I`` ``angle2.shape[0] == I``).
      Other dimensions are not restricted and corresponds to different configurations.

    Returns
    =======
    angle1 : (I, ...) :numpy:`ndarray`
        Polar angle or array of polar angles. If ``I==1``, then one dimension of
        length 1 is added at the beginning, otherwise matches
        the input dimensions of ``angle1`` and ``angle2``.
    angle2 : (I, ...) :numpy:`ndarray`
        Azimuthal angle or array of azimuthal angles. If ``I==1``, then one dimension of
        length 1 is added at the beginning, otherwise matches
        the input dimensions of ``angle1`` and ``angle2``.
    """

    # Check constrains on I
    if not isinstance(I, int):
        raise ValueError(f"Expected int, got I = {I}")
    if I < 1:
        raise ValueError(f"Expected at least one atom per unit cell, got I = {I}")

    if I == 1:
        angle1 = np.array([angle1], dtype=float)
        angle2 = np.array([angle2], dtype=float)
    else:
        angle1 = np.array(angle1, dtype=float)
        angle2 = np.array(angle2, dtype=float)

    # Check that input arrays are matching the amount of atoms per unit cell.
    if angle1.shape[0] != I:
        raise ValueError(
            f"Expected first dimension of length {I} for angle1, got {angle1.shape[0]}"
        )
    if angle2.shape[0] != I:
        raise ValueError(
            f"Expected first dimension of length {I} for angle2, got {angle2.shape[0]}"
        )

    # Check that input arrays have the same sizes.
    if angle1.shape != angle2.shape:
        raise ValueError(
            f"Expected to have matching shapes for angle1 and angle2, got {angle1.shape} != {angle2.shape}"
        )

    if in_degrees:
        angle1 *= TORADIANS
        angle2 *= TORADIANS

    return angle1, angle2


class Energy:
    R"""
    Describe total energy of given :py:class:`.SpinHamiltonian`.

    Allows one to access separate terms of it.

    Parameters
    ==========
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian.
    """

    def __init__(self, spinham: SpinHamiltonian):
        self._spinham = spinham
        self._magnetic_field = np.zeros(3, dtype=float)

    @property
    def magnetic_field(self):
        R"""
        Uniform magnetic field vector.
        Given in the same basis as the exchange Hamiltonian (xyz).

        Returns
        =======
        h : (3,) |array-like|_
            Magnetic field vector.
        """

        return self._magnetic_field

    @magnetic_field.setter
    def magnetic_field(self, new_value):
        new_value = np.array(new_value)
        if new_value.shape != (3,):
            raise ValueError(f"Magnetic field is a 3 component vector, got {new_value}")
        self._magnetic_field = new_value

    @property
    def spinham(self) -> SpinHamiltonian:
        R"""
        Spin Hamiltonian.

        Returns
        =======
        spinham : :py:class:`.SpinHamiltonian`
            Spin Hamiltonian.
        """

        return self._spinham

    @spinham.setter
    def spinham(self, new_spinham):
        if not isinstance(new_spinham, SpinHamiltonian):
            raise ValueError(
                "New spin Hamiltonian is not an instance of SpinHamiltonian class."
            )
        self._spinham = new_spinham

    def ferromagnetic(self, theta, phi, in_degrees=True):
        R"""
        Computes energy of the spin Hamiltonian, assuming ferromagnetic
        alignment between the unit cells.

        Parameters
        ==========
        theta : (I, ...) or (...) |array-like|_
            Polar angle or array of polar angles. See notes below for correct shape.
        phi : (I, ...) or (...) |array-like|_
            Azimuthal angle or array of azimuthal angles. See notes below for correct shape.
        I : int
            Amount of atoms in unit cell.
        in_degrees : bool, default True
            Whether angles are given in degrees or radians.

        Notes
        =====
        Shape of ``theta`` has to match the shape of ``phi``.

        * If ``I = 1``
          Allows you to pass n-dimensional array of different configurations.
        * If ``I > 1``
          For both arrays first index is running over atoms in unit cell
          (i.e. ``theta.shape[0] == I`` and ``phi.shape[0] == I``).

        Returns
        =======
        energy : (...) :numpy:`ndarray`
            Energy of the Hamiltonian, assuming ferromagnetic alignment between the
            unit cells. It matches matches the dimensions of the input arrays ``theta``
            and ``phi`` without the ``I`` dimension.
        """

        theta, phi = _check_input_shape(
            theta, phi, self.spinham.I, in_degrees=in_degrees
        )

        energy = np.zeros(theta.shape[1:], dtype=float)
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index - 1
            j = atom2.index - 1
            if self.spinham.spin_normalized:
                Si = 1
                Sj = 1
            else:
                Si = atom1.spin
                Sj = atom2.spin
            if atom1 == atom2 and ijk == (0, 0, 0):
                factor = self.spinham.on_site_factor
            else:
                factor = self.spinham.exchange_factor

            energy += (
                factor
                * MILLI_ELECTRON_VOLT
                * Si
                * Sj
                * (
                    J.zz * np.cos(theta[i]) * np.cos(theta[j])
                    + np.sin(theta[i])
                    * np.sin(theta[j])
                    * (
                        J.xx * np.cos(phi[i]) * np.cos(phi[j])
                        + J.yy * np.sin(phi[i]) * np.sin(phi[j])
                        + J.xy * np.cos(phi[i]) * np.sin(phi[j])
                        + J.yx * np.sin(phi[i]) * np.cos(phi[j])
                    )
                    + np.sin(theta[i])
                    * np.cos(theta[j])
                    * (J.xz * np.cos(phi[i]) + J.yz * np.sin(phi[i]))
                    + np.cos(theta[i])
                    * np.sin(theta[j])
                    * (J.zx * np.cos(phi[j]) + J.zy * np.sin(phi[j]))
                )
            )

        spins = np.array([atom.spin for atom in self.spinham.magnetic_atoms])

        energy += (
            MU_BOHR
            * TESLA
            * np.sum(
                spins
                * (
                    np.sin(theta)
                    * (
                        self.magnetic_field[0] * np.cos(phi)
                        + self.magnetic_field[1] * np.sin(phi)
                    )
                    + self.magnetic_field[2] * np.cos(theta)
                ),
                axis=0,
            )
        )

        return energy

    def antiferromagnetic_cone(self, theta, phi, q, is_relative=True, in_degrees=True):
        R"""
        Computes energy of the spin Hamiltonian, assuming antiferromagnetic
        conical alignment between the unit cells.

        Parameters
        ==========
        theta : (I, ...) or (...) |array-like|_
            Polar angle or array of polar angles. See notes below for correct shape.
        phi : (I, ...) or (...) |array-like|_
            Azimuthal angle or array of azimuthal angles. See notes below for correct shape.
        q : (3,) |array-like|_
            On contrary with the :py:attr:`.spiral` only one value of the q vector is allowed.
            Only the vectors, which fulfill :math:`\boldsymbol{q} = \boldsymbol{G}/2` condition are allowed.
        in_degrees : bool, default True
            Whether angles are given in degrees or radians.
        is_relative : bool, default=True
            Whether ``q`` is given in relative (with respect to the reciprocal cell) coordinates.

        Notes
        =====
        Shape of ``theta``  has to match the shape of ``phi``.

        * If ``I = 1``
          Allows you to pass n-dimensional array of different configurations.
        * If ``I > 1``
          For both arrays first index is running over atoms in unit cell
          (i.e. ``theta.shape[0] == I`` and ``phi.shape[0] == I``).

        Returns
        =======
        energy : (...) :numpy:`ndarray`
            Energy of the Hamiltonian, assuming antiferromagnetic conical alignment
            between the unit cells. It matches matches the dimensions of the input arrays
            ``theta`` and ``phi`` without the ``I`` dimension.
        """

        theta, phi = _check_input_shape(
            theta, phi, self.spinham.I, in_degrees=in_degrees
        )

        if not is_relative:
            q = absolute_to_relative(q, self.spinham.reciprocal_cell)

        if (
            not (np.allclose(abs(q[0]), 0) or np.allclose(abs(q[0]), 0.5))
            or not (np.allclose(abs(q[1]), 0) or np.allclose(abs(q[1]), 0.5))
            or not (np.allclose(abs(q[2]), 0) or np.allclose(abs(q[2]), 0.5))
        ):
            raise ValueError(
                f"q vector has to have components equal to 0 or 0.5 (in relative coordinates)"
                + f"got {q[0]} {q[1]} {q[2]}"
            )
        q = q @ self.spinham.reciprocal_cell

        energy = np.zeros(theta.shape[1:], dtype=float)
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index - 1
            j = atom2.index - 1
            if self.spinham.spin_normalized:
                Si = 1
                Sj = 1
            else:
                Si = atom1.spin
                Sj = atom2.spin
            if atom1 == atom2 and ijk == (0, 0, 0):
                factor = self.spinham.on_site_factor
            else:
                factor = self.spinham.exchange_factor
            d_vector = self.spinham.get_vector(atom1, atom2, ijk)
            energy += (
                factor
                * MILLI_ELECTRON_VOLT
                * Si
                * Sj
                * (
                    J.zz * np.cos(theta[i]) * np.cos(theta[j])
                    + np.sin(theta[i])
                    * np.sin(theta[j])
                    * (
                        J.xx * np.cos(phi[i]) * np.cos(phi[j] + q @ d_vector)
                        + J.yy * np.sin(phi[i]) * np.sin(phi[j] + q @ d_vector)
                        + J.xy * np.cos(phi[i]) * np.sin(phi[j] + q @ d_vector)
                        + J.yx * np.sin(phi[i]) * np.cos(phi[j] + q @ d_vector)
                    )
                )
            )

        spins = np.array([atom.spin for atom in self.spinham.magnetic_atoms])

        energy += (
            MU_BOHR
            * TESLA
            * np.sum(
                spins * self.magnetic_field[2] * np.cos(theta),
                axis=0,
            )
        )

        return energy

    def spiral(
        self, theta, phi, q, alpha=None, beta=None, is_relative=True, in_degrees=True
    ):
        R"""
        Computes energy of the spin Hamiltonian,
        assuming antiferromagnetic cone between the unit cells.

        Parameters
        ==========
        theta : (I, ...) or (...) |array-like|_
            Polar angle or array of polar angles.
            I is an amount of atoms in the unit cell.
        phi : (I, ...) or (...) |array-like|_
            Azimuthal angle or array of azimuthal angles.
            I is an amount of atoms in the unit cell.
        q : (3,) or (... ,3) |array-like|_
            Spiral phase vector.
        alpha : (...) |array-like|_, optional
            Global rotation axis polar angle.
        beta : (...) |array-like|_, optional
            Global rotation axis azimuthal angle.
        is_relative : bool, default True
            Whether q vector is given in relative coordinates
            (with respect ot the reciprocal lattice).
        in_degrees : bool, default True
            Whether angles are given in degrees or radians.

        Notes
        =====
        Shape of ``theta``, ``phi`` has to be the same. Shape of and ``alpha``,
        ``beta`` (if provided) has to match the shape of ``theta`` and ``phi``,
        apart from the first dimension of ``theta`` and ``phi`` if ``I > 1``:

        Shape of ``q`` has to match the shape of given angles, with extra
        dimension of the length 3 at the end and no dimension of ``I`` if present.

        * ``theta.shape == phi.shape``
        * ``theta.shape[0] == I`` if there is ``I > 1`` atom per unit cell
        * ``alpha.shape == beta.shape``
        * ``alpha.shape == theta.shape`` if there is one atom per unit cell
        * ``alpha.shape == theta.shape[1:]`` if there are more than one atom per unit cell
        * ``q.shape[:-1] == alpha.shape``
        * ``q.shape[-1] == 3``

        Returns
        =======
        energy : (...) :numpy:`ndarray`
            Energy of the Hamiltonian, assuming true spiral state.
        """

        theta, phi = _check_input_shape(
            theta, phi, self.spinham.I, in_degrees=in_degrees
        )

        if (alpha is None) ^ (beta is None):
            raise ValueError(
                "Either both beta and alpha has to be given or none of them."
            )
        if alpha is None and beta is None:
            C = np.zeros((*theta.shape[1:], 3, 3), dtype=float)
            b = np.zeros((*theta.shape[1:], 3), dtype=float)
            for atom1, atom2, ijk, J in self.spinham:
                i = atom1.index - 1
                j = atom2.index - 1
                if self.spinham.spin_normalized:
                    Si = 1
                    Sj = 1
                else:
                    Si = atom1.spin
                    Sj = atom2.spin
                d_vector = self.spinham.get_vector(atom1, atom2, ijk)
                theta_m = np.einsum("...j,j->...", q, d_vector)

                C += np.einsum(
                    "...,ij->...ij",
                    Si
                    * Sj
                    * (
                        np.cos(theta[i]) * np.cos(theta[i])
                        - np.sin(theta[i])
                        * np.sin(theta[j])
                        * np.cos(theta_m + phi[j] - phi[i])
                    ),
                    J.S,
                )
                b += np.einsum(
                    "...,i->...i",
                    Si
                    * Sj
                    * (
                        np.sin(theta[i])
                        * np.sin(theta[j])
                        * np.sin(theta_m + phi[j] - phi[i])
                    ),
                    J.dmi,
                )
            alpha, beta = _find_minimum(C, b)

        else:
            alpha = np.array(alpha, dtype=float)
            beta = np.array(beta, dtype=float)

            # Check that input arrays have the same sizes.
            if alpha.shape != beta.shape:
                raise ValueError(
                    f"Expected to have matching shapes for alpha and beta, got {alpha.shape} != {beta.shape}"
                )

            if in_degrees:
                alpha *= TORADIANS
                beta *= TORADIANS

        if alpha.shape != theta.shape[1:]:
            raise ValueError(
                f"Wrong shape of alpha and beta: {alpha.shape}, expected {theta.shape[1:]}"
            )

        q = np.array(q, dtype=float)

        if q.shape[:-1] != theta.shape[1:]:
            raise ValueError(
                f"Wrong shape of q: {q.shape}, expected ({', '.join(theta.shape[1:])},3)"
            )

        if is_relative:
            q = np.einsum("...i,ij->...j", q, self.spinham.reciprocal_cell)

        energy = np.zeros(theta.shape[1:], dtype=float)
        cosa = np.cos(alpha)
        sina = np.sin(alpha)
        cosb = np.cos(beta)
        sinb = np.sin(beta)
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index - 1
            j = atom2.index - 1
            if self.spinham.spin_normalized:
                Si = 1
                Sj = 1
            else:
                Si = atom1.spin
                Sj = atom2.spin
            if atom1 == atom2 and ijk == (0, 0, 0):
                factor = self.spinham.on_site_factor
            else:
                factor = self.spinham.exchange_factor
            d_vector = self.spinham.get_vector(atom1, atom2, ijk)
            theta_m = np.einsum("...j,j->...", q, d_vector)
            Dn = J.dmi[0] * cosb * sina + J.dmi[1] * sinb * sina + J.dmi[2] * cosa
            Snn = (
                J.aniso[0][0] * (cosb**2 * sina**2 - cosa**2)
                + J.aniso[1][1] * (sinb**2 * sina**2 - cosa**2)
                + 2 * J.aniso[0][1] * sinb * cosb * sina**2
                + 2 * J.aniso[0][2] * cosb * sina * cosa
                + 2 * J.aniso[0][2] * sinb * sina * cosa
            )
            energy += (
                factor
                * Si
                * Sj
                * MILLI_ELECTRON_VOLT
                * (
                    Snn
                    * (
                        costheta[i] * costheta[j]
                        - sintheta[i] * sintheta[j] * np.cos(theta_m + phi[j] - phi[i])
                    )
                    + J.iso
                    * (
                        costheta[i] * costheta[j]
                        + sintheta[i] * sintheta[j] * np.cos(theta_m + phi[j] - phi[i])
                    )
                    + Dn * sintheta[i] * sintheta[j] * np.sin(theta_m + phi[j] - phi[i])
                )
            )

        spins = np.array([atom.spin for atom in self.spinham.magnetic_atoms])

        energy += (
            MU_BOHR
            * TESLA
            * np.sum(
                spins * self.magnetic_field[2] * np.cos(theta),
                axis=0,
            )
        )
        return energy
