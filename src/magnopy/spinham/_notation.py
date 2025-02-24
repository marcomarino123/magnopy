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


R"""
Notation of spin Hamiltonian
"""

from magnopy._exceptions import NotationError
from magnopy.constants._spinham_notations import _NOTATIONS

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


class Notation:
    R"""
    Notation of the spin Hamiltonian.

    For the detailed description of the notation problem see :ref:`TODO`.

    Parameters
    ----------
    double_counting : bool, optional
        Whether the pairs of spins are counted twice in the Hamiltonian's sums. If
        ``True``, then pairs are counted twice.
    spin_normalized : bool, optional
        Whether spin vectors/operators are normalized to 1. If ``True``, then spin
        vectors/operators are normalized.
    c21 : float, optional
        Numerical factor before the two-spins/one-site sum of the Hamiltonian.
    c22 : float, optional
        Numerical factor before the two-spins/two-sites sum of the Hamiltonian.
    name : str, default "custom"
        A label for the notation. Any string, case-insensitive.

    Examples
    --------

    .. doctest::

        >>> from magnopy.spinham import Notation
        >>> n1 = Notation(True, True, c21=1, c22=-0.5)
        >>> n2 = Notation(False, True, c21=1, c22=-0.5)
        >>> n3 = Notation(False, True, c22=-0.5)
        >>> n1.double_counting
        True
        >>> n1 == n2
        False
        >>> n3.c21
        Traceback (most recent call last):
        ...
        ValueError: c21 factor of notation is not defined.
        >>> n3.name
        'custom'

    """

    __slots__ = ("_double_counting", "_spin_normalized", "_c22", "_c21", "_name")

    def __init__(
        self,
        double_counting: bool = None,
        spin_normalized: bool = None,
        c21: float = None,
        c22: float = None,
        name: str = "custom",
    ) -> None:
        if double_counting is not None:
            self._double_counting = bool(double_counting)
        else:
            self._double_counting = None

        if spin_normalized is not None:
            self._spin_normalized = bool(spin_normalized)
        else:
            self._spin_normalized = None

        if c22 is not None:
            self._c22 = float(c22)
        else:
            self._c22 = None

        if c21 is not None:
            self._c21 = float(c21)
        else:
            self._c21 = None

        self._name = str(name).lower()

    def summary(self, return_as_string=False):
        r"""
        Gives human-readable summary of the notation.

        Parameters
        ----------
        return_as_string : bool, default False
            Whether to print or return a ``str``. If ``True``, then return an ``str``.
            If ``False``, then print it.

        Examples
        --------

        .. doctest::

            >>> from magnopy.spinham import Notation
            >>> n1 = Notation(True, True, -0.5, 1)
            >>> n1.summary()
            custom notation where
              * Bonds are counted twice in the sum;
              * Spin vectors are normalized to 1;
              * c22 = -0.5;
              * c21 = 1.0.
        """

        summary = [f"{self.name} notation where"]

        if self._double_counting is None:
            summary.append("  * Undefined double counting;")
        elif self._double_counting:
            summary.append("  * Bonds are counted twice in the sum;")
        else:
            summary.append("  * Bonds are counted once in the sum;")

        if self._spin_normalized is None:
            summary.append("  * Undefined spin normalization;")
        elif self._spin_normalized:
            summary.append("  * Spin vectors are normalized to 1;")
        else:
            summary.append("  * Spin vectors are not normalized;")

        if self._c22 is None:
            summary.append("  * Undefined c22 factor;")
        else:
            summary.append(f"  * c22 = {self._c22};")

        if self._c21 is None:
            summary.append("  * Undefined c21 factor.")
        else:
            summary.append(f"  * c21 = {self._c21}.")

        summary = ("\n").join(summary)

        if return_as_string:
            return summary

        print(summary)

    @property
    def name(self) -> str:
        r"""
        A label for the notation. Any string, case-insensitive.
        """

        return self._name

    @name.setter
    def name(self, new_value: str):
        self._name = str(new_value).lower()

    @property
    def double_counting(self) -> bool:
        r"""
        Whether the pairs of spins are counted twice in the Hamiltonian's sums.

        If ``True``, then pairs are counted twice.
        """
        if self._double_counting is None:
            raise NotationError(notation=self, property="double_counting")
        return self._double_counting

    @property
    def spin_normalized(self) -> bool:
        r"""
        Whether spin vectors/operators are normalized to 1.

        If ``True``, then spin vectors/operators are normalized.
        """
        if self._spin_normalized is None:
            raise NotationError(notation=self, property="spin_normalized")
        return self._spin_normalized

    @property
    def c21(self) -> float:
        r"""
        Numerical factor before the two-spins/one-site sum of the Hamiltonian.
        """
        if self._c21 is None:
            raise NotationError(notation=self, property="c21")
        return self._c21

    @property
    def c22(self) -> float:
        r"""
        Numerical factor before the two-spins/two-sites sum of the Hamiltonian.
        """
        if self._c22 is None:
            raise NotationError(notation=self, property="c22")
        return self._c22

    @double_counting.setter
    def double_counting(self, new_value: bool):
        raise AttributeError(
            "It is intentionally forbidden to set properties of notation. "
            "Use correct methods of SpinHamiltonian class to change notation."
        )

    @spin_normalized.setter
    def spin_normalized(self, new_value: bool):
        raise AttributeError(
            "It is intentionally forbidden to set properties of notation. "
            "Use correct methods of SpinHamiltonian class to change notation."
        )

    @c21.setter
    def c21(self, new_value: float):
        raise AttributeError(
            "It is intentionally forbidden to set properties of notation. "
            "Use correct methods of SpinHamiltonian class to change notation."
        )

    @c22.setter
    def c22(self, new_value: float):
        raise AttributeError(
            "It is intentionally forbidden to set properties of notation. "
            "Use correct methods of SpinHamiltonian class to change notation."
        )

    def __eq__(self, other):
        # Note semi-private attributes are compared intentionally, as
        # public ones will raise an error if not defined
        # If attributes are not defined in both notations,
        # then that attribute is considered equal.
        return (
            self._double_counting == other._double_counting
            and self._spin_normalized == other._spin_normalized
            and self._c22 == other._c22
            and self._c21 == other._c21
        )

    @staticmethod
    def get_predefined(name: str):
        r"""
        Returns one of the pre-defined notations.

        Parameters
        ----------
        name : str
            Name of the desired pre-defined notation. Supported are

            * "tb2j"
            * "spinw"
            * vampire"

            Case-insensitive.

        Returns
        -------
        notation : :py:class:`wulfric.spinham.Notation`

        Examples
        --------

        .. doctest::

            >>> import magnopy
            >>> tb2j = magnopy.spinham.Notation.get_predefined("TB2J")
            >>> tb2j.summary()
            tb2j notation where
            * Bonds are counted twice in the sum;
            * Spin vectors are normalized to 1;
            * c22 = -1.0;
            * c21 = -1.0.
            >>> spinW = magnopy.spinham.Notation.get_predefined("spinW")
            >>> spinW.summary()
            spinw notation where
            * Bonds are counted twice in the sum;
            * Spin vectors are not normalized;
            * c22 = 1.0;
            * c21 = 1.0.
            >>> vampire = magnopy.spinham.Notation.get_predefined("Vampire")
            >>> vampire.summary()
            vampire notation where
            * Bonds are counted twice in the sum;
            * Spin vectors are normalized to 1;
            * c22 = -1.0;
            * c21 = -0.5.
        """

        name = name.lower()

        if name not in _NOTATIONS:
            ValueError(f"'{name}' notation is undefined.")

        return Notation(
            name=name,
            double_counting=_NOTATIONS[name][0],
            spin_normalized=_NOTATIONS[name][1],
            c21=_NOTATIONS[name][2],
            c22=_NOTATIONS[name][3],
        )


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
