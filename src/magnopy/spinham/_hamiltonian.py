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


from copy import deepcopy

import numpy as np
from wulfric import add_sugar
from wulfric.crystal import get_distance

from magnopy.spinham._c1 import _add_1, _p1, _remove_1
from magnopy.spinham._c21 import _add_2_1, _p21, _remove_2_1
from magnopy.spinham._c22 import _add_2_2, _p22, _remove_2_2
from magnopy.spinham._c31 import _add_3_1, _p31, _remove_3_1
from magnopy.spinham._c32 import _add_3_2, _p32, _remove_3_2
from magnopy.spinham._c41 import _add_4_1, _p41, _remove_4_1
from magnopy.spinham._notation import Notation
from magnopy.spinham._validators import _validate_atom_index, _validate_unit_cell_index

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


class SpinHamiltonian:
    r"""
    Spin Hamiltonian.

    Parameters
    ----------
    notation : :py:class:`.Notation` or str
        A notation of the spin Hamiltonian.
    cell : (3, 3) |array-like|_
        Matrix of a cell, rows are interpreted as vectors.
    atoms : dict
        Dictionary with atoms.

    """

    def __init__(self, cell, atoms, notation) -> None:
        self._cell = np.array(cell)

        self._atoms = add_sugar(atoms)

        # Only the magnetic sites
        self._magnetic_atoms = None
        self._index_map = None

        self._notation = notation

        # [[alpha, parameter], ...]
        self._1 = []

        # [[alpha, parameter], ...]
        self._2_1 = []

        # [[alpha, beta, nu, parameter], ...]
        self._2_2 = []

        # [[alpha, parameter], ...]
        self._3_1 = []

        # [[alpha, beta, nu, parameter], ...]
        self._3_2 = []

        # [[alpha, beta, gamma, nu, lambda, parameter], ...]
        self._3_3 = []

        # [[alpha, parameter], ...]
        self._4_1 = []

        # [[alpha, beta, nu, parameter], ...]
        self._4_2_1 = []

        # [[alpha, beta, nu, parameter], ...]
        self._4_2_2 = []

        # [[alpha, beta, gamma, nu, lambda, parameter], ...]
        self._4_3 = []

        # [[alpha, beta, gamma, epsilon, nu, lambda, rho, parameter], ...]
        self._4_4 = []

    ############################################################################
    #                              Cell and Atoms                              #
    ############################################################################

    @property
    def cell(self) -> dict:
        r"""
        Cell of the crystal on which the Hamiltonian is build.

        Returns
        -------
        cell : (3, 3) :numpy:`ndarray`
            Matrix of the cell, rows are lattice vectors.

        Notes
        -----
        If is not recommended to change the ``cell`` property after the creation of
        :py:class:`.SpinHamiltonian`. In fact an attempt to do so will raise an
        ``AttributeError``:

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> notation = magnopy.spinham.Notation()
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell = np.eye(3), atoms={}, notation=notation)
            >>> spinham.cell = 2 * np.eye(3)
            Traceback (most recent call last):
            ...
            AttributeError: Change of the cell attribute is not supported after the creation of SpinHamiltonian instance. If you need to modify cell, then use pre-defined methods of SpinHamiltonian or create a new one.

        Use pre-defined methods of the :py:class:`.SpinHamiltonian` class to safely
        modify the cell.

        If you need to change the cell attribute, then use

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> notation = magnopy.spinham.Notation()
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell = np.eye(3), atoms={}, notation=notation)
            >>> spinham.cell
            array([[1., 0., 0.],
                   [0., 1., 0.],
                   [0., 0., 1.]])
            >>> spinham._cell = 2 * np.eye(3)
            >>> spinham.cell
            array([[2., 0., 0.],
                   [0., 2., 0.],
                   [0., 0., 2.]])


        In the latter case correct behavior of magnopy **is not** guaranteed. Use only
        if you have a deep understanding of the magnopy source code.
        """

        return self._cell

    @cell.setter
    def cell(self, new_value):
        raise AttributeError(
            f"Change of the cell attribute is not supported after "
            "the creation of SpinHamiltonian instance. If you need to modify cell, "
            "then use pre-defined methods of SpinHamiltonian or create a new one."
        )

    @property
    def atoms(self) -> dict:
        r"""
        Atoms of the crystal on which the Hamiltonian is build.

        Returns
        -------
        atoms : dict (with added sugar)
            Dictionary with the atoms.

        Notes
        -----
        If is not recommended to change the atoms property after the creation of
        :py:class:`.SpinHamiltonian`. In fact an attempt to do so will raise an
        ``AttributeError``:

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> notation = magnopy.spinham.Notation()
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell = np.eye(3), atoms={}, notation=notation)
            >>> spinham.atoms = {"names" : ["Cr"]}
            Traceback (most recent call last):
            ...
            AttributeError: Change of the atoms dictionary is not supported after the creation of SpinHamiltonian instance. If you need to modify atoms, then use pre-defined methods of SpinHamiltonian or create a new one.

        Use pre-defined methods of the :py:class:`.SpinHamiltonian` class to safely
        modify atoms.

        If you need to change the whole dictionary at once, then use

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> notation = magnopy.spinham.Notation()
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell = np.eye(3), atoms={}, notation=notation)
            >>> spinham.atoms
            {}
            >>> spinham._atoms = {"names" : ["Cr"]}
            >>> spinham.atoms
            {'names': ['Cr']}

        In the latter case correct behavior of magnopy **is not** guaranteed. Use only
        if you have a deep understanding of the magnopy source code.
        """

        return self._atoms

    @atoms.setter
    def atoms(self, new_value):
        raise AttributeError(
            f"Change of the atoms dictionary is not supported after "
            "the creation of SpinHamiltonian instance. If you need to modify atoms, "
            "then use pre-defined methods of SpinHamiltonian or create a new one."
        )

    def _reset_internals(self):
        self._index_map = None
        self._magnetic_atoms = None

    def _update_internals(self):
        # Identify magnetic sites
        indices = set()

        for alpha, _ in self._1:
            indices.add(alpha)

        for alpha, _ in self._2_1:
            indices.add(alpha)

        for alpha, beta, _, _ in self._2_2:
            indices.add(alpha)
            indices.add(beta)

        for alpha, _ in self._3_1:
            indices.add(alpha)

        for alpha, beta, _, _ in self._3_2:
            indices.add(alpha)
            indices.add(beta)

        for alpha, _ in self._4_1:
            indices.add(alpha)

        # TODO three and four spin terms

        indices = sorted(list(indices))

        # Create index map
        self._index_map = [None for _ in range(len(self.atoms.names))]
        for i in range(len(indices)):
            self._index_map[indices[i]] = i

        # Create magnetic atoms dictionary
        self._magnetic_atoms = add_sugar({})

        for key in self.atoms:
            self._magnetic_atoms[key] = []

            for full_index in indices:
                self._magnetic_atoms[key].append(self.atoms[key][full_index])

    @property
    def index_map(self):
        r"""
        Index map from all atoms to the magnetic ones.

        Returns
        -------
        index_map (L, ) list of int
            Index map. Integers. ``L = len(spinham.atoms.names)``
        """

        if self._index_map is None:
            self._update_internals()

        return self._index_map

    @property
    def magnetic_atoms(self):
        r"""
        Magnetic atoms of the spin Hamiltonian.

        Magnetic atom is defined as an atom with at least one parameter associated with
        it.

        This property is dynamically computed at every call.

        Returns
        -------
        magnetic_atoms : list of int
            Indices of magnetic atoms in the ``spinham.atoms``. Sorted.

        See Also
        --------
        M
        """

        if self._magnetic_atoms is None:
            self._update_internals()

        return self._magnetic_atoms

    @property
    def M(self):
        r"""
        Number of spins (magnetic atoms) in the unit cell.

        Returns
        -------
        M : int
            Number of spins (magnetic atoms) in the unit cell.

        See Also
        --------
        magnetic_atoms
        """

        return len(self.magnetic_atoms.names)

    ############################################################################
    #                           Notation properties                            #
    ############################################################################
    @property
    def notation(self) -> Notation:
        r"""
        Notation of the spin Hamiltonian.

        See Also
        --------
        Notation
        """

        return self._notation

    @notation.setter
    def notation(self, new_notation: Notation):
        self._set_multiple_counting(new_notation._multiple_counting)

        self._set_spin_normalization(new_notation._spin_normalized)

        self._set_c1(new_notation._c1)

        self._set_c21(new_notation._c21)
        self._set_c22(new_notation._c22)

        self._set_c31(new_notation._c31)
        self._set_c32(new_notation._c32)
        self._set_c33(new_notation._c33)

        self._set_c41(new_notation._c41)
        self._set_c421(new_notation._c421)
        self._set_c422(new_notation._c422)
        self._set_c43(new_notation._c43)
        self._set_c44(new_notation._c44)

        self._notation = new_notation

    def _set_multiple_counting(self, multiple_counting: bool) -> None:
        if multiple_counting is None or self.notation._multiple_counting is None:
            return

        multiple_counting = bool(multiple_counting)

        if self.notation.multiple_counting == multiple_counting:
            return

        # For (two spins & two sites)

        # It was absent before
        if multiple_counting:
            factor = 0.5
        # It was present before
        else:
            factor = 2.0

        for index in range(len(self._2_2)):
            self._2_2[index][3] = self._2_2[index][3] * factor

        # For (three spins & two sites)

        # It was absent before
        if multiple_counting:
            factor = 0.5
        # It was present before
        else:
            factor = 2.0

        for index in range(len(self._3_2)):
            self._3_2[index][3] = self._3_2[index][3] * factor

        # TODO For (four spins & ...)

    def _set_spin_normalization(self, spin_normalized: bool) -> None:
        if spin_normalized is None or self.notation._spin_normalized is None:
            return

        spin_normalized = bool(spin_normalized)

        if self.notation.spin_normalized == spin_normalized:
            return

        # Before it was not normalized
        if spin_normalized:
            # For (one spin & one site)
            for index in range(len(self._1)):
                alpha = self._1[index][0]
                self._1[index][1] = self._1[index][1] * self.atoms.spins[alpha]
            # For (two spins & one site)
            for index in range(len(self._2_1)):
                alpha = self._2_1[index][0]
                self._2_1[index][1] = self._2_1[index][1] * self.atoms.spins[alpha] ** 2
            # For (two spins & two sites)
            for index in range(len(self._2_2)):
                alpha = self._2_2[index][0]
                beta = self._2_2[index][1]
                self._2_2[index][3] = self._2_2[index][3] * (
                    self.atoms.spins[alpha] * self.atoms.spins[beta]
                )
            # For (three spins & one site)
            for index in range(len(self._3_1)):
                alpha = self._3_1[index][0]
                self._3_1[index][1] = self._3_1[index][1] * self.atoms.spins[alpha] ** 3
            # For (three spins & two sites)
            for index in range(len(self._3_2)):
                alpha = self._3_2[index][0]
                beta = self._3_2[index][1]
                self._3_2[index][3] = self._3_2[index][3] * (
                    self.atoms.spins[alpha] ** 2 * self.atoms.spins[beta]
                )
            # For (four spins & one site)
            for index in range(len(self._4_1)):
                alpha = self._4_1[index][0]
                self._4_1[index][1] = self._4_1[index][1] * self.atoms.spins[alpha] ** 4
        # Before it was normalized
        else:
            # For (one spin & one site)
            for index in range(len(self._1)):
                alpha = self._1[index][0]
                self._1[index][1] = self._1[index][1] / self.atoms.spins[alpha]
            # For (two spins & one site)
            for index in range(len(self._2_1)):
                alpha = self._2_1[index][0]
                self._2_1[index][1] = self._2_1[index][1] / self.atoms.spins[alpha] ** 2
            # For (two spins & two sites)
            for index in range(len(self._2_2)):
                alpha = self._2_2[index][0]
                beta = self._2_2[index][1]
                self._2_2[index][3] = self._2_2[index][3] / (
                    self.atoms.spins[alpha] * self.atoms.spins[beta]
                )
            # For (three spins & one site)
            for index in range(len(self._3_1)):
                alpha = self._3_1[index][0]
                self._3_1[index][1] = self._3_1[index][1] / self.atoms.spins[alpha] ** 3
            # For (three spins & two sites)
            for index in range(len(self._3_2)):
                alpha = self._3_2[index][0]
                beta = self._3_2[index][1]
                self._3_2[index][3] = self._3_2[index][3] / (
                    self.atoms.spins[alpha] ** 2 * self.atoms.spins[beta]
                )
            # For (four spins & one site)
            for index in range(len(self._4_1)):
                alpha = self._4_1[index][0]
                self._4_1[index][1] = self._4_1[index][1] / self.atoms.spins[alpha] ** 4

        # TODO For (four spins & ...)

    def _set_c1(self, new_c1: float) -> None:
        if new_c1 is None or self.notation._c1 is None:
            return

        new_c1 = float(new_c1)

        if self.notation.c1 == new_c1:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._1)):
            self._1[index][1] = self._1[index][1] * self.notation.c1 / new_c1

    def _set_c21(self, new_c21: float) -> None:
        if new_c21 is None or self.notation._c21 is None:
            return

        new_c21 = float(new_c21)

        if self.notation.c21 == new_c21:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._2_1)):
            self._2_1[index][1] = self._2_1[index][1] * self.notation.c21 / new_c21

    def _set_c22(self, new_c22: float) -> None:
        if new_c22 is None or self.notation._c22 is None:
            return

        new_c22 = float(new_c22)

        if self.notation.c22 == new_c22:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._2_2)):
            self._2_2[index][3] = self._2_2[index][3] * self.notation.c22 / new_c22

    def _set_c31(self, new_c31: float) -> None:
        if new_c31 is None or self.notation._c31 is None:
            return

        new_c31 = float(new_c31)

        if self.notation.c31 == new_c31:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._3_1)):
            self._3_1[index][1] = self._3_1[index][1] * self.notation.c31 / new_c31

    def _set_c32(self, new_c32: float) -> None:
        if new_c32 is None or self.notation._c32 is None:
            return

        new_c32 = float(new_c32)

        if self.notation.c32 == new_c32:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._3_2)):
            self._3_2[index][3] = self._3_2[index][3] * self.notation.c32 / new_c32

    def _set_c33(self, new_c33: float) -> None:
        if new_c33 is None or self.notation._c33 is None:
            return

        new_c33 = float(new_c33)

        if self.notation.c33 == new_c33:
            return

        raise NotImplementedError

    def _set_c41(self, new_c41: float) -> None:
        if new_c41 is None or self.notation._c41 is None:
            return

        new_c41 = float(new_c41)

        if self.notation.c41 == new_c41:
            return

        # If factor is changing one has to scale parameters.
        for index in range(len(self._4_1)):
            self._4_1[index][1] = self._4_1[index][1] * self.notation.c41 / new_c41

    def _set_c421(self, new_c421: float) -> None:
        if new_c421 is None or self.notation._c421 is None:
            return

        new_c421 = float(new_c421)

        if self.notation.c421 == new_c421:
            return

        raise NotImplementedError

    def _set_c422(self, new_c422: float) -> None:
        if new_c422 is None or self.notation._c422 is None:
            return

        new_c422 = float(new_c422)

        if self.notation.c422 == new_c422:
            return

        raise NotImplementedError

    def _set_c43(self, new_c43: float) -> None:
        if new_c43 is None or self.notation._c43 is None:
            return

        new_c43 = float(new_c43)

        if self.notation.c43 == new_c43:
            return

        raise NotImplementedError

    def _set_c44(self, new_c44: float) -> None:
        if new_c44 is None or self.notation._c44 is None:
            return

        new_c44 = float(new_c44)

        if self.notation.c44 == new_c44:
            return

        raise NotImplementedError

    ############################################################################
    #                                Copy getter                               #
    ############################################################################
    def copy(self):
        R"""
        Returns a new, independent copy of the same Hamiltonian.

        Returns
        -------
        spinham : :py:class:`.SpinHamiltonian`
            A new instance of the same Hamiltonian.
        """

        return deepcopy(self)

    ############################################################################
    #                            One spin & one site                           #
    ############################################################################
    p1 = _p1
    add_1 = _add_1
    remove_1 = _remove_1

    ############################################################################
    #                           Two spins & one site                           #
    ############################################################################
    p21 = _p21
    add_2_1 = _add_2_1
    remove_2_1 = _remove_2_1

    ############################################################################
    #                           Two spins & two sites                          #
    ############################################################################
    p22 = _p22
    add_2_2 = _add_2_2
    remove_2_2 = _remove_2_2

    ############################################################################
    #                          Three spins & one site                          #
    ############################################################################
    p31 = _p31
    add_3_1 = _add_3_1
    remove_3_1 = _remove_3_1

    ############################################################################
    #                          Three spins & two sites                         #
    ############################################################################
    p32 = _p32
    add_3_2 = _add_3_2
    remove_3_2 = _remove_3_2

    ############################################################################
    #                           Four spins & one site                          #
    ############################################################################
    p41 = _p41
    add_4_1 = _add_4_1
    remove_4_1 = _remove_4_1


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
