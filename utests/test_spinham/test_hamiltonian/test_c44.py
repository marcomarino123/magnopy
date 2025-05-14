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

from magnopy import Notation, SpinHamiltonian
from magnopy._spinham._c44 import _get_primary_p44

MAX_MODULUS = 1e8
ARRAY_3x3x3x3 = harrays(
    np.float64,
    (3, 3, 3, 3),
    elements=st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)
RANDOM_UC = harrays(int, (2, 3), elements=st.integers(min_value=-1000, max_value=1000))


@given(
    st.integers(),
    st.integers(),
    st.integers(),
    st.integers(),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    ARRAY_3x3x3x3,
)
def test_add_44(alpha, beta, gamma, epsilon, nu, _lambda, rho, parameter):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    if (
        0 <= alpha < len(spinham.atoms.names)
        and 0 <= beta < len(spinham.atoms.names)
        and 0 <= gamma < len(spinham.atoms.names)
        and 0 <= epsilon < len(spinham.atoms.names)
    ):
        spinham.add_44(alpha, beta, gamma, epsilon, nu, _lambda, rho, parameter)
    else:
        with pytest.raises(ValueError):
            spinham.add_44(alpha, beta, gamma, epsilon, nu, _lambda, rho, parameter)


@given(
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.integers(min_value=0, max_value=8),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    ARRAY_3x3x3x3,
)
def test_add_44_sorting(
    alpha1,
    beta1,
    gamma1,
    epsilon1,
    nu1,
    _lambda1,
    rho1,
    alpha2,
    beta2,
    gamma2,
    epsilon2,
    nu2,
    _lambda2,
    rho2,
    alpha3,
    beta3,
    gamma3,
    epsilon3,
    nu3,
    _lambda3,
    rho3,
    alpha4,
    beta4,
    gamma4,
    epsilon4,
    nu4,
    _lambda4,
    rho4,
    parameter,
):
    atoms = {"names": ["Cr" for _ in range(9)], "spins": [1 for _ in range(9)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    spinham.add_44(alpha1, beta1, gamma1, epsilon1, nu1, _lambda1, rho1, parameter)

    if [alpha1, beta1, gamma1, epsilon1, nu1, _lambda1, rho1] == [
        alpha2,
        beta2,
        gamma2,
        epsilon2,
        nu2,
        _lambda2,
        rho2,
    ]:
        with pytest.raises(ValueError):
            spinham.add_44(
                alpha2, beta2, gamma2, epsilon2, nu2, _lambda2, rho2, parameter
            )
    else:
        spinham.add_44(alpha2, beta2, gamma2, epsilon2, nu2, _lambda2, rho2, parameter)

    spinham.add_44(
        alpha3, beta3, gamma3, epsilon3, nu3, _lambda3, rho3, parameter, replace=True
    )
    spinham.add_44(
        alpha4, beta4, gamma4, epsilon4, nu4, _lambda4, rho4, parameter, replace=True
    )

    for i in range(len(spinham._44) - 1):
        assert spinham._44[i][:-1] <= spinham._44[i + 1][:-1]


@given(
    st.integers(min_value=0, max_value=2),
    st.integers(min_value=0, max_value=2),
    st.integers(min_value=0, max_value=2),
    st.integers(min_value=0, max_value=2),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers(), st.integers()),
    RANDOM_UC,
    RANDOM_UC,
    RANDOM_UC,
)
def test_remove_44(
    r_alpha, r_beta, r_gamma, r_epsilon, r_nu, r_lambda, r_rho, nus, lambdas, rhos
):
    atoms = {"names": ["Cr" for _ in range(4)], "spins": [1 for _ in range(4)]}

    spinham = SpinHamiltonian(cell=np.eye(3), atoms=atoms, notation=Notation())

    for alpha in range(len(spinham.atoms.names)):
        for beta in range(alpha, len(spinham.atoms.names)):
            for gamma in range(beta, len(spinham.atoms.names)):
                for epsilon in range(gamma, len(spinham.atoms.names)):
                    for nu in nus:
                        for _lambda in lambdas:
                            for rho in rhos:
                                nu = (int(nu[0]), int(nu[1]), int(nu[2]))
                                _lambda = (
                                    int(_lambda[0]),
                                    int(_lambda[1]),
                                    int(_lambda[2]),
                                )
                                rho = (
                                    int(rho[0]),
                                    int(rho[1]),
                                    int(rho[2]),
                                )
                                spinham.add_44(
                                    alpha,
                                    beta,
                                    gamma,
                                    epsilon,
                                    nu,
                                    _lambda,
                                    rho,
                                    np.ones((3, 3, 3, 3)),
                                    replace=True,
                                )

    bond = [r_alpha, r_beta, r_gamma, r_epsilon, r_nu, r_lambda, r_rho]
    if (
        0 <= r_alpha < len(spinham.atoms.names)
        and 0 <= r_beta < len(spinham.atoms.names)
        and 0 <= r_gamma < len(spinham.atoms.names)
        and 0 <= r_epsilon < len(spinham.atoms.names)
    ):
        original_bonds = [tmp[:-1] for tmp in spinham._44]
        original_length = len(spinham._44)

        spinham.remove_44(*bond)

        primary_bond = list(_get_primary_p44(*bond))
        if primary_bond in original_bonds:
            updated_bonds = [tmp[:-1] for tmp in spinham._44]

            assert len(spinham._44) == original_length - 1
            assert bond not in updated_bonds
            assert primary_bond not in updated_bonds
        else:
            assert len(spinham._44) == original_length

    else:
        with pytest.raises(ValueError):
            spinham.remove_44(*bond)
