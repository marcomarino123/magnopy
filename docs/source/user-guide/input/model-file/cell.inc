.. _user-guide_input_model-file_cell:

Cell
====

.txt file
---------

.. code-block:: text
  :linenos:

  ==========
  Cell <units> <scale>
  a_x a_y a_z
  b_x b_y b_z
  c_x c_y c_z
  ==========

.. dropdown:: Description

  * line 1: Section separator (10 or more ``=`` symbols)
  * line 2: From one to three blocks, separated by spaces:

    - ``Cell`` keyword. Only the first letter is actually checked.
    - (optional) ``<units>``.
      One of the predefined keywords.
      Defines the units of the lattice vectors. Allowed values are

      - ``Angstrom`` (default)
      - ``Bohr``

      Note: Only the first letter is actually checked.

    - (optional) ``<Scale>``. One or three numbers, separated by spaces.
      Common or individual scale factors for the lattice vectors.

      - ``<s>`` - scale factor for the whole cell.

      - ``<s_a s_b s_c>`` - individual scale factors for each lattice vector. The order is fixed.

        Note: The order of ``<Scale>`` and ``<Units>`` can be changed, but ``Cell`` keyword
        has to be at the beginning of the line.

  * line 3: Three numbers, separated by spaces. The order is fixed.
    Coordinates of the first lattice vector. If ``<Scale>`` is present, then the
    coordinates are multiplied by ``s`` or ``s_a``.
  * line 4: Three numbers, separated by spaces. The order is fixed.
    Coordinates of the second lattice vector. If ``<Scale>`` is present, then the
    coordinates are multiplied by ``s`` or ``s_b``.
  * line 5: Three numbers, separated by spaces. The order is fixed.
    Coordinates of the third lattice vector. If ``<Scale>`` is present, then the
    coordinates are multiplied by ``s`` or ``s_c``.
  * line 6: Section separator (10 or more ``=`` symbols)

.. dropdown:: Examples

  Below we list several ways to specify the same lattice:

  ::

    ==========
    Cell
    1 0 0
    0 2 0
    0 0 3
    ==========

  ::

    ==========
    Cell Angstrom
    1 0 0
    0 2 0
    0 0 3
    ==========

  ::

    ==========
    Cell Bohr
    1.88972612462577 0 0
    0 3.77945224925154 0
    0 0 5.66917837387731
    ==========

  ::

    ==========
    Cell Bohr 1.88972612462577
    1 0 0
    0 2 0
    0 0 3
    ==========

  ::

    ==========
    Cell Angstrom 2
    0.5 0 0
    0   1 0
    0   0 1.5
    ==========

  ::

    ==========
    Cell 2 Angstrom
    0.5 0 0
    0   1 0
    0   0 1.5
    ==========

  ::

    ==========
    Cell 2
    0.5 0 0
    0   1 0
    0   0 1.5
    ==========

  ::

    ==========
    Cell Angstrom 1 2 3
    1 0 0
    0 1 0
    0 0 1
    ==========

  ::

    ==========
    Cell 1 2 3 Angstrom
    1 0 0
    0 1 0
    0 0 1
    ==========

  ::

    ==========
    Cell 1 2 3
    1 0 0
    0 1 0
    0 0 1
    ==========


.hdf5 file
----------

::

  spinham/           # this is a Group
  ├─── ...
  ├─── cell/         # this is a Group
  │    ├──> units    # this is a Dataset
  │    ├──> scale    # this is a Dataset
  │    ├──> a1       # this is a Dataset
  │    ├──> a2       # this is a Dataset
  │    ├──> a3       # this is a Dataset
  └─── ...

.. dropdown:: Description

  All names of Datasets and Groups are lowercase.

  Five Datasets are required:

  * "units" - either "Angstrom" or "Bohr".
  * "scale" - three numbers.
  * "a1" - three numbers.
  * "a2" - three numbers.
  * "a3" - three numbers.
