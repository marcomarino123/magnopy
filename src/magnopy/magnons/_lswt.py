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

from magnopy.magnons._local_rf import span_local_rfs
from magnopy.magnons._representations import get_hp_newton

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def get_A(spinham, spin_directions, k, A=None, B=None):
    r"""
    Compute :math:`A_{\alpha,\beta}(\boldsymbol{k})`.

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
    k : (3, ) |array-like|_
        Reciprocal vector.
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    Returns
    -------
    D_A : (M, M) :numpy:`ndarray`
    """

    spin_directions = np.array(spin_directions, dtype=float)
    spin_values = spinham.magnetic_atoms.spins
    k = np.array(k)

    if A is None and B is None:
        A, B = get_hp_newton(spin_values, n_max=1)

    if A is None:
        A = B

    if B is None:
        B = A

    p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

    D_A = np.zeros((len(spin_directions), len(spin_directions)), dtype=complex)

    # One spin one site
    for atom, parameter in spinham.p1:
        alpha = spinham.index_map[atom]
        tmp = -0.5 * spinham.notation.c1 * parameter @ spin_directions[alpha]

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom]

        D_A[alpha][alpha] += tmp

    # Two spins one site
    for atom, parameter in spinham.p21:
        alpha = spinham.index_map[atom]

        tmp = (
            spinham.notation.c21
            / 4
            * p[alpha]
            @ parameter
            @ np.conjugate(p[alpha])
            * B[alpha][0]
            * A[alpha][0]
            - spinham.notation.c21
            * z[alpha]
            @ parameter
            @ z[alpha]
            * spinham.atoms.spins[atom]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom] ** 2

        D_A[alpha][alpha] += tmp

    # Two spins two sites
    for atom1, atom2, ijk2, parameter in spinham.p22:
        alpha = spinham.index_map[atom1]
        beta = spinham.index_map[atom2]
        r_nu = ijk2 @ spinham.cell

        tmp1 = (
            spinham.notation.c22
            / 4
            * p[alpha]
            @ parameter
            @ np.conjugate(p[beta])
            * B[alpha][0]
            * A[beta][0]
            * np.exp(-1j * (k @ r_nu))
        )

        tmp2 = (
            -spinham.notation.c22
            * z[alpha]
            @ parameter
            @ z[beta]
            * spinham.atoms.spins[atom2]
        )

        if spinham.notation.spin_normalized:
            tmp1 /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]
            tmp2 /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]

        D_A[alpha][beta] += tmp1
        D_A[alpha][alpha] += tmp2

    return D_A


def get_D(spinham, spin_directions, k, A=None, B=None):
    r"""
    Compute :math:`D_{\alpha,\beta}(\boldsymbol{k})`.

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
    k : (3, ) |array-like|_
        Reciprocal vector.
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    Returns
    -------
    D_D : (M, M) :numpy:`ndarray`
    """

    spin_directions = np.array(spin_directions, dtype=float)
    spin_values = spinham.magnetic_atoms.spins
    k = np.array(k)

    if A is None and B is None:
        A, B = get_hp_newton(spin_values, n_max=1)

    if A is None:
        A = B

    if B is None:
        B = A

    p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

    D_D = np.zeros((len(spin_directions), len(spin_directions)), dtype=complex)

    # One spin one site
    for atom, parameter in spinham.p1:
        alpha = spinham.index_map[atom]
        tmp = -0.5 * spinham.notation.c1 * parameter @ spin_directions[alpha]

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom]

        D_D[alpha][alpha] += tmp

    # Two spins one site
    for atom, parameter in spinham.p21:
        alpha = spinham.index_map[atom]

        tmp = (
            spinham.notation.c21
            / 4
            * np.conjugate(p[alpha])
            @ parameter
            @ p[alpha]
            * A[alpha][0]
            * B[alpha][0]
            - spinham.notation.c21
            * z[alpha]
            @ parameter
            @ z[alpha]
            * spinham.atoms.spins[atom]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom] ** 2

        D_D[alpha][alpha] += tmp

    # Two spins two sites
    for atom1, atom2, ijk2, parameter in spinham.p22:
        alpha = spinham.index_map[atom1]
        beta = spinham.index_map[atom2]
        r_nu = ijk2 @ spinham.cell

        tmp1 = (
            spinham.notation.c22
            / 4
            * np.conjugate(p[alpha])
            @ parameter
            @ p[beta]
            * A[alpha][0]
            * B[beta][0]
            * np.exp(-1j * (k @ r_nu))
        )

        tmp2 = (
            -spinham.notation.c22
            * z[alpha]
            @ parameter
            @ z[beta]
            * spinham.atoms.spins[atom2]
        )

        if spinham.notation.spin_normalized:
            tmp1 /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]
            tmp2 /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]

        D_D[alpha][beta] += tmp1
        D_D[alpha][alpha] += tmp2

    return D_D


