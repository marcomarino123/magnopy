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

from magnopy.spinham._c22 import _get_primary_p22
from magnopy.spinham._hamiltonian import SpinHamiltonian
from magnopy.spinham._notation import Notation

MAX_MODULUS = 1e8
ARRAY_3X3 = harrays(
    np.float64,
    (3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)
RANDOM_UC = harrays(int, (10, 3), elements=st.integers(min_value=-1000, max_value=1000))


@given(
    st.integers(),
    st.integers(),
    st.tuples(st.integers(), st.integers(), st.integers()),
    ARRAY_3X3,
)
def test_add_22(atom1, atom2, ijk, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if not 0 <= atom1 < len(spinham.atoms.names) or not 0 <= atom2 < len(
        spinham.atoms.names
    ):
        with pytest.raises(ValueError):
            spinham.add_22(atom1, atom2, ijk, parameter)
    else:
        spinham.add_22(atom1, atom2, ijk, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    ARRAY_3X3,
)
def test_add_22_sorting(
    atom1_1,
    atom21,
    ijk_1,
    atom1_2,
    atom22,
    ijk_2,
    atom1_3,
    atom2_3,
    ijk_3,
    atom1_4,
    atom2_4,
    ijk_4,
    parameter,
):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    spinham.add_22(atom1_1, atom21, ijk_1, parameter)

    if (atom1_1, atom21, ijk_1) == (atom1_2, atom22, ijk_2):
        with pytest.raises(ValueError):
            spinham.add_22(atom1_2, atom22, ijk_2, parameter)
    else:
        spinham.add_22(atom1_2, atom22, ijk_2, parameter)

    spinham.add_22(atom1_3, atom2_3, ijk_3, parameter, replace=True)
    spinham.add_22(atom1_4, atom2_4, ijk_4, parameter, replace=True)

    for i in range(len(spinham._22) - 1):
        assert (spinham._22[i][0], spinham._22[i][1], spinham._22[i][2]) <= (
            spinham._22[i + 1][0],
            spinham._22[i + 1][1],
            spinham._22[i + 1][2],
        )


@given(
    st.integers(min_value=0, max_value=2),
    st.integers(min_value=0, max_value=2),
    st.tuples(st.integers(), st.integers(), st.integers()),
    RANDOM_UC,
)
def test_remove_22(r_atom1, r_atom2, r_ijk, unit_cells):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for i in range(len(spinham.atoms.names)):
        for j in range(i, len(spinham.atoms.names)):
            for ijk in unit_cells:
                ijk = (int(ijk[0]), int(ijk[1]), int(ijk[2]))
                spinham.add_22(i, j, ijk, np.eye(3), replace=True)

    if 0 <= r_atom1 < len(spinham.atoms.names) and 0 <= r_atom2 < len(
        spinham.atoms.names
    ):
        bonds_22 = []
        for atom1, atom2, ijk, _ in spinham._22:
            bonds_22.append((atom1, atom2, ijk))
        prev_length = len(spinham._22)

        spinham.remove_22(r_atom1, r_atom2, r_ijk)

        r_bond = _get_primary_p22(r_atom1, r_atom2, r_ijk)
        if r_bond in bonds_22:
            assert len(spinham._22) == prev_length - 1
            bonds_22 = []
            for atom1, atom2, ijk, _ in spinham._22:
                bonds_22.append((atom1, atom2, ijk))
            assert (r_atom1, r_atom2, r_ijk) not in bonds_22
        else:
            assert len(spinham._22) == prev_length

    else:
        with pytest.raises(ValueError):
            spinham.remove_22(r_atom1, r_atom2, r_ijk)
