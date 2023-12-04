.. _user-guide_methods_input-standard:

*******************************
Specification of the input file
*******************************

* File is expected to have ``utf-8`` encoding.
* Line is considered to be blank if it consists of any number of spaces (U+0020).
* All blank lines are ignored.
* If the character ``#`` (U+0023) is read than all symbols untill the next
  line symbols are ignored.
* Comment lines can appear at any line of the file.
* Sections are separated by 20 or more consecutive ``=`` (U+003D) symbols.
* Subsections inside eachsection are separated by 20 or more ``-`` (U+002D) syymbols.
* Whole file is case-insensetive.


Sections
========

Unit cell
---------

.. code-block:: text
    :linenos:

    ====================
    Cell: <Units>
    a_x a_y a_z
    b_x b_y b_z
    c_x c_y c_z
    ====================

* line 1: Section separator (20+ ``=`` symbols)
* line 2: ``Cell`` keyword. Spaces are ignored in this line. By default the Units
  for the lattice vectors are angstroms. You may use other predefined units by providing
  the keyword (case-insensetive):

  - Angstroms
  - Bohr

  If the keyword is provided it has to be preceeded by ``:`` character.
* line 3: Coordinates of the first lattice vector, separated by space.
* line 4: Coordinates of the second lattice vector, separated by space.
* line 5: Coordinates of the third lattice vector, separated by space.
* line 6: Section separator (20+ ``=`` symbols)

Additional rules:

* Lines 3-5 can contain additional information,
  given that first three space-separated are the coordinates of
  correcponding lattice vectors.

Atoms
-----

.. code-block:: text
    :linenos:

    ====================
    Atoms: <coordinate-type>
    A1 i j k <spin1>
    A2 i j k <spin2>
    A3 i j k <spin3>
    ====================

* line 1: Section separator (20+ ``=`` symbols)
* line 2: ``Atoms`` keyword. Spaces are ignored in this line.
  By the atom coordinates are relative to the lattice vectors:

  - :math:`i \rightarrow \vec{a}`
  - :math:`j \rightarrow \vec{b}`
  - :math:`k \rightarrow \vec{c}`

  You may use one of the predefined
  <coordinate-type> keywords (case-insensetive):

  - absolute
  - relative

  If the keyword is provided it has to be preceeded by ``:`` character.
* line 3: Information about the first atom, entries are separated by space:

  - Atoms's symbol
  - First coordinate (:math:`i` if relative, :math:`x` if absolute).
  - Second coordinate (:math:`j` if relative, :math:`y` if absolute).
  - Third coordinate (:math:`k` if relative, :math:`z` if absolute).
  - (optional) Spin of the first atom. Either one or three or four numbers separated by space:

    * If one: :math:`\vert S\vert` - value of the spin.
    * If three: :math:`S_x` :math:`S_y` :math:`S_z` - three components of the spin vector.
      Value is defined from the three components.
    * If four: :math:`\vert S\vert` :math:`S_x` :math:`S_y` :math:`S_z` - value and three component.
      Value is given directly, thus the components only define the direction.
* line 4: Information about the second atom.
* line 5: Information about the third atom.
* line 6: Section separator (20+ ``=`` symbols)

Notation
--------

# TODO

Magnetic field
--------------

.. code-block:: text
    :linenos:

    ====================
    Magnetic field: <Units>
    H_x H_y H_z
    ====================

* line 1: Section separator (20+ ``=`` symbols)
* line 2: ``Magnetic field`` keyword. # TODO
* line 3: Three components of the magnetic field, separated by spaces.
* line 4: Section separator (20+ ``=`` symbols)

Parameters
----------

.. code-block:: text
    :linenos:

    ====================
    Parameters: <Units>
    --------------------
    Bond 1
    --------------------
    Bond 2
    ====================

* line 1: Section separator (20+ ``=`` symbols)
* line 2: ``Parameters`` keyword. By default the units are meV.
  One can use optional <Units> keyword:

  - meV
  - eV (for electron-Volt)
  - J (for Joul)
  - K (for Kelvin)

* line 3: Subsection separator (20+ ``-`` symbols)
* line 4: Specification of the first bond.
* line 5: Subsection separator (20+ ``-`` symbols)
* line 6: Specification of the second bond.
* line 7: Section separator (20+ ``=`` symbols)

Specification of the bond:

.. code-block:: text
    :linenos:

    A1 A2 i j k <isotropic parameter>
    Matrix
    Jxx Jxy Jxz
    Jyx Jyy Jyz
    Jzx Jzy Jzz
    DMI Dx Dy Dz

* line 1:

  - A1 - Name of the first atom (in the (0,0,0) unit cell).
  - A2 - Name of the second atom (in the (i,j,k) unit cell).
  - i j k - Relative coordinates of the cell for Atom 2.
  - (optional) Isotropic parameter.

* line 2: (optional) Keyword ``Matrix``. Indicates that next three
  non-empty and non-comment lines give the full matrix of the parameter.
* line 3-5: (optional) Full parameter matrix.
* line 6: (optional) DMI vector:

  - ``DMI`` keyword
  - x component
  - y component
  - z component

Additional rules:

* If both ``Matrix`` and ``DMI`` are given, then antisymmetrix part of the
  matrix is ovewritten.
* If both ``Matrix`` and ``isotropic parameter`` are given, than
  isotropic part of the matrix is ovewritten.
