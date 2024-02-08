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

import numpy as np
from termcolor import colored
from wulfric import TORADIANS, Atom, absolute_to_relative

from magnopy.geometry import vector_to_angles
from magnopy.io.verify import _verify_model_file

_logger = logging.getLogger(__name__)

from magnopy._pinfo import logo
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

__all__ = ["load_model", "dump_model"]


SEPARATOR = "=" * 80
SUBSEPARATOR = "-" * 80


def _write_exchange(
    label1: str,
    label2: str,
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
    label1 : str
        Name of the first atom in the bond.
    label2 : str
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
            f"{label1:<6}",
            f"{label2:<6}",
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
        text.append("Symmetric-anisotropy")
        J_symm = parameter.aniso
        text.append(
            f"{J_symm[0][0]:>8.4f} {J_symm[1][1]:>8.4f} "
            + f"{J_symm[0][1]:>8.4f} {J_symm[0][2]:>8.4f} {J_symm[1][2]:>8.4f}"
        )

    if write_matrix:
        text.append("Matrix")
        for i in range(3):
            text.append(" ".join([f"{parameter.matrix[i][j]:>8.4f}" for j in range(3)]))

    return "\n".join(text)


def dump_model(
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
    =======
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
    text.append("Atoms Relative")
    text.append(f"# Name {'x':>10} {'y':>12} {'z':>12}")
    if write_spin_angles:
        text[-1] += f" {'phi':>6} {'theta':>6} {'S':>6}"
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
                S, theta, phi = vector_to_angles(atom.spin_vector, in_degreees=True)
                # We assume g = 2
                S *= 2
                text[-1] += " " + " ".join(
                    [
                        f"t{theta:8.4f}",
                        f"p{phi:8.4f}",
                        f"{S:8.4f}",
                    ]
                )
            else:
                # We assume g=2
                text[-1] += " " + " ".join(
                    [
                        f"{2*atom.spin_vector[0]:8.4f}",
                        f"{2*atom.spin_vector[1]:8.4f}",
                        f"{2*atom.spin_vector[2]:8.4f}",
                    ]
                )
        except ValueError:
            text[-1] += " #" + " ".join(
                [
                    f"{'-':>7}",
                    f"{'-':>8}",
                    f"{'-':>8}",
                ]
            )
    text.append(SEPARATOR)

    # Write notation
    text.append("Notation")
    text.append(f"Spin-normalized {spinham.spin_normalized}")
    text.append(f"Double-counting {spinham.double_counting}")
    text.append(f"Exchange-factor {spinham.exchange_factor}")
    text.append(f"On-site-factor {spinham.on_site_factor}")
    text.append(SEPARATOR)

    # Write exchange parameters
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

    if filename is not None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(text))
    elif print_if_none:
        print("\n".join(text))
    else:
        return text


def _read_cell(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the cell section as described in the documentation.

    Input lines have to follow the format::

        Cell <Units> <Scale>
        a_x a_y a_z
        b_x b_y b_z
        c_x c_y c_z

    where optional keywords are:

    * <Units> - starts either from "b" or "a".
    * <Scale> - either one float or three floats separated by at least one space.

    Parameters
    ==========
    lines : (4,) list of str
        Cell section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with updated cell.
    """

    # Cell <Units> <Scale>
    # or
    # Cell <Scale> <Units>
    line = lines[0].lower().split()

    # Search for the <Units> keyword
    if len(line) == 1:
        _logger.info("No <Units> nor <Scale> keywords are detected.")
        units = LENGTH_NAME
    if len(line) >= 2:
        # <Units> keyword can be first in the keyword list. Only the <Units> keyword is alphabetic.
        if str.isalpha(line[1]):
            units = line.pop(1).lower()
            _logger.info(f'"{units}" keyword is detected.')
        # <Units> keyword can be last in the keyword list. Only the <Units> keyword is alphabetic.
        elif str.isalpha(line[-1]):
            units = line.pop(-1).lower()
            _logger.info(f'"{units}" keyword is detected.')
        else:
            _logger.info(
                f"No <Units> keywords is detected. Fall back to default ({LENGTH_NAME})."
            )
            units = LENGTH_NAME

    # Process <Units> keyword
    # Only those two cases are possible since the input file is pre-verified
    if units.startswith("b"):
        units_conversion = BOHR_RADIUS / LENGTH
    elif units.startswith("a"):
        units_conversion = ANGSTROM / LENGTH

    # Process <Scale> keyword
    # The <Units> keyword is already popped out of the line list
    # Cell <s>
    # or
    # Cell <s_x s_y s_z>
    if len(line) == 2:
        scale_factors = [float(line[1]) for _ in range(3)]
    elif len(line) == 4:
        scale_factors = [float(line[i]) for i in range(1, 4)]
    else:
        scale_factors = [1.0, 1.0, 1.0]

    _logger.info(
        f"Units conversion factor: {units_conversion}; scale factors: {' '.join([str(f) for f in scale_factors])}"
    )

    cell = np.zeros((3, 3), dtype=float)
    for i in range(1, 4):
        line = lines[i]
        cell[i - 1] = [float(x) for x in line.split()[:3]]

    cell *= units_conversion
    for i in range(3):
        cell[i] *= scale_factors[i]

    spinham.cell = cell

    return spinham


def _read_atoms(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the atoms section as described in the documentation.

    Input lines have to follow the format::

        Atoms <Units>
        A1 i j k <spin1>
        ...

    where optional keywords are:

    * <Units> - starts either from "r" or "a" or "b".
    * <spin> - either one float or three floats or four
    floats separated by at least one space. Alternatively it can have the format
    "p<float> t<float> float"

    Parameters
    ==========
    lines : (N,) list of str
        Atoms section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added atoms.
    """

    line = lines[0].lower().split()

    # Search for the <Units>
    if len(line) == 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "relative"
        _logger.info(
            f"No <Units> keyword is detected. Fall back to default (Relative)."
        )

    # Decide the case based on <Units>
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
        f"Units conversion factor: {units_conversion}; coordinates are {'relative' if relative else 'absolute'}"
    )

    # Read atoms's information
    # A i j k <spin>
    for line in lines[1:]:
        line = line.split()
        # Label is always present, since file is pre-verified
        label = line[0]
        # Coordinates are always present, since file is pre-verified
        coordinates = np.array([float(x) for x in line[1:4]])
        spin_vector = None

        # Now trying to detect the spin vector
        line = line[4:]

        # Only spin value is given
        if len(line) == 1:
            spin_vector = [0, 0, float(line[0])]

        # Either spin vector is given or theta, phi and spin value
        if len(line) == 3:
            # Atom i j k p<angle> t<angle> S
            # or
            # Atom i j k p<angle> S t<angle>
            # or
            # Atom i j k t<angle> p<angle> S
            # or
            # Atom i j k t<angle> S p<angle>
            # or
            # Atom i j k S p<angle> t<angle>
            # or
            # Atom i j k S t<angle> p<angle>
            # It is enough to check for "p", since the file is pre-verified
            if "p" in " ".join(line).lower():
                for i in range(3):
                    if line[i].lower().startswith("p"):
                        phi = float(line[i][1:]) * TORADIANS
                    elif line[i].lower().startswith("t"):
                        theta = float(line[i][1:]) * TORADIANS
                    else:
                        S = float(line[i])
                spin_vector = [
                    S * np.cos(phi) * np.sin(theta),
                    S * np.sin(phi) * np.sin(theta),
                    S * np.cos(theta),
                ]
            # Atom i j k Sx Sy Sz
            else:
                spin_vector = np.array([float(x) for x in line])
        # Spin direction and spin value is given
        # A i j k sdirx sdiry sdirz S
        if len(line) == 4:
            spin_vector = np.array([float(x) for x in line[:3]])
            spin_vector = spin_vector / np.linalg.norm(spin_vector) * float(line[3])

        # Add atom to the Hamiltonian
        if spin_vector is None:
            spinham.add_atom(
                new_atom=label,
                position=coordinates * units_conversion,
                relative=relative,
            )
        else:
            # Here we assume g = 2
            spin_vector /= 2
            spinham.add_atom(
                new_atom=label,
                position=coordinates * units_conversion,
                spin=spin_vector,
                relative=relative,
            )

    return spinham


def _read_notation(lines, spinham):
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
    ==========
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added bonds.
    """

    # Search for the <Units>
    # Exchange <Units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "meV"
        _logger.info(f"No <Units> keyword is detected. Fall back to default (meV).")

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
    ==========
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added bond.
    """
    # Two labels and a unit cell relative position are always present,
    # since the files are pre-verified.
    line = lines[0].split()
    label1, label2 = line[:2]
    atom1 = spinham.get_atom(label1)
    atom2 = spinham.get_atom(label2)
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
            atom1, atom2, R, matrix=matrix, iso=iso, aniso=symm, dmi=dmi
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
    ==========
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added on-site anisotropy.
    """

    # Search for the <Units>
    # On-site <Units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "meV"
        _logger.info(
            f"No <Units> keyword is detected. Fall back to default ({ENERGY_NAME})."
        )

    # Decide the case based on <Units>
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

        # Add On-site anisotropy to the Hamiltonian as a bond
        spinham.add_on_site(atom, matrix=matrix)

    return spinham


def _read_ground_state(lines, spinham: SpinHamiltonian):
    R"""
    Read information from the ground state section as described in the documentation.

    Input lines have to follow the format::

        Ground-state <Units>
        qx qy qz
        nx ny nz

    or::

        Ground-state <Units>
        qx qy qz
        a<alpha> b<beta>

    where optional keywords are:

    * <Units> - starts either from "a" or "r".

    Parameters
    ==========
    lines : (N,) list of str
        Parameters section of the input file.
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with added ground-state information.
    """

    # Search for the <Units>
    # On-site <Units>
    line = lines[0].lower().split()
    if len(line) >= 2:
        units = line[1]
        _logger.info(f'"{units}" keyword is detected.')
    else:
        units = "relative"
        _logger.info(
            f"No <Units> keyword is detected. Fall back to default (Relative)."
        )

    # Decide the case based on <Units>
    # Only those cases are possible, since the input lines are pre-verified.
    if units.startswith("r"):
        relative = True
        _logger.info(
            "Spiral vector is provided in the relative coordinates (with respect to the reciprocal cell)"
        )
    elif units.startswith("a"):
        relative = False
        _logger.info("Spiral vector is provided in the absolute coordinates")

    _logger.info(
        f"Spiral vector is in {'relative' if relative else 'absolute'} coordinates."
    )

    q = [float(x) for x in lines[1].split()]

    if not relative:
        q = absolute_to_relative(q, spinham.reciprocal_cell)

    spinham.spiral_vector = q

    if "a" in lines[2]:
        for entry in lines[2].split():
            if entry.lower().startswith("a"):
                alpha = float(entry[1:]) * TORADIANS
            if entry.lower().startswith("b"):
                beta = float(entry[1:]) * TORADIANS
        n = (np.cos(beta) * np.sin(alpha), np.sin(beta) * np.sin(alpha), np.cos(alpha))
    else:
        n = [float(x) for x in lines[2].split()]

    spinham.cone_axis = n

    return spinham


def _filter_model_file(filename=None, lines=None, save_filtered=False):
    R"""
    Filter out all comments and blank lines from the model input file.

    Parameters
    ==========
    filename : str, optional
        Path to the file.
    lines : list of str, optional
        Lines of the model input file.
    save_filtered : bool, default False
        Whether to save filtered copy as a separate file.
        A name is the same as of the original file with ".filtered" added to the end.

    Returns
    =======
    filtered_lines : (N,) list of str
        Content of the file without comments and blank lines.
    lines_indices : (N,) list
        Indices of filtered lines in the original file.
    """

    if lines is None:
        # Read the content of the file
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

    # Filter comments and blank lines
    filtered_lines = []
    line_indices = []
    for l_i, line in enumerate(lines):
        if line.startswith("#"):
            continue
        line = line.strip().split("#")[0]
        if line:
            filtered_lines.append(line)
            line_indices.append(l_i + 1)

    if save_filtered:
        with open(filename + ".filtered", "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_lines))
        _logger.debug(
            f"Filtered input file is saved in {os.path.abspath(filename + '.filtered')}"
        )

    return filtered_lines, line_indices


def load_model(filename, save_filtered=False, verbose=False) -> SpinHamiltonian:
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

    lines, indices = _filter_model_file(filename=filename, save_filtered=save_filtered)

    # Verify input
    sections = _verify_model_file(
        lines, indices, raise_on_fail=True, return_sections=True
    )

    # Construct spin Hamiltonian:
    spinham = SpinHamiltonian()

    # Read the cell
    _read_cell(lines[slice(*sections["c"])], spinham)

    # Read atoms
    _read_atoms(lines[slice(*sections["a"])], spinham)

    # Read notation
    _read_notation(lines[slice(*sections["n"])], spinham)

    # If present read exchange parameters
    if "e" in sections:
        _read_exchange(lines[slice(*sections["e"])], spinham)

    # If present read on-site parameters
    if "o" in sections:
        _read_on_site(lines[slice(*sections["o"])], spinham)

    # If present read ground state
    if "g" in sections:
        _read_ground_state(lines[slice(*sections["g"])], spinham)

    return spinham
