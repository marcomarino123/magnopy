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

from magnopy.spinham._hamiltonian import SpinHamiltonian
from magnopy.spinham._notation import Notation

MAX_MODULUS = 1e8
ARRAY_3 = harrays(
    np.float64,
    (3,),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)


@given(st.integers(), ARRAY_3)
def test_add_1(alpha, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if 0 <= alpha < len(spinham.atoms.names):
        spinham.add_1(alpha, parameter)
    else:
        with pytest.raises(ValueError):
            spinham.add_1(alpha, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    ARRAY_3,
)
def test_add_1_sorting(alpha1, alpha2, alpha3, alpha4, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    spinham.add_1(alpha1, parameter)

    if alpha2 == alpha1:
        with pytest.raises(ValueError):
            spinham.add_1(alpha2, parameter)
    else:
        spinham.add_1(alpha2, parameter)

    spinham.add_1(alpha3, parameter, replace=True)
    spinham.add_1(alpha4, parameter, replace=True)

    for i in range(len(spinham._1) - 1):
        assert spinham._1[i][:-1] <= spinham._1[i + 1][:-1]


@given(st.integers())
def test_remove_1(r_alpha):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for alpha in range(len(spinham.atoms.names)):
        spinham.add_1(alpha, np.eye(3))

    bond = [r_alpha]
    if 0 <= r_alpha < len(spinham.atoms.names):
        original_bonds = [tmp[:-1] for tmp in spinham._1]
        original_length = len(spinham._1)

        spinham.remove_1(*bond)

        if bond in original_bonds:
            updated_bonds = [tmp[:-1] for tmp in spinham._1]

            assert len(spinham._1) == original_length - 1
            assert bond not in updated_bonds
        else:
            assert len(spinham._1) == original_length
    else:
        with pytest.raises(ValueError):
            spinham.remove_1(*bond)
