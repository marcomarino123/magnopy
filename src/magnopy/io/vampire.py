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

__all__ = ["dump_vampire", "dump_mat", "dump_ucf"]

import numpy as np

from magnopy._pinfo import logo
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.spinham.parameter import MatrixParameter
from magnopy.units.inside import ENERGY


def dump_vampire(
    spinham: SpinHamiltonian,
    seedname="vampire",
    anisotropic=True,
    dmi=True,
    custom_mask=None,
    decimals=5,
    materials=None,
    nologo=False,
):
    """
    Save the Hamiltonian in a Human-readable format.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian to be saved.
    seedname : str, default "vampire"
        Seedname for the .UCF and .mat files. Extensions are added automatically.
        Input file always have the name "input".
    anisotropic : bool, default True
        Whether to output anisotropic exchange.
    dmi : bool, default True
        Whether to output DMI exchange.
    custom_mask : func, optional
        Custom mask for the exchange parameter. Function which take (3,3) numpy:`ndarray`
        as an input and returns (3,3) numpy:`ndarray` as an output. If given, then
        ``anisotropic`` and ``dmi`` parameters are ignored.
    decimals : int, default 4
        Number of decimals to be printed (only for the exchange values).
    materials : list of int, optional
        List of materials for the atoms. Has to have the same length as the number of
        magnetic atoms in the ``spinham``. Order is the same as in :py:attr:`.SpinHamiltonian.magnetic_atoms`.
        If not given, each atom will be considered as a separate material. Starting from 0.
    nologo : bool, default False
        Whether to print the logo in the output files.

    Returns
    -------
    content : str
        Content of the .UCF file if ``filename`` is not given.
    """

    dump_ucf(
        spinham,
        filename=seedname + ".UCF",
        anisotropic=anisotropic,
        dmi=dmi,
        custom_mask=custom_mask,
        decimals=decimals,
        materials=materials,
        nologo=nologo,
    )
    dump_mat(
        spinham,
        filename=seedname + ".mat",
        materials=materials,
        nologo=nologo,
    )
    with open("input", "w", encoding="utf-8") as file:
        if not nologo:
            file.write(logo(comment=True, date_time=True) + "\n")

        file.write(
            "\n".join(
                [
                    "#------------------------------------------",
                    f"material:file={seedname}.mat",
                    f"material:unit-cell-file = {seedname}.UCF",
                    "#------------------------------------------",
                    "# TODO: your simulation parameters",
                ]
            )
        )


def dump_mat(spinham: SpinHamiltonian, filename=None, materials=None, nologo=False):
    """
    Write .mat file for |Vampire|_.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian to be saved.
    filename : str, optional
        Name for the .mat file. No extensions is added automatically.
        If not given, the output is returned as a string.
    materials : list of int, optional
        List of materials for the atoms. Has to have the same length as the number of
        magnetic atoms in the ``spinham``. Order is the same as in :py:attr:`.SpinHamiltonian.magnetic_atoms`.
        If not given, each atom will be considered as a separate material. Starting from 0.
    nologo : bool, default False
        Whether to print the logo in the output files.
    """
    if nologo:
        text = []
    else:
        text = [logo(comment=True, date_time=True)]
    if materials is not None:
        text.append(f"material:num-materials = {max(materials)+1}")
    else:
        text.append(f"material:num-materials = {len(spinham.magnetic_atoms)}")
    for i, atom in enumerate(spinham.magnetic_atoms):
        if materials is None or materials[i] not in materials[:i]:
            if materials is not None:
                m_i = materials[i] + 1
            else:
                m_i = i + 1
            text.append("#---------------------------------------------------")
            text.append(f"# Material {m_i} \n")
            text.append("#---------------------------------------------------")
            text.append(f"material[{m_i}]:material-name = {atom.name}")
            text.append(f"material[{m_i}]:material-element = {atom.type}")
            # Here we assume g=2
            text.append(f"material[{m_i}]:atomic-spin-moment={atom.spin*2} ! muB")
            if atom._spin_direction is not None:
                text.append(
                    f"material[{m_i}]:initial-spin-direction = {atom.spin_direction[0]:.8f},{atom.spin_direction[1]:.8f},{atom.spin_direction[2]:.8f}"
                )
            else:
                text.append(f"material[{m_i}]:initial-spin-direction = random")
            text.append(f"material[{m_i}]:damping-constant=0.1")
            text.append(f"material[{m_i}]:uniaxial-anisotropy-constant=0.0")
    text.append("#---------------------------------------------------")

    text = "\n".join(text)

    if filename is None:
        return "".join(text)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("".join(text))


