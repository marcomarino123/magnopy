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
from numpy.linalg import LinAlgError

from magnopy._exceptions import ColpaFailed

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def solve_via_colpa(D):
    r"""
    Diagonalize grand-dynamical matrix following the method of Colpa [1]_.

    Algorithm itself is described in section 3, Remark 1 of [1]_.

    Solves the Bogoliubov Hamiltonian of the form:

    .. math::

        \hat{H} = \sum_{r^{\prime}, r = 1}^m
        a_{r^{\prime}}^{\dagger}\boldsymbol{\Delta}_1^{r^{\prime}r}a_r +
        a_{r^{\prime}}^{\dagger}\boldsymbol{\Delta}_2^{r^{\prime}r}a_{m+r}^{\dagger} +
        a_{m+r^{\prime}}^{\dagger}\boldsymbol{\Delta}_3^{r^{\prime}r}a_r +
        a_{m+r^{\prime}}^{\dagger}\boldsymbol{\Delta}_4^{r^{\prime}r}a_{m+r}^{\dagger}

    In a matrix form the Hamiltonian is:

    .. math::

        \hat{H} = \boldsymbol{\cal A}^{\dagger} \boldsymbol{D} \boldsymbol{\cal A}

    where

    .. math::

        \boldsymbol{\cal A} =
        \begin{pmatrix}
            a_1 \\
            \cdots \\
            a_m \\
            a_{m+1} \\
            \cdots \\
            a_{2m} \\
        \end{pmatrix}

    After diagonalization the Hamiltonian is:

    .. math::

        \hat{H} = \boldsymbol{\cal B}^{\dagger} \boldsymbol{E} \boldsymbol{\cal B}

    Parameters
    ----------
    D : (2N, 2N) |array-like|_
        Grand dynamical matrix. If it is Hermitian and positive-defined, then obtained
        eigenvalues are positive and real.

        .. math::

            \boldsymbol{D} = \begin{pmatrix}
                \boldsymbol{\Delta_1} & \boldsymbol{\Delta_2} \\
                \boldsymbol{\Delta_3} & \boldsymbol{\Delta_4}
            \end{pmatrix}

    Returns
    -------
    E : (2N,) :numpy:`ndarray`
        The eigenvalues.
        It is an array of the diagonal elements of the
        diagonal matrix :math:`\boldsymbol{E}` from the diagonalized Hamiltonian. The
        eigenvalues are sorted in descending order before the multiplication by the
        paraunitary matrix. Therefore, first N elements correspond to the
        :math:`b^{\dagger}(\boldsymbol{k})b(\boldsymbol{k})` and last N elements - to
        the :math:`b(-\boldsymbol{k})b^{\dagger}(-\boldsymbol{k})`.


    G : (2N, 2N) :numpy:`ndarray`
        Transformation matrix, which changes the basis from the original set of bosonic
        operators :math:`\boldsymbol{a}` to the set of new bosonic operators
        :math:`\boldsymbol{b}` which diagonalize the Hamiltonian:

        .. math::

            \boldsymbol{\cal B} = \boldsymbol{G} \boldsymbol{\cal A}

        The rows are ordered in the same way as the eigenvalues.

    Raises
    ------
    ColpaFailed
        If the algorithm fails.

    Notes
    -----

    Let :math:`\boldsymbol{E}` be the diagonal matrix of eigenvalues ``E``, then:

    .. math::

        \boldsymbol{E} = (\boldsymbol{G}^{\dagger})^{-1} \boldsymbol{D} \boldsymbol{G}^{-1}



    References
    ----------
    .. [1] Colpa, J.H.P., 1978.
        Diagonalization of the quadratic boson hamiltonian.
        Physica A: Statistical Mechanics and its Applications,
        93(3-4), pp.327-353.
    """

    D = np.array(D)

    N = len(D) // 2
    g = np.diag(np.concatenate((np.ones(N), -np.ones(N))))

    try:
        # In Colpa article decomposition is K^{\dag}K, while numpy gives KK^{\dag}
        K = np.conjugate(np.linalg.cholesky(D)).T
    except LinAlgError:
        raise ColpaFailed

    L, U = np.linalg.eig(K @ g @ np.conjugate(K).T)

    # Sort with respect to L, in descending order
    U = np.concatenate((L[:, None], U.T), axis=1).T
    U = U[:, np.argsort(U[0])]
    L = U[0, ::-1]
    U = U[1:, ::-1]
    E = g @ L

    G_minus_one = np.linalg.inv(K) @ U @ np.sqrt(np.diag(E))

    # Compute G from G^-1 following Colpa, see equation (3.7) for details
    G = np.conjugate(G_minus_one).T
    G[:N, N:] *= -1
    G[N:, :N] *= -1

    return E, G


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