def get_B(spinham, spin_directions, k, A=None, B=None):
    r"""
    Compute :math:`B_{\alpha,\beta}(\boldsymbol{k})`.

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
    k : (3, ) |array-like|_
        Reciprocal vector.
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    Returns
    -------
    D_B : (M, M) :numpy:`ndarray`
    """

    spin_directions = np.array(spin_directions, dtype=float)
    spin_values = spinham.magnetic_atoms.spins
    k = np.array(k)

    if A is None and B is None:
        A, B = get_hp_newton(spin_values, n_max=1)

    if A is None:
        A = B

    if B is None:
        B = A

    p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

    D_B = np.zeros((len(spin_directions), len(spin_directions)), dtype=complex)

    # One spin one site do not contribute

    # Two spins one site
    for atom, parameter in spinham.p21:
        alpha = spinham.index_map[atom]

        tmp = (
            spinham.notation.c21
            / 4
            * p[alpha]
            @ parameter
            @ p[alpha]
            * B[alpha][0]
            * B[alpha][0]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom] ** 2

        D_B[alpha][alpha] += tmp

    # Two spins two sites
    for atom1, atom2, ijk2, parameter in spinham.p22:
        alpha = spinham.index_map[atom1]
        beta = spinham.index_map[atom2]
        r_nu = ijk2 @ spinham.cell

        tmp = (
            spinham.notation.c22
            / 4
            * p[alpha]
            @ parameter
            @ p[beta]
            * B[alpha][0]
            * B[beta][0]
            * np.exp(-1j * (k @ r_nu))
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]

        D_B[alpha][beta] += tmp

    return D_B


def get_C(spinham, spin_directions, k, A=None, B=None):
    r"""
    Compute :math:`C_{\alpha,\beta}(\boldsymbol{k})`.

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
    k : (3, ) |array-like|_
        Reciprocal vector.
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    Returns
    -------
    D_C : (M, M) :numpy:`ndarray`
    """

    spin_directions = np.array(spin_directions, dtype=float)
    spin_values = spinham.magnetic_atoms.spins
    k = np.array(k)

    if A is None and B is None:
        A, B = get_hp_newton(spin_values, n_max=1)

    if A is None:
        A = B

    if B is None:
        B = A

    p, z = span_local_rfs(directional_vectors=spin_directions, hybridize=True)

    D_C = np.zeros((len(spin_directions), len(spin_directions)), dtype=complex)

    # One spin one site do not contribute

    # Two spins one site
    for atom, parameter in spinham.p21:
        alpha = spinham.index_map[atom]

        tmp = (
            spinham.notation.c21
            / 4
            * np.conjugate(p[alpha])
            @ parameter
            @ np.conjugate(p[alpha])
            * A[alpha][0]
            * A[alpha][0]
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom] ** 2

        D_C[alpha][alpha] += tmp

    # Two spins two sites
    for atom1, atom2, ijk2, parameter in spinham.p22:
        alpha = spinham.index_map[atom1]
        beta = spinham.index_map[atom2]
        r_nu = ijk2 @ spinham.cell

        tmp = (
            spinham.notation.c22
            / 4
            * np.conjugate(p[alpha])
            @ parameter
            @ np.conjugate(p[beta])
            * A[alpha][0]
            * A[beta][0]
            * np.exp(-1j * (k @ r_nu))
        )

        if spinham.notation.spin_normalized:
            tmp /= spinham.atoms.spins[atom1] * spinham.atoms.spins[atom2]

        D_C[alpha][beta] += tmp

    return D_C


