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
ARRAY_3X3X3 = harrays(
    np.float64,
    (3, 3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)


@given(st.integers(), ARRAY_3X3X3)
def test_add_31(atom, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if not 0 <= atom < len(spinham.atoms.names):
        with pytest.raises(ValueError):
            spinham.add_31(atom, parameter)
    else:
        spinham.add_31(atom, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    ARRAY_3X3X3,
)
def test_add_31_sorting(atom1, atom2, atom3, atom4, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    spinham.add_31(atom1, parameter)

    if atom2 == atom1:
        with pytest.raises(ValueError):
            spinham.add_31(atom2, parameter)
    else:
        spinham.add_31(atom2, parameter)

    spinham.add_31(atom3, parameter, replace=True)
    spinham.add_31(atom4, parameter, replace=True)

    for i in range(len(spinham._31) - 1):
        assert spinham._31[i][0] <= spinham._31[i + 1][0]


@given(st.integers())
def test_remove_31(r_atom):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for i in range(len(spinham.atoms.names)):
        spinham.add_31(i, i * np.eye(3))

    if 0 <= r_atom < len(spinham.atoms.names):
        spinham.remove_31(r_atom)
        assert len(spinham._31) == len(spinham.atoms.names) - 1

        atoms_with_on_site = []
        for atom, _ in spinham._31:
            atoms_with_on_site.append(atom)

        assert r_atom not in atoms_with_on_site

    else:
        with pytest.raises(ValueError):
            spinham.remove_31(r_atom)