def dump_ucf(
    spinham: SpinHamiltonian,
    filename=None,
    anisotropic=True,
    dmi=True,
    custom_mask=None,
    decimals=5,
    materials=None,
    nologo=False,
):
    """
    Save the Hamiltonian in a Human-readable format.

    Parameters
    ----------
    spinham : :py:class:`.SpinHamiltonian`
        Spin Hamiltonian to be saved.
    filename : str, optional
        Name for the .UCF file. No extension is added automatically.
        If not given, the output is returned as a string.
    anisotropic : bool, default True
        Whether to output anisotropic exchange.
    dmi : bool, default True
        Whether to output DMI exchange.
    custom_mask : func, optional
        Custom mask for the exchange parameter. Function which take (3,3) numpy:`ndarray`
        as an input and returns (3,3) numpy:`ndarray` as an output. If given, then
        ``anisotropic`` and ``dmi`` parameters are ignored.
    decimals : int, default 4
        Number of decimals to be printed (only for the exchange values).
    materials : list of int, optional
        List of materials for the atoms. Has to have the same length as the number of
        magnetic atoms in the ``spinham``. Order is the same as in :py:attr:`.SpinHamiltonian.magnetic_atoms`.
        If not given, each atom will be considered as a separate material.
    nologo : bool, default False
        Whether to print the logo in the output files.

    Returns
    -------
    content : str
        Content of the .UCF file if ``filename`` is not given.
    """
    if materials is None:
        materials = [i for i in range(len(spinham.magnetic_atoms))]
    original_notation = spinham.notation
    spinham.notation = "vampire"
    if nologo:
        text = []
    else:
        text = [logo(comment=True, date_time=True)]
    text.append("# Unit cell size:")
    text.append(f"{spinham.a:.8f} {spinham.b:.8f} {spinham.c:.8f}")
    text.append("# Unit cell lattice vectors:")
    text.append(f"{spinham.a1[0]:15.8f} {spinham.a1[1]:15.8f} {spinham.a1[2]:15.8f}")
    text.append(f"{spinham.a2[0]:15.8f} {spinham.a2[1]:15.8f} {spinham.a2[2]:15.8f}")
    text.append(f"{spinham.a3[0]:15.8f} {spinham.a3[1]:15.8f} {spinham.a3[2]:15.8f}")
    text.append("# Atoms")
    text.append(f"{len(spinham.magnetic_atoms)} {len(np.unique(materials))}")
    atom_indices = {}
    for a_i, atom in enumerate(spinham.magnetic_atoms):
        text.append(
            f"{a_i:<5} {atom.position[0]:15.8f} {atom.position[1]:15.8f} {atom.position[2]:15.8f} {materials[a_i]:>5}"
        )
        atom_indices[atom] = a_i
    text.append("# Interactions")
    text.append(f"{len(spinham.exchange_like)} tensorial")

    IID = 0
    for atom1, atom2, (i, j, k), J in spinham.exchange_like:
        if custom_mask is not None:
            J = MatrixParameter(custom_mask(J.matrix))
        else:
            if not dmi:
                J = MatrixParameter(matrix=J.matrix - J.dmi_matrix)
            if not anisotropic:
                J = MatrixParameter(matrix=J.matrix - J.aniso)
        J = J * ENERGY
        fmt = f"{7+decimals}.{decimals}e"
        text.append(
            f"{IID:<5} {atom_indices[atom1]:>3} {atom_indices[atom2]:>3}  {i:>2} {j:>2} {k:>2}  "
            f"{J.xx:{fmt}} {J.xy:{fmt}} {J.xz:{fmt}} "
            f"{J.yx:{fmt}} {J.yy:{fmt}} {J.yz:{fmt}} "
            f"{J.zx:{fmt}} {J.zy:{fmt}} {J.zz:{fmt}}"
        )
        IID += 1

    spinham.notation = original_notation

    text = "\n".join(text)

    if filename is None:
        return text

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
