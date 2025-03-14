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


def get_hp_taylor(spin_values, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Taylor expansion around
    zero.

    Parameters
    ----------
    spin_values : (M) interable
        Values of atom's spins, i.e. ``atoms["spins"]``.
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

    A = [PolynomialParameter() for _ in range(len(spin_values))]
    B = [PolynomialParameter() for _ in range(len(spin_values))]

    for index in range(len(spin_values)):
        A[index][1, 1] = sqrt(2 * spin_values[index])
        B[index][1, 0] = sqrt(2 * spin_values[index])


def get_hp_newton(spin_values, n=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Newton expansion.

    Parameters
    ----------
    spin_values : (M) interable
        Values of atom's spins, i.e. ``atoms["spins"]``.
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

    A = [PolynomialParameter() for _ in range(len(spin_values))]
    B = [PolynomialParameter() for _ in range(len(spin_values))]

    for index in range(len(spin_values)):
        A[index][1, 1] = sqrt(2 * spin_values[index])
        B[index][1, 0] = sqrt(2 * spin_values[index])


def get_dyson_maleev(spin_values, conjugate=False):
    r"""
    Computes A and B for Dyson-Maleev  or conjugate Dyson-Maleev representation.

    Parameters
    ----------
    spin_values : (M) interable
        Values of atom's spins, i.e. ``atoms["spins"]``.
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

    A = [PolynomialParameter() for _ in range(len(spin_values))]
    B = [PolynomialParameter() for _ in range(len(spin_values))]

    if conjugate:
        for i in range(len(spin_values)):
            # n = 1
            A[i][1, 1] = sqrt(2 * spin_values[i])
            B[i][1, 0] = sqrt(2 * spin_values[i])
            # n = 3
            B[i][3, 1] = -1 / sqrt(2 * spin_values[i])
    else:
        for i in range(len(spin_values)):
            # n = 1
            A[i][1, 1] = sqrt(2 * spin_values[i])
            B[i][1, 0] = sqrt(2 * spin_values[i])

            # n = 3
            A[i][3, 2] = -1 / sqrt(2 * spin_values[i])

    return A, B


def _span_local_rf(direction_vector):
    r"""
    Span local  right-handed reference frame from the direction vector.

    Parameters
    ----------
    direction_vector : (3, ) |array-like|_
        Direction of the z axis of the local reference frame.

    Returns
    -------
    x : (3, ) :numpy:`ndarray`
    y : (3, ) :numpy:`ndarray`
    z : (3, ) :numpy:`ndarray`
    """

    direction_vector = np.array(direction_vector, dtype=float)

    if np.allclose(direction_vector, np.zeros(3)):
        raise ValueError("Zero vector.")

    direction_vector /= np.linalg.norm(direction_vector)

    if np.allclose(direction_vector, [0, 0, 1]):
        return np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            dtype=float,
        )

    if np.allclose(direction_vector, [0, 0, -1]):
        return np.array(
            [
                [0, -1, 0],
                [-1, 0, 0],
                [0, 0, -1],
            ],
            dtype=float,
        )

    z_dir = [0, 0, 1]

    sin_rot_angle = np.linalg.norm(np.cross(z_dir, direction_vector))
    cos_rot_angle = np.dot(direction_vector, z_dir)
    # direction_vector and z_dir are unit vectors
    ux, uy, uz = np.cross(z_dir, direction_vector) / sin_rot_angle

    x_a = np.array(
        [
            ux**2 * (1 - cos_rot_angle) + cos_rot_angle,
            ux * uy * (1 - cos_rot_angle) + uz * sin_rot_angle,
            ux * uz * (1 - cos_rot_angle) - uy * sin_rot_angle,
        ]
    )

    y_a = np.array(
        [
            ux * uy * (1 - cos_rot_angle) - uz * sin_rot_angle,
            uy**2 * (1 - cos_rot_angle) + cos_rot_angle,
            uy * uz * (1 - cos_rot_angle) + ux * sin_rot_angle,
        ]
    )

    return x_a, y_a, direction_vector


def get_vector_parameter(A, B, spin_values, spin_directions):
    r"""
    Computes :math:`\boldsymbol{v}^{nm}_{\alpha}`.

    Parameters
    ----------
    A : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`A^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^+_{\mu,\alpha}`.
    B : (M) list of :py:class:`.PolynomialParameter`
        Parameters :math:`B^{nm}_{\alpha}` of the bosonic expansion for
        :math:`\boldsymbol{S}^-_{\mu,\alpha}`.
    spin_values : (M) iterable
        Values of atom's spins, i.e. ``atoms["spins"]``.
    spin_directions : (M, 3) |array-like|_
        Directions of spin vectors. Only directions of vectors are used, modulus is
        ignored.

    Returns
    -------
    v : (M) list of :py:class:`.PolynomialParameter`
        Vector parameters :math:`\boldsymbol{v}^{nm}_{\alpha}`.
    """

    v = [PolynomialParameter() for _ in range(len(spin_values))]

    for index in range(len(spin_values)):
        x_a, y_a, z_a = span_local_rf(spin_directions[index])
        p_a = x_a + 1j * y_a
        nmax = max(A.nmax, B.nmax)

        for n in range(nmax + 1):
            for m in range(n + 1):
                v[n, m] = np.conjugate(p_a) / 2 * A[n, m] + p_a / 2 * B[n, m]

                if n == 0 and m == 0:
                    v[n, m] = v[n, m] + z_a * spin_values[index]

                if n == 2 and m == 1:
                    v[n, m] = v[n, m] - z_a

    return v


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
