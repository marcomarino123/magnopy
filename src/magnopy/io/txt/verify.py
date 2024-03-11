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

from magnopy.exceptions import FailedToVerifyTxtModelFile
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
                    f'got "{word}"',
                ]
            )
        )
    return error_messages


def _verify_cell(lines, line_indices):
    r"""
    Check that the found "cell" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "cell" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """
    # At the beginning we assume that the first line starts with the
    # case-insensitive word "cell", followed by the next line symbol or a space.

    # Checker for the cell units
    def is_units_keyword(word):
        return word.lower().startswith("a") or word.lower().startswith("b")

    # Error messages list
    error_messages = []

    # Check size of the cell section it has to have exactly 4 lines
    if len(lines) != 4:
        error_messages.append(
            f'Line {line_indices[0]}: "cell" section has to have exactly 4 lines, '
            + f"{len(lines)} found:\n    "
            + "\n    ".join(lines)
        )
        # Do not proceed with the rest of the checks,
        # since the behavior of the rest of the checks is unpredictable
        return error_messages

    # Starting from this line it is assumed that the section has exactly 4 lines
    line = lines[0].lower().split()
    # If  only <units> keyword present:
    # Cell Angstrom
    # or only <scale> keyword present and it is one number:
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
    # If both <units> and <scale> keywords are present and <scale> is one number:
    # Cell Angstrom 1.5
    # or
    # Cell 1.5 Angstrom
    elif len(line) == 3:
        if not (
            _is_float(line[1])
            and is_units_keyword(line[2])
            or is_units_keyword(line[1])
            and _is_float(line[2])
        ):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected a number",
                        f'and a word starting from "a" or "b",',
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    # If only <scale> keyword is present and three numbers are given:
    # Cell 1.2 1.4 1.1
    elif len(line) == 4:
        if not (_is_float(line[1]) and _is_float(line[2]) and _is_float(line[3])):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected three numbers,",
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    # If both <units> and <scale> keywords are present
    # and <scale> is given by three numbers:
    # Cell Angstrom 1.2 1.4 1.1
    # or
    # Cell 1.2 1.4 1.1 Angstrom
    elif len(line) == 5:
        if not (
            (
                _is_float(line[1])
                and _is_float(line[2])
                and _is_float(line[3])
                and is_units_keyword(line[4])
            )
            or (
                is_units_keyword(line[1])
                and _is_float(line[2])
                and _is_float(line[3])
                and _is_float(line[4])
            )
        ):
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
    # If there are too many entries
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "cell" keyword',
                    "and optional <units> and/or <scale>",
                    "(from 1 to 5 blocks in total, separated by spaces),",
                    f'got "{lines[0]}"',
                ]
            )
        )

    # Check that every lattice vector is provided as three numbers separated by spaces.
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
                        f'got "{lines[i]}"',
                    ]
                )
            )

    return error_messages


def _check_vector_keywords(keywords, liter, line_index):
    r"""
    Check that one of the three sets is provided:

    * s
    * sx sy sz
    * st sp s

    Parameters
    ----------
    keywords : list of str
        List of the keywords.
    liter : int
        liter of the value (i.e. "s", "l" or "j").
    line_index : int
        Original line number, before filtering.

    Returns
    -------
    error_messages : list of str
        List of error messages.
    """

    # Sorted keywords
    # <liter>
    # or
    # <liter>x <liter>y <liter>z
    # or
    # <liter> <liter>p <liter>t
    # or nothing
    keywords.sort()

    error_messages = []
    if not (
        keywords == [liter]
        or keywords == [f"{liter}x", f"{liter}y", f"{liter}z"]
        or keywords == [liter, f"{liter}p", f"{liter}t"]
        or not keywords
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: expected to have only {liter} or {liter}x",
                    f"{liter}y {liter}z or {liter} {liter}p {liter}t or nothing",
                    f'got "{" ".join(keywords)}"',
                ]
            )
        )

    return error_messages


