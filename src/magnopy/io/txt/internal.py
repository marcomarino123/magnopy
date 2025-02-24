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


import logging

import numpy as np
from wulfric import TORADIANS, Atom, absolute_to_relative, volume

from magnopy._pinfo import logo
from magnopy.exceptions import NotationError
from magnopy.geometry import vector_to_angles
from magnopy.io.txt.verify import _verify_model_file
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.spinham.parameter import MatrixParameter
from magnopy.units.inside import ENERGY, ENERGY_NAME, LENGTH, LENGTH_NAME, TRUE_KEYWORDS
from magnopy.units.si import (
    ANGSTROM,
    BOHR_RADIUS,
    ELECTRON_VOLT,
    K_BOLTZMANN,
    RYDBERG_ENERGY,
)

_logger = logging.getLogger(__name__)

__all__ = ["load_spinham_txt", "dump_spinham_txt"]


SEPARATOR = "=" * 80
SUBSEPARATOR = "-" * 80


def _write_exchange(
    name1: str,
    name2: str,
    ijk: tuple,
    parameter: MatrixParameter,
    write_matrix=True,
    write_iso=False,
    write_dmi=False,
    write_symm=False,
    distance=None,
):
    r"""
    Write a bond to the output file.

    Parameters
    ----------
    name1 : str
        Name of the first atom in the bond.
    name2 : str
        Name of the second atom in the bond.
    ijk : (3,) tuple
        Index of the bond.
    parameter : :py:class:`.MatrixParameter`
        Parameter.
    write_matrix : bool, default True
        Whether to write full matrix of the parameter.
    write_iso : bool, default False
        Whether to write isotropic parameter.
    write_dmi : bool, default False
        Whether to write DMI vector.
    write_symm : bool, default False
        Whether to write Symmetric anisotropic part of the parameter's matrix.
    distance : float, optional
        If passed, then it is written as a comment.
    """

    header_line = []
    header_line.extend(
        [
            f"{name1:<6}",
            f"{name2:<6}",
            f"{ijk[0]:>3}",
            f"{ijk[1]:>3}",
            f"{ijk[2]:>3}",
        ]
    )

    if distance is not None:
        header_line.append(f"# {distance:<8.4f}")

    text = [" ".join(header_line)]

    if write_iso:
        text.append(f"Isotropic {parameter.iso:>8.4f}")

    if write_dmi:
        text.append(" ".join(["DMI"] + [f"{parameter.dmi[i]:>8.4f}" for i in range(3)]))

    if write_symm:
        text.append(
            "#" + " " * 20 + f"{'Axx':>8} {'Ayy':>8} {'Axy':>8} {'Axz':>8} {'Ayz':>8}"
        )
        J_symm = parameter.aniso
        text.append(
            f"Symmetric-anisotropy {J_symm[0][0]:>8.4f} {J_symm[1][1]:>8.4f} "
            + f"{J_symm[0][1]:>8.4f} {J_symm[0][2]:>8.4f} {J_symm[1][2]:>8.4f}"
        )

    if write_matrix:
        text.append("Matrix")
        for i in range(3):
            text.append(" ".join([f"{parameter.matrix[i][j]:>8.4f}" for j in range(3)]))

    return "\n".join(text)


