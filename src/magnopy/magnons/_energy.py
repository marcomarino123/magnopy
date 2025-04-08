# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
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


def get_classical_energy(spinham, spin_directions) -> float:
    r"""
    Computes classical energy of the given spin configuration :math:`E^{(0)}`.

    Parameters
    ----------
    spinham : :py:class:`.spinham.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored. Note that spin directions have to be given for all atoms even if they
        are not magnetic. ``M`` is the amount of magnetic atoms in the Hamiltonian. The
        order of spin directions is the same as the order of magnetic atoms in
        ``spinham.atoms.spins``

    Returns
    -------
    E : float
        Classical energy.
    """

    energy = 0
    spin_directions = np.array(spin_directions, dtype=float)

    index_mapping = spinham.magnetic_atoms
    tmp = 0
    # One spin & one site
    for atom, parameter in spinham.p1:
        tmp = spinham.notation.c1 * parameter @ spin_directions[index_mapping[atom]]

        if not spinham.notation.spin_normalized:
            tmp *= spinham.atoms.spins[atom]

        energy += tmp

    # Two spins & one site
    for atom, parameter in spinham.p21:
        tmp = (
            spinham.notation.c21
            * spin_directions[index_mapping[atom]]
            @ parameter
            @ spin_directions[index_mapping[atom]]
        )

        if not spinham.notation.spin_normalized:
            tmp *= spinham.atoms.spins[atom] ** 2

        energy += tmp

    # Two spins & two sites
    for atom1, atom2, _, parameter in spinham.p22:
        tmp = (
            spinham.notation.c22
            * spin_directions[index_mapping[atom1]]
            @ parameter
            @ spin_directions[index_mapping[atom2]]
        )

        if not spinham.notation.spin_normalized:
            tmp *= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]

        energy += tmp

    # TODO three and four spin terms

    return energy


def get_energy_correction_lswt(spinham, spin_directions) -> float:
    r"""
    Computes correction to the classical energy of the given spin configuration at the
    level of LSWT :math:`E^{(2)}`.

    Parameters
    ----------
    spinham : :py:class:`.spinham.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored. Note that spin directions have to be given for all atoms even if they
        are not magnetic. ``M`` is the amount of magnetic atoms in the Hamiltonian. The
        order of spin directions is the same as the order of magnetic atoms in
        ``spinham.atoms.spins``

    Returns
    -------
    E : float
        Correction to the  classical energy.
    """

    energy = 0
    spin_directions = np.array(spin_directions, dtype=float)

    index_mapping = spinham.magnetic_atoms
    tmp = 0
    # One spin & one site
    for atom, parameter in spinham.p1:
        tmp = (
            0.5 * spinham.notation.c1 * parameter @ spin_directions[index_mapping[atom]]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom]

        energy += tmp

    # Two spins & one site
    for atom, parameter in spinham.p21:
        tmp = (
            spinham.notation.c21
            * spin_directions[index_mapping[atom]]
            @ parameter
            @ spin_directions[index_mapping[atom]]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom]
        else:
            tmp *= spinham.atoms.spins[atom]

        energy += tmp

    # Two spins & two sites
    for atom1, atom2, _, parameter in spinham.p22:
        tmp = (
            spinham.notation.c22
            * spin_directions[index_mapping[atom1]]
            @ parameter
            @ spin_directions[index_mapping[atom2]]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom1]
        else:
            tmp *= spinham.atoms.spins[atom2]

        energy += tmp

    # TODO three and four spin terms

    return energy