def _check_atoms_data_header(line, line_index):
    r"""
    Check the data header of the "atoms" section.

    Parameters
    ----------
    line : str
        The second line of the "atoms" section.
    line_index : int
        Original line number, before filtering.

    Returns
    -------
    N : int
        Number of blocks in the data header.
    name_index : int or None
        Index of the block with the atom's name.
        If None, then the atom's name is not present.
    error_messages : list of str
        List of error messages.
    """

    error_messages = []
    name_index = None
    N = len(line.split())

    keywords = line.lower().split()

    # Check that every block of the header is unique:
    if not len(keywords) == len(set(keywords)):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: expected unique blocks in the data header,",
                    f'got "{" ".join(keywords)}"',
                ]
            )
        )

    # Check that the required "name" keyword is present in the data header
    if "name" in keywords:
        name_index = keywords.index("name")
        keywords.remove("name")
    else:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: expected to have the atom's name",
                    "in the data header, got none",
                ]
            )
        )

    # Remove charge keywords from the list
    if "q" in keywords:
        keywords.remove("q")
    # Remove g-factor keywords from the list
    if "g" in keywords:
        keywords.remove("g")

    position_keywords = []
    spin_keywords = []
    orbital_moment_keywords = []
    total_moment_keywords = []

    # Categorized keywords
    for keyword in keywords:
        if keyword.startswith("r"):
            position_keywords.append(keyword)
        elif keyword in "xyz":
            position_keywords.append(keyword)
        elif keyword.startswith("s"):
            spin_keywords.append(keyword)
        elif keyword.startswith("l"):
            orbital_moment_keywords.append(keyword)
        elif keyword.startswith("j"):
            total_moment_keywords.append(keyword)

    # Check position keywords
    if not (
        position_keywords == ["r1", "r2", "r3"] or position_keywords == ["x", "y", "z"]
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: expected to have three position keywords.",
                    f'Either "r1 r2 r3" or "x y z", got "{" ".join(position_keywords)}"',
                ]
            )
        )
    # Remove position keywords from the list
    for keyword in position_keywords:
        keywords.remove(keyword)

    # Check spin keywords
    error_messages.extend(_check_vector_keywords(spin_keywords, "s", line_index))
    # Remove spin keywords from the list
    for keyword in spin_keywords:
        keywords.remove(keyword)

    # Check orbital moment keywords
    error_messages.extend(
        _check_vector_keywords(orbital_moment_keywords, "l", line_index)
    )
    # Remove orbital moment keywords from the list
    for keyword in orbital_moment_keywords:
        keywords.remove(keyword)

    # Check total moment keywords
    error_messages.extend(
        _check_vector_keywords(total_moment_keywords, "j", line_index)
    )
    # Remove total moment keywords from the list
    for keyword in total_moment_keywords:
        keywords.remove(keyword)

    # Check if there are any unsupported keywords left
    if keywords:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_index}: unsupported keywords in the data header:",
                    f'"{" ".join(keywords)}"',
                ]
            )
        )

    return N, name_index, error_messages


def _verify_atoms(lines, line_indices):
    r"""
    Check that the found "atoms" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "atoms" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """
    # At the beginning we assume that the first line starts with the
    # case-insensitive word "atoms", followed by the next line symbol or a space.

    # Checker for the atom's coordinate units
    def is_units_keyword(word):
        return word.lower().startswith("a") or word.lower().startswith("b")

    error_messages = []
    # Check condition about the size of the section
    # At least two lines have to be present: header and at least one atom
    if len(lines) < 3:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: "atoms" section has to contain a section ',
                    "header, a data header and at least one atom (at least 3 lines in total),",
                    f"{len(lines)} found\n    ",
                ]
            )
            + "\n    ".join(lines),
        )
        # Do not proceed with the rest of the checks,
        # since the behavior of the rest of the checks is unpredictable
        return error_messages

    # Starting from this line it is assumed that the section has at least 3 lines
    line = lines[0].lower().split()
    # If <units> are present, then line has 2 blocks:
    # Atoms <units>
    if len(line) == 2:
        if not is_units_keyword(line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected word starting from",
                        f'"a" or "b", got "{line[1]}"',
                    ]
                )
            )
    # If <units> are not present, then the line has only one block:
    # Atoms
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "atoms" keyword',
                    f'and/or <units>, got "{" ".join(line)}"',
                ]
            )
        )

    # Check the data header
    N, name_index, errors = _check_atoms_data_header(lines[1], line_indices[1])
    error_messages.extend(errors)

    # Check each atom line
    for i in range(2, len(lines)):
        line = lines[i].split()

        # Check the amount of blocks
        if len(lines[i].split()) != N:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: expected to have {N} blocks",
                        f'as per data header, got "{lines[i]}"',
                    ]
                )
            )

        # Check atom's names if any
        if name_index is not None:
            error_messages.extend(_is_atom_label(line[name_index], line_indices[i]))

        # Check other data fields
        for b_i, block in enumerate(line):
            # Skip the name
            if name_index is not None and b_i == name_index:
                continue

            # All other blocks have to be numbers
            if not _is_float(block):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}, block {b_i+1}: expected a number,",
                            f'got "{block}"',
                        ]
                    )
                )

    return error_messages


