.. _user-guide_input_model-file_atoms:

Atoms
=====

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
    Only the first letter is actually checked.
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

  - ``A1`` - Atom's label. Any string, that does not contain "#" or space symbols and
    starts with a letter (lowercase or uppercase) or a number.
    Atom's labels have to be unique.
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

.. _user-guide_input_model-file_notation:
