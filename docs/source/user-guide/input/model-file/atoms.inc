.. _user-guide_input_model-file_atoms:

Atoms
=====

.txt file
---------

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 6-12
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     One or two blocks, separated by spaces, the order is fixed:

        * ``atoms`` keyword

          * Required.
          * Full word is checked, case-insensitive.

        * ``units``

          * Optional.
          * Only first letter is checked, case-insensitive.
          * Recognized values:

            * ``Angstrom`` (default)
            * ``Bohr``

          Defines the units of the atom's coordinates.
          Affect the result only if <x y z> is present in the header (line 3).

  3     Data headers. Blocks are separated by spaces. Order is arbitrary.
        Each block defines the data interpretation of the corresponding column.
        If some block has to be skipped for some atoms use ``-`` symbol.

        * ``name`` keyword

          * Required.
          * Full word is checked, case-insensitive.

          Name of the atom.

        * ``r1``, ``r2``, ``r3`` keywords

          * Either <r1 r2 r3> or <x y z> have to be present.
            If both present, then they should be consistent.
          * Full word is checked, case-insensitive.

          Relative coordinates of the atom in the unit cell:

          .. math::
            \boldsymbol{r}
            =
            r_1\boldsymbol{a}
            +
            r_2\boldsymbol{b}
            +
            r_3\boldsymbol{c}

        * ``x``, ``y``, ``z`` keywords

          * Either <r1 r2 r3> or <x y z> have to be present.
            If both present, then they should be consistent.
          * Full word is checked, case-insensitive.

          Absolute coordinates of the atom in the unit cell.

        * ``sx``, ``sy``, ``sz``, ``s``, ``sp``, ``st`` keywords

          * Optional.
          * Full word is checked, case-insensitive.
          * Recognized combinations:

            * ``s`` - spin value. It is oriented along
              :math:`z` direction, i.e. :math:`\boldsymbol{S} = (0,\,0,\,S)^T`.

            * ``sx``, ``sy``, ``sz`` - spin vector. The order is fixed.
              :math:`\boldsymbol{S} = (S^x,\,S^y,\,S^z)^T`.

            * ``sp``, ``st``, ``s`` - polar (:math:`\phi`) and
              azimuthal (:math:`\theta`) angles and spin value.
              Two angles, that define the direction of the spin as described
              :ref:`here <user-guide_methods_spin-rotations>`.

              Angles are given in degrees :math:`0^{\circ} \le \phi \le 360^{\circ}`,
              :math:`0^{\circ} \le \theta \le 180^{\circ}`

              .. math::
                \boldsymbol{S}
                =
                S
                \begin{pmatrix}
                  \cos\phi\sin\theta \\
                  \sin\phi\sin\theta \\
                  \cos\theta
                \end{pmatrix}

          Spin momentum (:math:`\boldsymbol{S}`)

        * ``lx``, ``ly``, ``lz``, ``l``, ``lp``, ``lt`` keywords

          * Optional.
          * Full word is checked, case-insensitive.
          * See spin keywords for the allowed combinations.

          Orbital momentum (:math:`\boldsymbol{L}`).

        * ``jx``, ``jy``, ``jz``, ``j``, ``jp``, ``jt`` keywords

          * Optional.
          * Full word is checked, case-insensitive.
          * See spin keywords for the allowed combinations.

          Total momentum (:math:`\boldsymbol{J}`).

        * ``g`` keyword

          * Optional.
          * Full word is checked, case-insensitive.

          g factor of an atom.

        * ``q`` keyword

          * Optional.
          * Full word is checked, case-insensitive.

          Electric charge of an atom.

  4-6   Information about the atoms.
        The data are recognized with respect to the header at line 3.
  7     Section separator (10 or more ``=`` symbols)
  ====  ========================================================================


.. dropdown:: Examples

  Below we list a few ways to provide the same two atoms with the same positions and
  without the spin.

  The cell for all provided cases is

  .. code-block:: text

    ==========
    Cell
    1 0 0
    0 2 0
    0 0 3
    ==========

  .. code-block:: text

    ================
    Atoms
    name r1  r2  r3
    Fe1  0   0   0.5
    Fe2  0.1 0.5 0
    ================

  .. code-block:: text

    ================
    Atoms Relative
    name r1  r2  r3
    Fe1  0   0   0.5
    Fe2  0.1 0.5 0
    ================

  .. code-block:: text

    ================
    Atoms Angstrom
    name x   y   z
    Fe1  0   0   0.5
    Fe2  0.1 0.5 0
    ================

  .. code-block:: text

    =============================================
    Atoms Bohr
    name x y z
    Fe1  0         0           2.8345891869386555
    Fe2  0.18897261246257702 1.8897261246257702 0
    =============================================

  Below we list a few ways to provide two atoms with the same spin in each case.

  .. code-block:: text

    =========================================================
    Atoms
    name r1  r2  r3  Sx                 Sy                 Sz
    Fe1  0   0   0.5 1.2247448713915892 1.2247448713915892 1
    Fe2  0.1 0.5 0   0  0  2
    =========================================================

  .. code-block:: text

    ========================
    Atoms
    name r1  r2  r3  sp st S
    Fe1  0   0   0.5 45 60 2
    Fe2  0.1 0.5 0   0   0 2
    ========================

  .. code-block:: text

    ========================
    Atoms
    name r1  r2  r3  st sp S
    Fe1  0   0   0.5 60 45 2
    Fe2  0.1 0.5 0   0   0 2
    ========================

  .. code-block:: text

    ========================
    Atoms
    name r1  r2  r3  st S st
    Fe1  0   0   0.5 60 2 45
    Fe2  0.1 0.5 0   0  2 0
    ========================


.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,7-24,54
  :language: text

.. dropdown:: Description

  All names of datasets and groups are lowercase.

  * Groups

    At least one group is required. Every group describes an atom.
    Inside each group following datasets are recognized:

    * "name" - a string
    * "position" - three numbers (relative position)
    * "spin" - three numbers
    * "g-factor" - one number
    * "charge" - one number
    * "orbital-moment" - three numbers
    * "total-moment" - three numbers
