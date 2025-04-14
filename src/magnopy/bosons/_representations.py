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


from math import factorial, sqrt

import numpy as np

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def get_hp_taylor(spin_values, n_max=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Taylor expansion around
    zero.

    Parameters
    ----------
    spin_values : (M) interable
        Values of atom's spins, i.e. ``atoms["spins"]``.
    n_max : int, default 1
        From the equation (5) of the polynomial expansion. See notes

    Returns
    -------
    A : (M, n_max) :numpy:`ndarray`
        Parameters :math:`A^n_{\alpha}` of the bosonic expansion.
    B : (M, n_max) :numpy:`ndarray`
        Parameters :math:`B^n_{\alpha}` of the bosonic expansion.

    Notes
    -----

    .. math::

        \boldsymbol{S}_{\mu, \alpha}
        =
        \sum_{n=0}^{n_{max}}
        \left(
        \dfrac{\overline{\boldsymbol{p}_{\alpha}}A^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^n(a_{\mu, \alpha})^{n+1}
        +
        \dfrac{\boldsymbol{p}_{\alpha}B^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^{n+1}(a_{\mu, \alpha})^n
        +
        \boldsymbol{z}_{\alpha}
        (S_{\alpha} - a^{\dagger}_{\mu, \alpha}a_{\mu, \alpha})
        \right)
    """

    if n_max < 0:
        raise ValueError(R"Require n >= 0")

    if n_max == 0:
        return [[sqrt(2 * spin_value)] for spin_value in spin_values], [
            [sqrt(2 * spin_value)] for spin_value in spin_values
        ]

    if n_max == 1:
        return [
            [sqrt(2 * spin_value), -1 / 2 / sqrt(2 * spin_value)]
            for spin_value in spin_values
        ], [
            [sqrt(2 * spin_value), -1 / 2 / sqrt(2 * spin_value)]
            for spin_value in spin_values
        ]

    if n_max > 1:
        raise NotImplementedError(f"Not implemented for n_max > 1.")


def get_hp_newton(spin_values, n_max=1):
    r"""
    Computes A and B for Holstein-primakoff representation with Newton expansion.

    Parameters
    ----------
    spin_values : (M) |array-like|_
        Values of atom's spins, i.e. ``atoms["spins"]``.
    n_max : int, default 1
        From the equation (5) of the polynomial expansion. See notes

    Returns
    -------
    A : (M, n_max) :numpy:`ndarray`
        Parameters :math:`A^n_{\alpha}` of the bosonic expansion.
    B : (M, n_max) :numpy:`ndarray`
        Parameters :math:`B^n_{\alpha}` of the bosonic expansion.

    Notes
    -----

    .. math::

        \boldsymbol{S}_{\mu, \alpha}
        =
        \sum_{n=0}^{n_{max}}
        \left(
        \dfrac{\overline{\boldsymbol{p}_{\alpha}}A^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^n(a_{\mu, \alpha})^{n+1}
        +
        \dfrac{\boldsymbol{p}_{\alpha}B^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^{n+1}(a_{\mu, \alpha})^n
        +
        \boldsymbol{z}_{\alpha}
        (S_{\alpha} - a^{\dagger}_{\mu, \alpha}a_{\mu, \alpha})
        \right)

    .. math::
        A_{\alpha}^n = B_{\alpha}^n
        =
        \sum_{l=0}^{n}
        \dfrac{(-1)^{n-l}}{l!(n-l)!}
        \sqrt{2S_{\alpha} - l}
    """

    spin_values = np.array(spin_values)

    n_max_allowed = 2 * int(spin_values.min())

    if n_max > n_max_allowed:
        raise ValueError(f"For given spin_values n_max should be <= {n_max_allowed}.")

    A = []
    B = []
    for spin_value in spin_values:
        A.append([])
        B.append([])
        for n in range(int(2 * spin_value)):
            tmp = 0
            for l in range(n + 1):
                tmp += (
                    (-1) ** (n - l)
                    * sqrt(2 * spin_value - l)
                    / factorial(l)
                    / factorial(n - l)
                )
            A[-1].append(tmp)
            B[-1].append(tmp)

    return A, B


def get_dyson_maleev(spin_values, conjugate=False):
    r"""
    Computes A and B for Dyson-Maleev  or conjugate Dyson-Maleev representation.

    Parameters
    ----------
    spin_values : (M) |array-like|_
        Values of atom's spins, i.e. ``atoms["spins"]``.
    n_max : int, default 1
        From the equation (5) of the polynomial expansion. See notes

    Returns
    -------
    A : (M, n_max) :numpy:`ndarray`
        Parameters :math:`A^n_{\alpha}` of the bosonic expansion.
    B : (M, n_max) :numpy:`ndarray`
        Parameters :math:`B^n_{\alpha}` of the bosonic expansion.

    Notes
    -----

    .. math::

        \boldsymbol{S}_{\mu, \alpha}
        =
        \sum_{n=0}^{n_{max}}
        \left(
        \dfrac{\overline{\boldsymbol{p}_{\alpha}}A^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^n(a_{\mu, \alpha})^{n+1}
        +
        \dfrac{\boldsymbol{p}_{\alpha}B^n_{\alpha}}{2}
        (a_{\mu, \alpha}^{\dagger})^{n+1}(a_{\mu, \alpha})^n
        +
        \boldsymbol{z}_{\alpha}
        (S_{\alpha} - a^{\dagger}_{\mu, \alpha}a_{\mu, \alpha})
        \right)
    """

    if conjugate:
        return [[sqrt(2 * spin_value), 0] for spin_value in spin_values], [
            [sqrt(2 * spin_value), -1 / sqrt(2 * spin_value)]
            for spin_value in spin_values
        ]
    else:
        return [
            [sqrt(2 * spin_value), -1 / sqrt(2 * spin_value)]
            for spin_value in spin_values
        ], [[sqrt(2 * spin_value), 0] for spin_value in spin_values]

    return A, B


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
