# ================================== LICENSE ===================================
# MAGNOPY - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.org
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
#
# ================================ END LICENSE =================================


import os

import numpy as np

from magnopy._energy import Energy
from magnopy._package_info import logo
from magnopy._spinham._supercell import make_supercell
from magnopy.io._spin_directions import plot_spin_directions

try:
    import plotly.graph_objects as go  # noqa F401

    PLOTLY_AVAILABLE = True
    PLOTLY_ERROR_MESSAGE = (
        "If you see this message, please contact developers of the code."
    )
except ImportError:
    PLOTLY_AVAILABLE = False
    PLOTLY_ERROR_MESSAGE = (
        "\nCannot produce an .html picture with spin directions. In order to use spin "
        "projection\nplotter an installation of Plotly is required, please try to "
        "install it with the command\n\n  pip install plotly\n\nor\n\n  pip3 install "
        "plotly"
    )

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def optimize_sd(
    spinham,
    supercell=(1, 1, 1),
    magnetic_field=None,
    energy_tolerance=1e-5,
    torque_tolerance=1e-5,
    output_folder="magnopy-results",
    comment=None,
    no_sd_image=False,
    hide_personal_data=False,
) -> None:
    r"""
    Optimizes classical energy of spin Hamiltonian and finds a set of spin directions
    that describe local minima of energy landscape.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian.
    supercell : (3, ) tuple of int
        If different from ``(1, 1, 1)``, then a supercell Hamiltonian is constructed and
        spins are varied within the supercell and not a unit cell.
    magnetic_field : (3, ) |array-like|_
        Vector of external magnetic field, given in Tesla.
    energy_tolerance : float, default 1e-5
        Tolerance parameter. Difference between classical energies of two consecutive
        optimization steps.
    torque_tolerance : float, default 1e-5
        Tolerance parameter. Maximum torque among all spins.
    output_folder : str, default "magnopy-results"
        Name for the folder where to save the output files. If the folder does not exist
        then it will be created.
    comment : str, optional
        Any comment to output right after the logo.
    no_sd_image : bool, default False
        Whether to disable plotting of spin directions into an .html file.
    hide_personal_data : bool, default False
        Whether to use ``os.path.abspath()`` when printing the paths to the output and
        input files.

    Raises
    ------
    ValueError
        If ``len(supercell) != 3``.
    ValueError
        If ``supercell[0] < 1`` or ``supercell[1] < 1`` or ``supercell[2] < 1``.
    """

    def envelope_path(pathname):
        if hide_personal_data:
            return pathname
        else:
            return os.path.abspath(pathname)

    # Check input for the supercell
    supercell = tuple(supercell)
    if len(supercell) != 3:
        raise ValueError(
            f"Expected a tuple of three int, got {len(supercell)} elements."
        )
    if supercell[0] < 1 or supercell[1] < 1 or supercell[2] < 1:
        raise ValueError(f"Supercell repetitions must be >=1, got {supercell}.")

    print(logo(date_time=True))
    print(f"\n{' Comment ':=^90}\n")
    if comment is not None:
        print(comment)

    if magnetic_field is not None:
        spinham.add_magnetic_field(h=magnetic_field)

    print(f"\n{' Start optimization ':=^90}\n")

    print(f"Energy tolerance : {energy_tolerance:.5e}")
    print(f"Torque tolerance : {torque_tolerance:.5e}")

    original_spinham = spinham
    if supercell != (1, 1, 1):
        spinham = make_supercell(spinham=spinham, supercell=supercell)
        print(
            f"Minimizing on the supercell of {supercell[0]} x {supercell[1]} x {supercell[2]} unit cells."
        )
    else:
        print("Minimizing on the original unit cell of the Hamiltonian.")

    energy = Energy(spinham=spinham)

    initial_guess = np.random.uniform(low=-1, high=1, size=(spinham.M, 3))

    initial_guess = initial_guess / np.linalg.norm(initial_guess, axis=1)[:, np.newaxis]

    filename = os.path.join(output_folder, "INITIAL_GUESS.TXT")
    with open(filename, "w") as f:
        for i in range(spinham.M):
            f.write(
                f"{initial_guess[i][0]:12.8f} "
                f"{initial_guess[i][1]:12.8f} "
                f"{initial_guess[i][2]:12.8f}\n"
            )
    print(
        f"\nSpin directions of the initial guess are saved in file\n  {envelope_path(filename)}"
    )

    spin_directions = energy.optimize(
        initial_guess=initial_guess,
        energy_tolerance=energy_tolerance,
        torque_tolerance=torque_tolerance,
        quiet=False,
    )
    print("Optimization is done.")

    E_0 = energy.E_0(spin_directions=spin_directions)
    print(f"\nClassic ground state energy (E_0) : {E_0:>15.6f} meV")

    # Create the output directory if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.join(output_folder, "SPIN_DIRECTIONS.txt")
    with open(filename, "w") as f:
        for i in range(spinham.M):
            f.write(
                f"{spin_directions[i][0]:12.8f} "
                f"{spin_directions[i][1]:12.8f} "
                f"{spin_directions[i][2]:12.8f}\n"
            )

    print(f"\nSpin directions are saved in file\n  {envelope_path(filename)}")

    filename = os.path.join(output_folder, "SPIN_POSITIONS.txt")
    with open(filename, "w") as f:
        for i in range(spinham.M):
            tmp = spinham.magnetic_atoms.positions[i] @ spinham.cell
            f.write(f"{tmp[0]:12.8f} {tmp[1]:12.8f} {tmp[2]:12.8f}\n")

    print(f"\nSpin positions are saved in file\n  {envelope_path(filename)}")

    if not no_sd_image:
        if PLOTLY_AVAILABLE:
            positions = np.array(spinham.magnetic_atoms.positions) @ spinham.cell
            filename = os.path.join(output_folder, "SPIN_DIRECTIONS")

            plot_spin_directions(
                output_name=filename,
                positions=positions,
                spin_directions=spin_directions,
                cell=original_spinham.cell,
                highlight=[i for i in range(original_spinham.M)],
                name_highlighted="Original unit cell",
                name_other="Other unit cells",
                _full_plotly=True,
            )

            print(
                f"\nImage of spin directions is saved in file\n  {envelope_path(filename)}.html"
            )
        else:
            print(PLOTLY_ERROR_MESSAGE)

    print(f"\n{' Finished ':=^90}")


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
