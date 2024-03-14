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

import logging

import h5py
from wulfric.geometry import absolute_to_relative

from magnopy.io.txt.verify import _verify_atom_name
from magnopy.spinham import SpinHamiltonian
from magnopy.units.inside import ENERGY, ENERGY_NAME, LENGTH, LENGTH_NAME
from magnopy.units.si import (
    ANGSTROM,
    BOHR_RADIUS,
    ELECTRON_VOLT,
    K_BOLTZMANN,
    RYDBERG_ENERGY,
)

_logger = logging.getLogger(__name__)

__all__ = ["load_spinham_hdf5", "dump_spinham_hdf5"]


def load_spinham_hdf5(
    filename,
    groupname=None,
) -> SpinHamiltonian:
    r"""
    Load a SpinHamiltonian object from a HDF5 file.

    It reads spin Hamiltonian data from a ``groupname`` group
    of an existing ``filename`` HDF5 file.

    Parameters
    ----------
    filename : str
        The name of the file where the SpinHamiltonian object will be loaded from.
    groupname : str, optional
        The name of the root group for the spin Hamiltonian.
        If ``groupname`` is not provided, we try to detect the group with type "SpinHamiltonian".
        If several groups with type "SpinHamiltonian" are found, an error is raised.

    Raises
    ------
    RuntimeError
        If several groups with type "SpinHamiltonian" are found in the file and
        ``groupname`` is not provided.
    KeyError
        If ``groupname`` is provided and it is not found in the file.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        The SpinHamiltonian object loaded from the file.
    """

    # Open a file and try to detect the desired group
    file = h5py.File(filename, "r")

    if groupname is None:
        _logger.info(f"Groupname not provided, trying to detect it in file {filename}.")

        potential_groupnames = []

        # Parser rule for the groupname
        def find_spinhams(name):
            try:
                if file[name].attrs["type"].lower() == "spinhamiltonian":
                    potential_groupnames.append(name)
            except KeyError:
                pass

        # Visit all groups in the file
        file.visit(find_spinhams)
        # If there is no group with type "SpinHamiltonian" raise an error
        if len(potential_groupnames) == 0:
            message = f"No group with type 'SpinHamiltonian' found in file {filename}."
            _logger.error(message)
            raise RuntimeError(message)
        # If there is only one group with type "SpinHamiltonian" read it
        elif len(potential_groupnames) == 1:
            groupname = potential_groupnames[0]
            _logger.info(
                f'Found group "{groupname}" in file "{filename}" with type "SpinHamiltonian".'
            )
        # If there are multiple groups with type "SpinHamiltonian" raise an error
        else:
            message = (
                f'Multiple groups with type "SpinHamiltonian" found in file "{filename}": '
                + ", ".join(potential_groupnames)
            )
            _logger.error(message)
            raise RuntimeError(message)

    root_group = file[groupname]

    # create a SpinHamiltonian object
    spinham = SpinHamiltonian()

    # Read the cell
    cell = root_group["cell"]
    spinham.cell = [cell["a1"], cell["a2"], cell["a3"]]

    # In the correct hdf5 file only two cases are possible
    if cell.attrs["units"].lower().startswith("bohr"):
        units_conversion = BOHR_RADIUS / LENGTH
    elif cell.attrs["units"].lower().startswith("angstrom"):
        units_conversion = ANGSTROM / LENGTH
    else:
        _logger.error(f"Unknown units '{cell['units']}' for cell in file '{filename}'.")

    spinham.cell *= units_conversion

    # Read the atoms
    atoms = root_group["atoms"]
    for index in atoms:
        atom = atoms[index]
        name = atom["name"][()].decode("utf-8")
        if _verify_atom_name(name, line_index="hdf5 file"):
            _logger.error(f"Forbidden atom name '{name}' in file '{filename}'.")
        position = atom["position"][:]
        spin = atom["spin"][:]
        g_factor = atom["g-factor"][()]
        try:
            charge = atom["charge"][()]
        except KeyError:
            charge = None
        spinham.add_atom(
            name=name,
            position=position,
            spin=spin,
            g_factor=g_factor,
            charge=charge,
            relative=True,
        )
    # Read notation
    if "exchange" in root_group or "on-site" in root_group:
        try:
            notation = root_group["notation"]
        except KeyError as e:
            _logger.error(
                f"Missing notation group in file '{filename}' for exchange and/or on-site."
            )
            raise e

        try:
            spinham.spin_normalized = notation["spin-normalized"][()]
        except KeyError as e:
            _logger.error(
                f'Missing "spin-normalized" property in notation group in file "{filename}".'
            )
            raise e

        if "exchange" in root_group:
            try:
                spinham.double_counting = notation["double-counting"][()]
            except KeyError as e:
                _logger.error(
                    f'Missing "double-counting" property in notation group in file "{filename}".'
                )
                raise e
            try:
                spinham.exchange_factor = notation["exchange-factor"][()]
            except KeyError as e:
                _logger.error(
                    f'Missing "exchange-factor" property in notation group in file "{filename}".'
                )
                raise e

        if "on-site" in root_group:
            try:
                spinham.on_site_factor = notation["on-site-factor"][()]
            except KeyError as e:
                _logger.error(
                    f'Missing "on-site-factor" property in notation group in file "{filename}".'
                )
                raise e

    # Read exchange
    if "exchange" in root_group:
        exchange = root_group["exchange"]
        if exchange.attrs["units"].lower() == "rydberg":
            units_conversion = RYDBERG_ENERGY / ENERGY
        elif exchange.attrs["units"].lower() == "joule":
            units_conversion = 1.0 / ENERGY
        elif exchange.attrs["units"].lower() == "kelvin":
            units_conversion = K_BOLTZMANN / ENERGY
        elif exchange.attrs["units"].lower() == "electron-volt":
            units_conversion = ELECTRON_VOLT / ENERGY
        elif exchange.attrs["units"].lower() == "milli-electron-volt":
            units_conversion = 1e-3 * ELECTRON_VOLT / ENERGY
        else:
            _logger.error(
                f"Unknown units '{exchange.attrs['units']}' for exchange in file '{filename}'."
            )
            raise ValueError(f"Unknown units '{exchange.attrs['units']}'.")

        for index in exchange:
            bond = exchange[index]
            atom1 = bond["atom-1"][()].decode("utf-8")
            try:
                atom1 = spinham.get_atom(atom1)
            except ValueError as e:
                _logger.error(
                    f'Atom "{atom1}" in exchange bond {index+1} not found in the atoms group in file "{filename}".'
                )
            atom2 = bond["atom-2"][()].decode("utf-8")
            try:
                atom2 = spinham.get_atom(atom2)
            except ValueError as e:
                _logger.error(
                    f'Atom "{atom2}" in exchange bond {index+1} not found in the atoms group in file "{filename}".'
                )
            ijk = tuple(bond["ijk"][:])
            matrix = bond["matrix"][:]
            spinham.add_exchange(atom1, atom2, ijk, matrix=matrix * units_conversion)

    # Read on-site
    if "on-site" in root_group:
        on_site = root_group["on-site"]

        if on_site.attrs["units"].lower() == "rydberg":
            units_conversion = RYDBERG_ENERGY / ENERGY
        elif on_site.attrs["units"].lower() == "joule":
            units_conversion = 1.0 / ENERGY
        elif on_site.attrs["units"].lower() == "kelvin":
            units_conversion = K_BOLTZMANN / ENERGY
        elif on_site.attrs["units"].lower() == "electron-volt":
            units_conversion = ELECTRON_VOLT / ENERGY
        elif on_site.attrs["units"].lower() == "milli-electron-volt":
            units_conversion = 1e-3 * ELECTRON_VOLT / ENERGY
        else:
            _logger.error(
                f"Unknown units '{on_site.attrs['units']}' for on-site in file '{filename}'."
            )
            raise ValueError(f"Unknown units '{on_site.attrs['units']}'.")

        for index in on_site:
            parameters = on_site[index]
            atom = parameters["atom"][()].decode("utf-8")
            try:
                atom = spinham.get_atom(atom)
            except ValueError as e:
                _logger.error(
                    f'Atom "{atom}" in on-site bond {index+1} not found in the atoms group in file "{filename}".'
                )
            matrix = parameters["matrix"][:]
            spinham.add_on_site(atom, matrix=matrix * units_conversion)

    # Read spiral vector
    if "spiral-vector" in root_group:
        spiral_vector = root_group["spiral-vector"][:]
        units = root_group["spiral-vector"].attrs["units"].lower()

        if units == "absolute":
            spiral_vector = absolute_to_relative(spiral_vector, spinham.reciprocal_cell)
        elif units != "relative":
            _logger.error(
                f"Unknown units '{units}' for spiral vector in file '{filename}'."
            )
            raise ValueError(f"Unknown units '{units}'.")

        spinham.spiral_vector = spiral_vector

    # Read cone axis
    if "cone-axis" in root_group:
        cone_axis = root_group["cone-axis"][:]
        units = root_group["cone-axis"].attrs["units"].lower()
        if units == "relative":
            cone_axis = cone_axis @ spinham.cell
        elif units != "absolute":
            _logger.error(
                f"Unknown units '{units}' for cone axis in file '{filename}'."
            )
            raise ValueError(f"Unknown units '{units}'.")

        spinham.cone_axis = cone_axis

    return spinham


def dump_spinham_hdf5(
    spinham: SpinHamiltonian,
    filename="spinham.hdf5",
    groupname="spinham",
    overwrite=False,
) -> None:
    r"""
    Dump a SpinHamiltonian object to a HDF5 file.

    It can write spin Hamiltonian data to a new file or to a group of an existing file.


    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        The SpinHamiltonian object to be dumped.
    filename : str, default "spinham.hdf5"
        The name of the file where the SpinHamiltonian object will be dumped.
        If ``filename`` already exists, then new group with the name  ``groupname``
        will be created. If filename does not exist, then a new file will be created
        with the name ``filename``.
    groupname : str, default "spinham"
        The name of the root group for the spin Hamiltonian.
        If writing to an existing file, then there should not be a
        group with the name ``groupname`` inside it.

        Note: If you want to save the spin Hamiltonian to the group of second and
        higher depth use: ``groupname = "group/subgroup/subsubgroup"``.
    overwrite : bool, default False
        Whether to overwrite already existing ``groupname`` in the already
        existing ``filename``.
    """

    file = h5py.File(filename, "a")
    try:
        root_group = file.create_group(groupname)
    except ValueError:
        if overwrite:
            del file[groupname]
            root_group = file.create_group(groupname)
        else:
            raise FileExistsError(
                f"Group {groupname} already exists in file {filename}."
            )

    root_group.attrs["type"] = "SpinHamiltonian"

    # Cell
    cell = root_group.create_group("cell")
    cell.create_dataset("a1", data=spinham.a1, dtype="float")
    cell.create_dataset("a2", data=spinham.a2, dtype="float")
    cell.create_dataset("a3", data=spinham.a3, dtype="float")
    cell.attrs["units"] = LENGTH_NAME

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
        exchange.attrs["units"] = ENERGY_NAME
        for e_i, (atom1, atom2, ijk, parameter) in enumerate(spinham.exchange):
            bond = exchange.create_group(str(e_i + 1))
            bond.create_dataset("atom-1", data=atom1.name)
            bond.create_dataset("atom-2", data=atom2.name)
            bond.create_dataset("ijk", data=ijk, dtype=int)
            bond.create_dataset("matrix", data=parameter.matrix, dtype=float)

    # On-site
    if len(spinham.on_site) > 0:
        on_site = root_group.create_group("on-site")
        on_site.attrs["units"] = ENERGY_NAME
        for o_i, (atom, parameter) in enumerate(spinham.on_site):
            bond = on_site.create_group(str(o_i + 1))
            bond.create_dataset("atom", data=atom.name)
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
