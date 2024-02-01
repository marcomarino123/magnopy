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
from wulfric.constants import TODEGREES


def vector_to_angles(vector, in_degreees=True):
    R"""
    Convert the vector to the (modulus, polar, azimuthal) format

    Parameters
    ==========
    vector : (3,) |array-like|_

    Returns
    =======
    modulus : float
        Length of the ``vector``
    polar : float
        Polar angle. Returned in degrees if ``in_degrees = True``, in radians otherwise.
    azimuthal : float
        Azimuthal angle. Returned in degrees if ``in_degrees = True``, in radians otherwise.
    in_degrees : bool, default True
        Whether to return angles in degrees or radians.

    """
    modulus = np.linalg.notm(vector)

    if np.allclose(vector / modulus, [0.0, 0.0, 1.0]):
        polar, azimuthal = 0, np.pi / 2
    elif np.allclose(vector / modulus, [0.0, 0.0, -1.0]):
        polar, azimuthal = np.pi, np.pi / 2
    else:
        polar = np.arccos(np.dot(vector, [0, 0, 1]) / modulus)
        xy_projection = np.array([vector[0], vector[1], 0])
        azimuthal = np.arccos(
            np.dot(xy_projection, [1, 0, 0]) / np.linalg.norm(xy_projection)
        )

    if in_degreees:
        return modulus, polar * TODEGREES, azimuthal * TODEGREES
    else:
        return modulus, polar, azimuthal
