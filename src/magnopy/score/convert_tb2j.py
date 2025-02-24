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


from argparse import ArgumentParser

from magnopy._osfix import _winwait
from magnopy.io.hdf5.internal import dump_spinham_hdf5
from magnopy.io.txt.internal import dump_spinham_txt
from magnopy.io.txt.tb2j import load_tb2j


def manager(input_filename, output_filename="spinham.txt", format=None, verbose=False):
    spinham = load_tb2j(filename=input_filename, quiet=not verbose)

    if format is None:
        if output_filename.endswith(".hdf5"):
            format = "hdf5"
        else:
            format = "txt"

    if format.lower() == "txt":
        dump_spinham_txt(spinham, filename=output_filename)
    elif format.lower() == "hdf5":
        if output_filename.endswith(".txt"):
            output_filename = output_filename[:-4]
        if output_filename.endswith(".hdf5"):
            output_filename = output_filename[:-5]
        dump_spinham_hdf5(spinham=spinham, filename=output_filename + ".hdf5")
    else:
        raise RuntimeError(
            f'Format "{format}" is not supported. Supported formats are "txt" and "hdf5"'
        )


def create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-if",
        "--input-filename",
        type=str,
        required=True,
        help="File with the Hamiltonian from TB2J",
    )
    parser.add_argument(
        "-of",
        "--output-filename",
        type=str,
        default="spinham.txt",
        help="File for saving the spin Hamiltonian.",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["txt", "hdf5"],
        default=None,
        help="Format of the output file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="Whether to display details during the progress.",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    manager(**vars(args))
    _winwait()


if __name__ == "__main__":
    main()
