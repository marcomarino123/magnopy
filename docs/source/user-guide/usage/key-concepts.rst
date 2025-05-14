.. _user-guide_usage_key-concepts:

************
Key concepts
************

On this page we list main data structures, that are essential for understanding
of magnopy's scope, with code examples.

.. _user-guide_usage_key-concepts_wulfric:

Data structures of wulfric
==========================

As magnopy deals with the :ref:`user-guide_theory-behind_spin-hamiltonian`, it need
to store information about the crystal that this Hamiltonian is defined on. To do so
it needs to use :ref:`user-guide_usage_key-concepts_wulfric_cell` and
:ref:`user-guide_usage_key-concepts_wulfric_atoms`. Those two data structure are
implemented in a number of codes (if not in each one of them). Magnopy does not
re-implement them, but rather use the same data structure as in another python package
called |wulfric|_. In that way we can use all functions defined in |wulfric|_, that are
useful for the symmetries of |Wulfric-Bravais-lattices|_.

Here we briefly describe what are the data structures behind cell and atoms, if you
want to read the original description of |wulfric|_ we refer you
`here <https://docs.wulfric.org/en/latest/user-guide/usage/key-concepts.html>`_.

.. _user-guide_usage_key-concepts_wulfric_cell:

Cell
----

``cell`` is a two-dimensional :math:`3\times3` matrix (|array-like|_), that defines
three lattice vectors. The rows of the ``cell`` are vectors, while the columns are
cartesian coordinates. Here is an example of a simple orthorhombic cell

.. doctest::

    >>> cell = [
    ...     [3.553350, 0.000000, 0.000000],
    ...     [0.000000, 4.744935, 0.000000],
    ...     [0.000000, 0.000000, 8.760497],
    ... ]

.. _user-guide_usage_key-concepts_wulfric_atoms:

Atoms
-----

.. doctest::

    >>> atoms = {
    ...     "names": ["Cr1", "Br1", "S1", "Cr2", "Br2", "S2"],
    ...     "species": ["Cr", "Br", "S", "Cr", "Br", "S"],
    ...     "positions": [
    ...         [0.500000, 0.000000, 0.882382],
    ...         [0.000000, 0.000000, 0.677322],
    ...         [0.500000, 0.500000, 0.935321],
    ...         [0.000000, 0.500000, 0.117618],
    ...         [0.500000, 0.500000, 0.322678],
    ...         [0.000000, 0.000000, 0.064679],
    ...     ],
    ... }

Atoms are stored as a plain python dictionary. Keys of the ``atoms`` are
properties of atoms. Values are the lists of :math:`M` elements each, where :math:`M` is
an amount of atoms.

Keys recognized by magnopy:

*   "names" :
    ``list`` of ``str``. Inherited from |wulfric|_. This property is an informally a
    a main property and, as a rule of thumb, should be always present in the atoms
    dictionary.
*   "species" :
    ``list`` of ``str``. Inherited from |wulfric|_.
*   "positions" :
    ``list`` of **relative** coordinates of atoms. Inherited from |wulfric|_. Each
    element is an |array-like|_ of length :math:`3`.
*   "spins" :
    ``list`` of ``float``. Spin values for each atom.
*   "g_factors" :
    ``list`` of ``float``.

Magnopy extends the definition of ``atoms`` from |wulfric|_, therefore,
any function of |wulfric|_ may be used on it.

.. _user-guide_usage_key-concepts_notation:

Notation
========
To read on the background of the notation problem and why it is important see
:ref:`user-guide_theory-behind_notation`. To handle notation of the spin Hamiltonian
magnopy implements a small :py:class:`.spinham.Notation` class. It stores all parameters
that define notation in one data structure.

.. doctest::

    >>> from magnopy import Notation
    >>> notation = Notation(multiple_counting = True, spin_normalized = False, c1 = 1, c21 = 1)
    >>> notation.name
    'custom'
    >>> notation.multiple_counting
    True
    >>> notation.c21
    1.0
    >>> notation.summary()
    custom notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are not normalized;
      * c1 = 1.0;
      * c21 = 1.0;
      * Undefined c22 factor;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.

Notation is meant to be static, therefore the properties of the notation can not be changed

.. doctest::

    >>> notation.multiple_counting = False
    Traceback (most recent call last):
    ...
    AttributeError: It is intentionally forbidden to set properties of notation. Use correct methods of SpinHamiltonian class to change notation.

If you need to have a new notation, then create a new instance of the
:py:class:`.spinham.Notation` class.

Magnopy gives access to the predefined notations of the spin Hamiltonian from other
popular codes

.. doctest::

    >>> tb2j_notation = Notation.get_predefined("tb2j")
    >>> vampire_notation = Notation.get_predefined("vampire")
    >>> tb2j_notation.summary()
    tb2j notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are normalized to 1;
      * Undefined c1 factor;
      * c21 = -1.0;
      * c22 = -1.0;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.
    >>> vampire_notation.summary()
    vampire notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are normalized to 1;
      * Undefined c1 factor;
      * c21 = -1.0;
      * c22 = -0.5;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.

To see all supported codes see :py:meth:`.spinham.Notation.get_predefined`.


.. _user-guide_usage_key-concepts_spin-hamiltonian:

Spin Hamiltonian
================

