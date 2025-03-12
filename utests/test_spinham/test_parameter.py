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

################################################################################
#                                 Generic tests                                #
################################################################################


@given(st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS))
def test_get_matrix_parameter_from_iso(iso):
    matrix = get_matrix_parameter(iso=iso)
    assert np.allclose(matrix, iso * np.eye(3))


@given(
    st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
    st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
    st.floats(min_value=-MAX_MODULUS, max_value=MAX_MODULUS),
)
def test_get_matrix_parameter_from_aniso(a, b, c):
    aniso = np.array([[0, a, b], [a, 0, c], [b, c, 0]])
    matrix = get_matrix_parameter(aniso=aniso)
    assert np.allclose(matrix, aniso)


@given(ARRAY_3)
def test_get_matrix_parameter_from_dmi(dmi):
    matrix = get_matrix_parameter(dmi=dmi)
    assert np.allclose(
        matrix,
        [
            [0, dmi[2], -dmi[1]],
            [-dmi[2], 0, dmi[0]],
            [dmi[1], -dmi[0], 0],
        ],
    )


@given(ARRAY_3X3)
def test_get_isotropic_parameter(matrix):
    iso = get_isotropic_parameter(matrix)
    assert np.allclose(iso, np.trace(matrix) / 3.0)

    iso_matrix = get_isotropic_parameter(matrix, matrix_form=True)
    assert np.allclose(iso_matrix, np.trace(matrix) / 3.0 * np.eye(3))


@given(ARRAY_3X3)
def test_get_anisotropic_parameter(matrix):
    aniso = get_anisotropic_parameter(matrix)
    assert np.allclose(
        aniso, (matrix + matrix.T) / 2.0 - np.trace(matrix) / 3.0 * np.eye(3)
    )


@given(ARRAY_3X3)
def test_get_dmi(matrix):
    asymm = (matrix - matrix.T) / 2.0

    dmi = get_dmi(matrix)
    assert np.allclose(dmi, [asymm[1][2], asymm[2][0], asymm[0][1]])

    dmi_matrix = get_dmi(matrix, matrix_form=True)
    assert np.allclose(dmi_matrix, asymm)


################################################################################
#                           Tests that captured a bug                          #
################################################################################


def test_get_anisotropic_parameter_wrong_trace():
    r"""
    Bug when the input matrix was not made traceless, but rather all elements were
    decreased by a matrix trace.
    """

    # Intentionally not traceless
    aniso = [[3, 0, 0], [0, 0, 0], [0, 0, 0]]

    matrix = get_matrix_parameter(aniso=aniso)

    assert matrix[0][0] == 2
    assert matrix[0][1] == 0
    assert matrix[0][2] == 0

    assert matrix[1][0] == 0
    assert matrix[1][1] == -1
    assert matrix[1][2] == 0

    assert matrix[2][0] == 0
    assert matrix[2][1] == 0
    assert matrix[2][2] == -1


################################################################################
#                                 Legacy Tests                                 #
################################################################################


def test_legacy_test_1():
    full_matrix = get_matrix_parameter(iso=23)
    assert get_isotropic_parameter(full_matrix) == 23
    assert (
        get_anisotropic_parameter(full_matrix) == np.zeros((3, 3), dtype=float)
    ).all()
    assert (get_dmi(full_matrix) == np.zeros(3, dtype=float)).all()


def test_legacy_test_2():
    full_matrix = get_matrix_parameter(iso=23, dmi=(1, 1, 1))
    assert get_isotropic_parameter(full_matrix) == 23
    assert (
        get_anisotropic_parameter(full_matrix) == np.zeros((3, 3), dtype=float)
    ).all()
    assert (get_dmi(full_matrix) == np.ones(3, dtype=float)).all()


def test_legacy_test_3():
    full_matrix = get_matrix_parameter(
        iso=23, dmi=(1, 1, 1), aniso=[[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]]
    )
    assert get_isotropic_parameter(full_matrix) == 23
    assert (
        get_anisotropic_parameter(full_matrix)
        == np.array([[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]])
    ).all()
    assert (get_dmi(full_matrix) == np.ones(3, dtype=float)).all()


def test_legacy_test_4():
    matrix1 = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    matrix2 = np.array([[1, 2, 0], [1, 1, 0], [0, 0, 1]])

    assert (
        get_dmi(matrix1, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()

    assert (
        get_dmi(matrix2, matrix_form=True)
        == np.array([[0, 0.5, 0], [-0.5, 0, 0], [0, 0, 0]])
    ).all()


def test_legacy_test_5():
    matrix = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    assert get_isotropic_parameter(matrix) == 4

    assert (
        get_isotropic_parameter(matrix, matrix_form=True)
        == np.array([[4, 0, 0], [0, 4, 0], [0, 0, 4]])
    ).all()

    assert (
        get_anisotropic_parameter(matrix)
        == np.array([[-3, 5, 2], [5, 4, 5], [2, 5, -1]])
    ).all()

    assert (get_dmi(matrix) == np.array([-1, 0, 0])).all()

    assert (
        get_dmi(matrix, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()
