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


import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np

from magnopy._package_info import logo
from magnopy.io._grogu import load_grogu
from magnopy.io._spin_directions import read_spin_directions
from magnopy.io._tb2j import load_tb2j
from magnopy.scenarios._show_spin_directions import show_spin_directions


def manager():
    parser = get_parser()

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Load spin directions
    if args.spin_directions is None:
        pass
    elif len(args.spin_directions) == 1:
        args.spin_directions = read_spin_directions(filename=args.spin_directions[0])
    else:
        args.spin_directions = np.array(args.spin_directions)
        args.spin_directions = args.spin_directions.reshape(
            (len(args.spin_directions) // 3, 3)
        )

    # Load spin Hamiltonian
    if args.spinham_source.lower() == "tb2j":
        spinham = load_tb2j(
            filename=args.spinham_filename, spin_values=args.spin_values
        )
    elif args.spinham_source.lower() == "grogu":
        spinham = load_grogu(filename=args.spinham_filename)
    else:
        raise ValueError(
            'Supported sources of spin Hamiltonian are "GROGU" and "TB2J", '
            f'got "{args.spinham_source}".'
        )

    comment = (
        f'Source of the parameters is "{args.spinham_source}".\n'
        f"Loaded parameters of the spin Hamiltonian from the file\n  "
        f"{os.path.abspath(args.spinham_filename)}."
    )

    show_spin_directions(
        spinham=spinham,
        spin_directions=args.spin_directions,
        repeat=args.repeat,
        output_name=args.output_name,
        comment=comment,
    )


def get_parser():
    parser = ArgumentParser(
        description=logo()
        + "\n\nThis script creates an .html file with spin directions, that can be "
        "viewed in any modern browser.",
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-sf",
        "--spinham-filename",
        type=str,
        metavar="filename",
        default=None,
        required=True,
        help="Path to the spin Hamiltonian file, from where the parameters would be read.",
    )
    parser.add_argument(
        "-ss",
        "--spinham-source",
        type=str,
        metavar="name",
        default=None,
        required=True,
        choices=["GROGU", "TB2J"],
        help='Source of the spin Hamiltonian. Either "GROGU" or "TB2J"',
    )
    parser.add_argument(
        "-sd",
        "--spin-directions",
        nargs="*",
        type=str,
        default=None,
        metavar="S1_x S2_y S3_z ...",
        help="To fully define the system for the calculations of magnons one need the "
        "information about the ground state in addition to the parameters of the "
        "Hamiltonian. There are two ways to give this information to magnopy:\n"
        " * Give a path to the file. In the file there should be M lines with three "
        "numbers in each. The order of the lines would match the order of magnetic "
        "atoms in the spin Hamiltonian."
        " * Give a sequence of 3*M numbers directly to this parameter.\n"
        "If none provided, then magnopy attempts to optimize the spin directions prior "
        "to the LSWT calculations.",
    )
    parser.add_argument(
        "-r",
        "--repeat",
        type=int,
        nargs=3,
        default=(1, 1, 1),
        help="Number of unit cell's repetitions along the three lattice vectors.",
    )
    parser.add_argument(
        "-on",
        "--output-name",
        type=str,
        default="magnopy-sd",
        help="Name of the file for saving.",
    )

    return parser
