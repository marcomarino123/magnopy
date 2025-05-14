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


from math import cos, sqrt

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays as harrays

from magnopy._exceptions import ColpaFailed
from magnopy._spinham._hamiltonian import SpinHamiltonian
from magnopy._spinham._notation import Notation
from magnopy.lswt._dispersion import MagnonDispersion


@pytest.mark.parametrize(
    "spin_direction",
    ([0, 0, 1], [0, 0, -1], [0, 1, 0], [1, 0, 0], [1, 1, 1]),
)
@given(
    harrays(
        np.float64,
        (3,),
        elements=st.floats(min_value=-1e8, max_value=1e8, allow_subnormal=False),
    )
)
def test_ferromagnet_one_spin_cubic(spin_direction, k):
    a = 1
    J = -1
    S = 0.5

    atoms = {"names": ["Fe"], "spins": [S], "positions": [[0, 0, 0]]}

    omega_anal = (
        2 * S * J * 6 * (1 / 3 * (cos(k[0] * a) + cos(k[1] * a) + cos(k[2] * a)) - 1)
    )

    spinham = SpinHamiltonian(
        cell=[[a, 0, 0], [0, a, 0], [0, 0, a]],
        atoms=atoms,
        notation=Notation(spin_normalized=False, multiple_counting=True, c22=1),
    )

    spinham.add_22(
        atom1=0, atom2=0, ijk2=(1, 0, 0), parameter=J * np.eye(3, dtype=float)
    )
    spinham.add_22(
        atom1=0, atom2=0, ijk2=(0, 1, 0), parameter=J * np.eye(3, dtype=float)
    )
    spinham.add_22(
        atom1=0, atom2=0, ijk2=(0, 0, 1), parameter=J * np.eye(3, dtype=float)
    )

    disp = MagnonDispersion(spinham=spinham, spin_directions=[spin_direction])

    assert disp.M == 1

    assert len(disp.repr_A) == 1
    assert len(disp.repr_A[0]) == 1
    assert abs(disp.repr_A[0][0] - sqrt(2 * S)) < 1e-8

    assert len(disp.repr_B) == 1
    assert len(disp.repr_B[0]) == 1
    assert abs(disp.repr_B[0][0] - sqrt(2 * S)) < 1e-8

    assert len(disp.A_zero) == 1
    assert len(disp.A_zero[0]) == 1
    assert abs(disp.A_zero[0][0] - 3) < 1e-8

    assert len(disp.r_nu) == 6
    assert np.allclose(disp.r_nu[(1, 0, 0)], [a, 0, 0])
    assert np.allclose(disp.r_nu[(-1, 0, 0)], [-a, 0, 0])
    assert np.allclose(disp.r_nu[(0, 1, 0)], [0, a, 0])
    assert np.allclose(disp.r_nu[(0, -1, 0)], [0, -a, 0])
    assert np.allclose(disp.r_nu[(0, 0, 1)], [0, 0, a])
    assert np.allclose(disp.r_nu[(0, 0, -1)], [0, 0, -a])

    assert len(disp.J_A) == 6
    assert len(disp.J_B) == 6
    assert len(disp.J_C) == 6
    assert len(disp.J_D) == 6

    for ijk in disp.J_A:
        assert len(disp.J_A[ijk]) == 1
        assert len(disp.J_A[ijk][0]) == 1
        assert abs(disp.J_A[ijk][0][0].real - (-1 / 2)) < 1e-8

    for ijk in disp.J_B:
        assert len(disp.J_B[ijk]) == 1
        assert len(disp.J_B[ijk][0]) == 1
        assert abs(disp.J_B[ijk][0][0].real) < 1e-8

    for ijk in disp.J_C:
        assert len(disp.J_C[ijk]) == 1
        assert len(disp.J_C[ijk][0]) == 1
        assert abs(disp.J_C[ijk][0][0].real) < 1e-8

    for ijk in disp.J_D:
        assert len(disp.J_D[ijk]) == 1
        assert len(disp.J_D[ijk][0]) == 1
        assert abs(disp.J_D[ijk][0][0].real - (-1 / 2)) < 1e-8

    assert (
        abs(disp.A(k=k) - (3 - (cos(k[0] * a) + cos(k[1] * a) + cos(k[2] * a)))) < 1e-8
    )
    assert (
        abs(disp.D(k=k) - (3 - (cos(k[0] * a) + cos(k[1] * a) + cos(k[2] * a)))) < 1e-8
    )

    assert abs(disp.B(k=k)) < 1e-8
    assert abs(disp.C(k=k)) < 1e-8

    assert np.allclose(
        disp.GDM(k=k),
        [
            [3 - (cos(k[0] * a) + cos(k[1] * a) + cos(k[2] * a)), 0],
            [0, 3 - (cos(k[0] * a) + cos(k[1] * a) + cos(k[2] * a))],
        ],
    )

    if cos(k[0] * a) - 1 == 0 and cos(k[1] * a) - 1 == 0 and cos(k[2] * a) - 1 == 0:
        try:
            omega = disp.omegas(k=k)
        except ColpaFailed:
            return
    else:
        omega = disp.omegas(k=k)

    assert len(omega) == 1

    omega = omega[0]

    assert omega.imag == 0

    assert (omega.real - omega_anal) < 1e-8
