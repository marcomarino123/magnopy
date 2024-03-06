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

from magnopy.exceptions import FailedToVerifyModelFile
from magnopy.units.inside import FALSE_KEYWORDS, TRUE_KEYWORDS

_all_ = []

_logger = logging.getLogger(__name__)


def _is_float(word):
    r"""
    Check if the ``word`` can be converted to ``float``

    Returns
    -------
    bool
        Whether the word can be converted to a float.
    """
    try:
        word = float(word)
        return True
    except ValueError:
        return False


def _is_integer(word):
    r"""
    Check if the ``word`` can be converted to ``int``

    Returns
    -------
    bool
        Whether the word can be converted to an integer.
    """

    try:
        word = int(word)
        return True
    except ValueError:
        return False


def _is_bool(word):
    r"""
    Check if the ``word`` is one of the supported keywords for boolean values.

    Returns
    -------
    bool
        Whether the word is one of the supported keywords for boolean values.
    """
    return word.lower() in TRUE_KEYWORDS + FALSE_KEYWORDS


def _is_atom_label(word, line_index):
    error_messages = []
    # Atom's name has to start from a number or a letter and should not contain any "#".abs
    # Atom's name should not start nor end with double underscore "__"
    if (
        not (str.isalnum(word[0]) and word.count("#") == 0)
        or word.startswith("__")
        or word.endswith("__")
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: Atom labels have to start with a",
                    'letter or a number and should not contain any "#" symbols',
                    'and should not start nor end with double underscore "__",',
                    f"got {word}",
                ]
            )
        )
    return error_messages


def _verify_cell(lines, line_indices):
    error_messages = []

    # Check size of the cell section
    if len(lines) != 4:
        error_messages.append(
            f'"cell" section has to have exactly 4 lines, {len(lines)} found\n'
            + "\n".join(lines)
        )
        # Do not proceed with the rest of the checks
        return error_messages

    def is_units_keyword(word):
        return word.startswith("a") or word.startswith("b")

    # At this moment there are four lines present
    line = lines[0].lower().split()
    # If <Units> keyword present:
    # Cell Angstrom
    # or <Scale> keyword present and it is one number
    # Cell 1.5
    if len(line) == 2:
        if not (_is_float(line[1]) or is_units_keyword(line[1])):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected a number",
                        f'or a word starting from "a" or "b", got "{line[1]}"',
                    ]
                )
            )
    # If both <Units> and <Scale> keywords are present and <Scale> is one number:
    # Cell Angstrom 1.5
    # or
    # Cell 1.5 Angstrom
    elif len(line) == 3:
        if (_is_float(line[1]) and is_units_keyword(line[2])) or (
            _is_float(line[2]) and is_units_keyword(line[1])
        ):
            pass
        else:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected a number",
                        f'and a word starting from "a" or "b",',
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    # If only <Scale> keyword is present and three numbers are given:
    # Cell 1.2 1.4 1.1
    elif len(line) == 4:
        if _is_float(line[1]) and _is_float(line[2]) and _is_float(line[3]):
            pass
        else:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected three numbers,",
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    # If both <Units> and <Scale> keywords are present
    # and <Scale> is given by three numbers:
    # Cell Angstrom 1.2 1.4 1.1
    # or
    # Cell 1.2 1.4 1.1 Angstrom
    elif len(line) == 5:
        if (
            _is_float(line[1])
            and _is_float(line[2])
            and _is_float(line[3])
            and is_units_keyword(line[4])
        ) or (
            is_units_keyword(line[1])
            and _is_float(line[2])
            and _is_float(line[3])
            and _is_float(line[4])
        ):
            pass
        else:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}:",
                        "expected three numbers and",
                        'a word starting from "a" or "b"',
                        'or a word starting from "a" or "b" and three numbers,',
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "cell" keyword',
                    "and/or <Units> and/or <Scale>",
                    "(from 1 to 5 entries, separated by spaces),",
                    f'got "{" ".join(lines[0])}"',
                ]
            )
        )

    for i in range(1, 4):
        line = lines[i].split()
        if not (
            len(line) == 3
            and (_is_float(line[0]) and _is_float(line[1]) and _is_float(line[2]))
        ):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: expected three numbers,",
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )

    return error_messages


