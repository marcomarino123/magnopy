.. _user-guide_methods_input-standard:

*******************************
Specification of the input file
*******************************

* File is expected to have |utf-8|_ encoding.
* Line is considered to be blank if there are no other characters but any number of spaces (U+0020).
* All blank lines are ignored.
* Character ``#`` (U+0023) is used for comments. If it is read than all symbols until
  the next line symbol are ignored. Comments can appear anywhere, even inside a section
  provided that they do not break the format. An example for the "Cell" section is
  provided below

  .. code-block:: text
    :linenos:

    ==========
    # Comment line
    Cell <Units> <Scale>
    a_x a_y a_z # Inline comment
    b_x b_y b_z
    # Comment line
    c_x c_y c_z
    ==========

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

.. _user-guide_methods_input-standard_atoms:

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

  - ``A1`` - Atoms's label. Any string, that does not contain "#" or space symbols.
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
  Double counting = value #  true or false
  Spin normalized = value #  true or false
  Exchange factor = value #  1 or -1 or 0.5 or any number
  On-site factor  = value #  1 or -1 or any number
  ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: ``Notation`` keyword. Indicate the interpretation of the section.
* line 3-6: Four notation properties. The order can be arbitrary, but all four have to
  be present (If you hamiltonian does not have on-site anisotropy, then just put 1).

  - Double counting. True if both pairs :math:`(m,i;m^{\prime},j)` and :math:`(m^{\prime},j;m,i)`
    are included in the Hamiltonian. False otherwise.
  - Spin normalized. True if spin vectors are unit vectors
    (i.e. if spin value is effectively absorbed in the exchange/on-site anisotropy parameters).
    False otherwise.
  - Exchange factor. Numerical factor, that is written before the sum over spin pair.
    Usually it is either :math:`1`, :math:`-1`, :math:`0.5` or :math:`-0.5`.
  - On-site factor. Numerical factor, that is written before the sum over spins.
    Usually it is either :math:`1` or :math:`-1`.

  For the detailed discussion about various notations of spin Hamiltonian go
  :ref:`here <TODO>`.

  .. dropdown:: Example

    For the Hamiltonian from the user guide of magnopy

    #TODO

    The notation section can be written as

    .. code-block:: text

      ==========
      Notation
      Double counting = true
      Spin normalized = false
      Exchange factor = 0.5
      On-site factor  = 1
      ==========

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

  - A1 - label of the first atom (in the (0,0,0) unit cell).
    Label have to be consistent with :ref:`user-guide_methods_input-standard_atoms` section.
  - A2 - label of the second atom (in the (i,j,k) unit cell).
    Label have to be consistent with :ref:`user-guide_methods_input-standard_atoms` section.
  - i j k - Relative coordinates of the cell for Atom 2. Three integers, separated by spaces.
  - (optional) Isotropic parameter. One number.

* line 2: (optional) Keyword ``Matrix``. Indicates that next three
  lines give the full matrix of the parameter.
* line 3-5: (optional) Full parameter matrix.
  Each line has to contain three numbers, separated by spaces.
* line 2: (optional) Keyword ``Symmetric anisotropy``. Indicates that next three
  lines give the symmetric anisotropic part of the parameter's matrix.
  Note: This matrix has to be traceless.
* line 7-8: (optional) Symmetric anisotropic part of full parameter matrix matrix.
  Each line has to contain three numbers, separated by spaces.
* line 10: (optional) Dzyaroshinsky-Moria interaction vector.
  Also referred as antisymmetric anisotropic interaction.

  - ``DMI`` keyword
  - x component
  - y component
  - z component

Priority of given keywords:

* If both ``Matrix`` and ``DMI`` are given, then antisymmetric part of the
  matrix is ignored.
* If both ``Matrix`` and ``isotropic parameter`` are given, then
  isotropic part of the matrix is ignored.
* If both ``Matrix`` and ``Symmetric anisotropy`` are given, then
  symmetric anisotropic part of the matrix is ignored.

.. hint::
  For on-site anisotropy parameters the atom labels are the same and the unit
  cell of the second atom is always :math:`(0,0,0)`, i.e.

  .. code-block:: text

    Fe1 Fe1 0 0 0



.. dropdown:: Examples

  Usually either a full matrix is given, i.e.

  .. code-block:: text

    Fe1 Fe2 1 0 0
    Matrix
     1   -1  0
     2    3  0.3
    -0.43 0 -0.5

  or at least one of other parts (Isotropic, symmetric anisotropic or antisymmetric anisotropic)
  is given, i.e.

  .. code-block:: text

    Fe1 Fe2 1 0 0 1

  or

  .. code-block:: text

      Fe1 Fe2 1 0 0 1
      DMI 1 0 -0.4

  or

  .. code-block:: text

      Fe1 Fe2 1 0 0
      DMI 1 0 -0.4
      Symmetric anisotropy
       1    0.27 -0.43
       0.27 0.5   0.3
      -0.43 0.3  -1.5
