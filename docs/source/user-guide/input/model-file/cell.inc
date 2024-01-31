.. _user-guide_input_model-file_cell:

Cell
====

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
    Only the first letter is actually checked.
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