def _verify_atoms(lines, line_indices):
    error_messages = []
    # Check condition about the size of the section
    # At least two lines have to be present: header and at least one atom
    if len(lines) < 2:
        error_messages.append(
            " ".join(
                [
                    f'"atoms" section has to contain header and at least one atom',
                    f"(at least 2 lines in total), {len(lines)} found\n",
                    "\n".join(lines),
                ]
            )
        )
        # Do not proceed with the rest of the checks
        return error_messages

    def is_units_keyword(word):
        return word.startswith("r") or word.startswith("a") or word.startswith("b")

    # At this moment there are at least two lines present
    line = lines[0].lower().split()
    # If <Units> keyword is present, then line has 2 entries
    # Atoms <Units>
    if len(line) == 2:
        if not is_units_keyword(line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected word starting from",
                        f'"a" or "b" or "r", got "{line[1]}"',
                    ]
                )
            )
    # If units keyword is not present, then the line has only one entry:
    # Atoms
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "atoms" keyword',
                    f'and/or <Units>, got "{" ".join(line)}"',
                ]
            )
        )

    # Check each atom line
    for i in range(1, len(lines)):
        line = lines[i].split()

        # Minimum input is the atom label and coordinates:
        # Atom i j k
        if len(line) < 4:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: expected to have",
                        "an atom identifier",
                        '(any string, which does not contain "#" symbol) and',
                        "at least three numbers (atom coordinates),",
                        f'got "{" ".join(line)}"',
                    ]
                )
            )
        else:
            error_messages.extend(_is_atom_label(line[0], line_indices[i]))
            # Atom coordinates have to be convertible to float
            if not (_is_float(line[1]) and _is_float(line[2]) and _is_float(line[3])):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: expected atom's coordinates",
                            "(three numbers, separated by spaces),",
                            f'got "{" ".join(line[1:4])}"',
                        ]
                    )
                )
            # Spin may be specified as a number:
            # Atom i j k S
            if len(line) == 5:
                if not _is_float(line[4]):
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i]}: expected spin value (one number)",
                                f'(spin value), got "{" ".join(line[4])}"',
                            ]
                        )
                    )
            # Spin may be specified as a spin vector:
            # Atom i j k Sx Sy Sz
            # or as two angles and spin value
            # Atom i j k p90 t45 S
            # In the second case order of three last entries does not matter
            elif len(line) == 7:
                if not (
                    (_is_float(line[4]) and _is_float(line[5]) and _is_float(line[6]))
                    or (
                        _is_float(line[4].lower().replace("p", "").replace("t", ""))
                        and _is_float(line[5].lower().replace("p", "").replace("t", ""))
                        and _is_float(line[6].lower().replace("p", "").replace("t", ""))
                        and "".join(line[4:7]).lower().count("p") == 1
                        and "".join(line[4:7]).lower().count("t") == 1
                    )
                ):
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i]}: expected three numbers",
                                "(spin vector) or one number and",
                                "two entries in the format:",
                                '"p<number>" and "t<number>"',
                                "(spin value and two angles),",
                                f'got "{" ".join(line[4:8])}"',
                            ]
                        )
                    )
            # Spin may be specified as a direction vector and value:
            # Atom i j k x y z S
            elif len(line) == 8:
                if not (
                    _is_float(line[4])
                    and _is_float(line[5])
                    and _is_float(line[6])
                    and _is_float(line[7])
                ):
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i]}: expected four numbers",
                                "(spin direction (3) and spin value (1)),",
                                f'got "{" ".join(line[4:8])}"',
                            ]
                        )
                    )
            # If spin is not provided, then each line has to contain only four entries.
            elif len(line) != 4:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: expected nothing or",
                            "one of the supported formats for <spin> keyword",
                            "(1, 3 or 4 entries, separated by space),"
                            f'got "{" ".join(line[4:])}"',
                        ]
                    )
                )

    return error_messages


