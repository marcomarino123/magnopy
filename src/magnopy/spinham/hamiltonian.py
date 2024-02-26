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

    Child of the :ref:`wulfric:api_crystal` class.

    Parameters
    ----------
    crystal : :ref:`wulfric:api_crystal`, optional
        Crystal on which the spin Hamiltonian is build.
        By default it is cubic (:math:`a=1`) lattice with no atoms.
    notation : str or tuple of two bool and one or two floats, optional
        One of the predefined notations or tuple with custom notation.
        See :py:attr:`.notation` for details.
    **kwargs
        Keyword arguments for the :ref:`wulfric:api_crystal` constructor.

    """

    def __init__(self, crystal: Crystal = None, notation=None, **kwargs) -> None:
        if crystal is not None:
            kwargs["atoms"] = crystal.atoms
            kwargs["cell"] = crystal.cell

        super().__init__(**kwargs)

        self._exchange = {}
        self._on_site = {}
        self._spiral_vector = None
        self._cone_axis = None

        # Notation settings
        self._double_counting = None
        self._spin_normalized = None
        self._exchange_factor = None
        self._on_site_factor = None
        if notation is not None:
            self.notation = notation

    ################################################################################
    #                            Parameter's properties                            #
    ################################################################################

    @property
    def exchange(self):
        R"""
        Exchange parameters of the Hamiltonian together with the bond data::

            ``atom1, atom2, (i,j,k), parameter``

        It is an iterator.
        """
        return _SpinHamiltonianExchangeIterator(self)

    @property
    def on_site(self):
        R"""
        On-site parameters of the Hamiltonian together with the atom data::

            ``atom, parameter``

        It is an iterator.
        """
        return _SpinHamiltonianOnSiteIterator(self)

    @property
    def exchange_like(self):
        R"""
        Parameters of the Hamiltonian, that can be written in the exchange form
        together with the bond data::

            ``atom1, atom2, (i,j,k), parameter``

        It combines:

        * Exchange parameters: ``atom1, atom2, (i,j,k), parameter``
        * On-site parameters: ``atom, atom, (0,0,0), parameter``

        On-site parameters are scaled with the factor
        :py:attr:`.exchange_factor`/:py:attr:`.on_site_factor`

        It is an iterator.
        """
        return _SpinHamiltonianExchangeLikeIterator(self)

    ################################################################################
    #                           Ground state properties                            #
    ################################################################################
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
                f"New spiral vector has to be a 3 component vector, got {new_vector.shape}"
            )

        self._spiral_vector = new_vector

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

        if np.allclose(new_axis, np.zeros(3)):
            raise ValueError("New cone axis can not be a zero vector")

        self._cone_axis = new_axis / np.linalg.norm(new_axis)

    ################################################################################
    #                             Notation properties                              #
    ################################################################################
    @property
    def notation(self):
        r"""
        Tuple of the notation.

        It can be set with a

        * string
            One of the predefined notations: "Magnopy", "TB2J", "SpinW", "Vampire"

        * iterable with 3 or 4 elements
            First two elements are converted to ``bool``,
            third and fourth element are interpreted as floats.
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

        bonds_to_add = []
        for atom1, atom2, (i, j, k), parameter in self.exchange:
            # Remember the mirrored bond if it is not in the Hamiltonian yet
            if (atom2, atom1, (-i, -j, -k)) not in self.exchange:
                bonds_to_add.append((atom2, atom1, (-i, -j, -k), parameter.T))

        # Add all missing bonds
        for bond in bonds_to_add:
            self.add_exchange(*bond)

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

        bonds_to_remove = []
        bonds_to_add = []

        for atom1, atom2, (i, j, k), parameter in self.exchange:
            # If this bond has to stay
            if (
                i > 0
                or (i == 0 and j > 0)
                or (i == 0 and j == 0 and k > 0)
                or (i == 0 and j == 0 and k == 0 and atom1.index <= atom2.index)
            ):
                # Remember  mirrored bond  for removal, if it is in the model
                if (atom2, atom1, (-i, -j, -k)) in self:
                    bonds_to_remove.append((atom2, atom1, (-i, -j, -k)))
            # If mirrored bond has to stay
            else:
                # If mirrored bond is not in the model, then remember it for addition
                if (atom2, atom1, (-i, -j, -k)) not in self:
                    bonds_to_add.append(
                        atom2, atom1, (-i, -j, -k), parameter=parameter.T
                    )
                # Remember the bond for removal
                bonds_to_remove.append((atom1, atom2, (i, j, k)))

        for bond in bonds_to_add:
            self.add_exchange(*bond)

        for bond in bonds_to_remove:
            self.remove_exchange(*bond, raise_if_no_bond=False)

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
            # Scale exchange parameters
            if factor != 1:
                for atom1, atom2, ijk in self._exchange:
                    self[atom1, atom2, ijk].matrix *= factor

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
            # Remove the spin out of parameters
            if self._spin_normalized and not new_value:
                # For exchange
                for atom1, atom2, ijk in self._exchange:
                    self[atom1, atom2, ijk].matrix /= atom1.spin * atom2.spin
                # For on-site
                for atom in self._on_site:
                    self[atom].matrix /= atom.spin**2
            # Absorb spin in the parameters
            elif not self._spin_normalized and new_value:
                # For exchange
                for atom1, atom2, ijk in self._exchange:
                    self[atom1, atom2, ijk].matrix *= atom1.spin * atom2.spin
                # For on-site
                for atom in self._on_site:
                    self[atom].matrix *= atom.spin**2

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
            # Only exchange parameters have to be scaled
            for atom1, atom2, ijk in self._exchange:
                self[atom1, atom2, ijk].matrix *= self._exchange_factor / new_factor

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
            # Only on-site parameters have to be scaled
            for atom in self._on_site:
                self[atom].matrix *= self._on_site_factor / new_factor

        self._on_site_factor = new_factor

    ################################################################################
    #                           Dictionary-like behavior                           #
    ################################################################################
    def __contains__(self, key) -> bool:
        # User is asking for on-site terms
        if isinstance(key, str) or isinstance(key, Atom):
            # If atom is a string, get the atom object
            if isinstance(key, str):
                key = self.get_atom(key)
            return key in self._on_site
        # User is asking for exchange terms
        elif isinstance(key, Iterable) and len(key) == 3:
            atom1, atom2, R = key
            # If atom is a string, get the atom object
            if isinstance(atom1, str):
                atom1 = self.get_atom(atom1)
            if isinstance(atom2, str):
                atom2 = self.get_atom(atom2)

            key = (atom1, atom2, R)
            return key in self._exchange
        else:
            raise KeyError(
                f"Key is either a string an Atom or a tuple of length three:"
                + f"two Atoms or strings and a tuple of three integers. Got {key}"
            )

    def __getitem__(self, key) -> MatrixParameter:
        # User is asking for on-site terms
        if isinstance(key, str) or isinstance(key, Atom):
            # If atom is a string, get the atom object
            if isinstance(key, str):
                key = self.get_atom(key)
            return self._on_site[key]
        # User is asking for exchange terms
        elif isinstance(key, Iterable) and len(key) == 3:
            atom1, atom2, R = key
            # If atom is a string, get the atom object
            if isinstance(atom1, str):
                atom1 = self.get_atom(atom1)
            if isinstance(atom2, str):
                atom2 = self.get_atom(atom2)

            return self._exchange[atom1, atom2, R]
        else:
            raise KeyError(
                f"Key is either a string an Atom or a tuple of length three:"
                + f"two Atoms or strings and a tuple of three integers. Got {key}"
            )

    def __setitem__(self, key, value):
        # User is giving parameter for on-site term
        if isinstance(key, str) or isinstance(key, Atom):
            self.add_on_site(key, value)
        # User is giving parameter for exchange term
        elif isinstance(key, Iterable) and len(key) == 3:
            self.add_exchange(*key, value)
        else:
            raise KeyError(
                f"Key is either a string an Atom or a tuple of length three:"
                + f"two Atoms or strings and a tuple of three integers. Got {key}"
            )

    def __delitem__(self, key):
        # User wants to remove an on-site term
        if isinstance(key, str) or isinstance(key, Atom):
            self.remove_on_site(key)
        # User wants to remove an exchange term
        elif isinstance(key, Iterable) and len(key) == 3:
            self.remove_exchange(*key)
        else:
            raise KeyError(
                f"Key is either a string an Atom or a tuple of length three:"
                + f"two Atoms or strings and a tuple of three integers. Got {key}"
            )

    ################################################################################
    #                                  Copy getter                                 #
    ################################################################################
    def copy(self):
        R"""
        Return a new instance of the same Hamiltonian.

        Returns
        =======
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
        Magnetic atoms of the model.

        Atoms with at least one parameter associated with it.

        Atoms are ordered with respect to the :py:attr:`.Atom.index`.

        This property is dynamically computed at every call.

        Returns
        -------
        magnetic_atoms : list of :ref:`wulfric:api_Atom`
            List of magnetic atoms.
        """
        result = set()
        # Look through the exchange terms
        for atom1, atom2, _ in self._exchange:
            result.add(atom1)
            result.add(atom2)
        # Look through the on-site terms
        for atom in self._on_site:
            result.add(atom)

        return sorted(list(result), key=lambda x: x.index)

    @property
    def I(self):
        r"""
        Number of spins (magnetic atoms) in the unit cell.

        Returns
        -------
        I : int
            Number of spins (magnetic atoms) in the unit cell.

        See Also
        --------
        magnetic_atoms
        """

        return len(self.magnetic_atoms)

    ################################################################################
    #                          Manipulations with exchange                         #
    ################################################################################
    def add_exchange(
        self, atom1: Atom, atom2: Atom, ijk, parameter: MatrixParameter = None, **kwargs
    ):
        r"""
        Add one exchange bond to the Hamiltonian.

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
        parameter : :py:class:`.MatrixParameter`, optional
            An instance of :py:class:`MatrixParameter`.
        ** kwargs
            Keyword arguments for the constructor of :py:class:`MatrixParameter`.
            Ignored if ``parameter`` is given.
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
        if parameter is None:
            parameter = MatrixParameter(**kwargs)

        self._exchange[(atom1, atom2, ijk)] = parameter

        # Check for double counting
        try:
            i, j, k = ijk
            if (
                self.double_counting
                and (atom2, atom1, (-i, -j, -k)) not in self._exchange
            ):
                self._exchange[(atom2, atom1, (-i, -j, -k))] = parameter.T
        # If it fails, then we do not need to add a mirrored bond, since the notation
        # is not defined yet and it is not clear wether the mirrored bond has to
        # be added or not
        except NotationError:
            pass

    def remove_exchange(self, atom1: Atom, atom2: Atom, ijk, raise_if_no_bond=True):
        r"""
        Remove one bond from the Hamiltonian.

        If :py:attr:`.double_counting` is True, then the mirrored bond is removed as well.

        Parameters
        ----------
        atom1 : py:class:`.Atom`
            Atom object in (0, 0, 0) unit cell.
        atom2 : py:class:`.Atom`
            Atom object in R unit cell.
        ijk : tuple of ints
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
            del self._exchange[(atom1, atom2, ijk)]
        except KeyError:
            if raise_if_no_bond:
                raise KeyError(
                    f"Bond ({atom2.fullname}, {atom2.fullname}, {ijk}) "
                    + "is not present in the Hamiltonian."
                )

        # Check for double counting
        try:
            i, j, k = ijk
            if self.double_counting and (atom2, atom1, (-i, -j, -k)) in self._exchange:
                del self._exchange[(atom2, atom1, (-i, -j, -k))]
        except NotationError:
            pass

    ################################################################################
    #                           Manipulations with on-site                         #
    ################################################################################
    def add_on_site(self, atom: Atom, parameter: MatrixParameter = None, **kwargs):
        r"""
        Add one on-site parameter to the Hamiltonian.

        It will rewrite an existing one.

        Parameters
        ----------
        atom : :py:class:`Atom` or str
            Atom to which ``parameter`` is added.
            ``str`` works only if atom is already in the Hamiltonian.
        parameter : :py:class:`.MatrixParameter`, optional
            An instance of :py:class:`MatrixParameter`.
        ** kwargs
            Keyword arguments for the constructor of :py:class:`MatrixParameter`.
            Ignored if ``parameter`` is given.
        """

        # Get the atom by the name
        if isinstance(atom, str):
            atom = self.get_atom(atom)
        # Add atom to the Hamiltonian if it is not in it
        # Only works for Atom class
        elif atom not in self.atoms:
            self.add_atom(atom)

        # Construct parameter if it is not given
        if parameter is None:
            parameter = MatrixParameter(**kwargs)

        self._on_site[atom] = parameter

    def remove_on_site(self, atom: Atom, raise_if_no_bond=True):
        r"""
        Remove one one-site parameter from the Hamiltonian.

        Parameters
        ----------
        atom : :ref:`wulfric:api_Atom`
            Atom for which the parameter will be removed.
        raise_if_no_bond : bool, default True
            Whether to raise KeyError if the parameter for ``atom`` is not in the Hamiltonian.
        """

        # If atom is a string, get the atom object
        if isinstance(atom, str):
            atom1 = self.get_atom(atom)

        try:
            del self._on_site[atom]
        except KeyError:
            if raise_if_no_bond:
                raise KeyError(
                    f"There are not on-site anisotropy for the atom {atom.fullname} in the Hamiltonian."
                )

    ################################################################################
    #                                    Filters                                   #
    ################################################################################
    def filter(self, max_distance=None, min_distance=None, custom_filter=None):
        r"""
        Filter the parameter entries based on the given conditions.

        The result will be defined by logical conjugate of the conditions.
        Saying so the filtering will be performed for each given condition
        one by one.

        Parameters
        ----------
        max_distance : float or int, optional
            Distance for sorting, the condition to keep the bond is :math:`\le`.
        min_distance : float or int, optional
            Distance for sorting, the condition to keep thebond is :math:`\ge`.
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

        parameters_for_removal = set()

        # Filter the exchange interactions
        for atom1, atom2, ijk, parameter in self.exchange:
            dis = self.get_distance(atom1, atom2, ijk)

            if max_distance is not None and dis > max_distance:
                parameters_for_removal.add((atom1, atom2, ijk))

            if min_distance is not None and dis < min_distance:
                parameters_for_removal.add((atom1, atom2, ijk))

            if custom_filter is not None and not custom_filter(parameter):
                parameters_for_removal.add((atom1, atom2, ijk))

        # Filter the on-site parameters (only for custom_filter and min_distance,
        # since the distance for on-site is always 0)
        for atom, parameter in self.on_site:
            if min_distance is not None and min_distance > 0:
                parameters_for_removal.add(atom)
            if custom_filter is not None and not custom_filter(parameter):
                parameters_for_removal.add(atom)
        for parameter in parameters_for_removal:
            try:
                # Parameter has different type (tuple or atom) but the same syntax
                # works for both, see __delitem__ for details
                del self[parameter]
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

    ################################################################################
    #                          Manipulations with crystal                          #
    ################################################################################
    def remove_atom(self, atom):
        r"""
        Remove magnetic atom from the Hamiltonian.

        Note: this method will remove atom itself and all the
        parameters associated with it.

        Parameters
        ----------
        atom : :ref:`wulfric:api_Atom`
            Atom object.
        """

        # If atom given as a string, get the atom object
        if isinstance(atom, str):
            atom = self.get_atom(atom)

        parameters_for_removal = []
        # Look through exchange parameters
        for atom1, atom2, ijk in self._exchange:
            if atom1 == atom or atom2 == atom:
                parameters_for_removal.append((atom1, atom2, ijk))
        # Look through on-site parameters
        if atom in self._on_site:
            parameters_for_removal.append(atom)
        # No need to check for double counting explicitly
        # Both bonds -- ones that start and ones that end in atom -- are removed
        for parameter in parameters_for_removal:
            # Parameter has different type (tuple or atom) but the same syntax
            # works for both, see __delitem__ for details
            del self[parameter]

        # Remove an atom from the crystal
        super().remove_atom(atom)

    @property
    def crystal(self) -> Crystal:
        r"""
        Crystal of the Hamiltonian.

        Return an independent instance of a crystal.
        You can use it to play with the model`s crystal independently,
        but it will not affect the Hamiltonian itself.

        Returns
        -------
        crystal : :ref:`wulfric:api_crystal`
            Crystal of the Hamiltonian.

        See Also
        --------
        Crystal
        """
        return Crystal(self.lattice, self.atoms)


class _SpinHamiltonianExchangeIterator:
    R"""
    Iterator for exchange parameters of the Hamiltonian
    """

    def __init__(self, spinham: SpinHamiltonian) -> None:
        self.length = len(spinham._exchange)
        self.container = spinham._exchange
        self.iterator = spinham._exchange.__iter__()
        self.index = 0

    def __next__(self) -> Tuple[Atom, Atom, tuple, MatrixParameter]:
        if self.index < self.length:
            atom1, atom2, ijk = self.iterator.__next__()
            result = (atom1, atom2, ijk, self.container[atom1, atom2, ijk])
            self.index += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        return self.length


class _SpinHamiltonianOnSiteIterator:
    R"""
    Iterator for on-site parameters of the Hamiltonian
    """

    def __init__(self, spinham: SpinHamiltonian) -> None:
        self.length = len(spinham._on_site)
        self.container = spinham._on_site
        self.iterator = spinham._on_site.__iter__()
        self.index = 0

    def __next__(self) -> Tuple[Atom, MatrixParameter]:
        if self.index < self.length:
            atom = self.iterator.__next__()
            result = (atom, self.container[atom])
            self.index += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        return self.length


class _SpinHamiltonianExchangeLikeIterator:
    R"""
    Iterator for parameters of the Hamiltonian, that can be written in the
    form of exchange parameters:

    * exchange parameters: atom1, atom2, (i,j,k)
    * on-site parameters: atom, atom, (0,0,0)
    """

    def __init__(self, spinham: SpinHamiltonian) -> None:
        self.length1 = len(spinham._on_site)
        self.length2 = len(spinham._exchange)
        self.container1 = spinham._on_site
        self.container2 = spinham._exchange
        self.iterator1 = spinham._on_site.__iter__()
        self.iterator2 = spinham._exchange.__iter__()
        self.index1 = 0
        self.index2 = 0
        self.scale_factor = spinham.exchange_factor / spinham.on_site_factor

    def __next__(self) -> Tuple[Atom, Atom, tuple, MatrixParameter]:
        # First return all on-site terms
        # Note: they are scaled in order to have an exchange factor instead of the on-site one.
        if self.index1 < self.length1:
            atom = self.iterator1.__next__()
            result = (atom, atom, (0, 0, 0), self.container1[atom] * self.scale_factor)
            self.index1 += 1
            return result
        # Then return all exchange terms
        elif self.index2 < self.length2:
            atom1, atom2, ijk = self.iterator2.__next__()
            result = (atom1, atom2, ijk, self.container2[atom1, atom2, ijk])
            self.index1 += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        return self.length1 + self.length2