def dump_spinham_txt(
    spinham: SpinHamiltonian,
    filename=None,
    write_matrix=True,
    write_iso=False,
    write_dmi=False,
    write_symm=False,
    write_distance=False,
    write_spin_angles=False,
    print_if_none=True,
):
    r"""
    Dump a SpinHamiltonian object to a .txt file.

    Parameters
    ----------
    spinham : :py:class`.SpinHamiltonian`
        SpinHamiltonian object to dump.
    filename : str, optional
        Filename to dump SpinHamiltonian object to.
        If none provided, then the text is passed to the standard output (terminal).
    write_matrix : bool, default True
        Whether to write full matrix of the parameter.
    write_iso : bool, default False
        Whether to write isotropic parameter.
    write_dmi : bool, default False
        Whether to write DMI vector.
    write_symm : bool, default False
        Whether to write Symmetric anisotropic part of the parameter's matrix.
    write_distance : bool, default False
        Whether to write the distance as a comment.
    write_spin_angles : bool, default False
        Whether to write spin as (phi, theta, S) or (Sx, Sy, Sz).
    print_if_none : bools, default True
        Whether to print the lines if ``filename`` is ``None`` or return them as a list.

    Returns
    -------
    text : list of str
        Model as a text in magnopy format. Only returned if ``filename is None`` and
        ``print_if_none == True``.
        Note: next line symbols are not included. In order to print/write the text
        we advise to use ``"\n".join(text)``

    """

    # Write logo
    text = [logo(comment=True)]
    text.append(SEPARATOR)

    # Write unit cell
    text.append(f"Cell {LENGTH_NAME}")
    text.append(f"# {'x':>10} {'y':>12} {'z':>12}")
    comment_lines = [
        "# <- a (first lattice vector)",
        "# <- b (second lattice vector)",
        "# <- c (third lattice vector)",
    ]
    for i in range(3):
        text.append(
            " ".join(
                [f"{component:12.8f}" for component in spinham.cell[i]]
                + [comment_lines[i]]
            )
        )

    text.append(SEPARATOR)

    # Write atom's position and spins
    text.append("Atoms")
    text.append(f"name {'r1':>10} {'r2':>12} {'r3':>12}")
    if write_spin_angles:
        text[-1] += f" {'St':>6} {'Sp':>6} {'S':>6}"
    else:
        text[-1] += f" {'Sx':>8} {'Sy':>8} {'Sz':>8}"
    for atom in spinham.atoms:
        text.append(
            " ".join(
                [
                    f"{atom.name:4}",
                    f"{atom.position[0]:12.8f}",
                    f"{atom.position[1]:12.8f}",
                    f"{atom.position[2]:12.8f}",
                ]
            )
        )
        try:
            if write_spin_angles:
                S, theta, phi = vector_to_angles(atom.spin_vector, in_degrees=True)
                text[-1] += " " + " ".join(
                    [
                        f"t{theta:8.4f}",
                        f"p{phi:8.4f}",
                        f"{S:8.4f}",
                    ]
                )
            else:
                text[-1] += " " + " ".join(
                    [
                        f"{atom.spin_vector[0]:8.4f}",
                        f"{atom.spin_vector[1]:8.4f}",
                        f"{atom.spin_vector[2]:8.4f}",
                    ]
                )
        except ValueError:
            text[-1] += " " + " ".join(
                [
                    f"{'-':>8}",
                    f"{'-':>8}",
                    f"{'-':>8}",
                ]
            )
    text.append(SEPARATOR)

    # Write notation
    if len(spinham.exchange) > 0 or len(spinham.on_site) > 0:
        text.append("Notation")
        text.append(f"Spin-normalized {spinham.spin_normalized}")
        if len(spinham.exchange) > 0:
            text.append(f"Double-counting {spinham.double_counting}")
            text.append(f"Exchange-factor {spinham.exchange_factor}")
        if len(spinham.on_site) > 0:
            text.append(f"On-site-factor {spinham.on_site_factor}")
        text.append(SEPARATOR)

    # Write exchange parameters
    if len(spinham.exchange) > 0:
        text.append(f"Exchange {ENERGY_NAME}")
        text.append(f"{'# Atom1 Atom2':<13} {'i':>3} {'j':>3} {'k':>3}")
        if write_distance:
            text[-1] += f" # {'distance'}"
        text.append(SUBSEPARATOR)
        for atom1, atom2, ijk, parameter in spinham.exchange:
            if atom1 == atom2 and ijk == (0, 0, 0):
                continue
            if write_distance:
                distance = spinham.get_distance(atom1, atom2, ijk)
            else:
                distance = None
            text.append(
                _write_exchange(
                    atom1.name,
                    atom2.name,
                    ijk,
                    parameter,
                    write_matrix=write_matrix,
                    write_iso=write_iso,
                    write_symm=write_symm,
                    write_dmi=write_dmi,
                    distance=distance,
                )
            )
            text.append(SUBSEPARATOR)
        text.append(SEPARATOR)

    # Write on-site parameters
    if len(spinham.on_site) > 0:
        text.append(f"On-site {ENERGY_NAME}")
        text.append(SUBSEPARATOR)
        for atom, parameter in spinham.on_site:
            text.append(atom.name)
            text.append(
                f"{parameter.xx:>8.4f} {parameter.yy:>8.4f} {parameter.zz:>8.4f} "
                + f"{parameter.xy:>8.4f} {parameter.xz:>8.4f} {parameter.yz:>8.4f}"
            )
            text.append(SUBSEPARATOR)
        text.append(SEPARATOR)

    # Write cone axis
    if spinham.cone_axis is not None:
        text.append(f"Cone-axis absolute")
        text.append(
            f"{spinham.cone_axis[0]:12.8f} {spinham.cone_axis[1]:12.8f} {spinham.cone_axis[2]:12.8f}"
        )
        text.append(SEPARATOR)

    # Write spiral vector
    if spinham.spiral_vector is not None:
        text.append(f"Spiral-vector relative")
        text.append(
            f"{spinham.spiral_vector[0]:12.8f} {spinham.spiral_vector[1]:12.8f} {spinham.spiral_vector[2]:12.8f}"
        )
        text.append(SEPARATOR)

    if filename is not None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(text))
    elif print_if_none:
        print("\n".join(text))
    else:
        return text


