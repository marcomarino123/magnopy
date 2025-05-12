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
from magnopy.spinham._c21 import _add_21, _p21, _remove_21
from magnopy.spinham._notation import Notation
from magnopy.spinham._validators import _validate_ijk, _validate_index

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def _get_P22_prime(atom1, atom2, ijk, parameter=None):
    r"""
    Return the parameter with the properties:

    * i > 0
    * if i == 0, j > 0
    * if i == 0 and j == 0, k > 0
    * if i == 0 and j == 0 and k == 0, atom1 < atom2

    Parameters
    ----------
    atom1 : int
        Index of the first atom.
    atom2 : int
        Index of the second atom.
    ijk : tuple of 3 int
        Unit cell for the second atom.
    parameter : (3, 3) :numpy:`ndarray`, optional
        Full matrix of the parameter.

    Returns
    -------
    atom1 : int
        Index of the first atom.
    atom2 : int
        Index of the second atom.
    ijk : tuple of 3 int
        Unit cell for the second atom.
    parameter : (3, 3) :numpy:`ndarray`
        Full matrix of the parameter. Returnes if ``parameter`` is not ``None``.
    """

    i, j, k = ijk

    if (
        i < 0
        or (i == 0 and j < 0)
        or (i == 0 and j == 0 and k < 0)
        or (i == 0 and j == 0 and k == 0 and atom1 > atom2)
    ):
        if parameter is None:
            return atom2, atom1, (-i, -j, -k)
        return atom2, atom1, (-i, -j, -k), parameter.T

    if parameter is None:
        return atom1, atom2, ijk
    return atom1, atom2, ijk, parameter


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

        # [[atom, parameter], ...]
        self._1 = []

        # [[atom, parameter], ...]
        self._2_1 = []

        # [[atom1, atom2, ijk2, parameter], ...]
        self._2_2 = []

        # [[atom, parameter], ...]
        self._3_1 = []

        # [[atom1, atom2, ijk2, parameter], ...]
        self._3_2 = []

        # [[atom1, atom2, atom3, ijk2, ijk3, parameter], ...]
        self._3_3 = []

        # [[atom, parameter], ...]
        self._4_1 = []

        # [[atom1, atom2, ijk2, parameter], ...]
        self._4_2_1 = []

        # [[atom1, atom2, ijk2, parameter], ...]
        self._4_2_2 = []

        # [[atom1, atom2, atom3, ijk2, ijk3, parameter], ...]
        self._4_3 = []

        # [[atom1, atom2, atom3, atom4, ijk2, ijk3, ijk4, parameter], ...]
        self._4_4 = []

    ################################################################################
    #                                Cell and Atoms                                #
    ################################################################################

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

        for atom, _ in self._1:
            indices.add(atom)

        for atom, _ in self._2_1:
            indices.add(atom)

        for atom1, atom2, _, _ in self._2_2:
            indices.add(atom1)
            indices.add(atom2)

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

    ################################################################################
    #                  Manipulations with the underlying structure                 #
    ################################################################################
    def remove_atom(self, atom_index=None, atom_name=None) -> None:
        r"""
        Remove an atom from the crystal structure and all parameters that are associated
        with it.

        Parameters
        ----------
        atom_index : int, optional
            Index of an atom to be removed.
        atom_name : str, optional
            Name of the atom to be removed. If several atoms have the same name, then
            **all** of them are removed.

        Notes
        -----
        If both ``atom_index`` and ``atom_name`` are given, then atom with the matching
        index **and** all atoms with the matching name are removed.

        Examples
        --------

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            >>> atoms = {"names" : ["Cr1", "Cr2"]}
            >>> A = np.array([[1,0,0], [0,0,0], [0,0,0]])
            >>> notation = magnopy.spinham.Notation(False, False, c22=1)
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell, atoms, notation)
            >>> spinham.add_2_1(atom=0, parameter=A)
            >>> spinham.add_2_1(atom=1, parameter=2*A)
            >>> spinham.remove_atom(atom_name="Cr1")
            >>> spinham.atoms
            {'names': ['Cr2']}
            >>> for a, parameter in spinham.p21:
            ...    print(a)
            ...    print(parameter)
            ...
            0
            [[2 0 0]
             [0 0 0]
             [0 0 0]]
            >>> spinham.remove_atom(atom_index = 0)
            >>> spinham.atoms
            {'names': []}
            >>> len(spinham.p21)
            0

        """

        # After removing of atoms the indices in the parameters should change
        # Therefore, first we compute new indices and indices of the atoms to remove
        removed_atoms = set()
        new_indices = {}
        new_i = 0
        for i in range(len(self.atoms.names)):
            if atom_index is not None and atom_index == i:
                removed_atoms.add(i)
            elif atom_name is not None and self.atoms.names[i] == atom_name:
                removed_atoms.add(i)
            else:
                new_indices[i] = new_i
                new_i += 1

        # Then we remove atoms
        for index in sorted(removed_atoms, reverse=True):
            for key in self.atoms:
                del self.atoms.names[index]

        # Then we remove on-site terms and update indices of the on-site parameters
        for index in range(len(self._2_1) - 1, -1, -1):
            atom = self._2_1[index][0]

            if atom in removed_atoms:
                del self._2_1[index]
            else:
                self._2_1[index][0] = new_indices[atom]

        # Finally, we remove and update indices of the exchange parameters
        for index in range(len(self._2_2) - 1, -1, -1):
            atom1 = self._2_2[index][0]
            atom2 = self._2_2[index][1]

            if atom1 in removed_atoms or atom2 in removed_atoms:
                del self._2_2[index]
            else:
                self._2_2[index][0] = new_indices[atom1]
                self._2_2[index][1] = new_indices[atom2]

        # TODO take care of the rest of the terms

        self._reset_internals()

    ################################################################################
    #                             Notation properties                              #
    ################################################################################
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
                atom = self._1[index][0]
                self._1[index][1] = self._1[index][1] * self.atoms.spins[atom]
            # For (two spins & one site)
            for index in range(len(self._2_1)):
                atom = self._2_1[index][0]
                self._2_1[index][1] = self._2_1[index][1] * self.atoms.spins[atom] ** 2
            # For (two spins & two sites)
            for index in range(len(self._2_2)):
                atom1 = self._2_2[index][0]
                atom2 = self._2_2[index][1]
                self._2_2[index][3] = self._2_2[index][3] * (
                    self.atoms.spins[atom1] * self.atoms.spins[atom2]
                )
        # Before it was normalized
        else:
            # For (one spin & one site)
            for index in range(len(self._1)):
                atom = self._1[index][0]
                self._1[index][1] = self._1[index][1] / self.atoms.spins[atom]
            # For (two spins & one site)
            for index in range(len(self._2_1)):
                atom = self._2_1[index][0]
                self._2_1[index][1] = self._2_1[index][1] / self.atoms.spins[atom] ** 2
            # For (two spins & two sites)
            for index in range(len(self._2_2)):
                atom1 = self._2_2[index][0]
                atom2 = self._2_2[index][1]
                self._2_2[index][3] = self._2_2[index][3] / (
                    self.atoms.spins[atom1] * self.atoms.spins[atom2]
                )

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

        raise NotImplementedError

    def _set_c32(self, new_c32: float) -> None:
        if new_c32 is None or self.notation._c32 is None:
            return

        new_c32 = float(new_c32)

        if self.notation.c32 == new_c32:
            return

        raise NotImplementedError

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

        raise NotImplementedError

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

    ################################################################################
    #                                  Copy getter                                 #
    ################################################################################
    def copy(self):
        R"""
        Returns a new, independent copy of the same Hamiltonian.

        Returns
        -------
        spinham : :py:class:`.SpinHamiltonian`
            A new instance of the same Hamiltonian.
        """

        return deepcopy(self)

    ################################################################################
    #                              One spin & one site                             #
    ################################################################################
    p1 = _p1
    add_1 = _add_1
    remove_1 = _remove_1

    ################################################################################
    #                             Two spins & one site                             #
    ################################################################################
    p21 = _p21
    add_2_1 = _add_21
    remove_2_1 = _remove_21

    ################################################################################
    #                             Two spins & two sites                            #
    ################################################################################

    @property
    def p22(self):
        r"""
        Parameters of (two spins & two sites) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, ijk, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i, j, k) unit cell; ``ijk`` defines (i, j, k) unit
            cell; ``J`` is a (3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_2_2
        remove_2_2


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{2,2}(\boldsymbol{r}_{\nu,\alpha\beta})` of the term

        .. math::

            C_{2,2}
            \sum_{\substack{\mu,\nu, \\ \alpha, \beta, \\ k,l}}
            J^{kl}_{2,2}(\boldsymbol{r}_{\nu,\alpha\beta})
            S_{\mu,\alpha}^k
            S_{\mu+\nu,\beta}^l
        """

        return _P22_iterator(self)

    def add_2_2(
        self, atom1: int, atom2: int, ijk2: tuple, parameter, replace=False
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        Doubles of the bonds are managed automatically (independently of the notation
        of the Hamiltonian). ``atom2, atom1, (-i, -j, -k), parameter.T`` is a double
        of ``atom1, atom2, (i, j, k), parameter``.

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``.Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``.Specifies atom from
            (i, j, k) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        parameter : (3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p22
        remove_2_2

        Notes
        -----
        If ``spinham.notation.multiple_counting`` is ``True``, then this function adds both
        the bond and its double to the Hamiltonian. It will cause an ``ValueError`` to
        add the double of the bond after the bond is added.

        If ``spinham.notation.multiple_counting`` is ``False``, then only the "prime"
        version of the bond is added to the Hamiltonian. Out of the bond and its double
        magnopy keep the one that satisfies one of the following

        * i > 0
        * if i == 0, j > 0
        * if i == 0 and j == 0, k > 0
        * if i == 0 and j == 0 and k == 0, atom1 < atom2
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        self._reset_internals()

        parameter = np.array(parameter)

        atom1, atom2, (i, j, k), parameter = _get_P22_prime(
            atom1=atom1, atom2=atom2, ijk=ijk2, parameter=parameter
        )

        # TODO Replace with binary search

        # Try to find the place for the new one inside the list
        index = 0
        while index < len(self._2_2):
            # If already present in the model
            if (self._2_2[index][0], self._2_2[index][1], self._2_2[index][2]) == (
                atom1,
                atom2,
                (i, j, k),
            ):
                # Either replace
                if replace:
                    self._2_2[index] = [atom1, atom2, (i, j, k), parameter]
                    return
                # Or raise an error
                raise ValueError(
                    f"Exchange like parameter is already set for the pair of atoms "
                    f"{atom1} and {atom2} ({i}, {j}, {k}). Or for their double bond."
                )

            # If it should be inserted before current element
            if (self._2_2[index][0], self._2_2[index][1], self._2_2[index][2]) > (
                atom1,
                atom2,
                (i, j, k),
            ):
                self._2_2.insert(index, [atom1, atom2, (i, j, k), parameter])
                return

            index += 1

        # If it should be inserted at the end or at the beginning of the list
        self._2_2.append([atom1, atom2, (i, j, k), parameter])

    def remove_2_2(self, atom1: int, atom2: int, ijk2: tuple) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        Doubles of the bonds are managed automatically (independently of the notation
        of the Hamiltonian). ``atom2, atom1, (-i, -j, -k), parameter.T`` is a double
        of ``atom1, atom2, (i, j, k), parameter``.

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i, j, k) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.

        See Also
        --------
        p22
        add_2_2

        Notes
        -----
        If ``spinham.notation.multiple_counting`` is ``True``, then this function removes
        both the bond and its double from the Hamiltonian.

        If ``spinham.notation.multiple_counting`` is ``False``, then this function removes
        the "prime" version of the provided bond. Out of the bond and its double
        magnopy keep the one that satisfies one of the following

        * i > 0
        * if i == 0, j > 0
        * if i == 0 and j == 0, k > 0
        * if i == 0 and j == 0 and k == 0, atom1 < atom2

        For instance, if ``(1, 0, (0, 0, 0))`` is provided, then this function attempts to
        remove either both ``(1, 0, (0, 0, 0))`` and ``(0, 1, (0, 0, 0))`` if
        ``spinham.notation.multiple_counting == True`` or the prime version
        ``(0, 1, (0, 0, 0))`` if ``spinham.notation.multiple_counting == False``.
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        self._reset_internals()

        atom1, atom2, (i, j, k) = _get_P22_prime(atom1=atom1, atom2=atom2, ijk=ijk2)

        # TODO Replace with binary search

        for index in range(len(self._2_2)):
            # As the list is sorted, there is no point in resuming the search
            # when a larger element is found
            if (self._2_2[index][0], self._2_2[index][1], self._2_2[index][2]) > (
                atom1,
                atom2,
                (i, j, k),
            ):
                return

            if (self._2_2[index][0], self._2_2[index][1], self._2_2[index][2]) == (
                atom1,
                atom2,
                (i, j, k),
            ):
                del self._2_2[index]
                return


class _P22_iterator:
    R"""
    Iterator over the (two spins & two sites) parameters of the spin Hamiltonian.
    """

    def __init__(self, spinham) -> None:
        self.container = spinham._2_2
        self.dc = spinham.notation.multiple_counting
        self.length = len(self.container)
        self.index = 0

    def __next__(self):
        if self.index < self.length:
            self.index += 1
            return self.container[self.index - 1]

        elif self.dc and self.index < 2 * self.length:
            atom1, atom2, (i, j, k), parameter = self.container[
                2 * self.length - self.index - 1
            ]
            self.index += 1
            return [atom2, atom1, (-i, -j, -k), parameter.T]

        raise StopIteration

    def __len__(self):
        return self.length * (1 + int(self.dc))

    def __iter__(self):
        return self


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
