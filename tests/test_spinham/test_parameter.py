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
    matrix = converter22.from_iso(iso=iso)
    assert np.allclose(matrix, iso * np.eye(3))


@given(ARRAY_3)
def test_from_dmi(dmi):
    matrix = converter22.from_dmi(dmi=dmi)
    assert np.allclose(
        matrix,
        [
            [0, dmi[2], -dmi[1]],
            [-dmi[2], 0, dmi[0]],
            [dmi[1], -dmi[0], 0],
        ],
    )


@given(ARRAY_3X3)
def test_to_iso(matrix):
    iso = converter22.to_iso(matrix=matrix)
    assert np.allclose(iso, np.trace(matrix) / 3.0)

    iso_matrix = converter22.to_iso(matrix=matrix, matrix_form=True)
    assert np.allclose(iso_matrix, np.trace(matrix) / 3.0 * np.eye(3))


@given(ARRAY_3X3)
def test_to_symm_anisotropy(matrix):
    aniso = converter22.to_symm_anisotropy(matrix=matrix)
    assert np.allclose(
        aniso, (matrix + matrix.T) / 2.0 - np.trace(matrix) / 3.0 * np.eye(3)
    )


@given(ARRAY_3X3)
def test_to_dmi(matrix):
    asymm = (matrix - matrix.T) / 2.0

    dmi = converter22.to_dmi(matrix=matrix)
    assert np.allclose(dmi, [asymm[1][2], asymm[2][0], asymm[0][1]])

    dmi_matrix = converter22.to_dmi(matrix=matrix, matrix_form=True)
    assert np.allclose(dmi_matrix, asymm)


################################################################################
#                                 Legacy Tests                                 #
################################################################################


def test_legacy_test_1():
    full_matrix = converter22.from_iso(iso=23)
    assert converter22.to_iso(matrix=full_matrix) == 23
    assert (
        converter22.to_symm_anisotropy(matrix=full_matrix)
        == np.zeros((3, 3), dtype=float)
    ).all()
    assert (converter22.to_dmi(matrix=full_matrix) == np.zeros(3, dtype=float)).all()


def test_legacy_test_2():
    full_matrix = converter22.from_iso(iso=23) + converter22.from_dmi(dmi=(1, 1, 1))
    assert converter22.to_iso(matrix=full_matrix) == 23
    assert (
        converter22.to_symm_anisotropy(matrix=full_matrix)
        == np.zeros((3, 3), dtype=float)
    ).all()
    assert (converter22.to_dmi(matrix=full_matrix) == np.ones(3, dtype=float)).all()


def test_legacy_test_3():
    full_matrix = (
        converter22.from_iso(iso=23)
        + converter22.from_dmi(dmi=(1, 1, 1))
        + [[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]]
    )

    assert converter22.to_iso(matrix=full_matrix) == 23
    assert (
        converter22.to_symm_anisotropy(matrix=full_matrix)
        == np.array([[1, 1, 0], [1, -0.5, 0], [0, 0, -0.5]])
    ).all()
    assert (converter22.to_dmi(matrix=full_matrix) == np.ones(3, dtype=float)).all()


def test_legacy_test_4():
    matrix1 = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    matrix2 = np.array([[1, 2, 0], [1, 1, 0], [0, 0, 1]])

    assert (
        converter22.to_dmi(matrix=matrix1, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()

    assert (
        converter22.to_dmi(matrix=matrix2, matrix_form=True)
        == np.array([[0, 0.5, 0], [-0.5, 0, 0], [0, 0, 0]])
    ).all()


def test_legacy_test_5():
    matrix = np.array([[1, 5, 2], [5, 8, 4], [2, 6, 3]])
    assert converter22.to_iso(matrix=matrix) == 4

    assert (
        converter22.to_iso(matrix=matrix, matrix_form=True)
        == np.array([[4, 0, 0], [0, 4, 0], [0, 0, 4]])
    ).all()

    assert (
        converter22.to_symm_anisotropy(matrix=matrix)
        == np.array([[-3, 5, 2], [5, 4, 5], [2, 5, -1]])
    ).all()

    assert (converter22.to_dmi(matrix=matrix) == np.array([-1, 0, 0])).all()

    assert (
        converter22.to_dmi(matrix=matrix, matrix_form=True)
        == np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
    ).all()