def _verify_notation(
    lines,
    line_indices,
    expect_exchange_factor=True,
    expect_on_site_factor=True,
    expect_double_counting=True,
):
    r"""
    Check that the found "notation" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "notation" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    expect_exchange_factor : bool, default: True
        Whether the exchange factor is expected to be present.
    expect_on_site_factor : bool, default: True
        Whether the on-site factor is expected to be present.
    expect_double_counting : bool, default: True
        Whether the double-counting property is expected to be present.
    """
    error_messages = []
    # Check condition about the size of the section the minimum amount of lines is 2
    if len(lines) < 2:
        error_messages.append(
            " ".join(
                [
                    f'"notation" section has to contain at least 2 lines',
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
                    f'got "{lines[0]}"',
                ]
            )
        )

    # Dictionary of the found properties
    found_properties = {}
    for i in range(1, len(lines)):
        line = lines[i].lower().split()
        if len(line) != 2:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: expected to have two blocks,",
                        f'separated by spaces, got "{lines[i]}"',
                    ]
                )
            )
        else:
            # Only first letter is checked
            if line[0][0] in found_properties:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: found more than one entry of",
                            f'the "{line[0]}" property (only first letter is checked)',
                        ]
                    )
                )
            else:
                found_properties[line[0][0]] = (line[1], i)

    recognized_properties = ["d", "s", "e", "o"]
    expected = {
        "d": expect_double_counting,
        "s": True,
        "e": expect_exchange_factor,
        "o": expect_on_site_factor,
    }
    full_names = {
        "d": "double-counting",
        "s": "spin-normalized",
        "e": "exchange-factor",
        "o": "on-site-factor",
    }
    verify_functions = {
        "d": _is_bool,
        "s": _is_bool,
        "e": _is_float,
        "o": _is_float,
    }
    error_expect = {
        "d": "boolean",
        "s": "boolean",
        "e": "number",
        "o": "number",
    }

    # Check that every recognized property is present if it is expected
    # and that it has the correct value
    for prop in recognized_properties:
        if prop not in found_properties:
            if expected[prop]:
                error_messages.append(
                    f"Line {line_indices[0]}: did not "
                    f'find the "{full_names[prop]}" property in the notation section'
                )
        else:
            if not verify_functions[prop](found_properties[prop][0]):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[found_properties[prop][1]]}:",
                            f"expected to have a {error_expect[prop]},",
                            f'got "{found_properties[prop][0]}"',
                        ]
                    )
                )
            del found_properties[prop]

    # Check that there are no unrecognized properties
    if found_properties:
        error_messages.append(
            " ".join(
                [
                    f"Found unrecognized properties in the notation section:",
                    f'{" ".join(found_properties.keys())}',
                ]
            )
        )

    return error_messages