def _read_cell(lines):
    R"""
    Read information from the cell section as described in the documentation.

    Input lines have to follow the format::

        Cell <units>
        <scale>
        a_x a_y a_z
        b_x b_y b_z
        c_x c_y c_z

    where optional keywords are:

    * <units> - starts either from "b" or "a".
    * <scale> - either one float or three floats separated by at least one space.

    Parameters
    ----------
    lines : (4,) list of str
        Cell section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Scaled unit cell in the default units of magnopy (``LENGTH``). First index
        corresponds to the lattice vector, second index to the component.
    scale : (3,) :numpy:`ndarray`
        Scale factors for the lattice vectors and absolute atom coordinates.
        Index corresponds to the component.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    # cell <units>
    line = lines[0].split()

    # If no <units> keyword is provided, then the default is used
    if len(line) == 1:
        _logger.info("No <units> nor <scale> keywords are detected.")
        units = LENGTH_NAME
    # If <units> keyword is provided,
    if len(line) == 2:
        # <units> keyword can be first in the keyword list. Only the <units> keyword is alphabetic.
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')

    # Process <units> keyword
    # Only those two cases are possible since the input file is pre-verified
    if units.lower().startswith("b"):
        units_conversion = BOHR_RADIUS / LENGTH
    elif units.lower().startswith("a"):
        units_conversion = ANGSTROM / LENGTH

    # First we read the cell, since we might need to know its volume
    # For the computation of the scale factor

    # If scale factor is not provided
    if len(lines) == 4:
        cell_start = 1
    # If scale factor is provided
    elif len(lines) == 5:
        cell_start = 2

    cell = np.zeros((3, 3), dtype=float)
    for i in range(cell_start, cell_start + 3):
        line = lines[i]
        cell[i - cell_start] = [float(x) for x in line.split()[:3]]
    # Convert the units to the default units of magnopy
    cell *= units_conversion

    # Process <scale> keyword if it is present
    # s
    # or
    # s_x s_y s_z
    if len(lines) == 5:
        scale = lines[1].split()
        # One scale factor is provided
        if len(scale) == 1:
            scale = float(scale[0])

            # Target the desired volume if scale is negative
            if scale < 0:
                scale = abs(scale) / abs(np.linalg.det(cell))

            scale = np.ones(3, dtype=float) * scale
        elif len(scale) == 3:
            scale = [float(x) for x in scale]
    else:
        scale = np.ones(3, dtype=float)

    _logger.info(
        f"Units conversion factor: {units_conversion}; scale factors: {' '.join([str(f) for f in scale])}"
    )

    # Apply the scale factor
    cell *= scale

    return cell, scale


def _read_atoms(lines, spinham: SpinHamiltonian, scale):
    R"""
    Read information from the atoms section as described in the documentation.

    Input lines have to follow the format::

        Atoms <Units>
        name r1 r2 r3 ...
        ...

    Parameters
    ==========
    lines : (N,) list of str
        Atoms section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.
    scale : (3,) |array-like|_
        Scale factors for the lattice vectors and absolute atom coordinates.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added atoms.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    scale = np.array(scale, dtype=float)

    line = lines[0].lower().split()

    # Search for the <units>
    if len(line) == 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "relative"
        _logger.info(
            f"No <units> keyword is detected. Fall back to default (relative)."
        )

    # Decide the case based on <units>
    # Only three cases are possible, since the input lines are verified.
    if units.startswith("r"):
        relative = True
        units_conversion = 1
    elif units.startswith("b"):
        relative = False
        units_conversion = BOHR_RADIUS / LENGTH
    elif units.startswith("a"):
        relative = False
        units_conversion = ANGSTROM / LENGTH

    _logger.info(
        f"Units conversion factor: {units_conversion};"
        + f"coordinates are {'relative' if relative else 'absolute'}"
    )

    # Read atom's data header
    data_header = lines[1].lower().split()

    # Read atoms's information
    for line in lines[2:]:
        line = line.split()
        name = line[data_header.index("name")]

        # Find the coordinates
        if "r1" in data_header:
            relative = True
            _logger.info(f"Atom {name}: Relative coordinates are detected.")
            position = (
                float(line[data_header.index("r1")]),
                float(line[data_header.index("r2")]),
                float(line[data_header.index("r3")]),
            )
        else:
            relative = False
            _logger.info(f"Atom {name}: Absolute coordinates are detected.")
            x, y, z = (
                float(line[data_header.index("x")]),
                float(line[data_header.index("y")]),
                float(line[data_header.index("z")]),
            )
            position = (
                np.array([x * scale[0], y * scale[1], z * scale[2]], dtype=float)
                * units_conversion
            )

        # Find charge
        if "q" in data_header:
            charge = float(line[data_header.index("q")])
        else:
            charge = 0

        # Find g factor
        if "g" in data_header:
            g = float(line[data_header.index("g")])
        else:
            g = 2.0

        # Find spin
        if "sx" in data_header:
            spin = (
                float(line[data_header.index("sx")]),
                float(line[data_header.index("sy")]),
                float(line[data_header.index("sz")]),
            )
        elif "sp" in data_header:
            phi = float(line[data_header.index("sp")])
            theta = float(line[data_header.index("st")])
            s = float(line[data_header.index("s")])
            spin = [
                s * np.sin(theta * TORADIANS) * np.cos(phi * TORADIANS),
                s * np.sin(theta * TORADIANS) * np.sin(phi * TORADIANS),
                s * np.cos(theta * TORADIANS),
            ]
        elif "s" in data_header:
            spin = (
                0,
                0,
                float(line[data_header.index("s")]),
            )
        else:
            spin = (0, 0, 0)

        # At the moment we do not read orbital nor total angular momentum, but in the future we might
        # start to do so. Wulfric does not have the support for the orbital and total angular momentum yet.

        # Add atom to the Hamiltonian
        spinham.add_atom(
            new_atom=name,
            position=position,
            spin=spin,
            relative=relative,
            charge=charge,
            g_factor=g,
        )

    return spinham


