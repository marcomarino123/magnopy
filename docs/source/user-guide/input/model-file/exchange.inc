.. _user-guide_input_model-file_exchange:

Exchange parameters (bilinear)
==============================

.txt file
---------

Parameters of the bilinear exchange part of the Hamiltonian:

.. math::
  \boldsymbol{S_i}
  \boldsymbol{J_{ij}}
  \boldsymbol{S_j}

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 24-47
  :language: text

.. dropdown:: Description

  ======  ========================================================================
  Line    Content
  ======  ========================================================================
  1       Section separator (10 or more ``=`` symbols)
  2       One or two blocks, the order is fixed:

          * ``exchange`` keyword.

            * Required.
            * Full word is checked, case-insensitive.

          * ``units``

            * Optional.
            * Only first letter is actually checked, case-insensitive.
            * Recognized values:

              * ``meV`` -  :math:`10^{-3}` electron-Volt (default)
              * ``eV`` -  electron-Volt
              * ``J`` - Joule
              * ``K`` - Kelvin
              * ``Ry`` - Rydberg units of energy

            Defines the units of the exchange parameters.

  3       Subsection separator (10 or more ``-`` symbols)
  4       Five blocks, separated by spaces, the order is fixed:

          * ``atom-1``

            * Required.
            * Should be consistent with :ref:`user-guide_input_model-file_atoms` section.
            * Case-sensitive.

            Label of the first atom (the one in the (0,0,0) unit cell).

          * ``atom-2``

            * Required.
            * Should be consistent with :ref:`user-guide_input_model-file_atoms` section.
            * Case-sensitive.

            Label of the second atom (the one in the (i,j,k) unit cell).

          * ``i j k``

            * Required.

            Relative coordinates of the cell for atom-2. Three integers, separated
            by spaces. Second atom is understood to be located in the cell with the
            origin at the

            .. math::
              \boldsymbol{r}
              =
              i\cdot\boldsymbol{a}
              +
              j\cdot\boldsymbol{b}
              +
              k\cdot\boldsymbol{c}

            where :math:`\boldsymbol{a}`, :math:`\boldsymbol{b}`, :math:`\boldsymbol{c}`
            are the lattice vectors

  5       Isotropic part of the exchange matrix, optional. Two blocks, separated by spaces:

          * ``isotropic`` keyword

            * Only the first letter is actually checked, case-insensitive.

          * ``Jiso``

            * One number.

            Values of isotropic exchange

  6       Dzyaroshinsky-Moria interaction vector, optional.
          Four blocks, separated by spaces, the order is fixed:

          * ``DMI`` keyword

            * Only the first letter is actually checked, case-insensitive.

          * ``Dx``

            * One number.

            x component of the DMI vector

          * ``Dy``

            * One number.

            y component of the DMI vector

          * ``Dz``

            * One number.

            z component of the DMI vector


  7-10    Full matrix of exchange parameter, optional. Four lines.

          * ``matrix`` keyword

            * Only the first letter is actually checked, case-insensitive.

          * line 5: Three numbers, separated by spaces: Jxx Jxy Jxz
          * line 6: Three numbers, separated by spaces: Jyx Jyy Jyz
          * line 7: Three numbers, separated by spaces: Jzx Jzy Jzz

  11      Symmetric anisotropic part of full matrix of exchange parameter, optional.
          Six entries, separated by spaces:

          * ``symmetric-anisotropy`` keyword

            * Only the first letter is actually checked, case-insensitive.

          * ``Sxx Syy Sxy Sxz Syz``

            * Five numbers, separated by spaces.
            * The order is fixed.
            * In a matrix form they translates into:

            .. math::
              \boldsymbol{J^{SA}}
              =
              \begin{pmatrix}
              S^{xx} & S^{xy} & S^{xz} \\
                S^{xy} & S^{yy} & S^{yz} \\
                S^{xz} & S^{yz} & -S^{xx} - S^{yy} \\
              \end{pmatrix}

  12      Subsection separator (10 or more ``-`` symbols)
  13      Specifications of bonds
  14      Subsection separator (10 or more ``-`` symbols)
  15-22   Specification of the last bond.
  23      Subsection separator (10 or more ``=`` symbols)
  24      Section separator (10 or more ``=`` symbols)
  ======  ========================================================================


  .. note::
    At least one of the optional blocks with the parameter's value has to be present
    for each bond

  Priority of parameter parts:

  * ``Istoropic`` (:math:`J^{I}`) overwrites isotropic part of ``Matrix`` (:math:`\boldsymbol{J^{M}}`):

    .. math::
      \boldsymbol{J}
      =
      \boldsymbol{J^{M}}
      +
      (J^{I} - \dfrac{Tr(\boldsymbol{J^{M}})}{3})\cdot\boldsymbol{I}

    where :math:`\boldsymbol{I}` is a :math:`3\times3` identity matrix.

  * ``DMI`` (:math:`\boldsymbol{J^{A}}`) overwrites antisymmetric part of ``Matrix`` (:math:`\boldsymbol{J^{M}}`):

    .. math::
      \boldsymbol{J^A}
      =
      \begin{pmatrix}
        0 & D^z & -D^y \\
        -D^z & 0 & D^x \\
        D^y & -D^x & 0 \\
      \end{pmatrix}

    .. math::
      \boldsymbol{J}
      =
      \boldsymbol{J^{M}}
      +
      \boldsymbol{J^A}
      -\dfrac{\boldsymbol{J^{M}} - (\boldsymbol{J^{M}})^T}{2}

    where :math:`\boldsymbol{I}` is a :math:`3\times3` identity matrix.

  * ``Symmetric anisotropy`` (:math:`\boldsymbol{J^{SA}}`) overwrites symmetric anisotropic part of
    ``Matrix`` (:math:`\boldsymbol{J^{M}}`):

    .. math::
      \boldsymbol{J}
      =
      \boldsymbol{J^{M}}
      -
      (\dfrac{\boldsymbol{J^{M}}
      +
      (\boldsymbol{J^{M}})^T}{2}
      -
      \dfrac{Tr(\boldsymbol{J^{M}})}{3}\cdot\boldsymbol{I})
      +
      \boldsymbol{J^{SA}}

    where :math:`\boldsymbol{I}` is a :math:`3\times3` identity matrix.

