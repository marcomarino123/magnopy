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
import wulfric
from termcolor import cprint
from wulfric import Atom, print_2d_array
from wulfric.constants import TORADIANS

from magnopy._pinfo import logo
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.spinham.parameter import ExchangeParameter
from magnopy.units import BOHR_TO_ANGSTROM, JOULE_TO_meV, K_TO_meV, Ry_TO_meV

__all__ = ["load_model", "dump_model"]


SEPARATOR = "=" * 80
SUBSEPARATOR = "-" * 80


def _write_bond(name1: str, name2: str, ijk: tuple, J: ExchangeParameter):
    r"""
    Write a bond to the output file.

    Parameters
    ----------
    name1 : str
        Name of the first atom in the bond.
    name2 : str
        Name of the second atom in the bond.
    ijk : tuple
        Index of the bond.
    J : :py:class:`.ExchangeParameter`
        Exchange parameter for the bond.
    """

    text = [SUBSEPARATOR]
    text.append(
        f"{name1:<6} "
        + f"{name2:<6} "
        + f"{ijk[0]:>3} {ijk[1]:>3} {ijk[2]:>3} "
        + f"{J.iso:>8.4}"
    )
    text.append("Matrix")
    text.append(print_2d_array(J.matrix, fmt="8.4f", print_result=False, borders=False))

    return "\n".join(text)


def dump_model(spinham: SpinHamiltonian, filename):
    """
    Dump a SpinHamiltonian object to a .txt file.

    Parameters
    ----------
    spinham : :py:class`.SpinHamiltonian`
        SpinHamiltonian object to dump.
    filename : str
        Filename to dump SpinHamiltonian object to.
    """

    # Write logo
    text = [logo(comment=True)]
    text.append(SEPARATOR)

    # Write unit cell
    text.append("Cell: Angstrom")
    text.append(f"# {'x':>10} {'y':>12} {'z':>12}")
    text.append(
        wulfric.print_2d_array(
            spinham.cell,
            fmt="12.8f",
            print_result=False,
            borders=False,
            footer_column=[
                "# <- a (first lattice vector)",
                "# <- b (second lattice vector)",
                "# <- c (third lattice vector)",
            ],
        )
    )
    text.append(SEPARATOR)

    # Write atom's position and spins
    text.append("Atoms: relative")
    text.append(f"# Name {'x':>10} {'y':>12} {'z':>12}")
    for atom in spinham.atoms:
        text.append(
            f"{atom.name:4} "
            + f"{atom.position[0]:12.8f} "
            + f"{atom.position[1]:12.8f} "
            + f"{atom.position[2]:12.8f} "
        )
        try:
            text[-1] += (
                f"{atom.spin_vector[0]:8.4f} "
                + f"{atom.spin_vector[1]:8.4f} "
                + f"{atom.spin_vector[2]:8.4f}"
            )
        except ValueError:
            pass
    text.append(SEPARATOR)

    # Write notation
    text.append("Notation: ")
    try:
        text.append(f"Spin normalized: {spinham.spin_normalized}")
        text.append(f"Double counting: {spinham.double_counting}")
        text.append(f"Factor: {spinham.factor}")
        text.append("# Latex-styled:")
        text.append("# " + "\n# ".join(spinham.notation_string.split("\n")))
    except ValueError:
        text.append("Undefined")
    text.append(SEPARATOR)

    # Define which atom's names are unique
    names = [atom.name for atom in spinham.atoms]
    unique_names = [
        atom.name if names.count(atom.name) == 1 else atom.fullname
        for atom in spinham.atoms
    ]
    unique_names = dict(zip(spinham.atoms, unique_names))

    # Write exchange parameters
    text.append("Parameters: meV")
    text.append(f"{'# Atom1 Atom2':<13} {'i':>3} {'j':>3} {'k':>3} {'Jiso':>8}")
    for atom1, atom2, (i, j, k), J in spinham:
        text.append(_write_bond(unique_names[atom1], unique_names[atom2], (i, j, k), J))
    text.append(SEPARATOR)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(text))


