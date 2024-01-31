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
* line 2: From one to three entries, separated by spaces:

  - ``Cell`` keyword. Only the first letter is actually checked.
  - (optional) ``<Units>``. One of the predefined keywords. Define the units of the lattice vectors.
    Allowed values are

    - ``Angstrom`` (default)
    - ``Bohr``

    Note: Only the first letter is actually checked.

  - (optional) ``<Scale>``. One or three numbers, separated by spaces.
    Common or individual scale factors for the lattice vectors.

    - ``<s>`` - scale factor for the whole cell.

    - ``<s_a s_b s_c>`` - individual scale factors for each lattice vector.

* line 3: Three numbers, separated by spaces. Coordinates of the first lattice vector.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_a``.
* line 4: Three numbers, separated by spaces. Coordinates of the second lattice vector.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_b``.
* line 5: Three numbers, separated by spaces. Coordinates of the third lattice vector.
  If ``<Scale>`` is present, then the coordinates are multiplied by ``s`` or ``s_c``.
* line 6: Section separator (10 or more ``=`` symbols)

.. dropdown:: Examples

  Below we ist several ways to specify the same lattice:

  .. code-block:: text
    :linenos:

    ==========
    Cell
    1 0 0
    0 2 0
    0 0 3
    ==========

  .. code-block:: text
    :linenos:

    ==========
    Cell Angstrom
    1 0 0
    0 2 0
    0 0 3
    ==========

  .. code-block:: text
    :linenos:

    ==========
    Cell Bohr
    10.529177210903 0 0
    0 2 0
    0 0 3
    ==========