.. dropdown:: Examples

  Usually either a full matrix is given, i.e.

  .. code-block:: text

    -------------
    Fe1 Fe2 1 0 0
    Matrix
    1   -1  0
    2    3  0.3
    -0.43 0 -0.5
    -------------

  or at least one of other parts (Isotropic, symmetric anisotropic or antisymmetric anisotropic)
  is given, i.e.

  .. code-block:: text

    -------------
    Fe1 Fe2 1 0 0
    Isotropic 1
    -------------

  or

  .. code-block:: text

      ---------------
      Fe1 Fe2 1 0 0 1
      DMI 1 0 -0.4
      ---------------

  or

  .. code-block:: text

    -----------------------------------------
    Fe1 Fe2 1 0 0
    DMI 1 0 -0.4
    Symmetric-anisotropy 1 0.27 -0.43 0.5 0.3
    -----------------------------------------

.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,32-43,52
  :language: text

.. dropdown:: Description

  All names of datasets, groups and attributes are lowercase.

  * Attributes

    * "units" - one of the following: "milli-electron-Volt", "electron-Volt", "Joule", "Kelvin", "Rydberg". Case-insensitive. Full word is
      checked.

  * Groups

    * <number from 1 to n>

      Every group describes one exchange parameter.
      There may be no groups.
      Inside each group four datasets are required:

      * "atom-1" - a string.
      * "atom-2" - a string.
      * "ijk" - three integers.
      * "matrix" - :math:`3\times3` matrix of numbers.
