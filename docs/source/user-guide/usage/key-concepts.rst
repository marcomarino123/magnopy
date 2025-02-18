.. _user-guide_usage_key-concepts:

************
Key concepts
************

On this page we list concepts and data structures, that are essential for understanding
of magnopy's scope, with code examples.

.. _user-guide_usage_key-concepts_wulfric:

Data structures of wulfric
==========================

Magnopy is better used in a symphony with a |wulfric|_ package. Therefore, we refer you
to the `similar page of it <https://docs.wulfric.org/en/latest/user-guide/usage/key-concepts.html>`_
for better understanding of the magnopy's data structures.

Below we shortly recall two data-structures from there

.. _user-guide_usage_key-concepts_wulfric_cell:

Cell
----


``cell`` is a two-dimensianal :math:`3\times3` matrix, that defines three lattice
vectors. The rows of the ``cell`` are vectors, while the columns are cartesian
coordinates. Here is an example of a simple orthorhombic cell

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
properties of atoms. Values are the lists of :math:`N` elements each, where :math:`N` is
an amount of atoms.

Keys recognized by magnopy:

*   "names" :
    ``list`` of ``str``
*   "species" :
    ``list`` of ``str``.
*   "positions" :
    ``list`` of *relative* coordinates of atoms. Each element is an |array-like|_ of the
    length :math:`3`.
*   "spins" :
    ``list`` of ``float``. Spin values for each atom. It is assumed that
    ``atoms["spins"][i] * atoms["spin_directions"][i]`` results in a spin vector of i-th
    spin.
*   "spin_directions" :
    ``list`` of the direction vectors for atom's spins. Each element is an |array-like|_
    of the length :math:`3`. It is assumed that every element has a length 1.
*   "g_factors" :
    ``list`` of ``float``.

As you can see, magnopy extends the definition of ``atoms`` from |wulfric|_, therefore,
any function of |wulfric|_ may be used on it.

.. _user-guide_usage_key-concepts_spin-hamiltonian:

Spin Hamiltonian
================

Spin Hamiltonain in magnopy is understood as a triple of ``cell``, ``atoms`` and
``parameters``. All functions of magnopy expect all three data structures to be passed
separately. However, if you want to keep them together, then we advise to use the
following

.. code-block:: python

    spinham = [cell, atoms, parameters]
    some_function(*spinham)
    # equivalent to
    some_function(cell, atoms, parameters)

the order of the ``cell``, ``atoms``, ``parameter`` is guaranteed by magnopy

Magnopy is applied to the spin Hamiltonian of the general from

.. include:: hamiltonian.inc


Magnopy stores the parameters of the Hamiltonian as a python dictionary. Keys, that are
recognized by magnopy are

* ``"on-site"``

  Parameters of the third term. Stored as a list of elements. Each element is a list
  of two elements, first - index of an atom in the ``spinham["atoms"]``, second -
  a 3 x 3 symmetric matrix :math:`\boldsymbol{A}(\boldsymbol{r}_{\alpha})`.
* ``"exchange"``

  Parameters of the fourth term. Stored as a list of elements. Each element is a list
  of four elements, first - index of an atom in the ``spinham["atoms"]``, that is
  understood to be from the (0,0,0) unit cell; second - index of an atom in the
  ``spinham["atoms"]``, that is understood to be from the (i, j, k) unit cell;
  third a tuple ``(i,j,k)``; fourth - a 3 x 3 symmetric matrix
  :math:`\boldsymbol{J}(\boldsymbol{r}_{\nu,\alpha\beta})`.
* ``"double-counting"``

  Boolean flag. Indicates whether the both spin pairs :math:`(\mu,\alpha;\mu+\nu,\beta)`
  and :math:`(\mu+\nu,\beta;\mu,\alpha)` are included in the sum.
* ``"spin-normalized"``

  Boolean flag. Indicates whether the spin vectors are normalized in the third an fourth
  term.
* ``"C21"``

  A ``float``. Numerical coefficient before the third sum.
* ``"C22"``

  A ``float``. Numerical coefficient before the fourth sum.

First term describes effect of the magnetic field :math:`\boldsymbol{h}` in the Zeeman
form. For this term two parameters of the crystal have to be stored: g-factors and
spin vectors, both are stored as a part of the ``atoms`` dictionary in
``spinham["atoms"]``.

Second term describes a magnetic dipole-dipole interaction. It requires g-factors,
spin vectors and positions of the magnetic sites. All information is accessible from the
``atoms`` dictionary and ``cell``, the latter is stroed in ``spinham["cell"]``.

Third atom describe the quadratic anisotropy. (two spins / one magnetic site, hence
the indices of the constant :math:`C_{2,1}`). For the full description of that term one
has to store spin vectors (stored as a part of ``spinham["atoms"]``), a constant
:math:`C_{2,1}` (stored as ``spinham["C21"]``) and a set of parameters
:math:`\boldsymbol{A}(\boldsymbol{r}_{\alpha})` (stored as ``spinham["on-site"]``).

Third atom describe the bilinear exchange interaction. (two spins / two magnetic sites,
hence the indices of the constant :math:`C_{2,2}`). For the full description of that
term one has to store spin vectors (stored as a part of ``spinham["atoms"]``), a
constant :math:`C_{2,2}` (stored as ``spinham["C22"]``) and a set of parameters
:math:`\boldsymbol{J}(\boldsymbol{r}_{\nu,\alpha\beta})` (stored as
``spinham["exchange"]``).