:ref:`user-guide_theory-behind_spin-hamiltonian` is the main data structure in magnopy
as it stores all parameters of the input Hamiltonian. It is implemented as a class
:py:class:`.spinham.SpinHamiltonian`, that stores parameters of the
:ref:`user-guide_theory-behind_spin-hamiltonian_expanded-form` in individual attributes.
This class automatically handles the change of notation and addition and removal of the
parameters, that takes into account their symmetry. This class is intended to be a data
structure and not the focus point of calculations that magnopy can perform.

To create spin Hamiltonian one need three objects:
:ref:`user-guide_usage_key-concepts_wulfric_cell`,
:ref:`user-guide_usage_key-concepts_wulfric_atoms` and
:ref:`user-guide_usage_key-concepts_notation`.

.. doctest::

    >>> import numpy as np
    >>> import magnopy
    >>> cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> atoms = {
    ...     "names" : ["Fe1"],
    ...     "species" : ["Fe"],
    ...     "positions" : [[0, 0, 0]],
    ...     "spins" : [5/2],
    ...     "g_factors" : [2]
    ... }
    >>> notation = magnopy.Notation(
    ...     multiple_counting=True, spin_normalized=False, c1=1, c21=1, c22=1 / 2
    ... )
    >>> spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, notation=notation)

Once it is created you can add parameters to it. Spin Hamiltonian class
has a property (starts with ``p``) that give access to the parameters and two methods
that add (starts with ``add_``) and remove (starts with ``remove_``) parameters, for
every type of the parameter of the
:ref:`user-guide_theory-behind_spin-hamiltonian_expanded-form`.

.. doctest::

    >>> import numpy as np
    >>> # Add on-site anisotropy (two spins & one site)
    >>> # Atoms are given by their index in the spinham.atoms: 0 for Fe1
    >>> spinham.add_21(atom=0, parameter=np.diag([2, -1, -1]))
    >>> # Add nearest-neighbor bilinear exchange (two spins & two sites)
    >>> spinham.add_22(atom1 = 0, atom2 = 0, ijk2 = (1, 0, 0), parameter = np.eye(3))
    >>> spinham.add_22(atom1 = 0, atom2 = 0, ijk2 = (0, 1, 0), parameter = np.eye(3))
    >>> spinham.add_22(atom1 = 0, atom2 = 0, ijk2 = (0, 0, 1), parameter = np.eye(3))

Each parameter property behaves as a list with parameters (technically it is either a
list or an iterator)

.. doctest::

    >>> for index, parameter in spinham.p21:
    ...     print(spinham.atoms.names[index], parameter, sep="\n")
    ...
    Fe1
    [[ 2  0  0]
     [ 0 -1  0]
     [ 0  0 -1]]

Note that there are 6 parameters in the p22, as ``multiple_counting`` is ``True``

.. doctest::

    >>> for index1, index2, ijk, parameter in spinham.p22:
    ...     print(spinham.atoms.names[index1], spinham.atoms.names[index2], ijk)
    ...
    Fe1 Fe1 (0, 0, 1)
    Fe1 Fe1 (0, 1, 0)
    Fe1 Fe1 (1, 0, 0)
    Fe1 Fe1 (-1, 0, 0)
    Fe1 Fe1 (0, -1, 0)
    Fe1 Fe1 (0, 0, -1)

Spin Hamiltonian class stores cell and atoms as attributes

.. doctest::

    >>> spinham.cell
    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])
    >>> spinham.atoms
    {'names': ['Fe1'], 'species': ['Fe'], 'positions': [[0, 0, 0]], 'spins': [2.5], 'g_factors': [2]}
    >>> # Magnopy adds syntactic sugar to the atoms dictionary inside the SpinHamiltonian class:
    >>> # a command
    >>> spinham.atoms.names
    ['Fe1']
    >>> # is equivalent to
    >>> spinham.atoms["names"]
    ['Fe1']
    >>> # It works with any key of atoms dictionary
    >>> spinham.atoms.spins
    [2.5]

Cell and atoms are not meant to be changed once the Hamiltonian is created

.. doctest::

    >>> spinham.cell = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
    Traceback (most recent call last):
    ...
    AttributeError: Change of the cell attribute is not supported after the creation of SpinHamiltonian instance. If you need to modify cell, then use pre-defined methods of SpinHamiltonian or create a new one.
    >>> spinham.atoms = {}
    Traceback (most recent call last):
    ...
    AttributeError: Change of the atoms dictionary is not supported after the creation of SpinHamiltonian instance. If you need to modify atoms, then use pre-defined methods of SpinHamiltonian or create a new one.

The notation of the Hamiltonian can be changed. If the Notation is being changed, then
the parameters will be adjusted accordingly. For example if we change the numerical
factor before the two spins & one site term or remove multiple counting

.. doctest::

    >>> new_notation = magnopy.spinham.Notation(
    ...     multiple_counting=False, spin_normalized=False, c1=1, c21=2, c22=1 / 2
    ... )
    >>> spinham.notation = new_notation
    >>> for index, parameter in spinham.p21:
    ...     print(spinham.atoms.names[index], parameter, sep="\n")
    ...
    Fe1
    [[ 1.   0.   0. ]
     [ 0.  -0.5  0. ]
     [ 0.   0.  -0.5]]
    >>> for index1, index2, ijk, parameter in spinham.p22:
    ...     print(spinham.atoms.names[index1], spinham.atoms.names[index2], ijk)
    ...
    Fe1 Fe1 (0, 0, 1)
    Fe1 Fe1 (0, 1, 0)
    Fe1 Fe1 (1, 0, 0)
