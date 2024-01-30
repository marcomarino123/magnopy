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
from magnopy.units import MILLI_ELECTRON_VOLT, MU_BOHR, TESLA

__all__ = ["Energy"]


def _ensure_theta_phi_input_shape(theta, phi, I):
    R"""
    Check that input values are consistent with each other and
    with amount of atoms in unit cell.

    Parameters
    ==========
    theta : float or (I,) or (N,) or (N,I) |array-like|_
        Polar angle or array of polar angles.
        I is an amount of atoms in the unit cell.
    phi : float or (I,) or (N,) or (N,I) |array-like|_
        Azimuthal angle or array of azimuthal angles.
        I is an amount of atoms in the unit cell.
    I : int
        Amount of atoms in unit cell.

    Return
    ======
    theta : (N,I) |array-like|_
        Polar angle or array of polar angles.
        I is an amount of atoms in the unit cell.
    phi : (N,I) |array-like|_
        Azimuthal angle or array of azimuthal angles.
        I is an amount of atoms in the unit cell.

    """

    # Make two-dimensional array out of a single number.
    if isinstance(theta, float) or isinstance(theta, float):
        theta = np.array([[theta]], dtype=float)
    # Or convert into numpy ndarray
    else:
        theta = np.array(theta, dtype=float)

    # Make two-dimensional array out of a single number.
    if isinstance(phi, float) or isinstance(phi, float):
        phi = np.array([[phi]], dtype=float)
    # Or convert into numpy ndarray
    else:
        phi = np.array(phi, dtype=float)

    # If one-dimensional arrays are given
    if len(theta.shape) == 1:
        # If there is only one atom per unit cell, then theta is interpreted as
        # an array of different trial configurations.
        if I == 1:
            # First index for configuration, second index for atom
            theta = np.array([theta]).T
        # Otherwise it is interpreted as one configuration.
        elif len(theta) != I:
            raise ValueError(
                " ".join(
                    [
                        f"{I} atoms in unit cell,",
                        f"but {len(theta)} theta angles provided",
                    ]
                )
            )
        else:
            theta = np.array([theta], dtype=float)

    # If one-dimensional arrays are given
    if len(phi.shape) == 1:
        # If there is only one atom per unit cell, then phi is interpreted as
        # an array of different trial configurations.
        if I == 1:
            # First index for configuration, second index for atom
            phi = np.array([phi]).T
        # Otherwise it is interpreted as one configuration.
        elif len(phi) != I:
            raise ValueError(
                " ".join(
                    [
                        f"{I} atoms in unit cell,",
                        f"but {len(phi)} phi angles provided",
                    ]
                )
            )
        else:
            phi = np.array([phi], dtype=float)

    # If two-dimensional arrays are given:
    if theta.shape[1] != I:
        raise ValueError(
            " ".join(
                [
                    f"{I} atoms in unit cell,",
                    f"but {theta.shape[1]} theta angles provided",
                ]
            )
        )
    if phi.shape[1] != I:
        raise ValueError(
            " ".join(
                [
                    f"{I} atoms in unit cell,",
                    f"but {phi.shape[1]} phi angles provided",
                ]
            )
        )

    # If higher dimensional arrays are given
    if len(theta.shape) > 2:
        raise ValueError(
            " ".join(
                [
                    f"Expected float or one/two dimensional array,",
                    f"got {len(theta.shape)}-dimensional array for theta.",
                ]
            )
        )

    # If higher dimensional arrays are given
    if len(phi.shape) > 2:
        raise ValueError(
            " ".join(
                [
                    f"Expected float or one/two dimensional array,",
                    f"got {len(phi.shape)}-dimensional array for phi.",
                ]
            )
        )

    # If size are not consistent
    if theta.shape[0] != phi.shape[0]:
        raise ValueError(
            " ".join(
                [
                    f"Amount of theta angles ({theta.shape[0]})"
                    f"does not match the amount of phi angles ({phi.shape[0]})"
                ]
            )
        )

    return theta, phi


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

    def ferromagnetic(self, theta, phi):
        R"""
        Computes energy of the spin Hamiltonian, assuming ferromagnetic aligment between the unit cells.

        Parameters
        ==========
        theta : float or (I,) or (N,) or (I, N) |array-like|_
            Polar angle or array of polar angles.
            I is an amount of atoms in the unit cell.
        phi : float or (I,) or (N,) or (I, N) |array-like|_
            Azimuthal angle or array of azimuthal angles.
            I is an amount of atoms in the unit cell.

        Returns
        =======
        energy : float or (N,)  :numpy:`ndarray`
            Ferromagnetic energy or array of ferromagnetic energies, depending on the type of
        """

        theta, phi = _ensure_theta_phi_input_shape(theta, phi, self.spinham.I)

        energy = 0
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index
            j = atom2.index
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
                    * np.sin(
                        theta[j]
                        * (
                            J.xx * np.cos(phi[i]) * np.cos(phi[j])
                            + J.yy * np.sin(phi[i]) * np.sin(phi[j])
                            + J.xy * np.cos(phi[i]) * np.sin(phi[j])
                            + J.yx * np.sin(phi[i]) * np.cos(phi[j])
                        )
                    )
                    + np.sin(theta[i])
                    * np.cos(theta[j])
                    * (J.xz * np.cos(phi[i]) + J.yz * np.sin(phi[i]))
                    + np.cos(theta[i])
                    * np.sin(theta[j])
                    * (J.zx * np.cos(phi[j]) + J.zy * np.sin(phi[j]))
                )
            )

        spins = np.array([atom.spin for atom in self.spinham])

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

    def antiferromagnetic_cone(self, theta, phi):
        R"""
        Computes energy of the spin Hamiltonian, assuming antiferromagnetic cone between the unit cells.

        Parameters
        ==========
        theta : float or (I,) or (N,) or (I, N) |array-like|_
            Polar angle or array of polar angles.
            I is an amount of atoms in the unit cell.
        phi : float or (I,) or (N,) or (I, N) |array-like|_
            Azimuthal angle or array of azimuthal angles.
            I is an amount of atoms in the unit cell.

        Returns
        =======
        energy : float or (N,)  :numpy:`ndarray`
            Antiferromagnetic cone energy or array of ferromagnetic energies, depending on the type of
        """

        theta, phi = _ensure_theta_phi_input_shape(theta, phi, self.spinham.I)

        energy = 0
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index
            j = atom2.index
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
                    - np.sin(theta[i])
                    * np.sin(
                        theta[j]
                        * (
                            J.xx * np.cos(phi[i]) * np.cos(phi[j])
                            + J.yy * np.sin(phi[i]) * np.sin(phi[j])
                            + J.xy * np.cos(phi[i]) * np.sin(phi[j])
                            + J.yx * np.sin(phi[i]) * np.cos(phi[j])
                        )
                    )
                )
            )

        spins = np.array([atom.spin for atom in self.spinham])

        energy += (
            MU_BOHR
            * TESLA
            * np.sum(
                spins * self.magnetic_field[2] * np.cos(theta),
                axis=0,
            )
        )

        return energy

    def spiral(self, theta, phi, q, alpha, beta):
        R"""
        Computes energy of the spin Hamiltonian, assuming antiferromagnetic cone between the unit cells.

        Parameters
        ==========
        theta : float or (I,) or (I, N) |array-like|_
            Polar angle or array of polar angles.
            I is an amount of atoms in the unit cell.
        phi : float or (I,) or (I, N) |array-like|_
            Azimuthal angle or array of azimuthal angles.
            I is an amount of atoms in the unit cell.
        q : (3,) or (N,3) |array-like|_
            Spiral phase vector.
        alpha : float or (N,) |array-like|_
            Global rotation axis polar angle.
        beta : float or (N,) |array-like|_
            Global rotation axis azimuthal angle.

        Returns
        =======
        energy : float or (N,)  :numpy:`ndarray`
            Antiferromagnetic cone energy or array of ferromagnetic energies, depending on the type of
        """

        theta, phi = _ensure_theta_phi_input_shape(theta, phi, self.spinham.I)

        if isinstance(alpha, float) or isinstance(alpha, float):
            alpha = np.array([alpha], dtype=float)
        else:
            alpha = np.array(alpha, dtype=float)
        if isinstance(beta, float) or isinstance(beta, float):
            beta = np.array([beta], dtype=float)
        else:
            beta = np.array(beta, dtype=float)

        if alpha.shape[0] != theta.shape[0]:
            raise ValueError(
                " ".join(
                    [
                        f"Amount of alpha angles ({alpha.shape[0]})"
                        f"does not match the amount of theta and phi angles ({theta.shape[0]})"
                    ]
                )
            )
        elif len(alpha.shape) > 1:
            raise ValueError(
                f"Expected float or one-dimensional array for alpha, got {len(alpha.shape)}-dimensional array."
            )
        if beta.shape[0] != theta.shape[0]:
            raise ValueError(
                " ".join(
                    [
                        f"Amount of beta angles ({beta.shape[0]})"
                        f"does not match the amount of theta and phi angles ({theta.shape[0]})"
                    ]
                )
            )
        elif len(beta.shape) > 1:
            raise ValueError(
                f"Expected float or one-dimensional array for beta, got {len(beta.shape)}-dimensional array."
            )

        q = np.array(q, dtype=float)

        if q.shape == (3,):
            pass
        elif q.shape[0] != theta.shape[0]:
            raise ValueError(
                " ".join(
                    [
                        f"Amount of q vectors ({q.shape[0]})"
                        f"does not match the amount of theta and phi angles ({theta.shape[1]})"
                    ]
                )
            )
        elif len(q.shape) > 2:
            raise ValueError(
                f"Expected one/two-dimensional array for q vector, got {len(q.shape)}-dimensional array."
            )

        energy = 0
        cosa = np.cos(alpha)
        sina = np.sin(alpha)
        cosb = np.cos(beta)
        sinb = np.sin(beta)
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        for atom1, atom2, ijk, J in self.spinham:
            i = atom1.index
            j = atom2.index
            Si = atom1.spin
            Sj = atom2.spin
            if atom1 == atom2 and ijk == (0, 0, 0):
                factor = self.spinham.on_site_factor
            else:
                factor = self.spinham.exchange_factor
            distance = self.spinham.get_distance(atom1, atom2, ijk)
            theta_m = np.einsum("nj,j->n", q, distance)
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

        energy += (
            MU_BOHR
            * TESLA
            * np.sum(
                spins * self.magnetic_field[2] * np.cos(theta),
                axis=0,
            )
        )
        return energy
