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


from math import sqrt

import numpy as np

from magnopy._diagonalization import solve_via_colpa
from magnopy.bosons._local_rf import span_local_rfs
from magnopy.spinham._notation import Notation

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


class MagnonDispersion:
    r"""

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
    """

    def __init__(self, spinham, spin_directions):
        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions /= np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

        self.spins = spinham.magnetic_atoms.spins

        initial_notation = spinham.notation

        magnopy_notation = initial_notation.get_modified(
            spin_normalized=False, multiple_counting=True
        )

        spinham.notation = magnopy_notation

        self.M = spinham.M
        self._J = np.zeros(self.M, dtype=complex)

        self._J_A = {}
        self._J_B = {}

        self._r_nu = {}

        # One spin & one site
        for atom, parameter in spinham.p1:
            alpha = spinham.index_map[atom]

            self._J[alpha] += -0.5 * spinham.notation.c1 * (parameter @ z[alpha])

        # Two sites & one spin
        for atom, parameter in spinham.p21:
            alpha = spinham.index_map[atom]

            self._J[alpha] += (
                -spinham.notation.c21
                * spinham.atoms.spins[alpha]
                * (z[alpha] @ parameter @ z[alpha])
            )

            if (0, 0, 0) not in self._r_nu:
                self._r_nu[(0, 0, 0)] = np.zeros(3, dtype=float)

            if (0, 0, 0) not in self._J_A:
                self._J_A[(0, 0, 0)] = np.zeros((self.M, self.M), dtype=complex)

            if (0, 0, 0) not in self._J_B:
                self._J_B[(0, 0, 0)] = np.zeros((self.M, self.M), dtype=complex)

            self._J_A[(0, 0, 0)][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * 2
                * self.spins[alpha]
                * (p[alpha] @ parameter @ np.conjugate(p[alpha]))
            )

            self._J_B[(0, 0, 0)][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * 2
                * self.spins[alpha]
                * (p[alpha] @ parameter @ p[alpha])
            )

        # Two sites & two spins
        for atom1, atom2, ijk, parameter in spinham.p22:
            alpha = spinham.index_map[atom1]
            beta = spinham.index_map[atom2]

            self._J[alpha] += (
                -spinham.notation.c22
                * spinham.atoms.spins[beta]
                * (z[alpha] @ parameter @ z[beta])
            )

            if ijk not in self._r_nu:
                self._r_nu[ijk] = ijk @ spinham.cell

            if ijk not in self._J_A:
                self._J_A[ijk] = np.zeros((self.M, self.M), dtype=complex)

            if ijk not in self._J_B:
                self._J_B[ijk] = np.zeros((self.M, self.M), dtype=complex)

            self._J_A[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * 2
                * sqrt(self.spins[alpha] * self.spins[beta])
                * (p[alpha] @ parameter @ np.conjugate(p[beta]))
            )

            self._J_B[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * 2
                * sqrt(self.spins[alpha] * self.spins[beta])
                * (p[alpha] @ parameter @ p[beta])
            )
        spinham.notation = initial_notation

    def A(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.

        Returns
        -------
        A_alpha_beta : (M, M) :numpy:`ndarray`
        """

        k = np.array(k)

        result = np.zeros((self.M, self.M), dtype=complex)

        result += np.diag(self._J)

        for ijk in self._J_A:
            result += self._J_A[ijk] * np.exp(-1j * (k @ self._r_nu[ijk]))

        return result

    def B(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.
        """

        k = np.array(k)

        result = np.zeros((self.M, self.M), dtype=complex)

        for ijk in self._J_B:
            result += self._J_B[ijk] * np.exp(-1j * (k @ self._r_nu[ijk]))

        return result

    def GDM(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.

        Returns
        -------
        gdm : (M, M) :numpy:`ndarray`
        """

        k = np.array(k)

        A = self.A(k=k)

        B = self.B(k=k)

        D = np.conjugate(self.A(k=-k))

        C = np.conjugate(B).T

        left = np.concatenate((A, B), axis=0)
        right = np.concatenate((C, D), axis=0)
        gdm = np.concatenate((left, right), axis=1)

        return gdm

    def omegas(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.

        Returns
        -------
        gdm : (M, M) :numpy:`ndarray`
        """

        k_plus = np.array(k)
        k_minus = -k_plus

        E_plus, G_plus = solve_via_colpa(self.GDM(k_plus))
        E_minus, G_minus = solve_via_colpa(self.GDM(k_minus))

        E_plus = E_plus[: self.M]
        E_minus = E_minus[self.M :]

        G_plus = G_plus[: self.M]
        G_minus = G_minus[self.M :]

        order_plus = np.argsort(E_plus)
        order_minus = np.argsort(E_minus)

        E_plus = E_plus[order_plus]
        E_minus = E_minus[order_minus]

        G_plus = G_plus[order_plus]
        G_minus = G_minus[order_minus]

        G_minus = np.concatenate((G_minus[:, self.M :], G_minus[:, : self.M]), axis=1)

        if not np.allclose(G_plus, np.conjugate(G_minus), atol=1e-4):
            print(k)
            # raise NotImplementedError(
            #     r"Boson modes do not match, the logic is not implemented for this case."
            # )

        return E_plus + E_minus


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
