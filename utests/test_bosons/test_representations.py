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

from hypothesis import given
from hypothesis import strategies as st

from magnopy.bosons._representations import get_hp_newton


@given(
    st.floats(min_value=0, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_0_one_site(spin):
    A, B = get_hp_newton(spin_values=[spin], n_max=0)

    assert len(A) == 1
    assert len(B) == 1
    assert len(A[0]) == 1
    assert len(B[0]) == 1

    A0 = sqrt(2 * spin)

    assert abs(A[0][0] - A0) < 1e-8
    assert abs(B[0][0] - A0) < 1e-8


@given(
    st.floats(min_value=0, max_value=1e8, allow_subnormal=False),
    st.floats(min_value=0, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_0_two_sites(spin1, spin2):
    spins = [spin1, spin2]
    A, B = get_hp_newton(spin_values=spins, n_max=0)

    assert len(A) == 2
    assert len(B) == 2

    for i in range(2):
        A0 = sqrt(2 * spins[i])
        assert len(A[i]) == 1
        assert len(B[i]) == 1

        assert abs(A[i][0] - A0) < 1e-8
        assert abs(B[i][0] - A0) < 1e-8


@given(
    st.floats(min_value=0.5, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_1_one_site(spin):
    A, B = get_hp_newton(spin_values=[spin], n_max=1)

    assert len(A) == 1
    assert len(B) == 1
    assert len(A[0]) == 2
    assert len(B[0]) == 2

    A0 = sqrt(2 * spin)
    A1 = -sqrt(2 * spin) + sqrt(2 * spin - 1)

    assert abs(A[0][0] - A0) < 1e-8
    assert abs(B[0][0] - A0) < 1e-8
    assert abs(A[0][1] - A1) < 1e-8
    assert abs(B[0][1] - A1) < 1e-8


@given(
    st.floats(min_value=0.5, max_value=1e8, allow_subnormal=False),
    st.floats(min_value=0.5, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_1_two_sites(spin1, spin2):
    spins = [spin1, spin2]
    A, B = get_hp_newton(spin_values=spins, n_max=1)

    assert len(A) == 2
    assert len(B) == 2

    for i in range(2):
        assert len(A[i]) == 2
        assert len(B[i]) == 2

        A0 = sqrt(2 * spins[i])
        A1 = -sqrt(2 * spins[i]) + sqrt(2 * spins[i] - 1)

        assert abs(A[i][0] - A0) < 1e-8
        assert abs(B[i][0] - A0) < 1e-8
        assert abs(A[i][1] - A1) < 1e-8
        assert abs(B[i][1] - A1) < 1e-8


@given(
    st.floats(min_value=1, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_2_one_site(spin):
    A, B = get_hp_newton(spin_values=[spin], n_max=2)

    assert len(A) == 1
    assert len(B) == 1
    assert len(A[0]) == 3
    assert len(B[0]) == 3

    A0 = sqrt(2 * spin)
    A1 = -sqrt(2 * spin) + sqrt(2 * spin - 1)
    A2 = 0.5 * sqrt(2 * spin) - sqrt(2 * spin - 1) + 1 / sqrt(2) * sqrt(spin - 1)

    assert abs(A[0][0] - A0) < 1e-8
    assert abs(B[0][0] - A0) < 1e-8
    assert abs(A[0][1] - A1) < 1e-8
    assert abs(B[0][1] - A1) < 1e-8
    assert abs(A[0][2] - A2) < 1e-8
    assert abs(B[0][2] - A2) < 1e-8


@given(
    st.floats(min_value=1.5, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_3_one_site(spin):
    A, B = get_hp_newton(spin_values=[spin], n_max=3)

    assert len(A) == 1
    assert len(B) == 1
    assert len(A[0]) == 4
    assert len(B[0]) == 4

    A0 = sqrt(2 * spin)
    A1 = -sqrt(2 * spin) + sqrt(2 * spin - 1)
    A2 = 0.5 * sqrt(2 * spin) - sqrt(2 * spin - 1) + 1 / sqrt(2) * sqrt(spin - 1)
    A3 = (
        -1 / 6 * sqrt(2 * spin)
        + 0.5 * sqrt(2 * spin - 1)
        - 0.5 * sqrt(2 * spin - 2)
        + 1 / 6 * sqrt(2 * spin - 3)
    )

    assert abs(A[0][0] - A0) < 1e-8
    assert abs(B[0][0] - A0) < 1e-8
    assert abs(A[0][1] - A1) < 1e-8
    assert abs(B[0][1] - A1) < 1e-8
    assert abs(A[0][2] - A2) < 1e-8
    assert abs(B[0][2] - A2) < 1e-8
    assert abs(A[0][3] - A3) < 1e-8
    assert abs(B[0][3] - A3) < 1e-8


@given(
    st.floats(min_value=2, max_value=1e8, allow_subnormal=False),
)
def test_get_hp_newton_max_4_one_site(spin):
    A, B = get_hp_newton(spin_values=[spin], n_max=4)

    assert len(A) == 1
    assert len(B) == 1
    assert len(A[0]) == 5
    assert len(B[0]) == 5

    A0 = sqrt(2 * spin)
    A1 = -sqrt(2 * spin) + sqrt(2 * spin - 1)
    A2 = 0.5 * sqrt(2 * spin) - sqrt(2 * spin - 1) + 1 / sqrt(2) * sqrt(spin - 1)
    A3 = (
        -1 / 6 * sqrt(2 * spin)
        + 0.5 * sqrt(2 * spin - 1)
        - 0.5 * sqrt(2 * spin - 2)
        + 1 / 6 * sqrt(2 * spin - 3)
    )
    A4 = (
        1 / 24 * sqrt(2 * spin)
        - 1 / 6 * sqrt(2 * spin - 1)
        + 0.25 * sqrt(2 * spin - 2)
        - 1 / 6 * sqrt(2 * spin - 3)
        + 1 / 24 * sqrt(2 * spin - 4)
    )

    assert abs(A[0][0] - A0) < 1e-8
    assert abs(B[0][0] - A0) < 1e-8
    assert abs(A[0][1] - A1) < 1e-8
    assert abs(B[0][1] - A1) < 1e-8
    assert abs(A[0][2] - A2) < 1e-8
    assert abs(B[0][2] - A2) < 1e-8
    assert abs(A[0][3] - A3) < 1e-8
    assert abs(B[0][3] - A3) < 1e-8
    assert abs(A[0][4] - A4) < 1e-8
    assert abs(B[0][4] - A4) < 1e-8
