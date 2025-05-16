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

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def read_spin_directions(spins):
    r"""
    Read directions of the spins from the file.

    Parameters
    ----------
    spins : str or (3*M, ) |array-like|_
        File with the spin directions or a flattened array of spin components.
        See notes for the specification of the file format.

    Returns
    -------
    spin_directions : (M, ) :numpy:`ndarray`
        If ``spins`` is an |array-like|_, then first three elements are

    Notes
    -----
    If ``spins`` is a list, then it is interpreted as (for two spins)

    .. code-block:: python

        [S1_x, S1_y, S1_z, S2_x, S2_y, S2_z]

    .. doctest::

        >>> import magnopy.io as mio
        >>> spins = [0, 0, 2, 0, 1, 1]
        >>> spin_directions = mio.read_spin_directions(spins=spins)
        >>> spin_directions
        array([[0.        , 0.        , 1.        ],
               [0.        , 0.70710678, 0.70710678]])

    The file is expected to contain three numbers per line, here is an example for two
    spins

    .. code-block:: text

        S1_x S1_y S1_z
        S2_x S2_y S2_z

    Only the direction of the spin vector is recognized, the modulus is ignored.
    Comments are allowed at any place of the file and preceded by the symbol "#".
    If the symbol "#" is found, the part of the line after it is ignored. Here
    are examples of valid use of the comments

    .. code-block:: text

        # Spin vectors for the material XX
        S1_x S1_y S1_z # Atom X1
        # This comments is here by some reason
        S2_x S2_y S2_z # Atom X2

    """

    if isinstance(spins, str):
        spins = []
        with open(spins, "r") as f:
            i = 1
            for line in f:
                # Remove comment lines
                if line.startswith("#"):
                    continue
                # Remove inline comments and leading/trailing whitespaces
                line = line.split("#")[0].strip()
                # Check for empty lines empty lines
                if line:
                    line = line.split()
                    if len(line) != 3:
                        raise ValueError(
                            f"Expected three numbers per line (in line{i}),"
                            f"got: {len(line)}."
                        )
                    for tmp in line:
                        spins.append(float(tmp))

    if len(spins) % 3 != 0:
        raise ValueError(
            f"Length of the spin list should be dividable by three, got: {len(spins)}."
        )

    spins = np.array(spins, dtype=float)
    spins = np.reshape(spins, shape=(len(spins) // 3, 3))
    spin_directions = spins / np.linalg.norm(spins, axis=1)[:, np.newaxis]
    return spin_directions


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
