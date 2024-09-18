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
from argparse import ArgumentParser

import numpy as np

from magnopy._osfix import _winwait
from magnopy._pinfo import logo
from magnopy.io import load_spinham
from magnopy.spinham.energy import Energy

_logger = logging.getLogger(__name__)


def _minimize_ferro(energy: Energy, spinham, seedname, output_file):
    output_file.write(
        f"Start to minimize assuming ferromagnetic ground state type.\n"
        f"History of the minimization is written in the file\n"
        f"{seedname}-ferro-history\n"
    )
    spin_orientation = energy.optimize(
        case="ferro",
        save_history=True,
        history_filename=f"{seedname}-ferro-history",
    )[0]
    output_file.write(
        "Minimization for ferromagnetic case is done.\n"
        "Spin orientations in the minimum configuration:\n"
    )
    output_file.write(
        f"  {'name':>5} {'r1':>11} {'r2':>11} {'r3':>11} {'sx':>11} {'sy':>11} {'sz':>11}\n"
    )
    for i, spin in enumerate(spin_orientation):
        pos = spinham.magnetic_atoms[i].position
        output_file.write(
            f"  {spinham.magnetic_atoms[i].name:>5} "
            f"{pos[0]:11.8f} {pos[1]:11.8f} {pos[2]:11.8f} "
            f"{spin[0]:11.8f} {spin[1]:11.8f} {spin[2]:11.8f}\n"
        )

    return energy.ferro(spin_orientation)


def _minimize_antiferro(energy: Energy, spinham, seedname, output_file):
    output_file.write(
        f"Start to minimize assuming antiferromagnetic ground state type.\n"
        f"History of the minimization is written in the 26 files\n"
    )

    i = 0
    energies = []
    for qrel in (np.indices((3, 3, 3)) - 1).transpose((1, 2, 3, 0)).reshape(27, 3):
        i += 1
        print(qrel)
        history_file = f"{seedname}-antiferro-history-{i}"
        if (qrel == [0, 0, 0]).all():
            continue

        q = qrel @ spinham.reciprocal_cell / 2
        output_file.write(
            f"History for the q_rel = ({qrel[0]:2.0f}, {qrel[1]:2.0f}, {qrel[2]:2.0f}) "
            f"is written to the file {history_file}"
        )

        spin_orientation, cone_axis, _ = energy.optimize(
            case="antiferro",
            save_history=True,
            history_filename=history_file,
            antiferro_q=q,
        )
        output_file.write(
            f"Minimization for the antiferro case is done {i} out of 26.\n"
            "Spin orientations in the minimum configuration:\n"
        )
        output_file.write(
            f"  {'name':>5} {'r1':>11} {'r2':>11} {'r3':>11} {'sx':>11} {'sy':>11} {'sz':>11}\n"
        )
        for i, spin in enumerate(spin_orientation):
            pos = spinham.magnetic_atoms[i].position
            output_file.write(
                f"  {spinham.magnetic_atoms[i].name:>5} "
                f"{pos[0]:11.8f} {pos[1]:11.8f} {pos[2]:11.8f} "
                f"{spin[0]:11.8f} {spin[1]:11.8f} {spin[2]:11.8f}\n"
            )
        output_file.write(
            f"Cone axis is: {cone_axis[0]:.8f} {cone_axis[1]:.8f} {cone_axis[2]:.8f}\n"
        )
        output_file.write(f"Spiral vector is: {q[0]:.8f} {q[1]:.8f} {q[2]:.8f}\n")

        energies.append(energy.antiferro(spin_orientation, cone_axis, q))

    return energies