def get_GDM(spinham, spin_directions, k, A=None, B=None):
    r"""
    Compute :math:`\mathcal{D}_{\alpha,\beta}(\boldsymbol{k})`.

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
    k : (3, ) |array-like|_
        Reciprocal vector.
    A : (M, 2) |array-like|_, optional
        Coefficients :math:`A^0_{\alpha}` and :math:`A^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``B``. If ``B`` is not given,
        then defaults to the HP + Newton.
    B : (M, 2) |array-like|_, optional
        Coefficients :math:`B^0_{\alpha}` and :math:`B^1_{\alpha}` or the bosonic
        representation. If not given, then defaults to ``A``. If ``A`` is not given,
        then defaults to the HP + Newton.

    Returns
    -------
    gdm : (M, M) :numpy:`ndarray`
    """

    A = get_A(spinham=spinham, spin_directions=spin_directions, k=k, A=A, B=B)
    B = get_B(spinham=spinham, spin_directions=spin_directions, k=k, A=A, B=B)
    C = get_C(spinham=spinham, spin_directions=spin_directions, k=k, A=A, B=B)
    D = get_D(spinham=spinham, spin_directions=spin_directions, k=k, A=A, B=B)

    print(A, B, C, D, sep="\n")

    left = np.concatenate((A, C), axis=0)
    right = np.concatenate((B, D), axis=0)
    gdm = np.concatenate((left, right), axis=1)

    return gdm


def get_Delta(E):
    r"""
    Computes Delta terms.

    Parameters
    ----------
    E : (2N,) :numpy:`ndarray`
        The eigenvalues.
        It is an array of the diagonal elements of the
        diagonal matrix :math:`\boldsymbol{E}` from the diagonalized Hamiltonian. First
        N elements correspond to the
        :math:`b^{\dagger}(\boldsymbol{k})b(\boldsymbol{k})` and last N elements - to
        the :math:`b(-\boldsymbol{k})b^{\dagger}(-\boldsymbol{k})`.
    G : (2N, 2N) :numpy:`ndarray`
        Transformation matrix, which changes the basis from the original set of bosonic
        operators :math:`\boldsymbol{a}` to the set of new bosonic operators.

    Returns
    -------
    Delta_k : float
    """

    N = int(E.shape[0] / 2)

    return -0.5 * (np.sum(E[:N]) - np.sum(E[N:]))


def get_omegas(E1, G1, E2, G2):
    r"""
    Computes omegas.

    Parameters
    ----------
    E1 : (2N,) :numpy:`ndarray`
        The eigenvalues.
        It is an array of the diagonal elements of the
        diagonal matrix :math:`\boldsymbol{E}` from the diagonalized Hamiltonian. First
        N elements correspond to the
        :math:`b^{\dagger}(\boldsymbol{k})b(\boldsymbol{k})` and last N elements - to
        the :math:`b(-\boldsymbol{k})b^{\dagger}(-\boldsymbol{k})`. From solution of k.
    G1 : (2N, 2N) :numpy:`ndarray`
        Transformation matrix, which changes the basis from the original set of bosonic
        operators :math:`\boldsymbol{a}` to the set of new bosonic operators. From solution of k.
    E2 : (2N,) :numpy:`ndarray`
        The eigenvalues.
        It is an array of the diagonal elements of the
        diagonal matrix :math:`\boldsymbol{E}` from the diagonalized Hamiltonian. First
        N elements correspond to the
        :math:`b^{\dagger}(\boldsymbol{k})b(\boldsymbol{k})` and last N elements - to
        the :math:`b(-\boldsymbol{k})b^{\dagger}(-\boldsymbol{k})`. From solution of -k.
    G2 : (2N, 2N) :numpy:`ndarray`
        Transformation matrix, which changes the basis from the original set of bosonic
        operators :math:`\boldsymbol{a}` to the set of new bosonic operators. From solution of -k.

    Returns
    -------
    omegas : (N, ) :numpy:`ndarray`
    G : (N, 2N) :numpy:`ndarray`
    """

    N = int(E1.shape[0] / 2)

    E1 = E1[:N]
    E2 = E2[N:]

    G1 = G1[:N]
    G2 = G2[:N]

    order_1 = np.argsort(E1)
    order_2 = np.argsort(E2)

    E1 = E1[order_1]
    E2 = E2[order_2]

    G1 = G1[order_1]
    G2 = G2[order_2]

    if not np.allclose(G1, G2):
        raise NotImplementedError(
            r"Boson modes do not match, the logic is not implemented for this case."
        )

    return E1 + E2, G1


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