def _read_notation(lines, spinham):
    R"""
    Read the notation of the Hamiltonian as described in the documentation.

    Parameters
    ----------
    lines : (4,) list of str
        Notation section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added notation.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """
    # Skip first line with the section header
    i = 1
    while i < len(lines):
        line = lines[i]
        # Whether spins are normalized
        if line.lower().startswith("s"):
            spinham.spin_normalized = line.split()[1].lower() in TRUE_KEYWORDS
        # Whether double counting is present
        elif line.lower().startswith("d"):
            spinham.double_counting = line.split()[1].lower() in TRUE_KEYWORDS
        # Exchange factor
        elif line.lower().startswith("e"):
            spinham.exchange_factor = float(line.split()[1])
        # On-site factor
        elif line.lower().startswith("o"):
            spinham.on_site_factor = float(line.split()[1])
        i += 1
    return spinham


def _read_exchange(lines, spinham):
    R"""
    Read information from the exchange section as described in the documentation.

    Input lines have to follow the format::

        Exchange <Units>
        ----------
        bond
        ----------
        ...

    where optional keywords are:

    * <Units> - starts either from "m" or "e" or "k" or "j" or "r".

    Parameters
    ----------
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added bonds.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    # Search for the <units>
    # Exchange <units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "meV"
        _logger.info(f"No <units> keyword is detected. Fall back to default (meV).")

    # Decide the case based on <Units>
    # Only those cases are possible, since the input lines are pre-verified.
    if units.startswith("r"):
        units_conversion = RYDBERG_ENERGY / ENERGY
        _logger.info(
            "Exchange parameters are provided in Rydberg energy units. "
            + f"Will be converted to {ENERGY_NAME}.",
        )
    elif units.startswith("j"):
        units_conversion = 1 / ENERGY_UNITS
        _logger.info(
            "Exchange parameters are provided in Joule. "
            + f" Will be converted to {ENERGY_NAME}.",
        )
    elif units.startswith("k"):
        units_conversion = K_BOLTZMANN / ENERGY
        _logger.info(
            "Exchange parameters are provided in Kelvin. "
            + f"Will be converted to {ENERGY_NAME}.",
        )
    elif units.startswith("e"):
        units_conversion = ELECTRON_VOLT / ENERGY
        _logger.info(
            "Exchange parameters are provided in electron Volts. "
            + f"Will be converted to {ENERGY_NAME}.",
        )
    elif units.startswith("m"):
        units_conversion = 1e-3 * ELECTRON_VOLT / ENERGY
        _logger.info(
            f"Exchange parameters are provided in meV. "
            + f"Will be converted to {ENERGY_NAME}.",
        )

    _logger.info(f"Units conversion factor: {units_conversion}")

    # Skip first line with the section header
    i = 1
    while i < len(lines):
        # Skip subsection separators
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        # Check if we reached the end of the file
        if i >= len(lines):
            break

        # Detect the beginning and end of the bond data
        bond_start = i
        while i < len(lines) and not lines[i].startswith("-" * 10):
            i += 1
        bond_end = i

        # Read bond and add it to the Hamiltonian
        bond = _read_bond(
            lines[bond_start:bond_end], spinham, units_conversion=units_conversion
        )

    return spinham


def _read_bond(lines, spinham: SpinHamiltonian, units_conversion=1):
    R"""
    Read information from the bond subsection as described in the documentation.

    Input lines have to follow the format::

        A1 A2 i j k
        <Isotropic Jiso>
        <Matrix
        Jxx Jxy Jxz
        Jyx Jyy Jyz
        Jzx Jzy Jzz>
        <Symmetric anisotropy Sxx Syy Sxy Sxz Syz>
        <DMI Dx Dy Dz>

    Parameters
    ----------
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added bond.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """
    # Two labels and a unit cell relative position are always present,
    # since the files are pre-verified.
    line = lines[0].split()
    name1, name2 = line[:2]
    R = tuple([int(x) for x in line[2:5]])

    iso = None
    matrix = None
    symm = None
    dmi = None

    i = 1
    while i < len(lines):
        if lines[i].lower().startswith("i"):
            iso = float(lines[i].split()[1])
        if lines[i].lower().startswith("d"):
            dmi = [float(x) for x in lines[i].split()[1:]]
        if lines[i].lower().startswith("s"):
            Sxx, Syy, Sxy, Sxz, Syz = [float(x) for x in lines[i].split()[1:]]
            symm = [[Sxx, Sxy, Sxz], [Sxy, Syy, Syz], [Sxz, Syz, -Sxx - Syy]]
        if lines[i].lower().startswith("m"):
            matrix = np.zeros((3, 3), dtype=float)
            for j in range(3):
                i += 1
                matrix[j] = [float(x) for x in lines[i].split()]
        spinham.add_exchange(
            name1, name2, R, matrix=matrix, iso=iso, aniso=symm, dmi=dmi
        )
        i += 1
    return spinham


def _read_on_site(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the on-site section as described in the documentation.

    Input lines have to follow the format::

        On-site <Units>
        ----------
        A1
        Axx Ayy Azz Axy Axz Ayz
        ----------
        ...

    where optional keywords are:

    * <Units> - starts either from "m" or "e" or "k" or "j" or "r".

    Parameters
    ----------
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added on-site anisotropy.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    # Search for the <units>
    # On-site <units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "meV"
        _logger.info(
            f"No <units> keyword is detected. Fall back to default ({ENERGY_NAME})."
        )

    # Decide the case based on <units>
    # Only those cases are possible, since the input lines are pre-verified.
    if units.startswith("r"):
        units_conversion = RYDBERG_ENERGY / ENERGY
        _logger.info(
            "On-site anisotropy parameters are provided in Rydberg energy units. "
            + f"Will be converted to {ENERGY_NAME}."
        )
    elif units.startswith("j"):
        units_conversion = 1 / ENERGY
        _logger.info(
            f"On-site anisotropy parameters are provided in Joule. "
            + f"Will be converted to {ENERGY_NAME}."
        )
    elif units.startswith("k"):
        units_conversion = K_BOLTZMANN / ENERGY
        _logger.info(
            f"On-site anisotropy parameters are provided in Kelvin. "
            + f"Will be converted to {ENERGY_NAME}."
        )
    elif units.startswith("e"):
        units_conversion = ELECTRON_VOLT / ENERGY
        _logger.info(
            f"On-site anisotropy parameters are provided in electron-Volts. "
            + f"Will be converted to {ENERGY_NAME}."
        )
    elif units.startswith("m"):
        units_conversion = 1e-3 * ELECTRON_VOLT / ENERGY
        _logger.info(
            f"On-site anisotropy parameters are provided in meV. "
            + f"Will be converted to {ENERGY_NAME}."
        )

    _logger.info(f"Units conversion factor: {units_conversion}")

    # Skip first line with the section header
    i = 1
    while i < len(lines):
        # Skip subsection separators
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        # Check if we reached the end of the file
        if i >= len(lines):
            break

        # Read atom's label:
        atom = spinham.get_atom(lines[i].strip())

        i += 1

        Axx, Ayy, Azz, Axy, Axz, Ayz = [float(lines[i].split()[j]) for j in range(6)]
        matrix = (
            np.array([[Axx, Axy, Axz], [Axy, Ayy, Ayz], [Axz, Ayz, Azz]], dtype=float)
            * units_conversion
        )

        # Pass to the next line once matrix parameters are read
        i += 1

        # Add on-site anisotropy to the Hamiltonian
        spinham.add_on_site(atom, matrix=matrix)

    return spinham


def _read_cone_axis(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the cone-axis section as described in the documentation.

    Input lines have to follow the format::

        Cone-axis <Units>
        nx ny nz

    or::

        Cone-axis <Units>
        alpha beta

    where optional keywords are:

    * <Units> - starts either from "a" or "r".

    Parameters
    ----------
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added ground-state information.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    # Search for the <units>
    # On-site <units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "relative"
        _logger.info(
            f"No <units> keyword is detected. Fall back to default (relative)."
        )

    # Decide the case based on <units>
    # Only those cases are possible, since the input lines are pre-verified.
    if units.startswith("r"):
        relative = True
        _logger.info(
            "Cone axis is provided in the relative coordinates (with respect to the unit cell)"
        )
    elif units.startswith("a"):
        relative = False
        _logger.info("Cone axis is provided in the absolute coordinates")

    n = [float(x) for x in lines[1].split()]

    if len(n) == 2:
        alpha, beta = np.array(n) * TORADIANS
        n = (np.cos(beta) * np.sin(alpha), np.sin(beta) * np.sin(alpha), np.cos(alpha))
        _logger.info(
            "<Units> keyword for cone axis is ignored. Cone axis is provided with alpha and beta angles."
        )
    else:
        if relative:
            n = n @ spinham.cell
        n /= np.linalg.norm(n)

    spinham.cone_axis = n

    return spinham


def _read_spiral_vector(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the spiral-vector section as described in the documentation.

    Input lines have to follow the format::

        Spiral-vector <Units>
        nx ny nz

    or::

        Spiral-vector <Units>
        alpha beta

    where optional keywords are:

    * <Units> - starts either from "a" or "r".

    Parameters
    ----------
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    -------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added spiral-vector information.

    Notes
    -----
    It is assumed, that the input file (i.e. ``lines``) is already pre-verified and filtered.
    """

    # Search for the <units>
    # On-site <units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "relative"
        _logger.info(
            f"No <units> keyword is detected. Fall back to default (Relative)."
        )

    # Decide the case based on <units>
    # Only those cases are possible, since the input lines are pre-verified.
    if units.startswith("r"):
        relative = True
        _logger.info(
            "Spiral vector is provided in the relative coordinates (with respect to the reciprocal cell)"
        )
    elif units.startswith("a"):
        relative = False
        _logger.info("Spiral vector is provided in the absolute coordinates")

    q = [float(x) for x in lines[1].split()]

    if relative:
        q = q @ spinham.reciprocal_cell

    spinham.spiral_vector = q

    return spinham


