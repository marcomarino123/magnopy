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
ARRAY_3x3 = harrays(
    np.float64,
    (3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)


@given(st.integers(), ARRAY_3x3)
def test_add_21(alpha, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    if 0 <= alpha < len(spinham.atoms.names):
        spinham.add_21(alpha, parameter)
    else:
        with pytest.raises(ValueError):
            spinham.add_21(alpha, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    ARRAY_3x3,
)
def test_add_21_sorting(alpha1, alpha2, alpha3, alpha4, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_21(alpha1, parameter)

    if alpha2 == alpha1:
        with pytest.raises(ValueError):
            spinham.add_21(alpha2, parameter)
    else:
        spinham.add_21(alpha2, parameter)

    spinham.add_21(alpha3, parameter, replace=True)
    spinham.add_21(alpha4, parameter, replace=True)

    for i in range(len(spinham._21) - 1):
        assert spinham._21[i][:-1] <= spinham._21[i + 1][:-1]


@given(st.integers())
def test_remove_21(r_alpha):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    for alpha in range(len(spinham.atoms.names)):
        spinham.add_21(alpha, np.eye(3))

    bond = [r_alpha]
    if 0 <= r_alpha < len(spinham.atoms.names):
        original_bonds = [tmp[:-1] for tmp in spinham._21]
        original_length = len(spinham._21)

        spinham.remove_21(*bond)

        if bond in original_bonds:
            updated_bonds = [tmp[:-1] for tmp in spinham._21]

            assert len(spinham._21) == original_length - 1
            assert bond not in updated_bonds
        else:
            assert len(spinham._21) == original_length
    else:
        with pytest.raises(ValueError):
            spinham.remove_21(*bond)


@given(ARRAY_3x3, st.floats(min_value=0.1, max_value=1e4))
def test_mul(parameter, number):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_21(alpha=0, parameter=parameter)
    spinham.add_21(alpha=4, parameter=parameter * 1.32)
    spinham.add_21(alpha=7, parameter=parameter / 3)

    m_spinham = spinham * number

    assert spinham.M == m_spinham.M

    assert len(spinham.p21) == len(m_spinham.p21)

    params = list(spinham.p21)
    m_params = list(m_spinham.p21)
    for i in range(len(params)):
        assert params[i][0] == m_params[i][0]

        assert np.allclose(number * params[i][1], m_params[i][1])


@given(ARRAY_3x3, st.floats(min_value=0.1, max_value=1e4))
def test_rmul(parameter, number):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham.add_21(alpha=0, parameter=parameter)
    spinham.add_21(alpha=4, parameter=parameter * 1.32)
    spinham.add_21(alpha=7, parameter=parameter / 3)

    m_spinham = number * spinham

    assert spinham.M == m_spinham.M

    assert len(spinham.p21) == len(m_spinham.p21)

    params = list(spinham.p21)
    m_params = list(m_spinham.p21)
    for i in range(len(params)):
        assert params[i][0] == m_params[i][0]

        assert np.allclose(number * params[i][1], m_params[i][1])


@given(ARRAY_3x3, ARRAY_3x3)
def test_add(parameter1, parameter2):
    atoms = dict(
        names=["Cr" for _ in range(9)],
        spins=[1 for _ in range(9)],
        positions=[[0.1 * i, 0, 0] for i in range(9)],
        g_factors=[2 for _ in range(9)],
    )

    spinham1 = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())
    spinham2 = SpinHamiltonian(cell=np.eye(3), atoms=atoms, convention=Convention())

    spinham1.add_21(alpha=0, parameter=parameter1)
    spinham1.add_21(alpha=4, parameter=parameter1 * 1.32)
    spinham1.add_21(alpha=7, parameter=parameter1 / 3)

    spinham2.add_21(alpha=0, parameter=parameter2)
    spinham2.add_21(alpha=4, parameter=parameter2 * 1.32)
    spinham2.add_21(alpha=8, parameter=parameter2 / 3)

    m_spinham = spinham1 + spinham2

    assert m_spinham.M == 4

    assert len(m_spinham.p21) == 4

    for i in range(2):
        assert np.allclose(m_spinham._21[i][1], spinham1._21[i][1] + spinham2._21[i][1])

    assert np.allclose(m_spinham._21[2][1], spinham1._21[2][1])
    assert np.allclose(m_spinham._21[3][1], spinham2._21[2][1])
