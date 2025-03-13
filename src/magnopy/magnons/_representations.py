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


class PolynomialParameter:
    r"""
    Coefficients of polynomial bosonic representation :math:`A^{nm}`

    Syntax ``A[n,m]`` returns value of the parameter :math:`A^{nm}`.

    Syntax ``A[n]`` returns a list with :math:`n+1` parameters
    :math:`A^{n0}, \dots, A^{nn}`.

    Only syntax ``A[n,m] = 123`` supported for adding parameters.

    Examples
    --------

    .. doctest::

        >>> import magnopy
        >>> # Creation does not take any arguments
        >>> A = magnopy.magnons.PolynomialParameter()
        >>> # Now all coefficients are zero for any n and m
        >>> A[0,0]
        0.0
        >>> A[2,1]
        0.0
        >>> A[1232132, 232131]
        0.0
        >>> A[5]
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        >>> # Set value to some parameter
        >>> A[0,0] = 1
        >>> A[2,1] = 0.5
        >>> A[2]
        [0.0, 0.5, 0.0]
        >>> A[0]
        [1]
        >>> A[0,0]
        1

    Intended use-case for this class is

    .. doctest::

        >>> for n in range(0, A.nmax + 1):
        ...     for m in range(0, n + 1):
        ...         print(n, m, A[n,m])
        ...
        0 0 1
        1 0 0.0
        1 1 0.0
        2 0 0.0
        2 1 0.5
        2 2 0.0

    """

    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                raise ValueError("n < 0")

            if key >= len(self._data):
                return [0.0 for i in range(key + 1)]

            max_m = len(self._data[key]) - 1

            if key > max_m:
                for i in range(max_m, key):
                    self._data[key].append(0.0)

            return self._data[key]

        n, m = key

        if m > n:
            raise ValueError("m > n")

        if n < 0:
            raise ValueError("n < 0")

        if m < 0:
            raise ValueError("m < 0")

        if n >= len(self._data):
            return 0.0

        if m >= len(self._data[n]):
            return 0.0

        return self._data[n][m]

    def __setitem__(self, key, value):
        n, m = key

        if m > n:
            raise ValueError("m > n")

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

    @property
    def nmax(self) -> int:
        r"""
        Maximum value of n at which the sum is cut.

        Returns
        -------
        nmax : int

        Examples
        --------

        .. doctest::

            >>> import magnopy
            >>> A = magnopy.magnons.PolynomialParameter()
            >>> # -1 is intended here, as then range(0, A.nmax + 1) works correctly for
            >>> # any nmax
            >>> A.nmax
            -1
            >>> A[0,0] = 1
            >>> A.nmax
            0
            >>> A[1,0] = -3.14
            >>> A.nmax
            1
            >>> A[32,0] = -3.14
            >>> A.nmax
            32
        """

        return len(self._data) - 1


def get_hp_taylor(atoms, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Taylor expansion around
    zero.

    Parameters
    ----------
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["spins"]``.
    n : int, default 1
        Maximum allowed amount of the bosonic operators in the representation. Note that
        ``n=2k`` and ``n=2k+1`` will give the same result for any :math:`k \ge 0`.

    Returns
    -------
    A : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    """

    if n > 1:
        raise NotImplementedError

    A = [PolynomialParameter() for _ in range(len(atoms["spins"]))]
    B = [PolynomialParameter() for _ in range(len(atoms["spins"]))]

    for index in range(len(atoms["spins"])):
        A[index][1, 1] = sqrt(2 * spinham.atoms.spins[index])
        B[index][1, 0] = sqrt(2 * spinham.atoms.spins[index])


def get_hp_newton(atoms, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Newton expansion.

    Parameters
    ----------
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["spins"]``.
    n : int, default 1
        Maximum allowed amount of the bosonic operators in the representation. Note that
        ``n=2k`` and ``n=2k+1`` will give the same result for any :math:`k \ge 0`.

    Returns
    -------
    A : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    """

    if n > 1:
        raise NotImplementedError

    A = [PolynomialParameter() for _ in range(len(atoms["spins"]))]
    B = [PolynomialParameter() for _ in range(len(atoms["spins"]))]

    for index in range(len(atoms["spins"])):
        A[index][1, 1] = sqrt(2 * spinham.atoms.spins[index])
        B[index][1, 0] = sqrt(2 * spinham.atoms.spins[index])


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
    A : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (M) list of :py:class:`.PolynomialParameter`
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
