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
def test_c21(value, new_value):
    notation = Notation(c21=value)

    assert notation.c21 == value

    with pytest.raises(AttributeError):
        notation.c21 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c21(c21):
    notation1 = Notation(c21=c21)
    notation2 = Notation(c21=c21)
    notation3 = Notation(c21=3 if c21 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_c22(value, new_value):
    notation = Notation(c22=value)

    assert notation.c22 == value

    with pytest.raises(AttributeError):
        notation.c22 = new_value


@given(st.floats(allow_nan=False))
def test_eq_c22(c22):
    notation1 = Notation(c22=c22)
    notation2 = Notation(c22=c22)
    notation3 = Notation(c22=3 if c22 != 3 else 4)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4
