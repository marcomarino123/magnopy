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


def _validate_atom_index(index, atoms) -> None:
    r"""
    Validate that the atom index is in agreement with the amount of atoms

    Parameter
    ---------
    index
        Potential index of an atom.
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["names"]``.

    Raises
    ------
    TypeError
        If ``index`` is not an integer.
    ValueError
        If ``index`` is out of range.
    """

    if not isinstance(index, int):
        raise TypeError(
            f"Only integers are supported as atom indices, "
            f"got '{type(index)}' from '{index}'"
        )

    if not 0 <= index < len(atoms["names"]):
        raise ValueError(
            "Index should be greater or equal to 0 and less than "
            f"{len(atoms['names'])}', got {index}."
        )


def _validate_unit_cell_index(ijk) -> None:
    r"""
    Validate that ijk can specify unit cell.

    Parameters
    ----------
    ijk
        Potential index of the unit cell.

    Raises
    ------
    TypeError
        If ``ijk`` is not a ``tuple``.
    TypeError
        If either ``i``, ``j`` or ``k`` is not an ``int``.
    """

    if not isinstance(ijk, tuple):
        raise TypeError(f"Unit cell index has to be a tuple, got '{type(ijk)}'")

    if not isinstance(ijk[0], int):
        raise TypeError(
            f"First element of the unit cell index is not an 'int', got "
            f"{type(ijk[0])} from '{ijk[0]}'"
        )

    if not isinstance(ijk[1], int):
        raise TypeError(
            f"Second element of the unit cell index is not an 'int', got "
            f"{type(ijk[1])} from '{ijk[1]}'"
        )

    if not isinstance(ijk[2], int):
        raise TypeError(
            f"Third element of the unit cell index is not an 'int', got "
            f"{type(ijk[2])} from '{ijk[2]}'"
        )