def _verify_notation(lines, line_indices):
    error_messages = []
    # Check condition about the size of the section
    if len(lines) != 5:
        error_messages.append(
            " ".join(
                [
                    f'"notation" section has to contain exactly 5 lines',
                    f"{len(lines)} found\n",
                    "\n".join(lines),
                ]
            )
        )
        # Do not proceed with the rest of the checks
        return error_messages

    # Check that first line contains only the "notation" keyword
    if len(lines[0].split()) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected only the "notation" keyword,',
                    f"got {lines[0]}",
                ]
            )
        )

    # The order of properties after the sorting is: 'd' 'e' 'o' 's'
    # Shift in order to skip first line with the notation keyword
    sorted_indices = [
        i[0] + 1 for i in sorted(enumerate(lines[1:5]), key=lambda x: x[1][0].lower())
    ]

    # Check each property

    # error messages
    keywords = ["d", "e", "o", "s"]
    on_keyword_fail = [
        'expected line starting with "d" (for double-counting)',
        'expected line starting with "e" (for exchange-factor)',
        'expected line starting with "o" (for on-site-factor)',
        'expected line starting with "s" (for spi-normalized)',
    ]
    on_value_fail = [
        f'expected {" or ".join(TRUE_KEYWORDS+FALSE_KEYWORDS)}',
        "expected one number",
        "expected one number",
        f'expected {" or ".join(TRUE_KEYWORDS+FALSE_KEYWORDS)}',
    ]
    value_verify_function = [_is_bool, _is_float, _is_float, _is_bool]
    # Check every property:
    for i in range(4):
        line = lines[sorted_indices[i]].lower()
        if not line.startswith(keywords[i]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[sorted_indices[i]]}:",
                        f"{on_keyword_fail[i]}, got {line}",
                    ]
                )
            )
        line = line.split()
        if len(line) != 2:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[sorted_indices[i]]}: expected to have",
                        f"two entries, separated by spaces, got {' '.join(line)}",
                    ]
                )
            )

        elif not value_verify_function[i](line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[sorted_indices[i]]}:",
                        f"{on_value_fail[i]}, got {line[1]}",
                    ]
                )
            )

    return error_messages


