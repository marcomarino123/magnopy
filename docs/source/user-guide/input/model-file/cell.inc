.. _user-guide_input_model-file_cell:

Cell
====

.txt file
---------

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 1-6
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     From one to three blocks, separated by spaces:

        * ``cell`` keyword

          * Required.
          * Full word is checked, case-insensitive.

        * ``units``

          * Optional.
          * Only first letter is checked, case-insensitive.
          * Recognized values:

            * ``Angstrom`` (default)
            * ``Bohr``

          Defines the units of the lattice vectors.

        * ``scale``

          * Optional
          * One or three numbers, separated by spaces
          * Recognized values:

            * ``s`` - one number, scale factor for the whole cell.

            * ``s_a s_b s_c`` - three numbers, individual scale factors for
              each lattice vector. The order is fixed.

          Common or individual scale factors for the lattice vectors.

        Note: The order of ``<scale>`` and ``<units>`` can be changed, but
        ``cell`` keyword has to be at the beginning of the line.

  3     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the first lattice vector :math:`\boldsymbol{a_1}`.
        If ``<scale>`` is present, then the coordinates are multiplied by
        ``s`` or ``s_a``.
  4     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the second lattice vector :math:`\boldsymbol{a_2}`.
        If ``<scale>`` is present, then the coordinates are multiplied by
        ``s`` or ``s_b``.
  5     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the third lattice vector :math:`\boldsymbol{a_3}`.
        If ``<scale>`` is present, then the coordinates are multiplied by
        ``s`` or ``s_c``.
  6     Section separator (10 or more ``=`` symbols)
  ====  ========================================================================

.. dropdown:: Examples

  Below we list several ways to specify the same lattice:

  .. code-block:: text

    ==========
    Cell
    1 0 0
    0 2 0
    0 0 3
    ==========

  .. code-block:: text

    =============
    Cell Angstrom
    1 0 0
    0 2 0
    0 0 3
    =============

  .. code-block:: text

    ====================
    Cell Bohr
    1.88972612462577 0 0
    0 3.77945224925154 0
    0 0 5.66917837387731
    ====================

  .. code-block:: text

    ==========================
    Cell Bohr 1.88972612462577
    1 0 0
    0 2 0
    0 0 3
    ==========================

  .. code-block:: text

    ===============
    Cell Angstrom 2
    0.5 0 0
    0   1 0
    0   0 1.5
    ===============

  .. code-block:: text

    ===============
    Cell 2 Angstrom
    0.5 0 0
    0   1 0
    0   0 1.5
    ===============

  .. code-block:: text

    ==========
    Cell 2
    0.5 0 0
    0   1 0
    0   0 1.5
    ==========

  .. code-block:: text

    ===================
    Cell Angstrom 1 2 3
    1 0 0
    0 1 0
    0 0 1
    ===================

  .. code-block:: text

    ===================
    Cell 1 2 3 Angstrom
    1 0 0
    0 1 0
    0 0 1
    ===================

  .. code-block:: text

    ==========
    Cell 1 2 3
    1 0 0
    0 1 0
    0 0 1
    ==========


.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1-6,54
  :language: text

.. dropdown:: Description

  All names of datasets, groups and attributes are lowercase.

  * Attributes

    * "units" - either "Angstrom" or "Bohr".

  * Datasets

    * "a1" - three numbers.
    * "a2" - three numbers.
    * "a3" - three numbers.
