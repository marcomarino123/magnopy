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

import numpy as np

from magnopy._package_info import logo
from magnopy.io._spin_directions import plot_spin_directions

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def show_spin_directions(
    spinham, spin_directions, repeat=(1, 1, 1), output_name="magnopy-sd", comment=None
) -> None:
    r"""
    Shows the direction of spin vectors in spin Hamiltonian.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_
        Directions of the local quantization axis for each spin. Magnitude of the vector
        is ignored, only the direction is considered.
    repeat : (3, ) tuple of int, default (1, 1, 1)
        Repetitions of the unit cell along each three of the lattice vectors. Requires
        ``unit_cell`` to be provided. Each number should be ``>= 1``.
    output_name : str, default "magnopy-results"
        Name for the folder where to save the output files. If the folder does not exist
        then it will be created.
    comment : str, optional
        Any comment to output right after the logo.
    """

    all_good = True

    print(logo(date_time=True))

    if comment is not None:
        print(f"\n{' Comment ':=^90}\n")
        print(comment)

    print(f"\n{' Plotting spin directions ':=^90}\n")

    print("Directions of spin vectors are")

    print(f"{'Name':<6} {'Sx':>12} {'Sy':>12} {'Sz':>12}")

    for i in range(spinham.M):
        print(
            f"{spinham.magnetic_atoms.names[i]:<6} "
            f"{spin_directions[i][0]:12.8f} "
            f"{spin_directions[i][1]:12.8f} "
            f"{spin_directions[i][2]:12.8f}"
        )

    positions = np.array(spinham.magnetic_atoms.positions) @ spinham.cell

    plot_spin_directions(
        output_name=output_name,
        positions=positions,
        spin_directions=spin_directions,
        unit_cell=spinham.cell,
        repeat=repeat,
    )
    print(f"Plot is saved in file\n  {os.path.abspath(output_name)}.html")

    if all_good:
        print(f"\n{' Finished OK ':=^90}")
    else:
        print(f"\n{' Finished with WARNINGS ':=^90}")


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