def _filter_txt_file(filename=None, lines=None, save_filtered=False):
    R"""
    Filter out all comments and blank lines from the model input file.

    Parameters
    ----------
    filename : str, optional
        Path to the file. Either ``filename`` or ``lines`` have to be provided.
    lines : list of str, optional
        Lines of the model input file. Either ``filename`` or ``lines`` have to be provided.
    save_filtered : bool, default False
        Whether to save filtered copy as a separate file.
        A name is the same as of the original file with "filtered_" added to the beginning.

    Returns
    -------
    filtered_lines : (N,) list of str
        Content of the file without comments and blank lines.
    lines_indices : (N,) list
        Indices of filtered lines in the original file.

    Raises
    ------
    ValueError
        If neither ``filename`` nor ``lines`` are provided.
        If both ``filename`` and ``lines`` are provided.

    """

    # Verify input parameters
    if filename is None and lines is None:
        raise ValueError("Either filename or lines have to be provided.")

    if filename is not None and lines is not None:
        raise ValueError("Only one of filename or lines can be provided.")

    # Read the content of the file if lines are not provided
    if lines is None:
        # Read the content of the file
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

    # Filtered lines
    filtered_lines = []
    # Original line indices
    line_indices = []

    # Filter comments and blank lines
    for l_i, line in enumerate(lines):
        # Remove comment lines
        if line.startswith("#"):
            continue
        # Remove inline comments and leading/trailing whitespaces
        line = line.split("#")[0].strip()
        # Remove empty lines
        if line:
            filtered_lines.append(line)
            line_indices.append(l_i + 1)

    # Save filtered copy of the file
    if save_filtered:
        filtered_filename = f"filtered_{filename}"
        with open(filtered_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_lines))
        _logger.debug(
            f"Filtered input file is saved in {os.path.abspath(filtered_filename)}"
        )

    # Return filtered lines and original line indices
    # for the line filtered_lines[i] the original line index is line_indices[i]
    return filtered_lines, line_indices


