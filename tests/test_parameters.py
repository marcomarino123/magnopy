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
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays as harrays

from magnopy import converter22

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

################################################################################
#                                 Generic tests                                #
################################################################################


@given(st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS))
def test_from_iso(iso):
    parameter = converter22.from_iso(iso=iso)
    assert np.allclose(parameter, iso * np.eye(3))


@given(ARRAY_3)
def test_from_dmi(dmi):
    parameter = converter22.from_dmi(dmi=dmi)
    assert np.allclose(
        parameter,
        [
            [0, dmi[2], -dmi[1]],
            [-dmi[2], 0, dmi[0]],
            [dmi[1], -dmi[0], 0],
        ],
    )


@given(ARRAY_3X3)
def test_to_iso(parameter):
    iso = converter22.to_iso(parameter=parameter)
    assert np.allclose(iso, np.trace(parameter) / 3.0)

    iso_parameter = converter22.to_iso(parameter=parameter, matrix_form=True)
    assert np.allclose(iso_parameter, np.trace(parameter) / 3.0 * np.eye(3))


@given(ARRAY_3X3)
def test_to_symm_anisotropy(parameter):
    aniso = converter22.to_symm_anisotropy(parameter=parameter)
    assert np.allclose(
        aniso, (parameter + parameter.T) / 2.0 - np.trace(parameter) / 3.0 * np.eye(3)
    )


@given(ARRAY_3X3)
def test_to_dmi(parameter):
    asymm = (parameter - parameter.T) / 2.0

    dmi = converter22.to_dmi(parameter=parameter)
    assert np.allclose(dmi, [asymm[1][2], asymm[2][0], asymm[0][1]])

    dmi_parameter = converter22.to_dmi(parameter=parameter, matrix_form=True)
    assert np.allclose(dmi_parameter, asymm)


################################################################################
#                                 Legacy Tests                                 #
################################################################################


def test_legacy_test_1():
    full_parameter = converter22.from_iso(iso=23)
    assert converter22.to_iso(parameter=full_parameter) == 23
    assert (
        converter22.to_symm_anisotropy(parameter=full_parameter)
        == np.zeros((3, 3), dtype=float)
    ).all()
    assert (
        converter22.to_dmi(parameter=full_parameter) == np.zeros(3, dtype=float)
    ).all()


def test_legacy_test_2():
    full_parameter = converter22.from_iso(iso=23) + converter22.from_dmi(dmi=(1, 1, 1))
    assert converter22.to_iso(parameter=full_parameter) == 23
    assert (
        converter22.to_symm_anisotropy(parameter=full_parameter)
        == np.zeros((3, 3), dtype=float)
    ).all()
    assert (
        converter22.to_dmi(parameter=full_parameter) == np.ones(3, dtype=float)
    ).all()


def test_legacy_test_3():
    full_parameter = (
        converter22.from_iso(iso=23)
        + converter22.from_dmi(dmi=(1, 1, 1))
        + [[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]]
    )

    assert converter22.to_iso(parameter=full_parameter) == 23
    assert (
        converter22.to_symm_anisotropy(parameter=full_parameter)
        == np.array([[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]])
    ).all()
    assert (
        converter22.to_dmi(parameter=full_parameter) == np.ones(3, dtype=float)
    ).all()


def test_legacy_test_4():
    parameter1 = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    parameter2 = np.array([[1, 2, 0], [1, 1, 0], [0, 0, 1]])

    assert (
        converter22.to_dmi(parameter=parameter1, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()

    assert (
        converter22.to_dmi(parameter=parameter2, matrix_form=True)
        == np.array([[0, 0.5, 0], [-0.5, 0, 0], [0, 0, 0]])
    ).all()


def test_legacy_test_5():
    parameter = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    assert converter22.to_iso(parameter=parameter) == 4

    assert (
        converter22.to_iso(parameter=parameter, matrix_form=True)
        == np.array([[4, 0, 0], [0, 4, 0], [0, 0, 4]])
    ).all()

    assert (
        converter22.to_symm_anisotropy(parameter=parameter)
        == np.array([[-3, 5, 2], [5, 4, 5], [2, 5, -1]])
    ).all()

    assert (converter22.to_dmi(parameter=parameter) == np.array([-1, 0, 0])).all()

    assert (
        converter22.to_dmi(parameter=parameter, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()