def _verify_bond(lines, line_indices):
    error_messages = []

    # We need to make sure that only one entry of the type exists.
    found_data = {"matrix": 0, "symmetric": 0, "dmi": 0, "iso": 0}

    # Bond always has at least one line in it (due to the _verify_exchange)
    line = lines[0].split()
    # Check that the header line
    # A1 A2 i j k
    if len(line) != 5:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[0]}: expected two atom labels",
                    f"and three integers separated by spaces, got {' '.join(line)}",
                ]
            )
        )
    else:
        # Check the atom labels
        # - Does not contain "#"
        # - Start with a letter
        error_messages.extend(_is_atom_label(line[0], line_indices[0]))
        error_messages.extend(_is_atom_label(line[1], line_indices[0]))
        # Check i j k
        if not (_is_integer(line[2]) and _is_integer(line[3]) and _is_integer(line[4])):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected to have three integers,",
                        f'got {" ".join(line[2:5])}',
                    ]
                )
            )

    # Skip first line where atom's labels and ijk.
    i = 1
    while i < len(lines):
        line = lines[i].lower().split()
        # If Isotropic keyword found - check isotropic exchange
        # Isotropic Jiso
        if line[0].startswith("i"):
            found_data["iso"] += 1
            if len(line) != 2:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "Isotropic" keyword and one number,',
                            f'got {" ".join(line)}',
                        ]
                    )
                )
            elif not _is_float(line[1]):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected one number, got {" ".join(line[1:])}',
                        ]
                    )
                )

        # If DMI keyword found - check DMI
        # DMI Dx Dy Dz
        if line[0].startswith("d"):
            found_data["dmi"] += 1
            if len(line) != 4:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "DMI" keyword and three numbers,',
                            f'got {" ".join(line)}',
                        ]
                    )
                )
            elif not (_is_float(line[1]) and _is_float(line[2]) and _is_float(line[3])):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected three numbers, got {" ".join(line[1:])}',
                        ]
                    )
                )

        # If Symmetric-anisotropy keyword found - check it
        # Symmetric-anisotropy Sxx Syy Sxy Sxz Syz
        if line[0].startswith("s"):
            found_data["symmetric"] += 1
            if len(line) != 6:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "Symmetric-anisotropy" keyword and five numbers,',
                            f'got {" ".join(line)}',
                        ]
                    )
                )
            elif not (
                _is_float(line[1])
                and _is_float(line[2])
                and _is_float(line[3])
                and _is_float(line[4])
                and _is_float(line[5])
            ):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected five numbers, got {" ".join(line[1:])}',
                        ]
                    )
                )

        # If Matrix keyword found - check matrix
        # Matrix
        # Jxx Jxy Jxz
        # Jyx Jyy Jyz
        # Jzx Jzy Jzz
        elif line[0].startswith("m"):
            found_data["matrix"] += 1
            if len(line) != 1:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "Matrix" keyword and nothing else,',
                            f'got {" ".join(line)}',
                        ]
                    )
                )

            for j in range(3):
                i += 1
                # Check that end of the bond is not reached.
                if i >= len(lines):
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i-1]}: expected {3-j} more lines",
                                "with the parameter's matrix, got nothing",
                            ]
                        )
                    )
                    break
                else:
                    line = lines[i].split()
                    # Each line has to contain three numbers
                    if (
                        len(line) != 3
                        or not _is_float(line[0])
                        or not _is_float(line[1])
                        or not _is_float(line[2])
                    ):
                        error_messages.append(
                            " ".join(
                                [
                                    f"Line {line_indices[i]}: expected three numbers,",
                                    f"separated by spaces, got {' '.join(line)}",
                                ]
                            )
                        )

        i += 1

    # Check that every type of value was found only once
    total_found_data = 0
    for key in found_data:
        total_found_data += found_data[key]
        if found_data[key] > 1:
            error_messages.append(
                " ".join(
                    [
                        f"Found more then one {key} entry.",
                        f"Check the bond on lines {line_indices[0]}-{line_indices[-1]}",
                    ]
                )
            )

    # Check that at least some values was found
    if total_found_data == 0:
        error_messages.append(
            " ".join(
                [
                    "Did not find any information about the parameter value",
                    f"Check the bond on lines {line_indices[0]}-{line_indices[-1]}",
                ]
            )
        )

    return error_messages


def _verify_exchange(lines, line_indices):
    error_messages = []
    # At least one line is already present in lines
    line = lines[0].lower().split()
    # Check <Units> keyword
    # Either meV, eV, J, K or Ry
    if len(line) == 2:
        if not (line[1][0] in ["m", "e", "j", "k", "r"]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'"meV" or "eV" or "J" or "K" or "Ry", got {line[1]}',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected two entries, "exchange" keyword',
                    f'and "meV" or "eV" or "J" or "K" or "Ry", got {" ".join(line)}',
                ]
            )
        )

    # Find all bonds.
    # Skip first line with the section header
    i = 1
    found_bonds = []
    while i < len(lines):
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        if i >= len(lines):
            break

        bond_start = i
        while i < len(lines) and not lines[i].startswith("-" * 10):
            if len(lines[i].strip()) == lines[i].count("-"):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: Subsection separator is too short",
                            '(expected 10 or more "-" symbols),',
                            f'got {lines[i].count("-")} "-" symbols.',
                        ]
                    )
                )
            i += 1
        bond_end = i

        found_bonds.append((bond_start, bond_end))

    # Model has to have at least one bond
    if len(found_bonds) == 0:
        error_messages.append(
            'Found 0 bonds in the "exchange" section, expected at least one'
        )

    for bond in found_bonds:
        error_messages.extend(
            _verify_bond(
                lines[slice(*bond)],
                line_indices[slice(*bond)],
            )
        )

    return error_messages


