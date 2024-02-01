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

__all__ = ["SpinHamiltonian", "PREDEFINED_NOTATIONS"]

from copy import deepcopy
from typing import Iterable, Tuple

import numpy as np
from wulfric import Atom, Crystal

from magnopy.exceptions import NotationError
from magnopy.spinham.parameter import MatrixParameter

PREDEFINED_NOTATIONS = {
    "magnopy": (True, False, 0.5, 1),
    "tb2j": (True, True, -1, -1),
    "spinw": (True, False, 1, 1),
    "vampire": (True, True, -0.5, -1),
}


class SpinHamiltonian(Crystal):
    r"""
    Spin Hamiltonian.

    By default the notation of the spin Hamiltonian is not defined
    and could be one of many, depending on the context.
    However, in could always be checked via :py:attr:`.notation`.
    In user-specific cases it is the responsibility of the user to
    set the interpretation of the Hamiltonian`s notation.

    For the predefined notations see :py:meth:`.notation`.

    Child of the :py:class:`.Crystal` class.

    Parameters
    ----------
    crystal : :py:class:`.Crystal`, optional
        Crystal on which the spin Hamiltonian is build.
        By default it is cubic (:math:`a=1`) lattice with no atoms.
    notation : str or tuple of two bool and one float, optional
        One of the predefined notations or tuple with custom notation.
        See :py:attr:`.notation` for details. #TODO
    **kwargs
        Keyword arguments for the :py:class:`.Crystal` constructor.

    """

    def __init__(self, crystal: Crystal = None, notation=None, **kwargs) -> None:
        if crystal is not None:
            kwargs["atoms"] = crystal.atoms
            kwargs["cell"] = crystal.cell

        super().__init__(**kwargs)

        self._bonds = {}
        self._spiral_vector = None
        self._cone_axis = None

        # Notation settings
        self._double_counting = None
        self._spin_normalized = None
        self._exchange_factor = None
        self._on_site_factor = None
        if notation is not None:
            self.notation = notation

    def __len__(self):
        return self._bonds.__len__()

    @property
    def spiral_vector(self):
        R"""
        Spin spiral vector of the spiral ground state.
        In relative coordinates, with respect to the reciprocal cell.

        Returns
        =======
        spiral_vector : (3,) :numpy:`ndarray`
            Spiral vector :math:`\boldsymbol{q}`.
        """

        return self._spiral_vector

    @spiral_vector.setter
    def spiral_vector(self, new_vector):
        try:
            new_vector = np.array(new_vector, dtype=float)
        except:
            raise ValueError(f"New spiral vector is not array-like: {new_vector}")

        if new_vector.shape != (3,):
            raise ValueError(
                f"New spiral vector has to be a 3 component vector, got {new_vector.setflagshape}"
            )

        self._cone_axis = new_vector

    @property
    def cone_axis(self):
        R"""
        Cone axis (or global rotation axis) :math:`\boldsymbol{\hat{n}}`

        Returns
        =======
        n : (3,) :numpy:`ndarray`
            Unit vector of a cone axis.
        """

        return self._cone_axis

    @cone_axis.setter
    def cone_axis(self, new_axis):
        try:
            new_axis = np.array(new_axis, dtype=float)
        except:
            raise ValueError(f"New axis is not array-like: {new_axis}")

        if new_axis.shape != (3,):
            raise ValueError(
                f"New axis has to be a 3 component vector, got {new_axis.shape}"
            )

        self._cone_axis = new_axis / np.linalg.norm(new_axis)

    # Notation attributes
    @property
    def notation(self):
        r"""
        Tuple of the notation.

        It can be set with a

        * string
            One of the predefined notations: "Magnopy", "TB2J", "SpinW", "Vampire"

        * iterable with 3 or 4 elements
            First two elements are converted to ``bool``,
            third and fourth element is interpreted as a float.
            Order: (double counting, spin normalized, exchange_factor, on_site_factor).
            If only one factor is given, then
            ``exchange_factor`` = ``on_site_factor`` = ``factor``.

        See :ref:`user-guide_hamiltonian-notation` for the detailed description.


        See Also
        --------
        double_counting
        spin_normalized
        exchange_factor
        on_site_factor
        """

        return (
            self.double_counting,
            self.spin_normalized,
            self.exchange_factor,
            self.on_site_factor,
        )

    @notation.setter
    def notation(self, new_notation):
        # Set the notation from predefined notations
        if isinstance(new_notation, str):
            new_notation = new_notation.lower()
            if new_notation not in PREDEFINED_NOTATIONS:
                raise ValueError(
                    f"Predefine notations are: "
                    + f"{list(PREDEFINED_NOTATIONS)}, got: {new_notation}"
                )
            new_notation = PREDEFINED_NOTATIONS[new_notation]
        # Set the notation from three or four values
        elif isinstance(new_notation, Iterable):
            if len(new_notation) == 3:
                new_notation = (
                    bool(new_notation[0]),
                    bool(new_notation[1]),
                    float(new_notation[2]),
                    float(new_notation[2]),
                )
            elif len(new_notation) == 4:
                new_notation = (
                    bool(new_notation[0]),
                    bool(new_notation[1]),
                    float(new_notation[2]),
                    float(new_notation[3]),
                )
            else:
                raise ValueError(
                    "New notation has to be either a string "
                    + "or an iterable with three or four elements, "
                    + f"got iterable with {len(new_notation)} elements: {new_notation}"
                )
        else:
            raise ValueError(
                "New notation has to be either a string "
                + "or an iterable with three or four elements, "
                + f"got: {new_notation}"
            )
        (
            self.double_counting,
            self.spin_normalized,
            self.exchange_factor,
            self.on_site_factor,
        ) = new_notation

    @property
    def double_counting(self) -> bool:
        r"""
        Whether double counting is present in the Hamiltonian.

        Access this attribute to check the current notation of the Hamiltonian,
        set this attribute to change the notation of the Hamiltonian.

        Returns
        -------
        double_counting : bool
            ``True`` if double counting is present, ``False`` otherwise.

        Raises
        ------
        :py:exc:`.NotationError`
            If the interpretation of the Hamiltonian`s notation is not set.

        See Also
        --------
        spin_normalized
        exchange_factor
        on_site_factor
        notation
        """

        if self._double_counting is None:
            raise NotationError("double_counting")
        return self._double_counting

    def _ensure_double_counting(self):
        r"""
        Ensure double counting.

        Check and fix if needed, that for each (atom1, atom2, R)
        (atom2, atom1, -R) is present in the Hamiltonian.
        """

        bonds = list(self)
        for atom1, atom2, (i, j, k), J in bonds:
            if (atom2, atom1, (-i, -j, -k)) not in self:
                self.add_bond(atom2, atom1, (-i, -j, -k), J=J.T)

    def _ensure_no_double_counting(self):
        r"""
        Ensure that there is no double counting in the model.

        If the bond is (atom1, atom2, (i,j,k)), then the bond is kept in the model
        if one of the conditions is true:

        * i > 0
        * i = 0 and j > 0
        * i = 0, j = 0 and k > 0
        * i = 0, j = 0, k = 0 and atom1.index <= atom2.index
        """

        bonds = list(self)

        for atom1, atom2, (i, j, k), J in bonds:
            # For on-site parameters there is always only one bond in the model
            if (i, j, k) != (0, 0, 0) or atom1 != atom2:
                # If this bond has to stay
                if (
                    i > 0
                    or (i == 0 and j > 0)
                    or (i == 0 and j == 0 and k > 0)
                    or (i == 0 and j == 0 and k == 0 and atom1.index <= atom2.index)
                ):
                    # Delete mirrored bond if it is in the model
                    if (atom2, atom1, (-i, -j, -k)) in self:
                        self.remove_bond(atom2, atom1, (-i, -j, -k))
                # If mirrored bond has to stay
                else:
                    # If mirrored bond is not in the model, then add it
                    if (atom2, atom1, (-i, -j, -k)) not in self:
                        self.add_bond(atom2, atom1, (-i, -j, -k), J=J.T)
                    # Check if the bond is still in the model
                    if (atom1, atom2, (i, j, k)) in self:
                        self.remove_bond(atom1, atom2, (i, j, k))

    @double_counting.setter
    def double_counting(self, new_value: bool):
        # Need to be at the beginning, otherwise _ensure methods do not work
        old_value = self._double_counting
        self._double_counting = bool(new_value)

        # If the attribute is redefined we need to scale the value of parameters
        if old_value is not None:
            factor = 1
            # Mirrored bonds will be removed, remaining have to be doubled
            if old_value and not new_value:
                factor = 2
            # Mirror bonds will be added, existing ones have to be halfed
            elif not old_value and new_value:
                factor = 0.5
            # Scale parameters
            if factor != 1:
                for atom1, atom2, R, J in self:
                    # On-site parameters shall not be scaled,
                    # since they are not affected by double counting.
                    if R != (0, 0, 0) or atom1 != atom2:
                        self[atom1, atom2, R].matrix *= factor

        # Add missed mirror bonds if necessary
        if new_value:
            self._ensure_double_counting()
        # Remove mirrored bonds if any
        else:
            self._ensure_no_double_counting()

    @property
    def spin_normalized(self) -> bool:
        r"""
        Whether spin is normalized.

        Access this attribute to check the current notation of the Hamiltonian,
        set this attribute to change the notation of the Hamiltonian.

        Returns
        -------
        spin_normalized : bool
            ``True`` if spin is normalized, ``False`` otherwise.

        Raises
        ------
        :py:exc:`.NotationError`
            If the interpretation of the Hamiltonian`s notation is not set.

        See Also
        --------
        double_counting
        exchange_factor
        on_site_factor
        notation
        """

        if self._spin_normalized is None:
            raise NotationError("spin_normalized")
        return self._spin_normalized

    @spin_normalized.setter
    def spin_normalized(self, new_value: bool):
        # If the property is redefined, one need to scale the parameters
        if self._spin_normalized is not None:
            if self._spin_normalized and not new_value:
                for atom1, atom2, R, J in self:
                    self[atom1, atom2, R].matrix /= atom1.spin * atom2.spin
            elif not self._spin_normalized and new_value:
                for atom1, atom2, R, J in self:
                    self[atom1, atom2, R].matrix *= atom1.spin * atom2.spin

        self._spin_normalized = bool(new_value)

    @property
    def exchange_factor(self) -> float:
        r"""
        Exchange factor of the Hamiltonian.

        Access this attribute to check the current notation of the Hamiltonian,
        set this attribute to change the notation of the Hamiltonian.

        Returns
        -------
        exchange_factor : float
            Value of the factor before the exchange sum in the Hamiltonian.

        Raises
        ------
        :py:exc:`.NotationError`
            If the interpretation of the Hamiltonian`s notation is not set.

        See Also
        --------
        double_counting
        spin_normalized
        on_site_factor
        notation
        """

        if self._exchange_factor is None:
            raise NotationError("exchange_factor")
        return self._exchange_factor

    @exchange_factor.setter
    def exchange_factor(self, new_factor: float):
        new_factor = float(new_factor)
        # If factor is changing one need to scale parameters.
        if self._exchange_factor is not None and self._exchange_factor != new_factor:
            for atom1, atom2, R, J in self:
                # Only exchange parameters have to be scaled
                if R != (0, 0, 0) or atom1 != atom2:
                    self[atom1, atom2, R].matrix *= self._exchange_factor / new_factor

        self._exchange_factor = new_factor

    @property
    def on_site_factor(self) -> float:
        r"""
        On-site factor of the Hamiltonian.

        Access this attribute to check the current notation of the Hamiltonian,
        set this attribute to change the notation of the Hamiltonian.

        Returns
        -------
        on_site_factor : float
            Value of the factor before the on-site sum in the Hamiltonian.

        Raises
        ------
        :py:exc:`.NotationError`
            If the interpretation of the Hamiltonian`s notation is not set.

        See Also
        --------
        double_counting
        spin_normalized
        exchange_factor
        notation
        """

        if self._on_site_factor is None:
            raise NotationError("on_site_factor")
        return self._on_site_factor

    @on_site_factor.setter
    def on_site_factor(self, new_factor: float):
        new_factor = float(new_factor)
        # If factor is changing one need to scale parameters.
        if self._on_site_factor is not None and self._on_site_factor != new_factor:
            for atom1, atom2, R, J in self:
                # Only on-site parameters have to be scaled
                if R == (0, 0, 0) and atom1 == atom2:
                    self[atom1, atom2, R].matrix *= self._on_site_factor / new_factor

        self._on_site_factor = new_factor

    def __iter__(self):
        return SpinHamiltonianIterator(self)

    def __contains__(self, key):
        atom1, atom2, R = key
        # If atom is a string, get the atom object
        if isinstance(atom1, str):
            atom1 = self.get_atom(atom1)
        if isinstance(atom2, str):
            atom2 = self.get_atom(atom2)

        key = (atom1, atom2, R)
        return key in self._bonds

    def __getitem__(self, key) -> MatrixParameter:
        atom1, atom2, R = key
        # If atom is a string, get the atom object
        if isinstance(atom1, str):
            atom1 = self.get_atom(atom1)
        if isinstance(atom2, str):
            atom2 = self.get_atom(atom2)

        key = (atom1, atom2, R)
        return self._bonds[key]

    def __getattr__(self, name):
        raise AttributeError(name)

    def copy(self):
        R"""
        Return an independent copy of the Hamiltonian.

        Returns
        =======
        spinham : :py:class:`.SpinHamiltonian`
            An independent copy of the Hamiltonian.
        """

        return deepcopy(self)

    @property
    def crystal(self) -> Crystal:
        r"""
        Crystal of the Hamiltonian.

        Return an independent instance of a crystal.
        You can use it to play with the model`s crystal independently,
        but it will not affect the Hamiltonian itself.

        Returns
        -------
        crystal : :py:class:`.Crystal`
            Crystal of the Hamiltonian.

        See Also
        --------
        Crystal
        """
        return Crystal(self.lattice, self.atoms)

    @property
    def magnetic_atoms(self):
        r"""
        Magnetic atoms of the model.

        Atoms with at least one bond starting or finishing in it.

        Atoms are ordered with respect to the :py:attr:`.Atom.index`.

        This property is dynamically computed at every call.

        Returns
        -------
        magnetic_atoms : list of :py:class:`.Atom`
            List of magnetic atoms.
        """
        result = set()
        for atom1, atom2, R, J in self:
            result.add(atom1)
            result.add(atom2)

        return sorted(list(result), key=lambda x: x.index)

    @property
    def I(self):
        r"""
        Number of spins (or magnetic atoms) in the unit cell.

        Returns
        -------
        I : int
            Number of spins (or magnetic atoms) in the unit cell.
        """

        return len(self.magnetic_atoms)

    def __setitem__(self, key, value):
        self.add_bond(*key, value)

    def add_bond(
        self, atom1: Atom, atom2: Atom, ijk, J: MatrixParameter = None, **kwargs
    ):
        r"""
        Add one bond to the Hamiltonian.

        It will rewrite an existing one.

        Parameters
        ----------
        atom1 : :py:class:`Atom` or str
            Atom in (0, 0, 0) unit cell.
            str works only if atom is already in the Hamiltonian.
        atom2 : :py:class:`Atom` or str
            Atom in (i,j,k) unit cell.
            str works only if atom is already in the Hamiltonian.
        ijk : tuple of ints
            Vector of the unit cell for atom2.
            In the relative coordinates (i,j,k).
        J : :py:class:`.MatrixParameter`, optional
            An instance of :py:class:`MatrixParameter`.
        ** kwargs
            Keyword arguments for the constructor of :py:class:`MatrixParameter`.
            Ignored if J is given.
        """

        # Get the atom by the name
        if isinstance(atom1, str):
            atom1 = self.get_atom(atom1)
        elif atom1 not in self.atoms:
            self.add_atom(atom1)

        # Get the atom by the name
        if isinstance(atom2, str):
            atom2 = self.get_atom(atom2)
        elif atom2 not in self.atoms:
            self.add_atom(atom2)

        # Construct parameter if it is not given
        if J is None:
            J = MatrixParameter(**kwargs)

        self._bonds[(atom1, atom2, ijk)] = J

        # Check for double counting
        try:
            i, j, k = ijk
            if self.double_counting and (atom2, atom1, (-i, -j, -k)) not in self:
                self._bonds[(atom2, atom1, (-i, -j, -k))] = J.T
        # If it fails, then we do not need to add a mirrored bond
        except NotationError:
            pass

    def __delitem__(self, key):
        self.remove_bond(*key)

    def remove_bond(self, atom1: Atom, atom2: Atom, ijk, raise_if_no_bond=True):
        r"""
        Remove one bond from the Hamiltonian.

        If :py:attr:`.double_counting` is True, then the mirrored bond is removed as well.

        Parameters
        ----------
        atom1 : py:class:`.Atom`
            Atom object in (0, 0, 0) unit cell.
        atom2 : py:class:`.Atom`
            Atom object in R unit cell.
        R : tuple of ints
            Radius vector of the unit cell for atom2 (i,j,k).
        raise_if_no_bond : bool, default True
            Whether to raise KeyError if the bond is not in the model.
        """

        # If atom is a string, get the atom object
        if isinstance(atom1, str):
            atom1 = self.get_atom(atom1)
        if isinstance(atom2, str):
            atom2 = self.get_atom(atom2)

        try:
            del self._bonds[(atom1, atom2, ijk)]
        except KeyError:
            if raise_if_no_bond:
                raise KeyError(
                    f"Bond ({atom2.fullname}, {atom2.fullname}, {ijk}) is not present in the model."
                )

        # Check for double counting
        try:
            i, j, k = ijk
            if self.double_counting and (atom2, atom1, (-i, -j, -k)) in self:
                del self._bonds[(atom2, atom1, (-i, -j, -k))]
        except NotationError:
            pass

    def remove_atom(self, atom):
        r"""
        Remove magnetic atom from the Hamiltonian.

        Note: this method will remove atom itself and all the
        bonds, which starts or ends in this atom, if atom is magnetic.

        Parameters
        ----------
        atom : :py:class:`.Atom`
            Atom object.
        """

        # If atom given as a string, get the atom object
        if isinstance(atom, str):
            atom = self.get_atom(atom)

        bonds_for_removal = []
        for atom1, atom2, ijk, J in self:
            if atom1 == atom or atom2 == atom:
                bonds_for_removal.append((atom1, atom2, ijk))
        # No need to check for double counting explicitly
        # Both bonds -- ones that start and ones that end in atom -- are removed
        for bond in bonds_for_removal:
            del self[bond]

        super().remove_atom(atom)

    def filter(self, max_distance=None, min_distance=None, custom_filter=None):
        r"""
        Filter the parameter entries based on the given conditions.

        The result will be defined by logical conjugate of the conditions.
        Saying so the filtering will be performed for each given condition
        one by one.

        Parameters
        ----------
        max_distance : float or int, optional
            Distance for sorting, the condition is :math:`\le`.
        min_distance : float or int, optional
            Distance for sorting, the condition is :math:`\ge`.
        custom_filter : function, optional
            Custom function, that takes :py:class:`.MatrixParameter` as an input
            and returns ``bool``. If it returns ``True``, then the bond is
            kept in the Hamiltonian.

        See Also
        --------
        filtered : Returns new object.

        Notes
        -----
        This method modifies the instance at which it is called.
        """

        bonds_for_removal = set()
        for atom1, atom2, ijk, parameter in self:
            dis = self.get_distance(atom1, atom2, ijk)

            if max_distance is not None and dis > max_distance:
                bonds_for_removal.add((atom1, atom2, ijk))

            if min_distance is not None and dis < min_distance:
                bonds_for_removal.add((atom1, atom2, ijk))

            if custom_filter is not None and not custom_filter(parameter):
                bonds_for_removal.add((atom1, atom2, ijk))

        for bond in bonds_for_removal:
            try:
                del self[bond]
            except KeyError:
                pass

    def filtered(self, **kwargs):
        r"""
        Create filtered spin Hamiltonian based on the given conditions.

        The result will be defined by logical conjugate of the conditions.
        Saying so the filtering will be performed for each given condition
        one by one.
        Note: this method is not modifying the instance at which it is called.
        It will create a new instance with sorted :py:attr:`bonds` and all
        the other attributes will be copied (through :py:func:`deepcopy`).

        Parameters
        ----------
        **kwargs : keyword argument, that will be passed to the :py:attr:`.filter` method.

        Returns
        -------
        filtered_model : :py:class:`.SpinHamiltonian`
            Spin Hamiltonian after filtering.

        See Also
        --------
        filter : Modifies current object.

        Notes
        -----
        This method is not modifying the instance at which it is called.
        It creates a new instance (see :py:attr:`.copy`).
        """

        filtered_model = self.copy()
        filtered_model.filter(**kwargs)
        return filtered_model


class SpinHamiltonianIterator:
    def __init__(self, spinham: SpinHamiltonian) -> None:
        self._bonds = list(
            map(
                lambda x: (x[0], x[1], x[2], spinham._bonds[x]),
                spinham._bonds,
            )
        )
        self._index = 0

    def __next__(self) -> Tuple[Atom, Atom, tuple, MatrixParameter]:
        if self._index < len(self._bonds):
            result = self._bonds[self._index]
            self._index += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self
