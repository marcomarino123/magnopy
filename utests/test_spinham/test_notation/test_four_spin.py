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


import pytest
from hypothesis import given
from hypothesis import strategies as st

from magnopy.spinham._notation import Notation


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c41(value, new_value):
    notation = Notation(c41=value)

    assert notation.c41 == value

    with pytest.raises(AttributeError):
        notation.c41 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c41(c41):
    notation1 = Notation(c41=c41)
    notation2 = Notation(c41=c41)
    notation3 = Notation(c41=3 if c41 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c421(value, new_value):
    notation = Notation(c421=value)

    assert notation.c421 == value

    with pytest.raises(AttributeError):
        notation.c421 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c421(c421):
    notation1 = Notation(c421=c421)
    notation2 = Notation(c421=c421)
    notation3 = Notation(c421=3 if c421 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c422(value, new_value):
    notation = Notation(c422=value)

    assert notation.c422 == value

    with pytest.raises(AttributeError):
        notation.c422 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c422(c422):
    notation1 = Notation(c422=c422)
    notation2 = Notation(c422=c422)
    notation3 = Notation(c422=3 if c422 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c43(value, new_value):
    notation = Notation(c43=value)

    assert notation.c43 == value

    with pytest.raises(AttributeError):
        notation.c43 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c43(c43):
    notation1 = Notation(c43=c43)
    notation2 = Notation(c43=c43)
    notation3 = Notation(c43=3 if c43 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c44(value, new_value):
    notation = Notation(c44=value)

    assert notation.c44 == value

    with pytest.raises(AttributeError):
        notation.c44 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c44(c44):
    notation1 = Notation(c44=c44)
    notation2 = Notation(c44=c44)
    notation3 = Notation(c44=3 if c44 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4