def _verify_on_site(lines, line_indices):
    error_messages = []
    # At least one line is already present in lines
    line = lines[0].lower().split()
    # Check <Units> keyword
    # Either meV, eV, J, K or Ry
    if len(line) == 2:
        if not (line[1][0] in ["m", "e", "j", "k", "r"]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'"meV" or "eV" or "J" or "K" or "Ry", got {line[1]}',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected one or two entries, "on-site" keyword',
                    f'and/or "meV" or "eV" or "J" or "K" or "Ry", got {" ".join(line)}',
                ]
            )
        )

    # Find all bonds.
    # Skip first line with the section header
    i = 1
    found_parameters = 0
    while i < len(lines):
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        if i >= len(lines):
            break

        # Check for potential short separators
        if len(lines[i].strip()) == lines[i].count("-"):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: Subsection separator is too short",
                        '(expected 10 or more "-" symbols),',
                        f'got {lines[i].count("-")} "-" symbols.',
                    ]
                )
            )

        error_messages.extend(_is_atom_label(lines[i].split(), line_indices[i]))

        i += 1
        if i >= len(lines):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i-1]}: Expected to have five numbers,",
                        "separated with spaces at the next line, got nothing",
                    ]
                )
            )
            break
        line = lines[i].split()
        if len(line) != 6:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: Expected to have six numbers,",
                        f"separated with spaces, got {lines[i]}",
                    ]
                )
            )
        elif not (
            _is_float(line[0])
            and _is_float(line[1])
            and _is_float(line[2])
            and _is_float(line[3])
            and _is_float(line[4])
            and _is_float(line[5])
        ):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: Expected to have six numbers,",
                        f"separated with spaces, got {lines[i]}",
                    ]
                )
            )
        # Go to the next line after verifying the matrix elements
        i += 1
        found_parameters += 1

    # Model has to have at least one bond
    if found_parameters == 0:
        error_messages.append(
            'Found 0 parameters in the "on-site" section, expected at least one'
        )

    return error_messages


def _verify_ground_state(lines, line_indices):
    error_messages = []

    # Check size of the cell section
    if len(lines) != 3:
        error_messages.append(
            f'"ground-state" section has to have exactly 3 lines, {len(lines)} found\n'
            + "\n".join(lines)
        )
        # Do not proceed with the rest of the checks
        return error_messages

    def is_units_keyword(word):
        return word.startswith("a") or word.startswith("r")

    # At this moment there are four lines present
    line = lines[0].lower().split()
    # If <Units> keyword present:
    # Ground-state Relative
    # or
    # Ground-state Absolute
    if len(line) == 2:
        if not is_units_keyword(line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected a word starting ",
                        f'from "a" or "r", got "{lines[0]}"',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "ground-state" keyword',
                    "and/or <Units> (one or two entries, separated by spaces),",
                    f'got "{" ".join(lines[0])}"',
                ]
            )
        )

    # Check the q-vector
    line = lines[1].split()
    if not (
        len(line) == 3
        and (_is_float(line[0]) and _is_float(line[1]) and _is_float(line[2]))
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[1]}: expected three numbers,",
                    f'got "{line}"',
                ]
            )
        )
    # Check the cone axis
    line = lines[1].lower().split()
    if not (
        (
            len(line) == 3
            and (_is_float(line[0]) and _is_float(line[1]) and _is_float(line[2]))
        )
        or (
            len(line) == 2
            and (
                line[0].startswith("a")
                and line[1].startswith("b")
                or line[0].startswith("b")
                and line[1].startswith("a")
            )
            and _is_float(line[0][1:] and _is_float(line[1][1:]))
        )
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[2]}: expected three numbers,",
                    'Or two entries with of the form "a<number> b<number>,"',
                    f'got "{line}"',
                ]
            )
        )

    return error_messages


