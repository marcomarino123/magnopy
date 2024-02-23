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

.. code-block:: text
  :linenos:

  ====================
  Exchange <Units>
  --------------------
  atom-1 atom-2 i j k
  <Isotropic Jiso>
  <DMI Dx Dy Dz>
  <Matrix
  Jxx Jxy Jxz
  Jyx Jyy Jyz
  Jzx Jzy Jzz>
  <Symmetric-anisotropy Sxx Syy Sxy Sxz Syz>
  --------------------
  ...
  --------------------
  atom-1 atom-2 i j k
  <Isotropic Jiso>
  <DMI Dx Dy Dz>
  <Matrix
  Jxx Jxy Jxz
  Jyx Jyy Jyz
  Jzx Jzy Jzz>
  <Symmetric-anisotropy Sxx Syy Sxy Sxz Syz>
  --------------------
  ====================

.. dropdown:: Description

  * line 1: Section separator (10 or more ``=`` symbols)
  * line 2: One or two entries:

    - ``Exchange`` keyword. Only the first letter is actually checked.
    - ``<Units>``. One of the predefined keywords.
      Defines the units of the exchange parameters. Allowed values are

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

  .. note::
    At least one of the optional entries with the parameter's value has to be present
    in each bond

  * line 1: Five entries, separated by spaces:

    - ``A1`` - label of the first atom (the one in the (0,0,0) unit cell).
      Label has to be consistent with :ref:`user-guide_input_model-file_atoms` section.
    - ``A2`` - label of the second atom (the one in the (i,j,k) unit cell).
      Label has to be consistent with :ref:`user-guide_input_model-file_atoms` section.
    - ``i j k`` - Relative coordinates of the cell for Atom 2. Three integers, separated
      by spaces. Second atom is understood to be located in the cell with the origin at the
      :math:`\boldsymbol{r} = i\cdot\boldsymbol{a} + j\cdot\boldsymbol{b} + k\cdot\boldsymbol{c}`,
      where :math:`\boldsymbol{a}`, :math:`\boldsymbol{b}`, :math:`\boldsymbol{c}`
      are the lattice vectors
  * line 2: (optional) Isotropic part of the exchange matrix. Two entries, separated by spaces:

    - ``Isotropic`` keyword. Only the first letter is actually checked.
    - Value of isotropic parameter.
  * line 3: (optional) Dzyaroshinsky-Moria interaction vector.
    Also referred as antisymmetric anisotropic interaction. Four entries, separated by spaces:

    - ``DMI`` keyword. Only the first letter is actually checked
    - x component: :math:`D^x`
    - y component: :math:`D^y`
    - z component: :math:`D^z`
  * line 4-7: (optional) Full matrix of exchange parameter.

    - line 4: ``Matrix`` keyword. Only the first letter is actually checked.
    - line 5: Three numbers, separated by spaces: Jxx Jxy Jxz
    - line 6: Three numbers, separated by spaces: Jyx Jyy Jyz
    - line 7: Three numbers, separated by spaces: Jzx Jzy Jzz
  * line 8: (optional) Symmetric anisotropic part of full matrix of exchange parameter.
    Six entries, separated by spaces:

    - ``Symmetric-anisotropy`` keyword. Only the first letter is actually checked.
    - Five numbers, separated by spaces: ``Sxx Syy Sxy Sxz Syz``. In a matrix form they translates into:

      .. math::
        \boldsymbol{J^{SA}}
        =
        \begin{pmatrix}
          S^{xx} & S^{xy} & S^{xz} \\
          S^{xy} & S^{yy} & S^{yz} \\
          S^{xz} & S^{yz} & -S^{xx} - S^{yy} \\
        \end{pmatrix}

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

  ::

    Fe1 Fe2 1 0 0
    Matrix
    1   -1  0
    2    3  0.3
    -0.43 0 -0.5

  or at least one of other parts (Isotropic, symmetric anisotropic or antisymmetric anisotropic)
  is given, i.e.

  ::

    Fe1 Fe2 1 0 0
    Isotropic 1

  or

  ::

      Fe1 Fe2 1 0 0 1
      DMI 1 0 -0.4

  or

  ::

    Fe1 Fe2 1 0 0
    DMI 1 0 -0.4
    Symmetric-anisotropy 1 0.27 -0.43 0.5 0.3


.hdf5 file
----------


::

  spinham/                      # this is a Group
  ├─── ...
  ├─── exchange/                # this is a Group
  │    ├──> units               # this is a Dataset
  │    └─── parameters/         # this is a Group
  │         ├─── 1/             # this is a Group
  │         │    ├──> atom-1    # this is a Dataset
  │         │    ├──> atom-2    # this is a Dataset
  │         │    ├──> ijk       # this is a Dataset
  │         │    └──> matrix    # this is a Dataset
  │         ├─── ...            # this is a Dataset
  │         └─── n/             # this is a Group
  │              ├──> atom-1    # this is a Dataset
  │              ├──> atom-2    # this is a Dataset
  │              ├──> ijk       # this is a Dataset
  │              └──> matrix    # this is a Dataset
  └─── ...

.. dropdown:: Description

  All names of Datasets and Groups are lowercase.

  One Datasets is required:

  * "units" - one of the following: "meV", "eV", "Joule", "Kelvin", "Ry"

  One group is required:

  * "parameters"

    At least one group is required (:math:`n \ge 1`). Every group describes one parameter.
    Inside every group four Datasets are required:

    - "atom-1" - a string.
    - "atom-2" - a string.
    - "ijk" - three integers.

    - "matrix" - :math:`3\times3` matrix of numbers.
