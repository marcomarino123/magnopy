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

import wulfric
from wulfric import Atom, print_2d_array

from magnopy._pinfo import logo
from magnopy.spinham.energy import Energy
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.spinham.parameter import ExchangeParameter

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


def read_cell(lines, i, spinham: SpinHamiltonian):
    i += 1
    cell = []
    for j in range(3):
        line = lines[i + j]
        cell.append([float(x) for x in line.split()[:3]])
    spinham.cell = cell
    return spinham, i + 3


def read_atoms(lines, i, spinham: SpinHamiltonian):
    i += 1
    line = i < len(lines)
    while line and not lines[i].startswith("=" * 20):
        line = lines[i]
        name = line.split()[0]
        position = [float(x) for x in line.split()[1:4]]
        spin_vector = [float(x) for x in line.split()[4:7]]
        if len(spin_vector) == 3:
            spinham.add_atom(name, position=position, spin=spin_vector)
        elif len(spin_vector) == 1:
            spinham.add_atom(
                name, position=position, spin_vector=(0, 0, spin_vector[0])
            )
        else:
            spinham.add_atom(name, position=position)
        i += 1
    return spinham, i


def read_parameters(lines, i, spinham):
    i += 1
    line = i < len(lines)
    while line and not lines[i].startswith("=" * 20):
        line = lines[i]
        if line.startswith("-" * 20):
            spinham, i = read_parameters_section(lines, i, spinham)
        else:
            i += 1
    return spinham, i


def read_parameters_section(lines, i, spinham: SpinHamiltonian):
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


def read_notation(lines, i, spinham):
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


def choose_section(lines, i):
    r"""
    Choose which section to read from the file.

    Parameters
    ----------
    lines : list
        List of lines from the file.
    i : int
        Index of the line to read.

    Returns
    -------
    read_section : str
        Section to read.
    """
    if i >= len(lines):
        return None
    line = lines[i]
    if line.startswith("cell:"):
        read_section = read_cell
    elif line.startswith("atoms:"):
        read_section = read_atoms
    elif line.startswith("notation:"):
        read_section = read_notation
    elif line.startswith("parameters:"):
        read_section = read_parameters
    else:
        read_section = None

    return read_section


def load_model(filename, save_filtered=False) -> SpinHamiltonian:
    r"""
    Load a SpinHamiltonian object from a .txt file.

    Parameters
    ----------
    filename : str
        Filename to load SpinHamiltonian object from.
    save_filtered : bool
        Whether to save the pre-processed file.

    Returns
    -------
    spinham :py:class:`.SpinHamiltonian`
        SpinHamiltonian object loaded from file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    filtered_lines = []
    for line in lines:
        if line.startswith("#"):
            continue
        line = line.strip().lower().split("#")[0]
        if line:
            filtered_lines.append(line)

    if save_filtered:
        with open(filename + ".filtered", "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_lines))

    i = 0
    spinham = Energy()
    while i < len(filtered_lines):
        line = filtered_lines[i]
        if line.startswith("=" * 20) or i == 0:
            if line.startswith("=" * 20):
                i += 1
            read_section = choose_section(filtered_lines, i)
            if read_section is not None:
                spinham, i = read_section(filtered_lines, i, spinham)
        else:
            i += 1

    return spinham