# Rules

_REQUIRED_SECTIONS = ["c", "a", "n"]  # Cell  # Atoms  # Notation
_PARAMETERS_SECTIONS = ["e", "o"]  # Exchange # On-site

_KNOWN_SECTIONS = {
    "c": _verify_cell,  # Cell
    "a": _verify_atoms,  # Atoms
    "n": _verify_notation,  # Notation
    "e": _verify_exchange,  # Exchange
    "o": _verify_on_site,  # On-site
    "g": _verify_ground_state,  # Ground-state
}

_SECTION_FULL_NAMES = {
    "c": "Cell",
    "a": "Atoms",
    "n": "Notation",
    "e": "Exchange",
    "o": "On-site",
    "g": "Ground-state",
}


def _verify_model_file(lines, line_indices, raise_on_fail=True, return_sections=False):
    r"""
    Verify the content of the input file with the model.

    The input file shall be filtered. See :py:func:`._filter_model_file`.

    Parameters
    ==========
    lines : list of str
        List of the lines from the input file. Without comments and blank lines.
    line_indices : list of int
        Original line numbers, before filtering.
    raise_on_fail : bool, default True
        Whether to raise an Error if the file content is incorrect.
    return_sections : bool, default False
        Whether to return a dictionary with the positions of the found sections::

            {"keyword" : (start, end)}

        ``lines[start]`` is a first line of the section,
        ``lines[end-1]`` is the last line of the section.
    """
    error_messages = []
    found_sections = {}
    i = 0
    while i < len(lines):
        while i < len(lines) and lines[i].startswith("=" * 10):
            i += 1

        if i >= len(lines):
            break

        section_keyword = lines[i].split()[0].lower()
        section_start = i
        while i < len(lines) and not lines[i].startswith("=" * 10):
            if len(lines[i].strip()) == lines[i].count("="):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: Section separator is too short",
                            '(expected 10 or more "=" symbols),',
                            f'got {lines[i].count("=")} "=" symbols.',
                        ]
                    )
                )
            i += 1
        section_end = i

        _logger.info(
            f'Found section "{section_keyword}" on lines {line_indices[section_start]}-{line_indices[section_end-1]}'
        )

        # Only the first letter is used for the verification
        found_sections[section_keyword.lower()[0]] = (section_start, section_end)

    for name in _KNOWN_SECTIONS:
        if name in found_sections:
            error_messages.extend(
                _KNOWN_SECTIONS[name](
                    lines[slice(*found_sections[name])],
                    line_indices[slice(*found_sections[name])],
                )
            )

    # Check if all required sections are found
    for r_section in _REQUIRED_SECTIONS:
        if r_section not in found_sections:
            error_messages.append(
                f'Failed to find required section "{_SECTION_FULL_NAMES[r_section]}"'
            )

    # Check that at least one section of parameters is found
    parameters_sections = 0
    for r_section in _PARAMETERS_SECTIONS:
        if r_section in found_sections:
            parameters_sections += 1
    if parameters_sections == 0:
        error_messages.append(
            f"Failed to find at least one of the following sections:"
            + ", ".join(
                [_SECTION_FULL_NAMES[r_section] for r_section in _PARAMETERS_SECTIONS]
            ),
        )

    if len(error_messages) == 0:
        _logger.info("Model file verification finished: PASSED")
    else:
        if raise_on_fail:
            _logger.info("Model file verification finished: FAILED")
            import sys

            sys.tracebacklimit = 0
            raise FailedToVerifyModelFile("\n  ".join([""] + error_messages))
        else:
            _logger.error("\n  ".join([""] + error_messages))
            _logger.info("Model file verification finished: FAILED")

    if return_sections:
        return found_sections
