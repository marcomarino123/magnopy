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

from magnopy import ConventionError, Notation


def tes_raises():
    notation = Notation()

    with pytest.raises(ConventionError):
        notation.multiple_counting

    with pytest.raises(ConventionError):
        notation.spin_normalized

    with pytest.raises(ConventionError):
        notation.c1

    with pytest.raises(ConventionError):
        notation.c21

    with pytest.raises(ConventionError):
        notation.c22

    with pytest.raises(ConventionError):
        notation.c31

    with pytest.raises(ConventionError):
        notation.c32

    with pytest.raises(ConventionError):
        notation.c33

    with pytest.raises(ConventionError):
        notation.c41

    with pytest.raises(ConventionError):
        notation.c421

    with pytest.raises(ConventionError):
        notation.c422

    with pytest.raises(ConventionError):
        notation.c43

    with pytest.raises(ConventionError):
        notation.c44


@given(st.text())
def test_name(name):
    notation = Notation()

    assert notation.name == "custom"

    notation.name = name

    assert notation.name == name.lower()


def test_get_predefined():
    notation = Notation.get_predefined(name="tb2j")
    notation = Notation.get_predefined(name="vampire")
    notation = Notation.get_predefined(name="spinW")
