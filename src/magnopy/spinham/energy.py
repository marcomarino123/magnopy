# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2024 Magnopy Team
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
from wulfric import TORADIANS, absolute_to_relative

from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.units.inside import ENERGY
from magnopy.units.si import BOHR_MAGNETON

__all__ = ["Energy"]

# Convert to the internal units of energy
BOHR_MAGNETON /= ENERGY


def get_spinham_as_list(spinham: SpinHamiltonian):
    spinham_list = []
    for a1, a2, R, J in spinham.exchange_like:
        d = spinham.get_distance(a1, a2, R)
        spinham_list.append(a1.index, a2.index, d, J)

    spins = [atom.spin for atom in spinham.magnetic_atoms]

    return spinham_list, spins, spinham.exchange_factor


def ferro_energy(A, spinham_list, spins, exchange_factor):
    A = np.array(A)
    a = A[::3]
    b = A[1::3]
    c = A[2::3]

    theta = np.sqrt(a**2 + b**2 + c**2)
    l_1 = np.zeros_like(a)
    l_2 = -1j * theta
    l_3 = 1j * theta

    L = np.array(
        [
            [l_1, np.zeros_like(l_1), np.zeros_like(l_1)],
            [np.zeros_like(l_1), l_2, np.zeros_like(l_1)],
            [l_3, np.zeros_like(l_1), np.zeros_like(l_1)],
        ]
    )

    v_1 = np.array([c, -b, a])
    v_2 = (
        np.array([b * c + 1j * a * theta, a**2 + c**2, a * b - 1j**theta])
        / theta
        / np.sqrt(2 * (a**2 + c**2))
    )
    v_3 = np.conjugate(v_2)
    V = np.array([v_1, v_2, v_3])

    R = np.einsum("njk,jik,imk->nmk", V, L, np.conjugate(V))

    energy = 0

    for i, j, d, J in spinham_list:
        energy += (
            exchange_factor
            * spins[i]
            * spins[j]
            * (np.conjugate(R[i]) @ J @ R[j])[2, 2]
        )

    return energy
