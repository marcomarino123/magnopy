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

from magnopy import Notation


################################################################################
#                                Spin normalized                               #
################################################################################
@given(st.booleans(), st.booleans())
def test_spin_normalized(value, new_value):
    notation = Notation(spin_normalized=value)

    assert notation.spin_normalized == value

    with pytest.raises(AttributeError):
        notation.spin_normalized = new_value


@given(st.booleans())
def test_eq_spin_normalized(sn):
    notation1 = Notation(spin_normalized=sn)
    notation2 = Notation(spin_normalized=sn)
    notation3 = Notation(spin_normalized=not sn)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


def test_get_modified_spin_normalized():
    notation = Notation(
        spin_normalized=True,
        multiple_counting=True,
        c1=1,
        c21=1,
        c22=1,
        c31=1,
        c32=1,
        c33=1,
        c41=1,
        c421=1,
        c422=1,
        c43=1,
        c44=1,
    )

    mod_notation = notation.get_modified(spin_normalized=False)

    assert mod_notation.spin_normalized == False
    assert mod_notation.multiple_counting == True
    assert mod_notation.c1 == 1
    assert mod_notation.c21 == 1
    assert mod_notation.c22 == 1
    assert mod_notation.c31 == 1
    assert mod_notation.c32 == 1
    assert mod_notation.c33 == 1
    assert mod_notation.c41 == 1
    assert mod_notation.c421 == 1
    assert mod_notation.c422 == 1
    assert mod_notation.c43 == 1
    assert mod_notation.c44 == 1


################################################################################
#                               Multiple counting                              #
################################################################################
@given(st.booleans(), st.booleans())
def test_multiple_counting(value, new_value):
    notation = Notation(multiple_counting=value)

    assert notation.multiple_counting == value

    with pytest.raises(AttributeError):
        notation.multiple_counting = new_value


@given(st.booleans())
def test_eq_multiple_counting(mc):
    notation1 = Notation(multiple_counting=mc)
    notation2 = Notation(multiple_counting=mc)
    notation3 = Notation(multiple_counting=not mc)
    notation4 = Notation()

    assert notation1 == notation2
    assert notation1 != notation3
    assert notation1 != notation4
    assert notation2 != notation3
    assert notation2 != notation4
    assert notation3 != notation4


def test_get_modified_multiple_counting():
    notation = Notation(
        spin_normalized=True,
        multiple_counting=True,
        c1=1,
        c21=1,
        c22=1,
        c31=1,
        c32=1,
        c33=1,
        c41=1,
        c421=1,
        c422=1,
        c43=1,
        c44=1,
    )

    mod_notation = notation.get_modified(multiple_counting=False)

    assert mod_notation.spin_normalized == True
    assert mod_notation.multiple_counting == False
    assert mod_notation.c1 == 1
    assert mod_notation.c21 == 1
    assert mod_notation.c22 == 1
    assert mod_notation.c31 == 1
    assert mod_notation.c32 == 1
    assert mod_notation.c33 == 1
    assert mod_notation.c41 == 1
    assert mod_notation.c421 == 1
    assert mod_notation.c422 == 1
    assert mod_notation.c43 == 1
    assert mod_notation.c44 == 1
