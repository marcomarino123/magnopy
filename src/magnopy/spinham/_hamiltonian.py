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

from magnopy.spinham._notation import Notation

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def _validate_index(index, atoms) -> None:
    r"""
    Validate that the atom index is in agreement with the amount of atoms

    Parameter
    ---------
    index
        Potential index of an atom.
    atoms : dict
        Dictionary with the atoms. This function relies on ``atoms["names"]``.

    Raises
    ------
    TypeError
        If ``index`` is not an integer.
    ValueError
        If ``index`` is out of range.
    """

    if not isinstance(index, int):
        raise TypeError(
            f"Only integers are supported as atom indices, "
            f"got '{type(index)}' from '{index}'"
        )

    if not 0 <= index < len(atoms["names"]):
        raise ValueError(
            "Index should be greater or equal to 0 and less than "
            f"{len(atoms['names'])}', got {index}."
        )


def _validate_ijk(ijk) -> None:
    r"""
    Validate that ijk can specify unit cell.

    Parameters
    ----------
    ijk
        Potential index of the unit cell.

    Raises
    ------
    TypeError
        If ``ijk`` is not a ``tuple``.
    TypeError
        If either ``i``, ``j`` or ``k`` is not an ``int``.
    """

    if not isinstance(ijk, tuple):
        raise TypeError(f"Unit cell index has to be a tuple, got '{type(ijk)}'")

    if not isinstance(ijk[0], int):
        raise TypeError(
            f"First element of the unit cell index is not an 'int', got "
            f"{type(ijk[0])} from '{ijk[0]}'"
        )

    if not isinstance(ijk[1], int):
        raise TypeError(
            f"Second element of the unit cell index is not an 'int', got "
            f"{type(ijk[1])} from '{ijk[1]}'"
        )

    if not isinstance(ijk[2], int):
        raise TypeError(
            f"Third element of the unit cell index is not an 'int', got "
            f"{type(ijk[2])} from '{ijk[2]}'"
        )


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

    ################################################################################
    #                              One spin & one site                             #
    ################################################################################

    @property
    def p1(self) -> list:
        r"""
        Parameters of (one spin & one site) term of the Hamiltonian.

        Returns
        -------
        parameters : list
            List of parameters. Length of the list is between zero and amount of atoms
            in ``spinham.atoms``. The list has a format of

            .. code-block:: python

                [[i, A], ...]

            where ``i`` is an index of the atom to which the parameter is assigned and
            ``A`` is a (3, ) :numpy:`ndarray`. The parameters are sorted in the
            ascending order by the index of an atom ``i``.

        See Also
        --------
        add_1
        remove_1

        Notes
        -----
        Parameters :math:`\boldsymbol{J}_1(\boldsymbol{r}_{\alpha})` of the term

        .. math::

            C_1
            \sum_{\substack{\mu, \\ \alpha \\ k}}
            J_1^k(\boldsymbol{r}_{\alpha})
            S_{\mu,\alpha}^k
        """

        return self._1

    def add_1(self, atom: int, parameter, replace=False) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i. e. ``0 <= atom < len(spinham.atoms.names)``.
        parameter : (3, ) |array-like|_
            Vector of a parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p1
        remove_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        parameter = np.array(parameter)

        # TODO Replace with binary search
        # Try to find the place for the new one inside the list
        index = 0
        while index < len(self._1):
            # If already present in the model
            if self._1[index][0] == atom:
                # Either replace
                if replace:
                    self._1[index] = [atom, parameter]
                    return
                # Or raise an error
                raise ValueError(
                    f"(One spin & one site) parameter is already set "
                    f"for atom {atom} ('{self.atoms.names[atom]}')"
                )

            # If it should be inserted before current element
            if self._1[index][0] > atom:
                self._1.insert(index, [atom, parameter])
                return

            index += 1

        # If it should be inserted at the end or at the beginning of the list
        self._1.append([atom, parameter])

    def remove_1(self, atom: int) -> None:
        r"""
        Remove a parameter from the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i. e. ``0 <= atom < len(spinham.atoms.names)``.

        See Also
        --------
        p1
        add_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        for i in range(len(self._1)):
            # As the list is sorted, there is no point in resuming the search
            # when a larger element is found
            if self._1[i][0] > atom:
                return

            if self._1[i][0] == atom:
                del self._1[i]
                return

    ################################################################################
    #                             Two spins & one site                             #
    ################################################################################

    @property
    def p21(self) -> list:
        r"""
        Parameters of (two spins & one site) term of the Hamiltonian.

        Returns
        -------
        parameters : list
            List of parameters. Length of the list is between zero and amount of atoms
            in ``spinham.atoms``. The list has a format of

            .. code-block:: python

                [[i, A], ...]

            where ``i`` is an index of the atom to which the parameter is assigned and
            ``A`` is a (3, 3) :numpy:`ndarray`. The parameters are sorted in the
            ascending order by the index of an atom ``i``.

        See Also
        --------
        add_2_1
        remove_2_1

        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{2,1}(\boldsymbol{r}_{\alpha})` of the term

        .. math::

            C_{2,1}
            \sum_{\substack{\mu, \\ \alpha, \\ k,l}}
            J^{kl}_{2,1}(\boldsymbol{r}_{\alpha})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
        """

        return self._2_1

    def add_2_1(self, atom: int, parameter, replace=False) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i. e. ``0 <= atom < len(spinham.atoms.names)``.
        parameter : (3, 3) |array-like|_
            Full matrix of the parameter. It should be symmetric, but magnopy do not
            check for it.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p21
        remove_2_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        parameter = np.array(parameter)

        # TODO Replace with binary search
        # Try to find the place for the new one inside the list
        index = 0
        while index < len(self._2_1):
            # If already present in the model
            if self._2_1[index][0] == atom:
                # Either replace
                if replace:
                    self._2_1[index] = [atom, parameter]
                    return
                # Or raise an error
                raise ValueError(
                    f"On-site quadratic anisotropy already set "
                    f"for atom {atom} ('{self.atoms.names[atom]}')"
                )

            # If it should be inserted before current element
            if self._2_1[index][0] > atom:
                self._2_1.insert(index, [atom, parameter])
                return

            index += 1

        # If it should be inserted at the end or at the beginning of the list
        self._2_1.append([atom, parameter])

    def remove_2_1(self, atom: int) -> None:
        r"""
        Remove a parameter from the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i. e. ``0 <= atom < len(spinham.atoms.names)``.

        See Also
        --------
        p21
        add_2_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        for i in range(len(self._2_1)):
            # As the list is sorted, there is no point in resuming the search
            # when a larger element is found
            if self._2_1[i][0] > atom:
                return

            if self._2_1[i][0] == atom:
                del self._2_1[i]
                return

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

    ################################################################################
    #                            Three spins & one site                            #
    ################################################################################

    @property
    def p31(self):
        r"""
        Parameters of (three spins & one site) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i, J], ...]

            where ``i`` is an index of the atom from (0,0,0) unit cell ``J`` is a
            (3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_3_1
        remove_3_1


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{3, 1}(\boldsymbol{r}_{\alpha})` of the term

        .. math::

            C_{3, 1}
            \sum_{\substack{\mu, \\ \alpha, \\ k,l,i}}
            J_{3, 1}^{kli}(\boldsymbol{r}_{\alpha})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu,\alpha}^i
        """

        raise NotImplementedError

    def add_3_1(self, atom: int, parameter, replace=False) -> None:
        r"""
        Adds a parameter to the Hamiltonian.


        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        parameter : (3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p31
        remove_3_1
        """

        _validate_index(index=atom, atoms=self.atoms)
        parameter = np.array(parameter)

        raise NotImplementedError

    def remove_3_1(self, atom: int) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom < len(spinham.atoms.names)``.

        See Also
        --------
        p31
        add_3_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        raise NotImplementedError

    ################################################################################
    #                            Three spins & two sites                           #
    ################################################################################

    @property
    def p32(self):
        r"""
        Parameters of (three spins & two sites) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, ijk, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i, j, k) unit cell; ``ijk`` defines (i, j, k) unit
            cell; ``J`` is a (3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_3_2
        remove_3_2


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{3, 2}(\boldsymbol{r}_{\nu,\alpha\beta})` of
        the term

        .. math::

            C_{3, 2}
            \sum_{\substack{\mu,\nu, \\ \alpha,\beta, \\ k,l,i}}
            J_{3, 2}^{kli}(\boldsymbol{r}_{\nu,\alpha\beta})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu+\nu,\beta}^i
        """

        raise NotImplementedError

    def add_3_2(
        self, atom1: int, atom2: int, ijk2: tuple, parameter, replace=False
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

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
        parameter : (3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p32
        remove_3_2

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        parameter = np.array(parameter)

        raise NotImplementedError

    def remove_3_2(self, atom1: int, atom2: int, ijk2: tuple) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

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
        p32
        add_3_2

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)

        raise NotImplementedError

    ################################################################################
    #                           Three spins & three sites                          #
    ################################################################################

    @property
    def p33(self):
        r"""
        Parameters of (three spins & three sites) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, i3, ijk2, ijk3, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i2, j2, k2) unit cell; ``i3`` is an
            index of the atom from (i3, j3, k3) unit cell; ``ijk2`` defines (i2, j2, k2)
            unit cell; ``ijk3`` defines (i3, j3, k3) unit cell; ``J`` is a (3, 3, 3)
            :numpy:`ndarray`.

        See Also
        --------
        add_3_3
        remove_3_3


        Notes
        -----
        Parameters
        :math:`\boldsymbol{J}_{3, 3}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})`
        of the term

        .. math::

            C_{3, 3}
            \sum_{\substack{\mu,\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i}}
            J_{3, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
            S_{\mu,\alpha}^k
            S_{\mu+\nu,\beta}^l
            S_{\mu+\lambda,\gamma}^i
        """

        raise NotImplementedError

    def add_3_3(
        self,
        atom1: int,
        atom2: int,
        atom3: int,
        ijk2: tuple,
        ijk3: tuple,
        parameter,
        replace=False,
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.
        parameter : (3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p33
        remove_3_3

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)

        raise NotImplementedError

    def remove_3_3(
        self, atom1: int, atom2: int, atom3: int, ijk2: tuple, ijk3: tuple
    ) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.

        See Also
        --------
        p33
        add_3_3

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)

        raise NotImplementedError

    ################################################################################
    #                             Four spins & one site                            #
    ################################################################################

    @property
    def p41(self):
        r"""
        Parameters of (four spins & one site) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i, J], ...]

            where ``i`` is an index of the atom from (0,0,0) unit cell ``J`` is a
            (3, 3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_4_1
        remove_4_1


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{4, 1}(\boldsymbol{r}_{\alpha})` of the term

        .. math::

            C_{4, 1}
            \sum_{\substack{\mu, \\ \alpha, \\ k,l,i,j}}
            J_{4, 1}^{kli}(\boldsymbol{r}_{\alpha})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu,\alpha}^i
            S_{\mu,\alpha}^j
        """

        raise NotImplementedError

    def add_4_1(self, atom: int, parameter, replace=False) -> None:
        r"""
        Adds a parameter to the Hamiltonian.


        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        parameter : (3, 3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p41
        remove_4_1
        """

        _validate_index(index=atom, atoms=self.atoms)
        parameter = np.array(parameter)

        raise NotImplementedError

    def remove_4_1(self, atom: int) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        Parameters
        ----------
        atom : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom < len(spinham.atoms.names)``.

        See Also
        --------
        p41
        add_4_1
        """

        _validate_index(index=atom, atoms=self.atoms)

        raise NotImplementedError

    ################################################################################
    #                         Four spins & two sites (1+3)                         #
    ################################################################################

    @property
    def p421(self):
        r"""
        Parameters of (four spins & two sites (1+3)) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, ijk, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i, j, k) unit cell; ``ijk`` defines (i, j, k) unit
            cell; ``J`` is a (3, 3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_4_2_1
        remove_4_2_1


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{4, 2, 1}(\boldsymbol{r}_{\nu,\alpha\beta})` of
        the term

        .. math::

            C_{4, 2, 1}
            \sum_{\substack{\mu,\nu, \\ \alpha,\beta, \\ k,l,i,j}}
            J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu,\alpha}^i
            S_{\mu+\nu,\beta}^j
        """

        raise NotImplementedError

    def add_4_2_1(
        self, atom1: int, atom2: int, ijk2: tuple, parameter, replace=False
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

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
        parameter : (3, 3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p421
        remove_4_2_1

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        parameter = np.array(parameter)

        raise NotImplementedError

    def remove_4_2_1(self, atom1: int, atom2: int, ijk2: tuple) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

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
        p421
        add_4_2_1

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)

        raise NotImplementedError

    ################################################################################
    #                         Four spins & two sites (2+2)                         #
    ################################################################################

    @property
    def p422(self):
        r"""
        Parameters of (four spins & two sites (2+2)) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, ijk, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i, j, k) unit cell; ``ijk`` defines (i, j, k) unit
            cell; ``J`` is a (3, 3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_4_2_2
        remove_4_2_2


        Notes
        -----
        Parameters :math:`\boldsymbol{J}_{4, 2, 2}(\boldsymbol{r}_{\nu,\alpha\beta})` of
        the term

        .. math::

            C_{4, 2, 2}
            \sum_{\substack{\mu,\nu, \\ \alpha,\beta, \\ k,l,i,j}}
            J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu+\nu,\beta}^i
            S_{\mu+\nu,\beta}^j
        """

        raise NotImplementedError

    def add_4_2_2(
        self, atom1: int, atom2: int, ijk2: tuple, parameter, replace=False
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

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
        parameter : (3, 3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p422
        remove_4_2_2

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        parameter = np.array(parameter)

        raise NotImplementedError

    def remove_4_2_2(self, atom1: int, atom2: int, ijk2: tuple) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

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
        p422
        add_4_2_2

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)

        raise NotImplementedError

    ################################################################################
    #                           Four spins & three sites                           #
    ################################################################################

    @property
    def p43(self):
        r"""
        Parameters of (four spins & three sites) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, i3, ijk2, ijk3, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i2, j2, k2) unit cell; ``i3`` is an
            index of the atom from (i3, j3, k3) unit cell; ``ijk2`` defines (i2, j2, k2)
            unit cell; ``ijk3`` defines (i3, j3, k3) unit cell; ``J`` is a (3, 3, 3, 3)
            :numpy:`ndarray`.

        See Also
        --------
        add_4_3
        remove_4_3


        Notes
        -----
        Parameters
        :math:`\boldsymbol{J}_{4, 3}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})`
        of the term

        .. math::

            C_{4, 3}
            \sum_{\substack{\mu,\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
            J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
            S_{\mu,\alpha}^k
            S_{\mu,\alpha}^l
            S_{\mu+\nu,\beta}^i
            S_{\mu+\lambda,\gamma}^j
        """

        raise NotImplementedError

    def add_4_3(
        self,
        atom1: int,
        atom2: int,
        atom3: int,
        ijk2: tuple,
        ijk3: tuple,
        parameter,
        replace=False,
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.
        parameter : (3, 3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p43
        remove_4_3

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)

        raise NotImplementedError

    def remove_4_3(
        self, atom1: int, atom2: int, atom3: int, ijk2: tuple, ijk3: tuple
    ) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.

        See Also
        --------
        p43
        add_4_3

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)

        raise NotImplementedError

    ################################################################################
    #                            Four spins & four sites                           #
    ################################################################################

    @property
    def p44(self):
        r"""
        Parameters of (four spins & four sites) term of the Hamiltonian.

        Returns
        -------
        parameters : iterator
            List of parameters. The list has a format of

            .. code-block:: python

                [[i1, i2, i3, i4, ijk2, ijk3, ijk4, J], ...]

            where ``i1`` is an index of the atom from (0,0,0) unit cell; ``i2`` is an
            index of the atom from (i2, j2, k2) unit cell; ``i3`` is an
            index of the atom from (i3, j3, k3) unit cell; ``ijk2`` defines (i2, j2, k2)
            unit cell; ``ijk3`` defines (i3, j3, k3) unit cell; ``ijk4`` defines (i4,
            j4, k4) unit cell; ``J`` is a (3, 3, 3, 3) :numpy:`ndarray`.

        See Also
        --------
        add_4_4
        remove_4_4


        Notes
        -----
        Parameters
        :math:`\boldsymbol{J}_{4, 4}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})`
        of the term

        .. math::

            C_{4, 4}
            \sum_{\substack{\mu,\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
            J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
            S_{\mu,\alpha}^k
            S_{\mu+\nu,\beta}^l
            S_{\mu+\lambda,\gamma}^i
            S_{\mu+\rho,\varepsilon}^j
        """

        raise NotImplementedError

    def add_4_4(
        self,
        atom1: int,
        atom2: int,
        atom3: int,
        atom4: int,
        ijk2: tuple,
        ijk3: tuple,
        ijk4: tuple,
        parameter,
        replace=False,
    ) -> None:
        r"""
        Adds a parameter to the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        atom4 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom4 < len(spinham.atoms.names)``. Specifies atom from
            (i4, j4, k4) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.
        ijk4 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the fourth atom.
        parameter : (3, 3, 3, 3) |array-like|_
            Full matrix of the parameter.
        replace : bool, default False
            Whether to replace the parameter if it is already present in the Hamiltonian.

        See Also
        --------
        p44
        remove_4_4

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_index(index=atom4, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)
        _validate_ijk(ijk=ijk4)

        raise NotImplementedError

    def remove_4_4(
        self,
        atom1: int,
        atom2: int,
        atom3: int,
        atom4: int,
        ijk2: tuple,
        ijk3: tuple,
        ijk4: tuple,
    ) -> None:
        r"""
        Removes a parameter from the Hamiltonian.

        TODO

        Parameters
        ----------
        atom1 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom1 < len(spinham.atoms.names)``. Specifies atom from
            (0, 0, 0) unit cell
        atom2 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom2 < len(spinham.atoms.names)``. Specifies atom from
            (i2, j2, k2) unit cell
        atom3 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom3 < len(spinham.atoms.names)``. Specifies atom from
            (i3, j3, k3) unit cell
        atom4 : int
            Atom index, that should be consistent with the amount of ``spinham.atoms``,
            i.e. ``0 <= atom4 < len(spinham.atoms.names)``. Specifies atom from
            (i4, j4, k4) unit cell
        ijk2 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the second atom.
        ijk3 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the third atom.
        ijk4 : tuple of 3 int
            Three indices along three lattice vectors, that specify the unit cell of
            the fourth atom.

        See Also
        --------
        p44
        add_4_4

        Notes
        -----
        TODO
        """

        _validate_index(index=atom1, atoms=self.atoms)
        _validate_index(index=atom2, atoms=self.atoms)
        _validate_index(index=atom3, atoms=self.atoms)
        _validate_index(index=atom4, atoms=self.atoms)
        _validate_ijk(ijk=ijk2)
        _validate_ijk(ijk=ijk3)
        _validate_ijk(ijk=ijk4)

        raise NotImplementedError

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

        # If factor is changing one need to scale parameters.
        for index in range(len(self._1)):
            self._1[index][1] = self._1[index][1] * self.notation.c1 / new_c1

    def _set_c21(self, new_c21: float) -> None:
        if new_c21 is None or self.notation._c21 is None:
            return

        new_c21 = float(new_c21)

        if self.notation.c21 == new_c21:
            return

        # If factor is changing one need to scale parameters.
        for index in range(len(self._2_1)):
            self._2_1[index][1] = self._2_1[index][1] * self.notation.c21 / new_c21

    def _set_c22(self, new_c22: float) -> None:
        if new_c22 is None or self.notation._c22 is None:
            return

        new_c22 = float(new_c22)

        if self.notation.c22 == new_c22:
            return

        # If factor is changing one need to scale parameters.
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
    #                          Magnetic atoms in unit cell                         #
    ################################################################################
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
            Indices of magnetic atoms in the ``spinham.atoms``.

        See Also
        --------
        M
        """
        indices = set()

        for atom, _ in self._2_1:
            indices.add(atom)

        for atom1, atom2, _, _ in self._2_2:
            indices.add(atom1)
            indices.add(atom2)

        return list(indices)

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

        return len(self.magnetic_atoms)

    ################################################################################
    #                                    Filters                                   #
    ################################################################################
    def filter_2_2(
        self, max_distance=None, min_distance=None, custom_filter=None
    ) -> None:
        r"""
        Filter the (two spins; two sites) parameters based on the given conditions.


        Parameters
        ----------
        max_distance : float or int, optional
            Distance for sorting, the condition to keep the bond is :math:`\le`.
        min_distance : float or int, optional
            Distance for sorting, the condition to keep the bond is :math:`\ge`.
        custom_filter : function, optional
            Custom function, that returns ``bool``. If it returns ``True``, then the
            bond is removed from the Hamiltonian. The call signature to the function is
            ``custom_filter(parameter)`` where ``parameter`` is a :math:`3 \times 3`
            matrix.


        Notes
        -----
        The result is defined by logical conjugate of the conditions. Saying so, the
        bond is kept in the Hamiltonian if all given conditions are satisfied for it.

        Examples
        --------

        .. doctest::

            >>> import numpy as np
            >>> import magnopy
            >>> cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            >>> atoms = {"names" : ["Cr1", "Cr2"], "positions" : [[0, 0, 0], [0.5, 0.5, 0.5]]}
            >>> J = np.eye(3)
            >>> notation = magnopy.spinham.Notation(False, False, c22=1)
            >>> spinham = magnopy.spinham.SpinHamiltonian(cell, atoms, notation)
            >>> spinham.add_2_2(atom1=0, atom2=0, ijk2=(2,0,0), parameter=J)
            >>> spinham.add_2_2(atom1=0, atom2=1, ijk2=(0,0,0), parameter=2*J)
            >>> spinham.add_2_2(atom1=1, atom2=0, ijk2=(0,1,1), parameter=3*J)
            >>> spinham.filter_2_2(custom_filter = lambda x: np.trace(x) > 8)
            >>> for atom1, atom2, ijk, _ in spinham.p22:
            ...     print(atom1, atom2, ijk)
            ...
            0 0 (2, 0, 0)
            0 1 (0, 0, 0)
            >>> spinham.filter_2_2(max_distance = 1)
            >>> for atom1, atom2, ijk, _ in spinham.p22:
            ...     print(atom1, atom2, ijk)
            ...
            0 1 (0, 0, 0)
        """

        for index in range(len(self._2_2) - 1, -1, -1):
            atom1 = self._2_2[index][0]
            atom2 = self._2_2[index][1]
            ijk2 = self._2_2[index][2]

            dis = get_distance(
                cell=self.cell, atoms=self.atoms, atom1=atom1, atom2=atom2, R=ijk2
            )

            remove_bond = False
            if max_distance is not None:
                remove_bond = remove_bond or dis > max_distance

            if min_distance is not None:
                remove_bond = remove_bond or dis < min_distance

            if custom_filter is not None:
                remove_bond = remove_bond or custom_filter(self._2_2[index][3])

            if remove_bond:
                self.remove_2_2(atom1=atom1, atom2=atom2, ijk2=ijk2)

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
