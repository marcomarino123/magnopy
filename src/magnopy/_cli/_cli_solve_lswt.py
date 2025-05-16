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
from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np

from magnopy._package_info import logo
from magnopy.io._spin_directions import read_spin_directions
from magnopy.scenarios._solve_lswt import solve_lswt


def manager():
    parser = get_parser()

    args = parser.parse_args()

    if len(args.spin_directions) == 1:
        args.spin_directions = read_spin_directions(filename=args.spin_directions)
    else:
        args.spin_directions = np.array(args.spin_directions)
        args.spin_directions = args.spin_directions.reshape(
            (len(args.spin_directions) // 3, 3)
        )

    if args.spins is not None:
        args.spins = [float(tmp) for tmp in args.spins]

    kpoints = []
    if args.kpoints is not None:
        with open(args.kpoints, "r") as f:
            for line in f:
                # Remove comment lines
                if line.startswith("#"):
                    continue
                # Remove inline comments and leading/trailing whitespaces
                line = line.split("#")[0].strip()
                # Check for empty lines empty lines
                if line:
                    line = line.split()
                    if len(line) != 3:
                        raise ValueError(
                            f"Expected three numbers per line (in line{i}),"
                            f"got: {len(line)}."
                        )

                    kpoints.append(list(map(float, line)))

        args.kpoints = kpoints

    solve_lswt(**vars(args))


def get_parser():
    parser = ArgumentParser(
        description=logo()
        + "\n\nThis script solves the spin Hamiltonian at the level of "
        "Linear Spin Wave Theory (LSWT) and outputs (almost) every possible quantity.",
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-sf",
        "--spinham-filename",
        type=str,
        metavar="filename",
        default=None,
        help="Path to the spin Hamiltonian file.",
    )
    parser.add_argument(
        "-ss",
        "--spinham-source",
        type=str,
        metavar="name",
        default=None,
        choices=["GROGU", "TB2J"],
        help="Source of the spin Hamiltonian, case-insensitive.",
    )
    parser.add_argument(
        "-sd",
        "--spin-directions",
        nargs="*",
        type=str,
        metavar="S1_x S2_y S3_z ...",
        help="Either a file with the direction of spins in the ground state or directly "
        "the components of the spin directions. Order is the same as in the Hamiltonian",
    )
    parser.add_argument(
        "-s",
        "--spins",
        nargs="*",
        type=str,
        metavar="S1 S2 S3 ...",
        help="Spin values, same order as in the Hamiltonian.",
    )
    parser.add_argument(
        "-kp",
        "--k-path",
        default=None,
        metavar="G-X-S|G-Y",
        type=str,
        help="Path in reciprocal space for the magnon dispersion.",
    )
    parser.add_argument(
        "-kps",
        "--kpoints",
        type=str,
        default=None,
        help="File with kpoints. Every line is one kpoint and contain three floats.",
    )
    parser.add_argument(
        "-r",
        "--relative",
        type=bool,
        default=False,
        help="Whether to interpret the coordinates of given kpoints as relative or absolute.",
    )
    parser.add_argument(
        "-os",
        "--output-folder",
        type=str,
        default="magnopy-results",
        help="Seedname for output files.",
    )
    parser.add_argument(
        "-np",
        "--number-processors",
        type=int,
        default=None,
        help="Number of processes for multithreading. Uses all available processors by "
        "default. Pass 1 to run in serial.",
    )

    return parser
