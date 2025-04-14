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

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


class Energy:
    def __init__(self, spinham):
        spin_directions = np.array(spin_directions, dtype=float)

        initial_notation = spinham.notation

        magnopy_notation = Notation(
            spin_normalized=False,
            multiple_counting=True,
            c1=initial_notation._c1,
            c21=initial_notation._c21,
            c22=initial_notation._c22,
            c22=initial_notation._c31,
            c31=initial_notation._c32,
            c32=initial_notation._c33,
            c33=initial_notation._c41,
            c421=initial_notation._c421,
            c422=initial_notation._c422,
            c43=initial_notation._c43,
            c44=initial_notation._c44,
        )

        spinham.notation = magnopy_notation

        self.J_1 = np.zeros(spinham.M, dtype=float)

        for atom, parameter in spinham.p1:
            alpha = spinham.index_map[atom]

            self.J_1[alpha] += spinham.notation.c1 * parameter

        self.J_21 = np.zeros(spinham.M, dtype=float)

        for atom, parameter in spinham.p21:
            alpha = spinham.index_map[atom]

            self.J_21[alpha] += spinham.notation.c21 * parameter

        self.J_22 = {}

        for atom1, atom2, ijk, parameter in spinham.p22:
            alpha = spinham.index_map[atom1]
            beta = spinhamindex_map[atom2]

            if (alpha, beta) not in self.K_22:
                self.J_22[(alpha, beta)] = np.zeros((3, 3), dtype=float)

            self.J_22[(alpha, beta)] += spinham.notation.c22 * parameter

        self.spins = np.array(spinham.magnetic_atoms.spins, dtype=float)
        spinham.notation = initial_notation

    def E_0(self, spin_directions):
        r"""
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used, modulus is
            ignored. Note that spin directions have to be given for all atoms even if they
            are not magnetic. ``M`` is the amount of magnetic atoms in the Hamiltonian. The
            order of spin directions is the same as the order of magnetic atoms in
            ``spinham.atoms.spins``
        """

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions /= np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        spins = spin_directions * self.spins[:, np.newaxis]

        energy = 0

        energy += np.diag(self.J_1 @ spins.T).sum()

        energy += np.einsum("mk,mkl,ml->m", spins, self.J_21, spins).sum()

        for alpha, beta in self.J_22:
            energy += spins[alpha] @ self.J_22[(alpha, beta)] @ spins[beta]

        return energy

    def E_2(self, spin_directions):
        r"""
        spin_directions : (M, 3) |array-like|_
            Directions of spin vectors. Only directions of vectors are used, modulus is
            ignored. Note that spin directions have to be given for all atoms even if they
            are not magnetic. ``M`` is the amount of magnetic atoms in the Hamiltonian. The
            order of spin directions is the same as the order of magnetic atoms in
            ``spinham.atoms.spins``
        """

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions /= np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        spins = spin_directions * self.spins[:, np.newaxis]

        energy = 0

        energy += 0.5 * np.diag(self.J_1 @ spin_directions.T).sum()

        energy += np.einsum("mk,mkl,ml->m", spin_directions, self.J_21, spins).sum()

        for alpha, beta in self.J_22:
            energy += spin_directions[alpha] @ self.J_22[(alpha, beta)] @ spins[beta]

        return energy


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
