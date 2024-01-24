.. _user-guide_methods_input-standard:

*******************************
Specification of the input file
*******************************

* File is expected to have ``utf-8`` encoding.
* Line is considered to be blank if it consists of any number of spaces (U+0020).
* All blank lines are ignored.
* If the character ``#`` (U+0023) is read than all symbols until the next
  line symbol are ignored.
* Comment lines can appear at any line of the file.
* Sections are separated by 10 or more consecutive ``=`` (U+003D) symbols.
* Subsections inside each section are separated by 10 or more ``-`` (U+002D) symbols.
* All keywords are case-insensitive.
* Sections have to follow the order from this page.


Sections
========

.. note::
  If keyword name is enclosed as <keyword>, then it is optional.

Unit cell
---------

.. code-block:: text
    :linenos:

    ==========
    Cell <Units> <Scale>
    a_x a_y a_z
    b_x b_y b_z
    c_x c_y c_z
    ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: From one to three keyword entries:

  - ``Cell`` keyword. Indicate the interpretation of the section.
  - ``<Units>``. One of the predefined units for the lattice vectors.
    Allowed keyword values:

    - "Angstrom" (default)
    - "Bohr"

    Note: Only the first letter is actually checked.

  - ``<Scale>``. Scale factor for the lattice vectors.

    - One number: ``s``.
      Scale factor for the unit cell.

    - Three numbers: ``s_a s_b s_c``.
      Individual scale factors for each lattice vector.

* line 3: Coordinates of the first lattice vector, separated by space.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_a``.
* line 4: Coordinates of the second lattice vector, separated by space.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_b``.
* line 5: Coordinates of the third lattice vector, separated by space.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_c``.
* line 6: Section separator (10 or more ``=`` symbols)

Atoms
-----

.. code-block:: text
    :linenos:

    ==========
    Atoms <Units>
    A1 i j k <spin1>
    A2 i j k <spin2>
    A3 i j k <spin3>
    ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: One or two keyword entries:

  - ``Atoms`` keyword. Indicate the interpretation of the section.
  - ``<Units>``. One of the predefined units for the atom coordinates.
    Allowed keyword values are

    - "Relative" (default)

      Atom coordinates are relative to the unit cell vectors.
    - "Angstrom"

      Atom coordinates are absolute and given in Angstroms.
    - "Bohr"

      Atom coordinates are absolute and given in Bohr.

    Note: Only the first letter is actually checked.

* line 3: Information about the first atom, entries are separated by space:

  - ``A1`` - Atoms's symbol.
  - ``i`` - First coordinate.
  - ``j`` -  Second coordinate.
  - ``k`` - Third coordinate.
  - ``<spin1>`` -  Spin of the first atom.
    Either 1, 3 or 4 entries separated by space:

    - :math:`S` - one number. Indicates the value of the spin. It will be oriented along
      :math:`z` direction, i.e. :math:`\boldsymbol{S} = (0, 0, S)^T`.

    - :math:`S_x` :math:`S_y` :math:`S_z` - three numbers.
      Describe spin vector.
    - :math:`S_x` :math:`S_y` :math:`S_z` :math:`S` - four numbers.
      Describe spin direction and its value. The module of the vector is ignored and
      the provided value is used.
    - :math:`p\phi` :math:`t\theta` :math:`S` - two strings and one number.
      Two angles, that define the direction of the spin as described
      :ref:`here <user-guide_methods_spin-rotations>`. :math:`p` and :math:`t` are used
      to distinguish this case from the spin vector one. Example:

      - ``p30 t90 0.5`` - two angles and value
      - ``30 90 0.5`` - spin vector





* line 4: Information about the second atom.
* line 5: Information about the third atom.
* line 6: Section separator (10 or more ``=`` symbols)

Notation
--------

.. code-block:: text
  :linenos:

  ==========
  Notation
  <Spin normalized>
  <Double counting>
  <Exchange factor>
  <On-site factor>
  ==========

Magnetic field
--------------

# TODO

Parameters
----------

.. code-block:: text
    :linenos:

    ==========
    Parameters <Units>
    ----------
    Bond 1
    ----------
    Bond 2
    ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: One or two keyword entries:

  - ``Parameters`` keyword. Indicate the interpretation of the section.
  - ``<Units>``. One of the predefined units for the Hamiltonian parameters.
    Allowed keyword values are

    - meV -  :math:`10^{-3}` electron-Volt (default)
    - eV -  electron-Volt
    - J - Joule
    - K - Kelvin
    - Ry - Rydberg units of energy


    Note: Only the first letter is actually checked.

* line 3: Subsection separator (10 or more ``-`` symbols)
* line 4: Specification of the first bond.
* line 5: Subsection separator (10 or more ``-`` symbols)
* line 6: Specification of the second bond.
* line 7: Section separator (10 or more ``=`` symbols)

Specification of the bond:

.. code-block:: text
    :linenos:

    A1 A2 i j k <isotropic parameter>
    <Matrix
    Jxx Jxy Jxz
    Jyx Jyy Jyz
    Jzx Jzy Jzz>
    <Symmetric anisotropy
    Sxx Sxy Sxz
    Sxy Syy Syz
    Sxz Syz Szz>
    <DMI Dx Dy Dz>

* line 1:

  - A1 - Name of the first atom (in the (0,0,0) unit cell).
  - A2 - Name of the second atom (in the (i,j,k) unit cell).
  - i j k - Relative coordinates of the cell for Atom 2.
  - (optional) Isotropic parameter.

* line 2: (optional) Keyword ``Matrix``. Indicates that next three
  non-empty and non-comment lines give the full matrix of the parameter.
* line 3-5: (optional) Full parameter matrix.
* line 2: (optional) Keyword ``Symmetric anisotropy``. Indicates that next three
  non-empty and non-comment lines give the symmetric anisotropic part of the parameter's matrix.
  Note: This matrix has to be traceless.
* line 7-8: (optional) Full parameter matrix.
* line 10: (optional) DMI vector:

  - ``DMI`` keyword
  - x component
  - y component
  - z component

Additional rules:

* If both ``Matrix`` and ``DMI`` are given, then antisymmetric part of the
  matrix is overwritten.
* If both ``Matrix`` and ``isotropic parameter`` are given, then
  isotropic part of the matrix is overwritten.
* If both ``Matrix`` and ``Symmetric anisotropy`` are given, then
  symmetric anisotropic part of the matrix is overwritten.
