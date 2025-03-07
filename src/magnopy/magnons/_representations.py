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

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


# TODO add iteration
# TODO add tests
class PolynomialParameter:
    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        n, m = key

        if m > n:
            raise ValueError("n > m")

        if n < 0:
            raise ValueError("n < 0")

        if m < 0:
            raise ValueError("m < 0")

        if n >= len(self._data):
            return 0.0

        if m > len(self._data[n]):
            return 0.0

        return self._data[n][m]

    def __setitem__(self, key, value):
        n, m = key

        if m > n:
            raise ValueError("n > m")

        if n < 0:
            raise ValueError("n < 0")

        if m < 0:
            raise ValueError("m < 0")

        max_n = len(self._data) - 1

        if n > max_n:
            for _ in range(max_n, n):
                self._data.append([])

        max_m = len(self._data[n]) - 1

        if m > max_m:
            for i in range(max_m, m):
                self._data[n].append(0.0)

        self._data[n][m] = value


def get_hp_taylor(atoms, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Taylor expansion around
    zero.

    Parameters
    ----------
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["spins"]``.
    n : int, default 1
        Maximum allowed amount of the bosonic operators in the expansion. Note that
        ``n=2k`` and ``n=2k+1`` will give the same result for any :math:`k \ge 0`.

    Returns
    -------
    A : (I, n, non-uniform) list of lists of lists
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (I, n, non-uniform) list of lists of lists
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    """

    raise NotImplementedError

    A = [PolynomialParameter() for _ in range(len(atoms["spins"]))]
    B = [PolynomialParameter() for _ in range(len(atoms["spins"]))]


def get_hp_newton(atoms, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Newton expansion.

    Parameters
    ----------
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["spins"]``.
    n : int, default 1
        Maximum allowed amount of the bosonic operators in the expansion.

    Returns
    -------
    A : (I, n, non-uniform) list of lists of lists
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (I, n, non-uniform) list of lists of lists
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    """

    raise NotImplementedError

    A = [PolynomialParameter() for _ in range(len(atoms["spins"]))]
    B = [PolynomialParameter() for _ in range(len(atoms["spins"]))]


def get_dyson_maleev(atoms, conjugate=False):
    r"""
    Computes A and B for Dyson-Maleev  or conjugate Dyson-Maleev representation.

    Parameters
    ----------
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["spins"]``.
    conjugate : bool, default False
        Whether to return normal or conjugate Dyson-Maleev representation.


    Returns
    -------
    A : (I) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (I) list of :py:class:`.PolynomialParameter`
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    """

    A = [PolynomialParameter() for _ in range(len(atoms["spins"]))]
    B = [PolynomialParameter() for _ in range(len(atoms["spins"]))]

    if conjugate:
        for i in range(len(atoms["spins"])):
            # n = 1
            A[i][1, 1] = sqrt(2 * atoms["spins"][i])
            B[i][1, 0] = sqrt(2 * atoms["spins"][i])
            # n = 3
            B[i][3, 1] = -1 / sqrt(2 * atoms["spins"][i])
    else:
        for i in range(len(atoms["spins"])):
            # n = 1
            A[i][1, 1] = sqrt(2 * atoms["spins"][i])
            B[i][1, 0] = sqrt(2 * atoms["spins"][i])

            # n = 3
            A[i][3, 2] = -1 / sqrt(2 * atoms["spins"][i])

    return A, B


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
