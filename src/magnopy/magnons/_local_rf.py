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


from math import factorial, sqrt

import numpy as np

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def span_local_rf(direction_vector):
    r"""
    Span local  right-handed reference frame from the direction vector.

    Parameters
    ----------
    direction_vector : (3, ) |array-like|_
        Direction of the z axis of the local reference frame.

    Returns
    -------
    x_alpha : (3, ) :numpy:`ndarray`
    y_alpha : (3, ) :numpy:`ndarray`
    z_alpha : (3, ) :numpy:`ndarray`
    """

    direction_vector = np.array(direction_vector, dtype=float)

    if np.allclose(direction_vector, np.zeros(3)):
        raise ValueError("Zero vector.")

    direction_vector /= np.linalg.norm(direction_vector)

    if np.allclose(direction_vector, [0, 0, 1]):
        return np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            dtype=float,
        )

    if np.allclose(direction_vector, [0, 0, -1]):
        return np.array(
            [
                [0, -1, 0],
                [-1, 0, 0],
                [0, 0, -1],
            ],
            dtype=float,
        )

    z_dir = [0, 0, 1]

    sin_rot_angle = np.linalg.norm(np.cross(z_dir, direction_vector))
    cos_rot_angle = np.dot(direction_vector, z_dir)
    # direction_vector and z_dir are unit vectors
    ux, uy, uz = np.cross(z_dir, direction_vector) / sin_rot_angle

    x_alpha = np.array(
        [
            ux**2 * (1 - cos_rot_angle) + cos_rot_angle,
            ux * uy * (1 - cos_rot_angle) + uz * sin_rot_angle,
            ux * uz * (1 - cos_rot_angle) - uy * sin_rot_angle,
        ]
    )

    y_alpha = np.array(
        [
            ux * uy * (1 - cos_rot_angle) - uz * sin_rot_angle,
            uy**2 * (1 - cos_rot_angle) + cos_rot_angle,
            uy * uz * (1 - cos_rot_angle) + ux * sin_rot_angle,
        ]
    )

    return x_alpha, y_alpha, direction_vector


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