def _read_cell(lines, i, spinham: SpinHamiltonian, verbose=False):
    R"""
    Read information from the cell section as described in the documentation.

    Parameters
    ==========
    lines : list of str
        Lines from the input file
    i : int
        Index of the section header, which contain keyword "cell"
    spinham: :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.
    verbose : bool, default False
        Whether to output comments about the reading process.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with the updated cell.
    index : int
        Index of the next line after the section.
    """

    line = lines[i].lower().split()

    # Search for the <Units> keyword
    units_factor = 1
    if len(line) == 1 and verbose:
        print("No <Units> nor <Scale> keywords are detected.")
        units = "angstroms"
    if len(line) >= 2:
        if str.isalpha(line[1]):
            units = line.pop(1).lower()
            if verbose:
                print(f'"{units}" keyword is detected.')
        elif str.isalpha(line[-1]):
            units = line.pop(-1).lower()
            if verbose:
                print(f'"{units}" keyword is detected.')
        else:
            print("No <Units> keywords is detected.")
            units = "angstroms"

    # Process found or default <Units> keyword
    if units.startswith("b"):
        units_factor = BOHR_TO_ANGSTROM
        if verbose:
            print(f"Bohr units are used, will be converted to angstroms.")
    elif units.startswith("a") and verbose:
        print(f"Angstrom units are used.")
    elif verbose:
        cprint(
            f'Units keyword "{units}" does not match the allowed ones (angstrom or bohr).\n'
            + "Lattice vectors are interpreted as given in Angstroms.",
            color="red",
        )

    # Search for the <Scale>
    scale_factors = [1, 1, 1]
    if len(line) == 2:
        try:
            scale = float(line[1])
            scale_factors = [scale for _ in range(3)]
        except ValueError:
            if verbose:
                cprint(
                    f"Failed to read <Scale>: {line[1]}\n"
                    + "Expected 1 number.\n"
                    + "Continue with unscaled lattice vectors.",
                    color="red",
                )
    elif len(line) == 4:
        try:
            scale_factors = [float(line[i]) for i in range(1, 4)]
        except ValueError:
            if verbose:
                cprint(
                    f'Failed to read <Scale>: {" ".join(line[1:4])}\n'
                    + "Expected 3 numbers.\n"
                    + "Continue with unscaled lattice vectors.",
                    color="red",
                )
    elif len(line) != 1 and verbose:
        cprint(
            f"Failed to read <Scale>: {' '.join(line[1:])}\n"
            + "Expected 1 or 3 numbers.\n"
            + "Continue with unscaled lattice vectors.",
            color="red",
        )

    if verbose:
        print(
            f"Unit factor: {units_factor}, scale factors: {' '.join([str(f) for f in scale_factors])}"
        )

    cell = []
    for j in range(3):
        i += 1
        line = lines[i]
        try:
            cell.append(
                [float(x) * scale_factors[j] * units_factor for x in line.split()[:3]]
            )
        except ValueError:
            raise ValueError(f'Failed to read lattice vector from a line "{line}"')
    spinham.cell = cell
    return spinham, i + 1