def load_spinham_txt(filename, save_filtered=False, verbose=False) -> SpinHamiltonian:
    r"""
    Load a SpinHamiltonian object from a .txt file.

    Parameters
    ----------
    filename : str
        Filename to load SpinHamiltonian object from.
    save_filtered : bool
        Whether to save the pre-processed file.
    verbose : bool, default False
        Whether to output verbose comments on the progress.

    Returns
    -------
    spinham :py:class:`.SpinHamiltonian`
        SpinHamiltonian object loaded from file.
    """

    # Read the content of the file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines, indices = _filter_txt_file(filename=filename, save_filtered=save_filtered)

    # Verify input
    sections = _verify_model_file(
        lines, indices, raise_on_fail=True, return_sections=True
    )

    # Construct spin Hamiltonian:
    spinham = SpinHamiltonian()

    # Read the cell
    cell, scale = _read_cell(lines[slice(*sections["cell"])])
    spinham.cell = cell

    # Read atoms
    _read_atoms(lines[slice(*sections["atoms"])], spinham, scale)

    # Read notation
    if "exchange" in sections or "on-site" in sections:
        _read_notation(lines[slice(*sections["notation"])], spinham)

    # If present read exchange parameters
    if "exchange" in sections:
        _read_exchange(lines[slice(*sections["exchange"])], spinham)

    # If present read on-site parameters
    if "on-site" in sections:
        _read_on_site(lines[slice(*sections["on-site"])], spinham)

    # If present read cone axis
    if "cone-axis" in sections:
        _read_cone_axis(lines[slice(*sections["cone-axis"])], spinham)

    # If present read spiral-vector
    if "spiral-vector" in sections:
        _read_spiral_vector(lines[slice(*sections["spiral-vector"])], spinham)

    return spinham