def _verify_bond(lines, line_indices):
    R"""
    Check that the found "bond" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "bond" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """
    # At the beginning we assume that the the bond has at least one line in it
    # with the atom's labels and ijk.

    # Error messages list
    error_messages = []

    # We need to make sure that only one entry of the type exists.
    found_data = {"matrix": 0, "symmetric": 0, "dmi": 0, "iso": 0}

    line = lines[0].split()
    # Check that the header line
    # A1 A2 i j k
    if len(line) != 5:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[0]}: expected two atom labels",
                    f'and three integers separated by spaces, got "{" ".join(line)}"',
                ]
            )
        )
    else:
        # Check the atom labels
        error_messages.extend(_is_atom_label(line[0], line_indices[0]))
        error_messages.extend(_is_atom_label(line[1], line_indices[0]))
        # Check i j k
        if not (_is_integer(line[2]) and _is_integer(line[3]) and _is_integer(line[4])):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected to have three integers,",
                        f'got "{" ".join(line[2:5])}"',
                    ]
                )
            )

    # Skip first line with atom's labels and ijk.
    i = 1
    while i < len(lines):
        line = lines[i].lower().split()
        # If Isotropic keyword found - check isotropic exchange
        # Isotropic Jiso
        if line[0].startswith("i"):
            found_data["iso"] += 1
            # Isotropic line has to have two blocks
            if len(line) != 2:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "Isotropic" keyword and one number,',
                            f'got "{" ".join(line)}"',
                        ]
                    )
                )
            # Second block has to be a number
            elif not _is_float(line[1]):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected one number, got "{" ".join(line[1:])}"',
                        ]
                    )
                )

        # If DMI keyword found - check DMI
        # DMI Dx Dy Dz
        if line[0].startswith("d"):
            found_data["dmi"] += 1
            # DMI line has to have four blocks
            if len(line) != 4:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "DMI" keyword and three numbers,',
                            f'got "{" ".join(line)}"',
                        ]
                    )
                )
            # Second, third and fourth blocks have to be numbers
            elif not (_is_float(line[1]) and _is_float(line[2]) and _is_float(line[3])):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected three numbers, got "{" ".join(line[1:])}"',
                        ]
                    )
                )

        # If symmetric-anisotropy keyword found - check it
        # Symmetric-anisotropy Sxx Syy Sxy Sxz Syz
        if line[0].startswith("s"):
            found_data["symmetric"] += 1
            # Symmetric-anisotropy line has to have six blocks
            if len(line) != 6:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "symmetric-anisotropy" keyword and five numbers,',
                            f'got "{" ".join(line)}"',
                        ]
                    )
                )
            # 2nd, 3rd, 4th, 5th and 6th blocks have to be numbers
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
                            f'expected five numbers, got "{" ".join(line[1:])}"',
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
            # First line of the matrix block has to contain only the "matrix" keyword
            if len(line) != 1:
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}:",
                            f'expected "Matrix" keyword and nothing else,',
                            f'got "{" ".join(line)}"',
                        ]
                    )
                )
            # Next three lines have to contain three numbers each
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
                                    f'separated by spaces, got "{" ".join(line)}"',
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
                        f'Line {line_indices[0]}: found more than one "{key}" entry.',
                        f"Check the bond on lines {line_indices[0]}-{line_indices[-1]}",
                    ]
                )
            )

    # Check that at least some values were found
    if total_found_data == 0:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[0]}: did not find any information about the parameter value.",
                    f"Check the bond on lines {line_indices[0]}-{line_indices[-1]}",
                ]
            )
        )

    return error_messages


def _verify_exchange(lines, line_indices):
    R"""
    Check that the found "exchange" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "exchange" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """
    # At the beginning we assume that the the exchange section has at least one line in it
    # with the section header

    # Error messages list
    error_messages = []

    line = lines[0].lower().split()
    # Check <units> keyword
    # Either meV, eV, J, K or Ry
    if len(line) == 2:
        if not (line[1][0] in ["m", "e", "j", "k", "r"]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'"meV" or "eV" or "J" or "K" or "Ry", got "{line[1]}"',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected one or two blocks, "exchange" keyword',
                    f'and/or <units> keyword ("meV" or "eV" or "J" or "K" or "Ry"),',
                    f'got "{" ".join(line)}"',
                ]
            )
        )

    # Find all bonds.
    # Skip first line with the section header
    i = 1
    found_bonds = []
    while i < len(lines):
        # Skip all possible subsection separators
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        # Check that some data is present
        if i >= len(lines):
            break

        bond_start = i
        while i < len(lines) and not lines[i].startswith("-" * 10):
            # Check if the separator is present, but too short
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
            _verify_bond(lines[slice(*bond)], line_indices[slice(*bond)])
        )

    return error_messages


