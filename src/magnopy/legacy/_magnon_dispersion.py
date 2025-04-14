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
import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np

from magnopy._osfix import _winwait
from magnopy._package_info import logo
from magnopy.io import load_spinham
from magnopy.magnons.dispersion import MagnonDispersion
from magnopy.spinham.energy import Energy

_logger = logging.getLogger(__name__)


def manager(
    spinham,
    spinham_format=None,
    output_seedname="dispersion",
    k_points=None,
    k_path=None,
    save_txt=False,
    interactive=False,
    verbose=False,
    join_output=False,
):
    head, _ = os.path.split(spinham)
    out_head, out_tail = os.path.split(output_seedname)
    if len(out_head) == 0:
        out_head = head
    if len(out_tail) == 0:
        out_tail = "dispersion"

    output_name = os.path.join(out_head, out_tail)

    # Create the output directory if it does not exist
    if out_head != "":
        os.makedirs(out_head, exist_ok=True)

    # Load spin Hamiltonian from the input file
    input_file = spinham
    spinham = load_spinham(spinham, spinham_format=spinham_format)

    # Standardize the unit cell
    spinham.standardize()

    print(f"{spinham.variation} crystal detected")

    # Get k points of the spinham
    kp = spinham.kpoints

    # Add additional points
    if k_points is not None:
        for i in range(len(k_points) // 5):
            point_name = k_points[5 * i]
            point_label = k_points[5 * i + 1]
            point_coordinates = list(map(float, k_points[5 * i + 2 : 5 * i + 5]))
            kp.add_hs_point(
                name=point_name, coordinates=point_coordinates, label=point_label
            )

    # Set custom k path
    if k_path is not None:
        kp.path = k_path

    if verbose:
        print("Predefined high symmetry k points:")
        for name in kp.hs_names:
            print(f"  {name} : {kp.hs_coordinates[name]}")

    # Get the magnon dispersion
    dispersion = MagnonDispersion(spinham)

    fig, ax = plt.subplots()

    omegas = dispersion(kp)

    ax.set_xticks(kp.ticks(), kp.labels, fontsize=15)
    ax.set_ylabel("E, meV", fontsize=15)
    ax.vlines(
        kp.ticks(),
        0,
        1,
        transform=ax.get_xaxis_transform(),
        colors="black",
        alpha=0.5,
        lw=1,
        ls="dashed",
    )
    colors = ["#174FD5", "#F8AB00", "#0CE1A2", "#FF003C", "#46EC00", "#9823C9"]
    i = 0
    for omega in omegas:
        ax.plot(kp.flatten_points(), omega, color=colors[i % len(colors)])
        i += 1

    ax.set_xlim(kp.flatten_points()[0], kp.flatten_points()[-1])

    if save_txt:
        main_separator = "=" * 80 + "\n"
        info = [
            main_separator,
            logo(date_time=True, line_length=80),
            f"\nMagnon dispersion is computed based on the file:\n{os.path.abspath(input_file)}\n",
        ]
        info.append(main_separator)
        info.append("Cell:" + "\n")
        info.append(str(spinham.cell) + "\n")
        info.append(f"Detected Bravais lattice: {spinham.variation}\n")
        info.append(main_separator)

        info.append(main_separator)
        info.append("kpath" + "\n")
        info.append(f"  {kp.path_string}\n")
        info.append("kpoints" + "\n")
        names_data = []
        header_column = []
        for name in kp.hs_names:
            header_column.append(f"{name:<6}")
            names_data.append(kp.hs_coordinates[name])
        info.append(
            str(names_data),
        )

        info.append("klabels" + "\n")
        labels_data = []
        header_column = []
        for i in range(len(kp.labels)):
            header_column.append(f"{kp.labels[i]:<10}")
            labels_data.append([kp.ticks()[i]])
        info.append(str(labels_data))
        info.append(main_separator)
        info.append("dispersion" + "\n")

        header = ["Coordinate"]
        for i in range(omegas.shape[0]):
            header.append(f' {f"omega_{i}":>14}')
        header.append(f"    {'b1 (rel)':>10} {'b2 (rel)':>10} {'b3 (rel)':>10}")
        header.append(f"    {'k_x (abs)':>10} {'k_y (abs)':>10} {'k_z (abs)':>10}")
        info.append("".join(header))

        if not join_output:
            filename = f"{output_name}_data.txt"
            info.extend(
                [
                    "\n",
                    "separate",
                    "\n",
                    os.path.abspath(filename),
                ]
            )
            info = "".join(info)
            with open(f"{output_name}_info.txt", "w", encoding="utf-8") as file:
                file.write(info)
            info = ""
            comments = "#"
        else:
            info = "".join(info)
            filename = f"{output_name}.txt"
            comments = ""

        np.savetxt(
            filename,
            np.concatenate(
                (
                    [kp.flatten_points()],
                    omegas,
                    kp.points(relative=True).T,
                    kp.points(relative=False).T,
                ),
                axis=0,
            ).T,
            fmt="%.8f"
            + " %.8e" * omegas.shape[0]
            + "   "
            + " %.8f" * 3
            + "   "
            + " %.8f" * 3,
            header=info,
            comments=comments,
        )
    if interactive:
        plt.show()
    else:
        plt.savefig(
            f"{output_name}.png",
            bbox_inches="tight",
            dpi=600,
        )
        print(f"Results are in {os.path.abspath(out_head)}, seedname: {out_tail}.")


def create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-sh",
        "--spinham",
        type=str,
        required=True,
        help="Relative or absolute path to the file with spin Hamiltonian, "
        "including the name and extension of the file. ",
    )
    parser.add_argument(
        "-shf",
        "--spinham-format",
        type=str,
        choices=["txt", "hdf5", "tb2j"],
        default=None,
        help="Format of the file with spin Hamiltonian.",
    )
    parser.add_argument(
        "-os",
        "--output-seedname",
        type=str,
        default="dispersion",
        help="Seedname for output files",
    )
    parser.add_argument(
        "-kps",
        "--k-points",
        default=None,
        metavar="name label xrel yrel zrel ...",
        type=str,
        nargs="*",
        help="Additional high-symmetry k-points.",
    )
    parser.add_argument(
        "-kp",
        "--k-path",
        default=None,
        metavar="G-X-M-G|G-Y",
        type=str,
        help="Path in reciprocal space for the magnon dispersion.",
    )
    parser.add_argument(
        "-st",
        "--save-txt",
        default=False,
        action="store_true",
        help="Whether to save data to .txt file.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        default=False,
        action="store_true",
        help="Whether to show interactive plot.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="Verbose output, propagates to the called methods.",
    )
    parser.add_argument(
        "-jo",
        "--join-output",
        default=False,
        action="store_true",
        help="Whether to join the output files into a single file.",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    manager(**vars(args))
    _winwait()


if __name__ == "__main__":
    main()
