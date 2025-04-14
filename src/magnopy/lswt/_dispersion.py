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

from magnopy._diagonalization import solve_via_colpa
from magnopy.bosons._local_rf import span_local_rfs
from magnopy.bosons._representations import get_hp_newton
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
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    """

    def __init__(self, spinham, spin_directions, A=None, B=None):
        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions /= np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

        if A is None and B is None:
            A, B = get_hp_newton(spinham.magnetic_atoms.spins, n_max=0)

        if A is None:
            A = B

        if B is None:
            B = A

        self.repr_A = A
        self.repr_B = B

        initial_notation = spinham.notation

        magnopy_notation = Notation(
            spin_normalized=False,
            multiple_counting=True,
            c1=initial_notation._c1,
            c21=initial_notation._c21,
            c22=initial_notation._c22,
            c31=initial_notation._c31,
            c32=initial_notation._c32,
            c33=initial_notation._c33,
            c41=initial_notation._c41,
            c421=initial_notation._c421,
            c422=initial_notation._c422,
            c43=initial_notation._c43,
            c44=initial_notation._c44,
        )

        spinham.notation = magnopy_notation

        self.M = spinham.M
        self.A_zero = np.zeros((self.M, self.M), dtype=complex)

        self.J_A = {}
        self.J_B = {}
        self.J_C = {}
        self.J_D = {}

        self.r_nu = {}

        for atom, parameter in spinham.p1:
            alpha = spinham.index_map[atom]

            self.A_zero[alpha][alpha] += (
                -0.5 * spinham.notation.c1 * parameter @ z[alpha]
            )

        for atom, parameter in spinham.p21:
            if (0, 0, 0) not in self.J_A:
                self.J_A[(0, 0, 0)] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if (0, 0, 0) not in self.J_B:
                self.J_B[(0, 0, 0)] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if (0, 0, 0) not in self.J_C:
                self.J_C[(0, 0, 0)] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if (0, 0, 0) not in self.J_D:
                self.J_D[(0, 0, 0)] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if (0, 0, 0) not in self.r_nu:
                self.r_nu[(0, 0, 0)] = np.zeros(3, dtype=float)

            alpha = spinham.index_map[atom]

            self.A_zero[alpha][alpha] += (
                -spinham.notation.c21
                * z[alpha]
                @ parameter
                @ z[alpha]
                * spinham.atoms.spins[alpha]
            )

            self.J_A[ijk][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * p[alpha]
                @ parameter
                @ np.conjugate(p[alpha])
                * B[alpha][0]
                * A[alpha][0]
            )

            self.J_B[ijk][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * p[alpha]
                @ parameter
                @ p[alpha]
                * B[alpha][0]
                * B[alpha][0]
            )

            self.J_C[ijk][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * np.conjugate(p[alpha])
                @ parameter
                @ np.conjugate(p[alpha])
                * A[alpha][0]
                * A[alpha][0]
            )

            self.J_D[ijk][alpha][alpha] += (
                0.25
                * spinham.notation.c21
                * np.conjugate(p[alpha])
                @ parameter
                @ p[alpha]
                * A[alpha][0]
                * B[alpha][0]
            )

        for atom1, atom2, ijk, parameter in spinham.p22:
            if ijk not in self.J_A:
                self.J_A[ijk] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if ijk not in self.J_B:
                self.J_B[ijk] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if ijk not in self.J_C:
                self.J_C[ijk] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if ijk not in self.J_D:
                self.J_D[ijk] = np.zeros((spinham.M, spinham.M), dtype=complex)

            if ijk not in self.r_nu:
                self.r_nu[ijk] = ijk @ spinham.cell

            alpha = spinham.index_map[atom1]
            beta = spinham.index_map[atom2]

            self.A_zero[alpha][beta] += (
                -spinham.notation.c22
                * z[alpha]
                @ parameter
                @ z[beta]
                * spinham.atoms.spins[beta]
            )

            self.J_A[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * p[alpha]
                @ parameter
                @ np.conjugate(p[beta])
                * B[alpha][0]
                * A[beta][0]
            )

            self.J_B[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * p[alpha]
                @ parameter
                @ p[beta]
                * B[alpha][0]
                * B[beta][0]
            )

            self.J_C[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * np.conjugate(p[alpha])
                @ parameter
                @ np.conjugate(p[beta])
                * A[alpha][0]
                * A[beta][0]
            )

            self.J_D[ijk][alpha][beta] += (
                0.25
                * spinham.notation.c22
                * np.conjugate(p[alpha])
                @ parameter
                @ p[beta]
                * A[alpha][0]
                * B[beta][0]
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

        result += self.A_zero

        for ijk in self.J_A:
            result += self.J_A[ijk] * np.exp(-1j * (k @ self.r_nu[ijk]))

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

        for ijk in self.J_B:
            result += self.J_B[ijk] * np.exp(-1j * (k @ self.r_nu[ijk]))

        return result

    def C(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.
        """

        k = np.array(k)

        result = np.zeros((self.M, self.M), dtype=complex)

        for ijk in self.J_C:
            result += self.J_C[ijk] * np.exp(-1j * (k @ self.r_nu[ijk]))

        return result

    def D(self, k):
        r"""

        Parameters
        ----------
        k : (3,) |array-like|_
            Absolute.
        """

        k = np.array(k)

        result = np.zeros((self.M, self.M), dtype=complex)

        result += self.A_zero

        for ijk in self.J_D:
            result += self.J_D[ijk] * np.exp(-1j * (k @ self.r_nu[ijk]))

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

        left = np.concatenate((self.A(k=k), self.C(k=k)), axis=0)
        right = np.concatenate((self.B(k=k), self.D(k=k)), axis=0)
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

        if not np.allclose(G_plus, G_minus, atol=1e-4):
            raise NotImplementedError(
                r"Boson modes do not match, the logic is not implemented for this case."
            )

        return E_plus + E_minus


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
