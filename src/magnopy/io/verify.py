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

__all__ = {"verify_model_file"}

_logger = logging.getLogger(__name__)


class FailedToVerifyModelFile(Exception):
    def __init__(self, message):
        super().__init__(message)


def _is_number(word):
    try:
        word = float(word)
        return True
    except ValueError:
        return False


def _is_bool(word):
    return word.lower() in ["true", "false", "t", "f", "1", "0", "yes", "no"]


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
        if _is_number(line[1]) or is_units_keyword(line[1]):
            pass
        else:
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
        if (_is_number(line[1]) and is_units_keyword(line[2])) or (
            _is_number(line[2]) and is_units_keyword(line[1])
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
        if _is_number(line[1]) and _is_number(line[2]) and _is_number(line[3]):
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
            _is_number(line[1])
            and _is_number(line[2])
            and _is_number(line[3])
            and is_units_keyword(line[4])
        ) or (
            is_units_keyword(line[1])
            and _is_number(line[2])
            and _is_number(line[3])
            and _is_number(line[4])
        ):
            pass
        else:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[0]}:",
                        "expected three numbers and",
                        'a word starting from "a" or "b",',
                        f'got "{" ".join(line[1:])}"',
                    ]
                )
            )
    elif len(line) != 1:
        error_messages.append(
            " ".join(
                [
                    f"Line {line_indices[0]}: expected nothing",
                    "or <Units> and/or <Scale> keywords",
                    "(from 0 to 4 entries, separated by spaces),",
                    f'separated by spaces, got "{" ".join(line[1:])}"',
                ]
            )
        )

    for i in range(1, 4):
        line = lines[i].split()
        if len(line) == 3 and (
            _is_number(line[0]) and _is_number(line[1]) and _is_number(line[2])
        ):
            pass
        else:
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
    # Check condition about hte size of the section
    if len(lines) < 2:
        error_messages.append(
            " ".join(
                [
                    f'"atoms" section has to contain at least one atom',
                    f"(at least 2 lines in total), {len(lines)} found\n",
                    "\n".join(lines),
                ]
            )
        )
        # Do not proceed with the rest of the checks
        return error_messages

    def is_units_keyword(word):
        return word.startswith("r") or word.startswith("a") or word.startswith("b")

    # At this moment there at least two lines present
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
                    f"Line {line_indices[0]}: expected <Units> keyword",
                    f'or nothing, got "{" ".join(line[1:])}"',
                ]
            )
        )

    # Check each atom line
    for i in range(1, len(lines)):
        line = lines[i].lower().split()

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
            # Atom coordinates have to be convertible to float
            if not (
                _is_number(line[1]) and _is_number(line[2]) and _is_number(line[3])
            ):
                error_messages.append(
                    " ".join(
                        [
                            f"Line {line_indices[i]}: expected three numbers,",
                            f'got "{" ".join(line[1:4])}"',
                        ]
                    )
                )
            # Spin may be specified as a number:
            # Atom i j k S
            if len(line) == 5:
                if not _is_number(line[4]):
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i]}: expected one number",
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
                if (
                    _is_number(line[4]) and _is_number(line[5]) and _is_number(line[6])
                ) or (
                    _is_number(line[4].lower().replace("p", "").replace("t", ""))
                    and _is_number(line[5].lower().replace("p", "").replace("t", ""))
                    and _is_number(line[6].lower().replace("p", "").replace("t", ""))
                    and "".join(line[4:7]).lower().count("p") == 1
                    and "".join(line[4:7]).lower().count("t") == 1
                ):
                    pass
                else:
                    error_messages.append(
                        " ".join(
                            [
                                f"Line {line_indices[i]}: expected three numbers",
                                "(spin vector) or one number and",
                                "two entries if the format:",
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
                    _is_number(line[4])
                    and _is_number(line[5])
                    and _is_number(line[6])
                    and _is_number(line[7])
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

    # The order of properties now is: 'd' 'e' 'o' 's'
    sorted_indices = [
        i[0] for i in sorted(enumerate(lines[1:5]), key=lambda x: x[1][0].lower())
    ]
    # Shift in order to skip first line with the notation keyword
    sorted_indices = [i + 1 for i in sorted_indices]

    # Check each property

    # error messages
    keywords = ["d", "e", "o", "s"]
    on_keyword_fail = [
        'expected line starting with "d" (for double counting)',
        'expected line starting with "e" (for exchange factor)',
        'expected line starting with "o" (for on-site-factor)',
        'expected line starting with "s" (for spin normalized)',
    ]
    on_value_fail = [
        'expected "true" or "false or "f" or "t" or "1" or "0" or "yes" or "no"',
        "expected one number",
        "expected one number",
        'expected "true" or "false or "f" or "t" or "1" or "0" or "yes" or "no"',
    ]
    value_verify_function = [_is_bool, _is_number, _is_number, _is_bool]
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
        if line.count("=") != 1:
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[sorted_indices[i]]}: expected ",
                        'to have exactly one "=" symbol,',
                        f"got {line}",
                    ]
                )
            )

        elif not value_verify_function[i](line.split("=")[1].strip()):
            error_messages.append(
                " ".join(
                    [
                        f"Line {line_indices[sorted_indices[i]]}: expected ",
                        f"{on_value_fail[i]}, got {line.split('=')[1].strip()}",
                    ]
                )
            )

    return error_messages


def _verify_parameters(lines, line_indices):
    error_messages = []
    return error_messages


# Rules

REQUIRED_SECTIONS = ["cell", "atoms", "parameters", "notation"]

KNOWN_SECTIONS = {
    "cell": _verify_cell,
    "atoms": _verify_atoms,
    "notation": _verify_notation,
    "parameters": _verify_parameters,
}


def verify_model_file(filtered_lines, line_indices, raise_on_fail=True):
    r"""
    Verify the content of the input file with the model.

    The input file shall be filtered. See :py:func:`.filter_model_file`.

    Parameters
    ==========
    filtered_lines : list of str
        List of the lines from the input file. Without comments and blank lines.
    line_indices : list of int
        Original line numbers, before filtering.
    raise_on_fail : bool, default True
        Whether to raise an Error if the file content is incorrect.
    """
    error_messages = []
    found_sections = {}
    i = 0
    while i < len(filtered_lines):
        while i < len(filtered_lines) and filtered_lines[i].startswith("=" * 10):
            i += 1

        if i >= len(filtered_lines):
            break

        section_keyword = filtered_lines[i].split()[0].lower()
        section_start = i
        while i < len(filtered_lines) and not filtered_lines[i].startswith("=" * 10):
            i += 1
        section_end = i

        _logger.info(
            f'Found section "{section_keyword}" from line {section_start} to line {section_end-1}'
        )

        found_sections[section_keyword.lower()] = (section_start, section_end)

    for name in KNOWN_SECTIONS:
        if name in found_sections:
            error_messages.extend(
                KNOWN_SECTIONS[name](
                    filtered_lines[slice(*found_sections[name])],
                    line_indices[slice(*found_sections[name])],
                )
            )

    for r_section in REQUIRED_SECTIONS:
        if r_section not in found_sections:
            error_messages.append(f'Failed to find required section "{r_section}"')

    if len(error_messages) == 0:
        _logger.info("Model file verification finished: PASSED")
    else:
        if raise_on_fail:
            _logger.info("Model file verification finished: FAILED")
            import sys

            sys.tracebacklimit = 0
            raise FailedToVerifyModelFile("\n".join(error_messages))
        else:
            _logger.error("\n".join(error_messages))
            _logger.info("Model file verification finished: FAILED")
