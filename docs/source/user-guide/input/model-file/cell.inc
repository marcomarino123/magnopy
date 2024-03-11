.. _user-guide_input_model-file_cell:

Cell
====

.txt file
---------

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 1-7
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     One or two blocks, separated by spaces:

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
  3     ``scale``

        * Optional
        * One or three numbers, separated by spaces
        * Recognized values:

          * ``s`` - one number, scale factor for the whole cell.

          * ``s^x s^y s^z`` - three numbers, individual scale factors for
            each lattice vector. The order is fixed.

        The scale factor, that behaves in the same way as in |POSCAR|_ file:

        * If one positive number, then it is a general scale factor that is applied to each
          lattice vector and to the atomic positions if they are provided in absolute coordinates
          (``x y z`` and not ``r1 r2 r3``).
        * If one negative number, then the absolute value is understood as
          the desired volume of the unit cell and scale factor is computed automatically.
        * Can not be zero.
        * If three positive numbers, then first is the scale factor of x component, second is
          the scale factor of y component, and third is the scale factor of z component
          for lattice vectors and atom position if they are provided in absolute coordinates.
        * If three numbers, then all have to be non-zero and positive

  4     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the first lattice vector :math:`\boldsymbol{a_1}`.
        If ``<scale>`` is present:

        * One positive number, then the lattice vector is :math:`s\cdot \boldsymbol{a_1}`
        * One negative number number, then the lattice vector is
          :math:`\dfrac{\vert s\vert\cdot \boldsymbol{a_1}}{\vert\boldsymbol{a_1}\cdot (\boldsymbol{a_2}\times \boldsymbol{a_3})\vert}`
        * Three positive numbers, then the lattice vector is
          :math:`(s^x\cdot a_1^x, s^y\cdot a_1^y, s^z\cdot a_1^z)^T`

  5     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the second lattice vector :math:`\boldsymbol{a_2}`.
        If ``<scale>`` is present:

        * One positive number, then the lattice vector is :math:`s\cdot \boldsymbol{a_2}`
        * One negative number number, then the lattice vector is
          :math:`\dfrac{\vert s\vert\cdot \boldsymbol{a_2}}{\vert\boldsymbol{a_1}\cdot (\boldsymbol{a_2}\times \boldsymbol{a_3})\vert}`
        * Three positive numbers, then the lattice vector is
          :math:`(s^x\cdot a_2^x, s^y\cdot a_2^y, s^z\cdot a_2^z)^T`

  6     Three numbers, separated by spaces. The order is fixed.
        Coordinates of the third lattice vector :math:`\boldsymbol{a_3}`.
        If ``<scale>`` is present:

        * One positive number, then the lattice vector is :math:`s\cdot \boldsymbol{a_3}`
        * One negative number number, then the lattice vector is
          :math:`\dfrac{\vert s\vert\cdot \boldsymbol{a_3}}{\vert\boldsymbol{a_1}\cdot (\boldsymbol{a_2}\times \boldsymbol{a_3})\vert}`
        * Three positive numbers, then the lattice vector is
          :math:`(s^x\cdot a_3^x, s^y\cdot a_3^y, s^z\cdot a_3^z)^T`

  7     Section separator (10 or more ``=`` symbols)
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

    ================
    Cell Bohr
    1.88972612462577
    1 0 0
    0 2 0
    0 0 3
    ================

  .. code-block:: text

    =============
    Cell Angstrom
    2
    0.5 0 0
    0   1 0
    0   0 1.5
    =============

  .. code-block:: text

    ==========
    Cell
    2
    0.5 0 0
    0   1 0
    0   0 1.5
    ==========

  .. code-block:: text

    =============
    Cell Angstrom
    1 2 3
    1 0 0
    0 1 0
    0 0 1
    =============

  .. code-block:: text

    ==========
    Cell
    1 2 3
    1 0 0
    0 1 0
    0 0 1
    ==========


.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1-6,52
  :language: text

.. dropdown:: Description

  All names of datasets, groups and attributes are lowercase.

  Group's name: "cell".

  * Attributes

    * "units" - either "Angstrom" or "Bohr". Case-insensitive. Full word is
      checked.

  * Datasets

    * "a1" - three numbers.
    * "a2" - three numbers.
    * "a3" - three numbers.
