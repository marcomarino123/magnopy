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


import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays as harrays

from magnopy import Convention, SpinHamiltonian

MAX_MODULUS = 1e8
ARRAY_3 = harrays(
    np.float64,
    (3,),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)


@given(st.integers(), ARRAY_3)
def test_add_remove(alpha, h):
    atoms = {
        "names": ["Cr" for _ in range(9)],
        "spins": [1 for _ in range(9)],
        "g_factors": [2 for _ in range(9)],
    }

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    for i in range(9):
        spinham.add_21(alpha=i, parameter=np.eye(3))

    assert len(spinham.p1) == 0

    spinham.add_magnetic_field(h=h)
    assert len(spinham.p1) == 9

    spinham.add_magnetic_field(h=-h)
    assert np.allclose(np.zeros((9, 3)), [parameter for _, parameter in spinham.p1])


@given(st.integers(), ARRAY_3)
def test_double_add(alpha, h):
    atoms = {
        "names": ["Cr" for _ in range(9)],
        "spins": [1 for _ in range(9)],
        "g_factors": [2 for _ in range(9)],
    }

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    for i in range(9):
        spinham.add_21(alpha=i, parameter=np.eye(3))

    assert len(spinham.p1) == 0

    spinham.add_magnetic_field(h=h)

    params = np.array([parameter for _, parameter in spinham.p1])

    spinham.add_magnetic_field(h=h)

    double_params = np.array([parameter for _, parameter in spinham.p1])

    assert np.allclose(2 * params, double_params)
