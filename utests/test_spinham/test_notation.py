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


from math import isnan

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from magnopy._exceptions import NotationError
from magnopy.spinham._notation import Notation


def test_Notation_raises():
    notation = Notation()

    with pytest.raises(NotationError):
        notation.multiple_counting

    with pytest.raises(NotationError):
        notation.spin_normalized

    with pytest.raises(NotationError):
        notation.c21

    with pytest.raises(NotationError):
        notation.c22


@given(st.text())
def test_Notation_name(name):
    notation = Notation()

    assert notation.name == "custom"

    notation.name = name

    assert notation.name == name.lower()


@given(st.booleans(), st.booleans())
def test_Notation_multiple_counting(value, new_value):
    notation = Notation(multiple_counting=value)

    assert notation.multiple_counting == value

    with pytest.raises(AttributeError):
        notation.multiple_counting = new_value


@given(st.booleans(), st.booleans())
def test_Notation_spin_normalized(value, new_value):
    notation = Notation(spin_normalized=value)

    assert notation.spin_normalized == value

    with pytest.raises(AttributeError):
        notation.spin_normalized = new_value


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_Notation_c21(value, new_value):
    notation = Notation(c21=value)

    assert notation.c21 == value

    with pytest.raises(AttributeError):
        notation.c21 = new_value


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_Notation_c22(value, new_value):
    notation = Notation(c22=value)

    assert notation.c22 == value

    with pytest.raises(AttributeError):
        notation.c22 = new_value


@given(
    st.booleans(), st.booleans(), st.floats(allow_nan=False), st.floats(allow_nan=False)
)
def test_Notation_eq_dc(dc, sn, c21, c22):
    notation1 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation2 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation3 = Notation(multiple_counting=not dc, spin_normalized=sn, c21=c21, c22=c22)
    notation4 = Notation()
    notation5 = Notation(multiple_counting=dc)
    notation6 = Notation(multiple_counting=dc)

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation3 != notation4
    assert notation5 == notation6


@given(
    st.booleans(), st.booleans(), st.floats(allow_nan=False), st.floats(allow_nan=False)
)
def test_Notation_eq_sn(dc, sn, c21, c22):
    notation1 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation2 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation3 = Notation(multiple_counting=dc, spin_normalized=not sn, c21=c21, c22=c22)
    notation4 = Notation()
    notation5 = Notation(spin_normalized=sn)
    notation6 = Notation(spin_normalized=sn)

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation3 != notation4
    assert notation5 == notation6


@given(
    st.booleans(), st.booleans(), st.floats(allow_nan=False), st.floats(allow_nan=False)
)
def test_Notation_eq_c21(dc, sn, c21, c22):
    notation1 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation2 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation3 = Notation(
        multiple_counting=dc, spin_normalized=sn, c21=3 if c21 != 3 else 4, c22=c22
    )
    notation4 = Notation()
    notation5 = Notation(c21=c21)
    notation6 = Notation(c21=c21)

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation3 != notation4
    assert notation5 == notation6


@given(
    st.booleans(), st.booleans(), st.floats(allow_nan=False), st.floats(allow_nan=False)
)
def test_Notation_eq_c22(dc, sn, c21, c22):
    notation1 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation2 = Notation(multiple_counting=dc, spin_normalized=sn, c21=c21, c22=c22)
    notation3 = Notation(
        multiple_counting=dc, spin_normalized=sn, c21=c21, c22=3 if c22 != 3 else 4
    )
    notation4 = Notation()
    notation5 = Notation(c22=c22)
    notation6 = Notation(c22=c22)

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation3 != notation4
    assert notation5 == notation6


def test_Notation_get_predefined():
    notation = Notation.get_predefined(name="tb2j")
    notation = Notation.get_predefined(name="vampire")
    notation = Notation.get_predefined(name="spinW")
