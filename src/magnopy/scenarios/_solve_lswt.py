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
import wulfric

from magnopy._energy import Energy
from magnopy._lswt import LSWT
from magnopy._package_info import logo
from magnopy._parallelization import multiprocess_over_k
from magnopy.io._k_resolved import output_k_resolved, plot_k_resolved
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
        "directions\nplotter an installation of Plotly is required, please try to "
        "install it with the command\n\n  pip install plotly\n\nor\n\n  pip3 install "
        "plotly"
    )

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def solve_lswt(
    spinham,
    spin_directions=None,
    k_path=None,
    kpoints=None,
    relative=False,
    magnetic_field=None,
    output_folder="magnopy-results",
    number_processors=None,
    comment=None,
    no_html=False,
    hide_personal_data=False,
    spglib_symprec=1e-5,
) -> None:
    r"""
    Solves the spin Hamiltonian at the level of Linear Spin Wave theory.
    Outputs progress in the standard output (``print()``) and saves some data to
    the files on the disk.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian.
    spin_directions : (M, 3) |array-like|_, optional.
        Directions of the local quantization axis for each spin. Magnitude of the vector
        is ignored, only the direction is considered. If ``None``, then magnopy attempts
        to optimize classical energy of spin Hamiltonian to determine spin directions.
    k_path : str, optional
        Specification of the k-path. The format is "G-X-Y|G-Z" For more details
        on the format see documentation of |wulfric|_. If nothing given, then the
        k-path is computed by |wulfric|_ automatically based on the lattice type.
        Ignored if ``kpoints`` are given.
    kpoints : (N, 3) |array-like|_, optional
        Explicit list of k-points to be used instead of automatically generated.
    relative : bool, default False
        If ``relative == True``, then ``kpoints`` are interpreted as given relative to
        the reciprocal unit cell. Otherwise it is interpreted as given in absolute
        coordinates.
    magnetic_field : (3, ) |array-like|_
        Vector of external magnetic field, given in Tesla.
    output_folder : str, default "magnopy-results"
        Name for the folder where to save the output files. If the folder does not exist
        then it will be created.
    number_processors : int, optional
        Number of processors to be used in computation. By default magnopy uses all
        available processes. Use ``number_processors=1`` to run in serial mode.
    comment : str, optional
        Any comment to output right after the logo.
    no_html : bool, default False
        Whether to produce a series with html files with visual representation of
        spin directions or high symmetry points and k-path. The latter is only plotted
        when ``kpoints`` is not used.

        .. versionadded:: 0.1.10
    hide_personal_data : bool, default False
        Whether to use ``os.path.abspath()`` when printing the paths to the output and
        input files.
    spglib_symprec : float, default 1e-5
        Tolerance parameter for the space group symmetry search by |spglib|_. Reduce it
        if the space group is not the one you expected.

        .. versionadded:: 0.1.10

    Notes
    -----

    When using this function of magnopy in your Python scripts make sure to safeguard
    your script with the

    .. code-block:: python

        import magnopy

        # Import more stuff
        # or
        # Define your functions, classes

        if __name__ == "__main__":

            # Write your executable code here

    For more information refer to the  "Safe importing of main module" section in
    |multiprocessing|_ docs.

    """

    def envelope_path(pathname):
        if hide_personal_data:
            return pathname
        else:
            return os.path.abspath(pathname)

    all_good = True

    print(logo(date_time=True))
    if comment is not None:
        print(f"\n{' Comment ':=^90}\n")
        print(comment)

    if magnetic_field is not None:
        spinham.add_magnetic_field(h=magnetic_field)

    print(f"\n{' Ground state ':=^90}\n")
    energy = Energy(spinham=spinham)

    if spin_directions is None:
        print("Spin directions are not given, start to optimize ...")

        spin_directions = energy.optimize(
            energy_tolerance=1e-5, torque_tolerance=1e-5, quiet=False
        )
        print("Optimization is done.")
    else:
        print("Spin directions of the ground state are provided by the user.")

        spin_directions = np.array(spin_directions, dtype=float)
        spin_directions = (
            spin_directions / np.linalg.norm(spin_directions, axis=1)[:, np.newaxis]
        )

    E_0 = energy.E_0(spin_directions=spin_directions)
    print(f"\n{'Classic ground state energy (E_0)':<51} : {E_0:>15.6f} meV\n")

    print("Directions of spin vectors of the ground state and spin values are")

    print(f"{'Name':<6} {'S':>7} {'Sx':>12} {'Sy':>12} {'Sz':>12}")

    for i in range(spinham.M):
        print(
            f"{spinham.magnetic_atoms.names[i]:<6} "
            f"{spinham.magnetic_atoms.spins[i]:7.4f} "
            f"{spin_directions[i][0]:12.8f} "
            f"{spin_directions[i][1]:12.8f} "
            f"{spin_directions[i][2]:12.8f}"
        )

    print(f"\n{' Start LSWT ':=^90}\n")

    # Create the output directory if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Treat kpoints
    if kpoints is not None:
        kpoints = np.array(kpoints, dtype=float)
        if relative:
            kpoints = kpoints @ wulfric.cell.get_reciprocal(cell=spinham.cell)
        kp = None
        flat_indices = None
    else:
        spglib_data = wulfric.get_spglib_data(
            cell=spinham.cell, atoms=spinham.atoms, spglib_symprec=spglib_symprec
        )
        print(f"Space group {spglib_data.space_group_number} detected.")
        print(
            f"Bravais lattice is {spglib_data.crystal_family + spglib_data.centring_type}."
        )
        kp = wulfric.Kpoints.from_crystal(
            cell=spinham.cell,
            atoms=spinham.atoms,
            convention="HPKOT",
            spglib_data=spglib_data,
        )
        # Set custom k path
        if k_path is not None:
            kp.path = k_path
        kpoints = kp.points(relative=False)
        flat_indices = kp.flat_points(relative=False)

        print("\nList of high symmetry k points")

        header_names = ["k_b1", "k_b2", "k_b3", "k_x", "k_y", "k_z"]
        print(
            " ".join(
                [f"{'name':<5}", f"{'label':>10}"]
                + [f"{tmp:>10}" for tmp in header_names]
            )
        )
        for n_i, name in enumerate(kp.hs_names):
            line = [f"{name:<5}", f"{kp.hs_labels[name]:>10}"]
            for comp in kp.hs_coordinates[name]:
                line.append(f"{comp:>10.6f}")
            rcell = wulfric.cell.get_reciprocal(cell=spinham.cell)
            for comp in kp.hs_coordinates[name] @ rcell:
                line.append(f"{comp:>10.6f}")
            print(" ".join(line))

        print(f'\nK path is "{kp.path_string}"')
        print("\nFlat indices and labels of the points in k path are")
        print(
            "  "
            + "\n  ".join(
                [
                    f"{label:<10} {tick:>12.8f}"
                    for (label, tick) in zip(kp.labels, kp.ticks(relative=False))
                ]
            )
        )

        if not no_html:
            filename = os.path.join(output_folder, "K-POINTS.html")
            pe = wulfric.PlotlyEngine()

            prim_cell, _ = wulfric.crystal.get_primitive(
                cell=spinham.cell,
                atoms=spinham.atoms,
                convention="SC",
                spglib_data=spglib_data,
            )
            pe.plot_brillouin_zone(
                cell=prim_cell,
                color="red",
                legend_label="Brillouin zone of the primitive cell",
            )
            pe.plot_brillouin_zone(
                cell=spinham.cell,
                color="chocolate",
                legend_label="Brillouin zone of the spinham.cell",
            )
            pe.plot_kpath(kp=kp)
            pe.plot_kpoints(kp=kp, only_from_kpath=True)

            pe.save(output_name=filename)
            print(
                f"\nHigh-symmetry points and chosen k-path are plotted in\n  {envelope_path(filename)}"
            )

    lswt = LSWT(spinham=spinham, spin_directions=spin_directions)

    print(
        f"{'Correction to the classic ground state energy (E_2)':<50} : "
        f"{lswt.E_2:>15.6f} meV\n"
    )

    print(
        "Coefficient before one-operator terms (shall be zero if the ground state is correct)"
    )

    print("  " + "\n  ".join([f"{o:12.8f}" for o in lswt.O]))

    if not np.allclose(lswt.O, np.zeros(lswt.O.shape)):
        all_good = False
        print(f"\n{'  WARNING  ':!^90}")
        print(
            "Coefficients before the one-operator terms are not zero. It might indicate  that\n"
            "the ground state (spin directions) is not a ground state of the considered spin\n"
            "Hamiltonian. The results might not be meaningful. If coefficients are << 1, that might\n"
            "be an artifact of the finite point arithmetic and the results might be just fine."
        )
        print(f"{'  END OF WARNING  ':!^90}\n")

    print("\nStart calculations over k ... ", end="")

    results = multiprocess_over_k(
        kpoints,
        function=lswt.diagonalize,
        relative=False,
        number_processors=number_processors,
    )

    omegas = np.array([i[0] for i in results])
    deltas = np.array([i[1] for i in results])
    print("Done")

    filename = os.path.join(output_folder, "OMEGAS.txt")
    output_k_resolved(
        data=omegas.real,
        data_headers=[f"mode {i + 1}" for i in range(len(omegas[0]))],
        output_filename=filename,
        kpoints=kpoints,
        relative=False,
        rcell=wulfric.cell.get_reciprocal(cell=spinham.cell),
        flat_indices=flat_indices,
        digits=6,
        scientific_notation=True,
    )
    print(f"\nOmegas are saved in file\n  {envelope_path(filename)}")

    filename = filename[:-4] + ".png"
    plot_k_resolved(
        data=omegas.real,
        kp=kp,
        output_filename=filename,
        ylabel=R"$\omega_{\alpha}(\boldsymbol{k})$, meV",
    )
    print(f"Plot is saved in file\n  {envelope_path(filename)}")

    if not np.allclose(omegas.imag, np.zeros(omegas.imag.shape)):
        all_good = False
        print(f"\n{'  WARNING  ':!^90}")
        print(
            "Eigenfrequiencies has non-zero imaginary component for some k vectors. It might\n"
            "indicate that the ground state (spin directions) is not a ground state of the\n"
            "considered spin Hamiltonian. The results might not be meaningful.\n"
        )
        filename = os.path.join(output_folder, "OMEGAS-IMAG.txt")
        output_k_resolved(
            data=omegas.imag,
            data_headers=[f"mode {i + 1}" for i in range(len(omegas[0]))],
            output_filename=filename,
            kpoints=kpoints,
            relative=False,
            rcell=wulfric.cell.get_reciprocal(cell=spinham.cell),
            flat_indices=(flat_indices),
            digits=6,
            scientific_notation=True,
        )
        print(f"Imaginary part of omegas is saved in file\n  {envelope_path(filename)}")

        filename = filename[:-4] + ".png"
        plot_k_resolved(
            data=omegas.imag,
            kp=kp,
            output_filename=filename,
            ylabel=R"$\mathcal{Im}(\omega_{\alpha}(\boldsymbol{k}))$, meV",
        )
        print(f"Plot of imaginary part is saved in file\n  {envelope_path(filename)}")
        print(f"{'  END OF WARNING  ':!^90}\n")

    filename = os.path.join(output_folder, "DELTAS.txt")
    output_k_resolved(
        data=deltas.real,
        data_headers=["Delta"],
        output_filename=filename,
        kpoints=kpoints,
        relative=False,
        rcell=wulfric.cell.get_reciprocal(cell=spinham.cell),
        flat_indices=flat_indices,
        digits=6,
        scientific_notation=True,
    )
    print(f"Deltas are saved in file\n  {envelope_path(filename)}")

    filename = filename[:-4] + ".png"
    plot_k_resolved(
        data=deltas.real,
        kp=kp,
        output_filename=filename,
        ylabel=R"$\Delta(\boldsymbol{k})$, meV",
    )
    print(f"Plot is saved in file\n  {envelope_path(filename)}")

    if not no_html:
        if PLOTLY_AVAILABLE:
            positions = np.array(spinham.magnetic_atoms.positions) @ spinham.cell
            filename = os.path.join(output_folder, "SPIN_DIRECTIONS")

            plot_spin_directions(
                output_name=filename,
                positions=positions,
                spin_directions=spin_directions,
                cell=spinham.cell,
                _full_plotly=True,
            )

            print(
                f"\nImage of spin directions is saved in file\n  {envelope_path(filename)}.html"
            )
        else:
            print(PLOTLY_ERROR_MESSAGE)

    if all_good:
        print(f"\n{' Finished OK ':=^90}")
    else:
        print(f"\n{' Finished with WARNINGS ':=^90}")


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