def _read_atoms(lines, i, spinham: SpinHamiltonian, verbose=False):
    R"""
    Read information from the atoms section as described in the documentation.

    Parameters
    ==========
    lines : list of str
        Lines from the input file
    i : int
        Index of the section header, which contain keyword "cell"
    spinham: :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.
    verbose : bool, default False
        Whether to output comments about the reading process.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with the updated cell.
    index : int
        Index of the next line after the section.
    """

    line = lines[i].lower().split()

    # Search for the <Units>
    if len(line) >= 2:
        units = line[1]
        if verbose:
            print(f'"{line[1]}" keyword is detected.')
    else:
        units = "relative"
        if verbose:
            print(f"No <Units> keyword is detected. Default value (relative) is used.")

    # Decide the case based on <Units>
    if units.startswith("r"):
        relative = True
        units_factor = 1
        if verbose:
            print(f"Coordinates are interpreted as relative.")
    elif units.startswith("b"):
        relative = False
        units_factor = BOHR_TO_ANGSTROM
        if verbose:
            print(
                f"Bohr units are used, will be converted to angstroms. Coordinates are absolute."
            )
    elif units.startswith("a"):
        relative = False
        units_factor = 1
        if verbose:
            print(f"Angstrom units are used. Coordinates are absolute.")
    else:
        relative = False
        units_factor = 1
        if verbose:
            cprint(
                f'Units keyword "{units}" does not match the allowed ones '
                + '("relative" or "angstrom" or "bohr").\n'
                + "Atom coordinates are interpreted as relative.",
                color="red",
            )

    if verbose:
        print(f"Units factor: {units_factor}")

    # Read atoms's information
    i += 1
    while i < len(lines) and not lines[i].startswith("=" * 10):
        line = lines[i]
        if len(line.split()) < 4:
            raise ValueError(
                f'Failed to read atom information from the line "{line}"\n'
                + "Expected at least one string and three numbers."
            )
        name = line.split()[0]
        try:
            position = [float(x) * units_factor for x in line.split()[1:4]]
        except ValueError:
            raise ValueError(
                f'Failed to read positions from "{" ".join(line.split()[1:4])}".'
            )

        # Try to read spin information
        spin_vector = None
        if len(line.split()) > 4:
            line = line.split()[4:]
            if len(line) == 1:
                try:
                    spin_vector = [0, 0, float(line[0])]
                except ValueError:
                    raise ValueError(
                        f'Failed to read spin value from "{line[0]}".\n'
                        + "Expected one number."
                    )
            elif len(line) == 4:
                try:
                    spin_vector = np.array(
                        [float(line[j]) for j in range(3)], dtype=float
                    )
                    s_value = float(line[3])
                except ValueError:
                    raise ValueError(
                        f'Failed to read spin direction and value from "{" ".join(line)}".\n'
                        + "Expected four numbers."
                    )
                spin_vector = spin_vector / np.linalg.norm(spin_vector) * s_value
            elif len(line) == 3:
                if line[0].startswith("p") and line[1].startswith("t"):
                    try:
                        phi = float(line[0][1:]) * TORADIANS
                        theta = float(line[1][1:]) * TORADIANS
                        s_value = float(line[2])
                        spin_vector = [
                            s_value * np.sin(theta) * np.cos(phi),
                            s_value * np.sin(theta) * np.sin(phi),
                            s_value * np.cos(theta),
                        ]
                    except ValueError:
                        raise ValueError(
                            f'Failed to read phi, theta, S from "{" ".join(line)}".\n'
                            + "Expected three numbers with the format: "
                            + "p<number> t<number> number"
                        )
                else:
                    try:
                        spin_vector = [float(line[j]) for j in range(3)]
                    except ValueError:
                        raise ValueError(
                            f'Failed to read spin from "{" ".join(line)}".\n'
                            + "Expected three numbers."
                        )

            elif verbose:
                cprint(
                    f'Failed to read spin information from "{" ".join(line)}". '
                    + "Expected either 1 or 3 or 4 numbers.\n"
                    + f"Proceed with spinless atom {name}",
                    color="red",
                )

        # Add atom to the Hamiltonian
        if spin_vector is not None:
            spinham.add_atom(name, position=position, spin=spin_vector)
        else:
            spinham.add_atom(name, position=position)

        i += 1
    return spinham, i