def _minimize_spiral(energy: Energy, spinham, seedname, output_file):
    output_file.write(
        f"Start to minimize assuming spiral ground state type.\n"
        f"History of the minimization is written in the file\n"
        f"{seedname}-spiral-history\n"
    )

    spin_orientation, cone_axis, spiral_vector = energy.optimize(
        case="spiral",
        save_history=True,
        history_filename=f"{seedname}-spiral-history",
    )
    output_file.write(
        "Minimization for the spiral case is done.\n"
        "Spin orientations in the minimum configuration:\n"
    )
    output_file.write(
        f"  {'name':>5} {'r1':>11} {'r2':>11} {'r3':>11} {'sx':>11} {'sy':>11} {'sz':>11}\n"
    )
    for i, spin in enumerate(spin_orientation):
        pos = spinham.magnetic_atoms[i].position
        output_file.write(
            f"  {spinham.magnetic_atoms[i].name:>5} "
            f"{pos[0]:11.8f} {pos[1]:11.8f} {pos[2]:11.8f} "
            f"{spin[0]:11.8f} {spin[1]:11.8f} {spin[2]:11.8f}\n"
        )
    output_file.write(
        f"Cone axis is: {cone_axis[0]:.8f} {cone_axis[1]:.8f} {cone_axis[2]:.8f}\n"
    )
    output_file.write(
        f"Spiral vector is: {spiral_vector[0]:.8f} {spiral_vector[1]:.8f} {spiral_vector[2]:.8f}\n"
    )

    return energy.spiral(spin_orientation, cone_axis, spiral_vector)


def manager(
    spinham,
    spinham_format=None,
    ground_state_type=None,
    magnetic_field=None,
    output_seedname="minim",
):
    # Open main output file
    output_file = open(f"{output_seedname}-results", "w")
    # Write a logo
    output_file.write(logo(date_time=True) + "\n")

    # Load spin Hamiltonian from the input file
    spinham = load_spinham(spinham, spinham_format=spinham_format)

    # Create an instance of the energy class
    energy = Energy(spinham)

    # Put some magnetic field into it
    if magnetic_field is not None:
        energy.magnetic_field = magnetic_field

    # Decide which ground state types to minimize
    if "all" in ground_state_type:
        gs_to_minimize = ["ferro", "antiferro", "spiral"]
    else:
        gs_to_minimize = ground_state_type

    energies = []
    for gs in gs_to_minimize:
        if gs == "ferro":
            energies.append(
                _minimize_ferro(
                    energy=energy,
                    spinham=spinham,
                    seedname=output_seedname,
                    output_file=output_file,
                )
            )
        elif gs == "antiferro":
            energies.append(
                _minimize_antiferro(
                    energy=energy,
                    spinham=spinham,
                    seedname=output_seedname,
                    output_file=output_file,
                )
            )
        elif gs == "spiral":
            energies.append(
                _minimize_spiral(
                    energy=energy,
                    spinham=spinham,
                    seedname=output_seedname,
                    output_file=output_file,
                )
            )

    output_file.write("All minimization routines are finished. Summary:\n")
    for i in range(len(energies)):
        if gs_to_minimize[i] == "ferro":
            output_file.write(f"Ferromagnetic energy : {energies[i]:.8f}\n")
        if gs_to_minimize[i] == "antiferro":
            output_file.write(f"Antiferromagnetic energies :\n")
            for i in range(26):
                output_file.write(f"  {i+1} {energies[i]:.8f}\n")
        if gs_to_minimize[i] == "spiral":
            output_file.write(f"Spiral energy : {energies[i]:.8f}\n")


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
        "-gst",
        "--ground-state-type",
        nargs="*",
        type=str,
        choices=["all", "ferro", "antiferro", "spiral"],
        default="all",
        help="Type of the ground state to be assumed for the minimization.",
    )
    parser.add_argument(
        "-mf",
        "--magnetic_field",
        default=None,
        type=float,
        nargs=3,
        help="External magnetic field.",
        metavar="Hx Hy Hz",
    )
    parser.add_argument(
        "-os",
        "--output-seedname",
        type=str,
        default="minim",
        help="Seedname for output files",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    manager(**vars(args))
    _winwait()


if __name__ == "__main__":
    main()
