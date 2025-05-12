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

from magnopy.spinham._notation import Notation

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


class Energy:
    r"""
    Ground state energy of the given spin Hamiltonian.

    This class is optimized for the computation of the energy for any spin
    directions for the given Hamiltonian.

    If the spin Hamiltonian is modified, then a new instance of the energy class
    should be created from it.

    Parameters
    ----------
    spinham : py:class:.SpinHamiltonian`
        Spin Hamiltonian for the calculation of energy.
    """

    def __init__(self, spinham):
        initial_notation = spinham.notation

        magnopy_notation = initial_notation.get_modified(
            spin_normalized=False, multiple_counting=False
        )

        spinham.notation = magnopy_notation

        self.spins = np.array(spinham.magnetic_atoms.spins, dtype=float)

        ########################################################################
        #                               One spin                               #
        ########################################################################

        self.J_1 = np.zeros((spinham.M, 3), dtype=float)

        for atom, parameter in spinham.p1:
            alpha = spinham.index_map[atom]

            self.J_1[alpha] += spinham.notation.c1 * parameter

        ########################################################################
        #                               Two spins                              #
        ########################################################################

        self.J_21 = np.zeros((spinham.M, 3, 3), dtype=float)

        for atom, parameter in spinham.p21:
            alpha = spinham.index_map[atom]

            self.J_21[alpha] += spinham.notation.c21 * parameter

        self.J_22 = {}

        for atom1, atom2, ijk, parameter in spinham.p22:
            alpha = spinham.index_map[atom1]
            beta = spinham.index_map[atom2]

            if (alpha, beta) not in self.J_22:
                self.J_22[(alpha, beta)] = np.zeros((3, 3), dtype=float)

            self.J_22[(alpha, beta)] += spinham.notation.c22 * parameter

        ########################################################################
        #                              Three spins                             #
        ########################################################################
        # TODO
        ########################################################################
        #                              Four spins                              #
        ########################################################################
        # TODO

        spinham.notation = initial_notation

    def E_0(self, spin_directions):
        r"""
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used,
            modulus is ignored. ``M`` is the amount of magnetic atoms in the
            Hamiltonian. The order of spin directions is the same as the order
            of magnetic atoms in ``spinham.magnetic_atoms.spins``.
        """

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions /= np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        spins = spin_directions * self.spins[:, np.newaxis]

        energy = 0

        energy += np.diag(self.J_1 @ spins.T).sum()

        energy += np.einsum("mk,mkl,ml->m", spins, self.J_21, spins).sum()

        for alpha, beta in self.J_22:
            energy += spins[alpha] @ self.J_22[(alpha, beta)] @ spins[beta]

        # TODO three and four spins

        return energy


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