def _verify_on_site(lines, line_indices):
    r"""
    Check that the found "on-site" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "on-site" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """
    # At the beginning we assume that the the on-site section has at least one line in it
    # with the section header

    # Error messages list
    error_messages = []

    line = lines[0].lower().split()
    # Check <units> keyword
    # Either meV, eV, J, K or Ry
    if len(line) == 2:
        if not (line[1][0] in ["m", "e", "j", "k", "r"]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'"meV" or "eV" or "J" or "K" or "Ry", got "{line[1]}"',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected one or two entries, "on-site" keyword',
                    f'and/or <units> ("meV" or "eV" or "J" or "K" or "Ry"),',
                    f'got "{" ".join(line)}"',
                ]
            )
        )

    # Find all bonds.
    # Skip first line with the section header
    i = 1
    found_parameters = 0
    while i < len(lines):
        # Skip all possible subsection separators
        while i < len(lines) and lines[i].startswith("-" * 10):
            i += 1

        # Check that some data is present
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
        # Check that the atom's label is present
        if len(lines[i].split()) != 1:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i]}: expected only the atom's label,",
                        f'got "{lines[i]}"',
                    ]
                )
            )
        # Check the atom's label
        error_messages.extend(_is_atom_label(lines[i].split()[0], line_indices[i]))

        i += 1
        if i >= len(lines):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[i-1]}: Expected to have six numbers,",
                        "separated with spaces at the next line, got nothing",
                    ]
                )
            )
            break
        line = lines[i].split()
        if len(line) != 6 or not (
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
                        f'separated with spaces, got "{lines[i]}"',
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


def _verify_cone_axis(lines, line_indices):
    r"""
    Check that the found "cone-axis" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "cone-axis" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """

    # At the beginning we assume that the the cone-axis section has at least one line in it
    # with the section header that starts with "cone-axis" keyword.

    # Error messages list
    error_messages = []

    # Checker for the cell units
    def is_units_keyword(word):
        return word.lower().startswith("r") or word.lower().startswith("a")

    # Check size of the cone-axis section, it has to have exactly 2 lines
    if len(lines) != 2:
        error_messages.append(
            f'Line {line_indices[0]}: "cone-axis" section has to have exactly 2 lines, '
            + f"{len(lines)} found:\n    "
            + "\n    ".join(lines)
        )
        # Do not proceed with the rest of the checks,
        # since the behavior of the rest of the checks is unpredictable
        return error_messages

    # Starting from this line it is assumed that the section has exactly 2 lines
    line = lines[0].lower().split()
    # If  <units> keyword present:
    # cone-axis <units>
    if len(line) == 2:
        if not is_units_keyword(line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'a word starting from "r" or "a", got "{line[1]}"',
                    ]
                )
            )
    # If there are too many entries
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "cone-axis" keyword',
                    "and optional <units> (one or two blocks in total,",
                    f'separated by spaces), got "{lines[0]}"',
                ]
            )
        )

    # Check that next line contain three or two numbers
    line = lines[1].split()
    if not (
        len(line) == 3
        and _is_float(line[0])
        and _is_float(line[1])
        and _is_float(line[2])
        or len(line) == 2
        and _is_float(line[0])
        and _is_float(line[1])
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[1]}: expected two or three numbers,",
                    f'got "{lines[1]}"',
                ]
            )
        )

    return error_messages


def _verify_spiral_vector(lines, line_indices):
    r"""
    Check that the found "spiral-vector" section is following the input file specification.

    Parameters
    ----------
    lines : list of str
        List of the "spiral-vector" section lines from the input file.
        Without comments and blank lines.
        ``len(lines) == len(line_indices)``
    line_indices : list of int
        Original line numbers, before filtering.
        ``len(line_indices) == len(lines)``
    """

    # At the beginning we assume that the the spiral-vector section has at least one line in it
    # with the section header that starts with "spiral-vector" keyword.

    # Error messages list
    error_messages = []

    # Checker for the cell units
    def is_units_keyword(word):
        return word.lower().startswith("r") or word.lower().startswith("a")

    # Check size of the spiral-vector section, it has to have exactly 2 lines
    if len(lines) != 2:
        error_messages.append(
            f'Line {line_indices[0]}: "spiral-vector" section has to have exactly 2 lines, '
            + f"{len(lines)} found:\n    "
            + "\n    ".join(lines)
        )
        # Do not proceed with the rest of the checks,
        # since the behavior of the rest of the checks is unpredictable
        return error_messages

    # Starting from this line it is assumed that the section has exactly 2 lines
    line = lines[0].lower().split()
    # If  <units> keyword present:
    # spiral-vector <units>
    if len(line) == 2:
        if not is_units_keyword(line[1]):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}: expected",
                        f'a word starting from "r" or "a", got "{line[1]}"',
                    ]
                )
            )
    # If there are too many entries
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f'Line {line_indices[0]}: expected "spiral-vector" keyword',
                    "and optional <units> (one or two blocks in total,",
                    f'separated by spaces), got "{lines[0]}"',
                ]
            )
        )

    # Check that next line contain three  numbers
    line = lines[1].split()
    if not (
        len(line) == 3
        and _is_float(line[0])
        and _is_float(line[1])
        and _is_float(line[2])
    ):
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[1]}: expected three numbers,",
                    f'got "{lines[1]}"',
                ]
            )
        )

    return error_messages


