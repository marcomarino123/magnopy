import wulfric
from wulfric import Atom, print_2d_array

from magnopy._pinfo import logo
from magnopy.spinham.hamiltonian import SpinHamiltonian
from magnopy.spinham.parameter import ExchangeParameter

__all__ = ["load_model", "dump_model"]


SEPARATOR = "=" * 80
SUBSEPARATOR = "-" * 80


def _write_bond(name1: str, name2: str, ijk: tuple, J: ExchangeParameter):
    r"""
    Write a bond to the output file.

    Parameters
    ----------
    name1 : str
        Name of the first atom in the bond.
    name2 : str
        Name of the second atom in the bond.
    ijk : tuple
        Index of the bond.
    J : :py:class:`.ExchangeParameter`
        Exchange parameter for the bond.
    """

    text = [SUBSEPARATOR]
    text.append(
        f"{name1:6} "
        + f"{name2:6} "
        + f"{ijk[0]:3} {ijk[1]:3} {ijk[2]:3}"
        + f"{J.iso:8.4}"
    )
    text.append("Matrix")
    text.append(print_2d_array(J.matrix, fmt="8.4f", print_result=False, borders=False))

    return "\n".join(text)


def dump_model(spinham: SpinHamiltonian, filename):
    """
    Dump a SpinHamiltonian object to a .txt file.

    Parameters
    ----------
    spinham : :py:class`.SpinHamiltonian`
        SpinHamiltonian object to dump.
    filename : str
        Filename to dump SpinHamiltonian object to.
    """

    # Write logo
    text = [logo(comment=True)]
    text.append(SEPARATOR)

    # Write unit cell
    text.append("Cell: Angstrom")
    text.append(
        wulfric.print_2d_array(
            spinham.cell, fmt="12.8f", print_result=False, borders=False
        )
    )
    text.append(SEPARATOR)

    # Write atom's position and spins
    text.append("Atoms: relative")
    for atom in spinham.atoms:
        text.append(
            f"{atom.name:4} "
            + f"{atom.position[0]:12.8f} "
            + f"{atom.position[1]:12.8f} "
            + f"{atom.position[2]:12.8f} "
        )
        try:
            text[-1] += (
                f"{atom.spin_vector[0]:8.4f} "
                + f"{atom.spin_vector[1]:8.4f} "
                + f"{atom.spin_vector[2]:8.4f}"
            )
        except ValueError:
            pass
    text.append(SEPARATOR)

    # Define which atom's names are unique
    names = [atom.name for atom in spinham.atoms]
    unique_names = [
        atom.name if names.count(atom.name) == 1 else atom.fullname
        for atom in spinham.atoms
    ]
    unique_names = dict(zip(spinham.atoms, unique_names))

    # Write exchange parameters
    text.append("Parameters: meV")
    for atom1, atom2, (i, j, k), J in spinham:
        text.append(_write_bond(unique_names[atom1], unique_names[atom2], (i, j, k), J))
    text.append(SEPARATOR)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(text))


def load_model():
    pass
