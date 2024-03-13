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

import h5py

from magnopy.spinham import SpinHamiltonian
from magnopy.units.inside import ENERGY_NAME, LENGTH_NAME

__all__ = ["load_model_hdf5", "dump_model_hdf5"]


def load_model_hdf5(filename) -> SpinHamiltonian:
    pass


def dump_model_hdf5(
    spinham: SpinHamiltonian, filename=None, group=None, groupname="spinham"
) -> None:
    r"""
    Dump a SpinHamiltonian object to a HDF5 file.
    """
    if not (filename is not None) ^ (group is not None):
        raise ValueError("Either filename or group must be provided.")

    if filename is not None:
        file = h5py.File(filename, "w")
        root_group = file.create_group(groupname)
    else:
        root_group = group

    root_group.attrs["type"] = "SpinHamiltonian"

    # Cell
    cell = root_group.create_group("cell")
    cell.create_dataset("a1", data=spinham.a1, dtype="float")
    cell.create_dataset("a2", data=spinham.a2, dtype="float")
    cell.create_dataset("a3", data=spinham.a3, dtype="float")
    cell.create_dataset("units", data=LENGTH_NAME)

    # Atoms
    atoms = root_group.create_group("atoms")
    for a_i, atom in enumerate(spinham.atoms):
        atom_group = atoms.create_group(str(a_i + 1))
        atom_group.create_dataset("name", data=atom.name)
        atom_group.create_dataset("position", data=atom.position, dtype=float)
        atom_group.create_dataset("spin", data=atom.spin_vector, dtype=float)
        atom_group.create_dataset("g-factor", data=atom.g_factor, dtype=float)
        try:
            atom_group.create_dataset("charge", data=atom.charge, dtype=float)
        except ValueError:
            pass

    # Notation
    if len(spinham.exchange) > 0 or len(spinham.on_site) > 0:
        notation = root_group.create_group("notation")
        notation.create_dataset(
            "spin-normalized", data=spinham.spin_normalized, dtype=int
        )
        if len(spinham.exchange) > 0:
            notation.create_dataset(
                "double-counting", data=spinham.double_counting, dtype=int
            )
            notation.create_dataset(
                "exchange-factor", data=spinham.exchange_factor, dtype=float
            )
        if len(spinham.on_site) > 0:
            notation.create_dataset(
                "on-site-factor", data=spinham.on_site_factor, dtype=float
            )

    # Exchange
    if len(spinham.exchange) > 0:
        exchange = root_group.create_group("exchange")
        exchange.create_dataset("units", data=ENERGY_NAME)
        for e_i, (atom1, atom2, ijk, parameter) in enumerate(spinham.exchange):
            bond = exchange.create_group(str(e_i + 1))
            bond.create_dataset("atom-1", data=atom1)
            bond.create_dataset("atom-2", data=atom2)
            bond.create_dataset("ijk", data=ijk, dtype=int)
            bond.create_dataset("matrix", data=parameter.matrix, dtype=float)

    # On-site
    if len(spinham.on_site) > 0:
        on_site = root_group.create_group("on-site")
        on_site.create_dataset("units", data=ENERGY_NAME)
        for o_i, (atom, parameter) in enumerate(spinham.on_site):
            bond = on_site.create_group(str(o_i + 1))
            bond.create_dataset("atom", data=atom)
            bond.create_dataset("matrix", data=parameter.matrix, dtype=float)

    # Spiral vector
    if spinham.spiral_vector is not None:
        spiral_vector = root_group.create_dataset(
            "spiral-vector", data=spinham.spiral_vector, dtype=float
        )
        spiral_vector.attrs["units"] = "Relative"

    # Cone axis
    if spinham.cone_axis is not None:
        cone_axis = root_group.create_dataset(
            "cone-axis", data=spinham.cone_axis, dtype=float
        )
        cone_axis.attrs["units"] = "Absolute"

    if filename is not None:
        file.close()
