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

from magnopy.energy import Energy
from magnopy.spinham import Notation, SpinHamiltonian


@pytest.mark.parametrize("spin_normalized", (True, False))
def test_spin_normalized(spin_normalized):
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    spinham.notation = Notation(
        spin_normalized=spin_normalized, multiple_counting=True, c1=1, c21=1, c22=1
    )

    energy = Energy(spinham)

    assert abs(energy.E_0(spin_directions) - target_energy.E_0(spin_directions)) < 1e-8


@pytest.mark.parametrize("multiple_counting", (True, False))
def test_multiple_counting(multiple_counting):
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    spinham.notation = Notation(
        spin_normalized=False,
        multiple_counting=multiple_counting,
        c1=1,
        c21=1,
        c22=1,
    )

    energy = Energy(spinham)

    assert abs(energy.E_0(spin_directions) - target_energy.E_0(spin_directions)) < 1e-8


@pytest.mark.parametrize("c1", (-1, -0.5, 0.5, 1))
def test_c1(c1):
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    spinham.notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=c1, c21=1, c22=1
    )

    energy = Energy(spinham)

    assert abs(energy.E_0(spin_directions) - target_energy.E_0(spin_directions)) < 1e-8


@pytest.mark.parametrize("c21", (-1, -0.5, 0.5, 1))
def test_c21(c21):
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    spinham.notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=c21, c22=1
    )

    energy = Energy(spinham)

    assert abs(energy.E_0(spin_directions) - target_energy.E_0(spin_directions)) < 1e-8


@pytest.mark.parametrize("c22", (-1, -0.5, 0.5, 1))
def test_c22(c22):
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    spinham.notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=c22
    )

    energy = Energy(spinham)

    assert abs(energy.E_0(spin_directions) - target_energy.E_0(spin_directions)) < 1e-8


def test_all_notations():
    notation = Notation(
        spin_normalized=False, multiple_counting=True, c1=1, c21=1, c22=1
    )

    cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    atoms = dict(names=["Fe"], spins=[5 / 2])

    spin_directions = [[0, 0, 1]]

    spinham = SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

    parameter = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    spinham.add_1(alpha=0, parameter=[0, 0, 1])
    spinham.add_2_1(alpha=0, parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
    spinham.add_2_2(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

    target_energy = Energy(spinham)

    for spin_normalized in [True, False]:
        for multiple_counting in [True, False]:
            for c1 in [-1, -0.5, 0.5, 1]:
                for c21 in [-1, -0.5, 0.5, 1]:
                    for c22 in [-1, -0.5, 0.5, 1]:
                        spinham.notation = Notation(
                            spin_normalized=spin_normalized,
                            multiple_counting=multiple_counting,
                            c1=c1,
                            c21=c21,
                            c22=c22,
                        )

                        energy = Energy(spinham)

                        assert (
                            abs(
                                energy.E_0(spin_directions)
                                - target_energy.E_0(spin_directions)
                            )
                            < 1e-8
                        )
