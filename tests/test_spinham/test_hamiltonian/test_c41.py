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
ARRAY_3x3x3x3 = harrays(
    np.float64,
    (3, 3, 3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)


@given(st.integers(), ARRAY_3x3x3x3)
def test_add_41(alpha, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    if 0 <= alpha < len(spinham.atoms.names):
        spinham.add_41(alpha, parameter)
    else:
        with pytest.raises(ValueError):
            spinham.add_41(alpha, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    ARRAY_3x3x3x3,
)
def test_add_41_sorting(alpha1, alpha2, alpha3, alpha4, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_41(alpha1, parameter)

    if alpha2 == alpha1:
        with pytest.raises(ValueError):
            spinham.add_41(alpha2, parameter)
    else:
        spinham.add_41(alpha2, parameter)

    spinham.add_41(alpha3, parameter, replace=True)
    spinham.add_41(alpha4, parameter, replace=True)

    for i in range(len(spinham._41) - 1):
        assert spinham._41[i][:-1] <= spinham._41[i + 1][:-1]


@given(st.integers())
def test_remove_41(r_alpha):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    for alpha in range(len(spinham.atoms.names)):
        spinham.add_41(alpha, np.eye(3))

    bond = [r_alpha]
    if 0 <= r_alpha < len(spinham.atoms.names):
        original_bonds = [tmp[:-1] for tmp in spinham._41]
        original_length = len(spinham._41)

        spinham.remove_41(*bond)

        if bond in original_bonds:
            updated_bonds = [tmp[:-1] for tmp in spinham._41]

            assert len(spinham._41) == original_length - 1
            assert bond not in updated_bonds
        else:
            assert len(spinham._41) == original_length
    else:
        with pytest.raises(ValueError):
            spinham.remove_41(*bond)


@given(ARRAY_3x3x3x3, st.floats(min_value=0.1, max_value=1e4))
def test_mul(parameter, number):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_21(alpha=0, parameter=parameter)
    spinham.add_21(alpha=4, parameter=parameter * 1.32)
    spinham.add_21(alpha=7, parameter=parameter / 3)

    m_spinham = spinham * number

    assert spinham.M == m_spinham.M

    assert len(spinham.p41) == len(m_spinham.p41)

    params = list(spinham.p41)
    m_params = list(m_spinham.p41)
    for i in range(len(params)):
        assert params[i][0] == m_params[i][0]

        assert np.allclose(number * params[i][1], m_params[i][1])


@given(ARRAY_3x3x3x3, st.floats(min_value=0.1, max_value=1e4))
def test_rmul(parameter, number):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_21(alpha=0, parameter=parameter)
    spinham.add_21(alpha=4, parameter=parameter * 1.32)
    spinham.add_21(alpha=7, parameter=parameter / 3)

    m_spinham = number * spinham

    assert spinham.M == m_spinham.M

    assert len(spinham.p41) == len(m_spinham.p41)

    params = list(spinham.p41)
    m_params = list(m_spinham.p41)
    for i in range(len(params)):
        assert params[i][0] == m_params[i][0]

        assert np.allclose(number * params[i][1], m_params[i][1])