def _read_parameters(lines, i, spinham, verbose=False):
    R"""
    Read information from the parameters section as described in the documentation.

    Parameters
    ==========
    lines : list of str
        Lines from the input file
    i : int
        Index of the section header, which contain keyword "cell"
    spinham: :py:class:`.SpinHamiltonian`
        Spin Hamiltonian, where the data are saved.
    verbose : bool, default False
        Whether to output comments about the reading process.

    Returns
    =======
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian with the updated cell.
    index : int
        Index of the next line after the section.
    """

    # Search for the <Units>
    line = lines[i].lower().split()
    if len(line) >= 2:
        units = line[1]
        if verbose:
            print(f'"{line[1]}" keyword is detected.')
    else:
        units = "meV"
        if verbose:
            print(f"No <Units> keyword is detected. Default value (meV) is used.")

    # Decide the case based on <Units>
    if units.startswith("r"):
        units_factor = Ry_TO_meV
        if verbose:
            print(
                f"Parameters are provided in Rydberg energy units. Will be converted to meV."
            )
    elif units.startswith("j"):
        units_factor = JOULE_TO_meV
        if verbose:
            print(f"Parameters are provided in Joule. Will be converted to meV.")
    elif units.startswith("k"):
        units_factor = K_TO_meV
        if verbose:
            print(f"Parameters are provided in Kelvin. Will be converted to meV.")
    elif units.startswith("e"):
        units_factor = 1e3
        if verbose:
            print(
                f"Parameters are provided in electron-Volts. Will be converted to meV."
            )
    elif units.startswith("m"):
        units_factor = 1
        if verbose:
            print(f"Parameters are provided in meV.")
    else:
        units_factor = 1
        if verbose:
            cprint(
                f'Units keyword "{units}" does not match the allowed ones '
                + '("meV", "eV", "K", "J", "Ry").\n'
                + "Parameters are interpreted as provided in meV.",
                color="red",
            )

    if verbose:
        print(f"Units factor: {units_factor}")

    i += 1
    while i < len(lines) and not lines[i].startswith("=" * 10):
        line = lines[i]
        if line.startswith("-" * 10):
            spinham, i = _read_parameters_section(
                lines, i, spinham, units_factor=units_factor, verbose=verbose
            )
        else:
            i += 1
    return spinham, i


def _read_parameters_section(
    lines, i, spinham: SpinHamiltonian, units_factor=1, verbose=False
):
    i += 1
    name1, name2 = lines[i].split()[:2]
    atom1 = spinham.get_atom(name1)
    atom2 = spinham.get_atom(name2)
    R = tuple([int(x) for x in lines[i].split()[2:5]])
    i += 2
    matrix = []
    for j in range(3):
        line = lines[i + j]
        matrix.append([float(x) for x in line.split()[:3]])
    i += 3
    spinham.add_bond(atom1, atom2, R, matrix=matrix)

    return spinham, i


def _read_notation(lines, i, spinham, verbose=False):
    i += 1
    for j in range(3):
        line = lines[i + j]
        if line.startswith("spin normalized"):
            spinham.spin_normalized = line.split(":")[1].strip() in ["true", "1"]
        elif line.startswith("double counting"):
            spinham.double_counting = line.split(":")[1].strip() in ["true", "1"]
        elif line.startswith("factor"):
            spinham.factor = float(line.split(":")[1])
    return spinham, i + 3


SUPPORTED_SECTIONS = {
    "cell": _read_cell,
    "atoms": _read_atoms,
    "notation": _read_notation,
    "parameters": _read_parameters,
}


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

    # Filter comments and blank lines
    filtered_lines = []
    line_mapping = []
    for l_i, line in enumerate(lines):
        if line.startswith("#"):
            continue
        line = line.strip().split("#")[0]
        if line:
            filtered_lines.append(line)
            line_mapping.append(l_i)

    if save_filtered:
        with open(filename + ".filtered", "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_lines))

    # Read sections
    spinham = SpinHamiltonian()
    i = 0
    while i < len(filtered_lines):
        if filtered_lines[i].startswith("=" * 10) or i == 0:
            i += int(filtered_lines[i].startswith("=" * 10))
            if i >= len(filtered_lines):
                break

            section_keyword = filtered_lines[i].split()[0].lower()
            if section_keyword in SUPPORTED_SECTIONS:
                if verbose:
                    print(f"Found {section_keyword} section, reading...")
                spinham, i = SUPPORTED_SECTIONS[section_keyword](
                    filtered_lines, i, spinham, verbose=verbose
                )
                if verbose:
                    cprint("Done", color="green")
            elif verbose:
                cprint(
                    f"Tried to detect the section from the line {line_mapping[i]}:\n\n"
                    + f'    "{filtered_lines[i]}"\n\n'
                    + "Failed. Supported section keywords are (case-insensitive):\n\n    "
                    + "\n    ".join(SUPPORTED_SECTIONS)
                    + '\n\nProceed to search for the next section separator (10 or more "=" symbols)',
                    color="red",
                )
                i += 1
        else:
            if verbose:
                cprint(
                    f"Skipping line {line_mapping[i]}:\n\n    " + filtered_lines[i],
                    color="red",
                )
            i += 1

    if verbose:
        print("Reached end of the file.")

    return spinham
