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

from magnopy.magnons._representations import PolynomialParameter


@given(st.integers(), st.integers())
def test_PolynomialParameter_errors_zeros(n, m):
    A = PolynomialParameter()

    if n >= 0 and m >= 0 and n >= m:
        assert A[n, m] == 0.0
    else:
        with pytest.raises(ValueError):
            A[n, m]


def test_PolynomialParameter():
    A = PolynomialParameter()

    assert A.nmax == -1

    A[0, 0] = 1
    assert A.nmax == 0

    A[2, 1] = 3
    assert A.nmax == 2