# Rules

_REQUIRED_SECTIONS = ["cell", "atoms", "notation"]  # Cell  # Atoms  # Notation
_PARAMETERS_SECTIONS = ["exchange", "on-site"]  # Exchange # On-site

_SUPPORTED_SECTIONS = {
    "cell": _verify_cell,
    "atoms": _verify_atoms,
    "notation": _verify_notation,
    "exchange": _verify_exchange,
    "on-site": _verify_on_site,
    "cone-axis": _verify_cone_axis,
    "spiral-vector": _verify_spiral_vector,
}


def _verify_model_file(lines, line_indices, raise_on_fail=True, return_sections=False):
    r"""
    Verify the content of the input file with the model.

    The input file shall be filtered. See :py:func:`._filter_txt_file`.

    Parameters
    -------------
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

    # Error messages list
    error_messages = []

    # Tracker the found sections
    found_sections = {}

    # Start fir the first line
    i = 0
    while i < len(lines):
        # Skip arbitrary number of the section separators
        while i < len(lines) and lines[i].startswith("=" * 10):
            i += 1

        # Check that there are some data present
        if i >= len(lines):
            break

        section_keyword = lines[i].split()[0].lower()
        section_start = i
        # Iterate until the next section separator is found or the end of the file
        while i < len(lines) and not lines[i].startswith("=" * 10):
            # Check for possible short separators
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

        # Save the position of the found section
        found_sections[section_keyword] = (section_start, section_end)

    for name in _SUPPORTED_SECTIONS:
        if name in found_sections:
            # Custom call for notation section
            if name == "notation":
                error_messages.extend(
                    _SUPPORTED_SECTIONS[name](
                        lines[slice(*found_sections[name])],
                        line_indices[slice(*found_sections[name])],
                        expect_exchange_factor="exchange" in found_sections,
                        expect_on_site_factor="on-site" in found_sections,
                        expect_double_counting="exchange" in found_sections,
                    )
                )
            # Universal call for all other sections
            else:
                error_messages.extend(
                    _SUPPORTED_SECTIONS[name](
                        lines[slice(*found_sections[name])],
                        line_indices[slice(*found_sections[name])],
                    )
                )

    # Check if all required sections are found
    for r_section in _REQUIRED_SECTIONS:
        if r_section not in found_sections:
            error_messages.append(
                f'File: failed to find required section "{r_section}"'
            )

    # Check that at least one section of parameters is found
    parameters_sections = 0
    for r_section in _PARAMETERS_SECTIONS:
        if r_section in found_sections:
            parameters_sections += 1
    if parameters_sections == 0:
        error_messages.append(
            f"File: failed to find at least one of the following sections:"
            + ", ".join([r_section for r_section in _PARAMETERS_SECTIONS]),
        )

    # Process all errors if any
    if len(error_messages) == 0:
        _logger.info("Model file verification finished: PASSED")
    else:
        if raise_on_fail:
            _logger.info("Model file verification finished: FAILED")
            import sys

            sys.tracebacklimit = 0
            raise FailedToVerifyTxtModelFile(
                "\n  ".join([""] + "\n".join(error_messages).split("\n"))
            )
        else:
            _logger.error("\n  ".join([""] + error_messages))
            _logger.info("Model file verification finished: FAILED")

    if return_sections:
        return found_sections
