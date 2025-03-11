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

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays as harrays

from magnopy.spinham._hamiltonian import SpinHamiltonian, _get_P22_prime
from magnopy.spinham._notation import Notation
from magnopy.spinham._parameter import (
    get_anisotropic_parameter,
    get_dmi,
    get_isotropic_parameter,
    get_matrix_parameter,
)

MAX_MODULUS = 1e8
ARRAY_3X3 = harrays(
    np.float64,
    (3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)
ARRAY_3 = harrays(
    np.float64,
    (3,),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)
RANDOM_UC = harrays(int, (10, 3), elements=st.integers(min_value=-1000, max_value=1000))


@given(st.integers(), ARRAY_3X3)
def test_add_2_1(atom, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if not 0 <= atom < len(spinham.atoms.names):
        with pytest.raises(ValueError):
            spinham.add_2_1(atom, parameter)
    else:
        spinham.add_2_1(atom, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    ARRAY_3X3,
)
def test_add_2_1_sorting(atom1, atom2, atom3, atom4, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    spinham.add_2_1(atom1, parameter)

    if atom2 == atom1:
        with pytest.raises(ValueError):
            spinham.add_2_1(atom2, parameter)
    else:
        spinham.add_2_1(atom2, parameter)

    spinham.add_2_1(atom3, parameter, replace=True)
    spinham.add_2_1(atom4, parameter, replace=True)

    for i in range(len(spinham._2_1) - 1):
        assert spinham._2_1[i][0] <= spinham._2_1[i + 1][0]


@given(
    st.integers(),
    st.integers(),
    st.tuples(st.integers(), st.integers(), st.integers()),
    ARRAY_3X3,
)
def test_add_2_2(atom1, atom2, ijk, parameter):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if not 0 <= atom1 < len(spinham.atoms.names) or not 0 <= atom2 < len(
        spinham.atoms.names
    ):
        with pytest.raises(ValueError):
            spinham.add_2_2(atom1, atom2, ijk, parameter)
    else:
        spinham.add_2_2(atom1, atom2, ijk, parameter)


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
def test_add_2_2_sorting(
    atom1_1,
    atom2_1,
    ijk_1,
    atom1_2,
    atom2_2,
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

    spinham.add_2_2(atom1_1, atom2_1, ijk_1, parameter)

    if (atom1_1, atom2_1, ijk_1) == (atom1_2, atom2_2, ijk_2):
        with pytest.raises(ValueError):
            spinham.add_2_2(atom1_2, atom2_2, ijk_2, parameter)
    else:
        spinham.add_2_2(atom1_2, atom2_2, ijk_2, parameter)

    spinham.add_2_2(atom1_3, atom2_3, ijk_3, parameter, replace=True)
    spinham.add_2_2(atom1_4, atom2_4, ijk_4, parameter, replace=True)

    for i in range(len(spinham._2_2) - 1):
        assert (spinham._2_2[i][0], spinham._2_2[i][1], spinham._2_2[i][2]) <= (
            spinham._2_2[i + 1][0],
            spinham._2_2[i + 1][1],
            spinham._2_2[i + 1][2],
        )


@given(st.integers())
def test_remove_2_1(r_atom):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for i in range(len(spinham.atoms.names)):
        spinham.add_2_1(i, i * np.eye(3))

    if 0 <= r_atom < len(spinham.atoms.names):
        spinham.remove_2_1(r_atom)
        assert len(spinham._2_1) == len(spinham.atoms.names) - 1

        atoms_with_on_site = []
        for atom, _ in spinham._2_1:
            atoms_with_on_site.append(atom)

        assert r_atom not in atoms_with_on_site

    else:
        with pytest.raises(ValueError):
            spinham.remove_2_1(r_atom)


@given(
    st.integers(min_value=0, max_value=2),
    st.integers(min_value=0, max_value=2),
    st.tuples(st.integers(), st.integers(), st.integers()),
    RANDOM_UC,
)
def test_remove_2_2(r_atom1, r_atom2, r_ijk, unit_cells):
    atoms = {"names": ["Cr", "Cr", "Cr", "Cr"]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for i in range(len(spinham.atoms.names)):
        for j in range(i, len(spinham.atoms.names)):
            for ijk in unit_cells:
                ijk = (int(ijk[0]), int(ijk[1]), int(ijk[2]))
                spinham.add_2_2(i, j, ijk, np.eye(3), replace=True)

    if 0 <= r_atom1 < len(spinham.atoms.names) and 0 <= r_atom2 < len(
        spinham.atoms.names
    ):
        bonds_22 = []
        for atom1, atom2, ijk, _ in spinham._2_2:
            bonds_22.append((atom1, atom2, ijk))
        prev_length = len(spinham._2_2)

        spinham.remove_2_2(r_atom1, r_atom2, r_ijk)

        r_bond = _get_P22_prime(r_atom1, r_atom2, r_ijk)
        if r_bond in bonds_22:
            assert len(spinham._2_2) == prev_length - 1
            bonds_22 = []
            for atom1, atom2, ijk, _ in spinham._2_2:
                bonds_22.append((atom1, atom2, ijk))
            assert (r_atom1, r_atom2, r_ijk) not in bonds_22
        else:
            assert len(spinham._2_2) == prev_length

    else:
        with pytest.raises(ValueError):
            spinham.remove_2_2(r_atom1, r_atom2, r_ijk)


def test_notation_multiple_counting():
    spinham = SpinHamiltonian(
        cell=np.eye(3),
        atoms={"names": ["Cr1", "Cr2"]},
        notation=Notation(multiple_counting=True),
    )

    spinham.add_2_1(0, np.eye(3))
    spinham.add_2_2(0, 1, (0, 0, 0), 1 * np.eye(3))
    spinham.add_2_2(0, 1, (1, 0, 0), 2 * np.eye(3))
    spinham.add_2_2(1, 0, (0, -1, 0), 2 * np.eye(3))

    assert len(spinham._2_2) == 3
    assert len(spinham.p22) == 6

    assert len(spinham._2_1) == 1
    assert len(spinham.p21) == 1

    params = list(spinham.p22)

    assert (params[0][3] == params[-1][3]).all()
    assert (params[1][3] == params[-2][3]).all()
    assert (params[2][3] == params[-3][3]).all()

    spinham.notation = Notation(multiple_counting=False)

    assert len(spinham._2_2) == 3
    assert len(spinham.p22) == 3

    assert len(spinham._2_1) == 1
    assert len(spinham.p21) == 1


def test_magnetic_atoms():
    spinham = SpinHamiltonian(
        cell=np.eye(3),
        atoms={"names": ["Cr1", "Cr2"]},
        notation=Notation(multiple_counting=True),
    )

    spinham.add_2_1(0, np.eye(3))
    assert len(spinham.magnetic_atoms) == 1
    assert spinham.I == 1
    assert spinham.magnetic_atoms[0] == 0

    spinham.add_2_2(0, 1, (0, 0, 0), 1 * np.eye(3))
    assert len(spinham.magnetic_atoms) == 2
    assert spinham.I == 2
    assert spinham.magnetic_atoms[0] == 0
    assert spinham.magnetic_atoms[1] == 1
    spinham.add_2_2(0, 1, (1, 0, 0), 2 * np.eye(3))
    assert len(spinham.magnetic_atoms) == 2
    assert spinham.I == 2
    assert spinham.magnetic_atoms[0] == 0
    assert spinham.magnetic_atoms[1] == 1
    spinham.add_2_2(1, 0, (0, -1, 0), 2 * np.eye(3))
    assert len(spinham.magnetic_atoms) == 2
    assert spinham.I == 2
    assert spinham.magnetic_atoms[0] == 0
    assert spinham.magnetic_atoms[1] == 1

    spinham.remove_atom(1)
    assert len(spinham.magnetic_atoms) == 1
    assert spinham.I == 1
    assert spinham.magnetic_atoms[0] == 0


################################################################################
#                                 Legacy Tests                                 #
################################################################################

# def test_iteration_exchange_like():
#     model = SpinHamiltonian()
#     Cr1 = Atom("Cr1", (0.25, 0.25, 0))
#     Cr2 = Atom("Cr2", (0.75, 0.75, 0))
#     model.add_atom(Cr1)
#     model.add_atom(Cr2)
#     bonds = [
#         (12, Cr1, Cr2, (0, 0, 0)),
#         (2, Cr2, Cr1, (0, 0, 0)),
#         (6, Cr1, Cr1, (1, 0, 0)),
#         (3.425, Cr1, Cr1, (-1, 0, 0)),
#         (5.3, Cr2, Cr2, (1, 0, 0)),
#         (7.34, Cr2, Cr2, (-1, 0, 0)),
#         (12.4, Cr1, Cr1, (0, 2, 0)),
#         (34, Cr1, Cr1, (0, -2, 0)),
#         (1.098, Cr2, Cr2, (0, 2, 0)),
#         (0.0054, Cr2, Cr2, (0, -2, 0)),
#         (0.35, Cr2, Cr1, (2, 2, 0)),
#         (-2.35, Cr1, Cr2, (-2, -2, 0)),
#     ]
#     model.add_on_site("Cr1", matrix=np.eye(3))
#     model.add_on_site("Cr2", matrix=np.eye(3))
#     for iso, atom1, atom2, R in bonds:
#         model.add_exchange(atom1, atom2, R, iso=iso)
#     with pytest.raises(NotationError):
#         assert len(model.exchange_like) == 14

#     model.exchange_factor = 1
#     model.on_site_factor = 1
#     assert len(model.exchange_like) == 14

#     for i, (atom1, atom2, R, parameter) in enumerate(model.exchange_like):
#         assert isinstance(atom1, Atom)
#         assert isinstance(atom2, Atom)
#         assert isinstance(R, tuple)
#         assert isinstance(parameter, MatrixParameter)


def test_remove_atom():
    spinham = SpinHamiltonian(
        cell=np.eye(3), atoms={"names": ["Cr1", "Cr2", "Cr3"]}, notation=Notation()
    )
    spinham.add_2_2(0, 1, (0, 0, 0), 12 * np.eye(3))
    spinham.add_2_2(1, 2, (0, 0, 0), 23 * np.eye(3))
    spinham.add_2_2(2, 0, (0, 0, 0), 31 * np.eye(3))
    spinham.add_2_1(0, np.eye(3))
    assert len(spinham._2_2) == 3
    assert len(spinham._2_1) == 1
    assert "Cr1" in spinham.atoms.names
    assert len(spinham.magnetic_atoms) == 3
    spinham.remove_atom(0)
    assert len(spinham.magnetic_atoms) == 2
    assert len(spinham._2_2) == 1
    assert len(spinham._2_1) == 0
    assert "Cr1" not in spinham.atoms.names


def test_filter():
    atoms = {"names": ["Cr1", "Cr2"], "positions": [(0.25, 0.25, 0), (0.75, 0.75, 0)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())
    bonds = [
        (12, 0, 1, (0, 0, 0)),
        (12, 0, 0, (1, 0, 0)),
        (12, 1, 1, (1, 0, 0)),
        (12, 0, 0, (0, 2, 0)),
        (12, 1, 1, (0, 2, 0)),
        (12, 1, 0, (2, 2, 0)),
    ]
    for iso, atom1, atom2, ijk in bonds:
        spinham.add_2_2(atom1, atom2, ijk, iso * np.eye(3))

    assert len(spinham._2_2) == 6
    spinham.filter_2_2(max_distance=1)
    assert len(spinham._2_2) == 3

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())
    bonds = [
        (12, 0, 1, (0, 0, 0)),
        (12, 0, 0, (1, 0, 0)),
        (12, 1, 1, (1, 0, 0)),
        (12, 0, 0, (0, 2, 0)),
        (12, 1, 1, (0, 2, 0)),
        (12, 1, 0, (2, 2, 0)),
    ]
    for iso, atom1, atom2, ijk in bonds:
        spinham.add_2_2(atom1, atom2, ijk, iso * np.eye(3))
    spinham.filter_2_2(min_distance=1)
    assert len(spinham._2_2) == 5

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())
    bonds = [
        (12, 0, 1, (0, 0, 0)),
        (12, 0, 0, (1, 0, 0)),
        (12, 1, 1, (1, 0, 0)),
        (12, 0, 0, (0, 2, 0)),
        (12, 1, 1, (0, 2, 0)),
        (12, 1, 0, (2, 2, 0)),
    ]
    for iso, atom1, atom2, ijk in bonds:
        spinham.add_2_2(atom1, atom2, ijk, iso * np.eye(3))
    spinham.filter_2_2(min_distance=1, max_distance=2)
    assert len(spinham._2_2) == 4


def test_notation_manipulation():
    atoms = dict(names=["Cr"], postions=[[0, 0, 0]], spins=[3 / 2])

    spinham = SpinHamiltonian(
        cell=np.eye(3), atoms=atoms, notation=Notation(True, False, c21=1, c22=0.5)
    )
    spinham.add_2_1(0, np.eye(3))
    spinham.add_2_2(0, 0, (1, 0, 0), np.eye(3))

    assert len(spinham.p22) == 2
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 1
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    assert spinham.notation.multiple_counting

    spinham.notation = Notation(False, False, c21=1, c22=0.5)
    assert len(spinham.p22) == 1
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 2
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=0.5)
    assert len(spinham.p22) == 2
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 1
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    assert not spinham.notation.spin_normalized

    spinham.notation = Notation(True, True, c21=1, c22=0.5)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 9 / 4
    assert get_isotropic_parameter(spinham.p21[0][1]) == 9 / 4

    spinham.notation = Notation(True, False, c21=1, c22=0.5)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 1
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    assert spinham.notation.c22 == 0.5

    spinham.notation = Notation(True, False, c21=1, c22=-1 / 2)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -1
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-2)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.25
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-1 / 2)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -1
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-2)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.25
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    assert spinham.notation.c22 == -1

    spinham.notation = Notation(True, False, c21=1, c22=1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=1, c22=-1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation(True, False, c21=-1, c22=-1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == -1

    spinham.notation = Notation(True, False, c21=0.5, c22=-1)
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 2

    spinham.notation = Notation(True, False, c21=1, c22=-1)

    spinham.notation = Notation.get_predefined("spinw")
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == 0.5
    assert get_isotropic_parameter(spinham.p21[0][1]) == 1

    spinham.notation = Notation.get_predefined("tb2j")
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -9 / 8
    assert get_isotropic_parameter(spinham.p21[0][1]) == -9 / 4

    spinham.notation = Notation.get_predefined("vampire")
    assert get_isotropic_parameter(list(spinham.p22)[0][3]) == -9 / 4
    assert get_isotropic_parameter(spinham.p21[0][1]) == -9 / 4
