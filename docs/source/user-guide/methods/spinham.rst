.. _user-guide_methods_spinham:

****************
Spin Hamiltonian
****************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/transpose-complex-conjugate.inc
  * .. include:: page-notations/exchange-tensor.inc

* We define a Bravais lattice with primitve vectors
  :math:`\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}\}`.
  The Bravais lattice is composed of :math:`M=M_1 \times M_2 \times M_3`
  unit cells whose positions are given by

  .. math::
    \boldsymbol{r}_m
    =
    m_1\, \boldsymbol{a_1} + m_2\, \boldsymbol{a_2} + m_3\, \boldsymbol{a_3}

Each cell :math:`m` contains :math:`I` atoms, and ach atom in the cell
is denoted by :math:`(m,\,i)`. The atom has intra-cell positions
:math:`\boldsymbol{r}_i` and overall positions

  .. math::
    \boldsymbol{r}_{mi} = \boldsymbol{r}_m + \boldsymbol{r}_i

* Each atomic site in the lattice is populated with its own spin vector

  .. math::
    \ket{S_{mi}}=\hbar\,S_i \,\ket{f_{mi}}

  where :math:`S_i` is the spin modulus, and :math:`\ket{f_{mi}}` is a unit
  vector collinear to :math:`\ket{S_{mi}}`. :math:`\hbar` is henceforth set to 1.
  Spin vector components are given initially in the cartesian basis,
  :math:`^z\boldsymbol{S_{mi}}=\braket{\,x\,y\,z\,|S_{mi}}`.

* The bond between atoms :math:`(m,i)` and :math:`(m^{\prime},j)` is denoted by
  :math:`(m,i;m^{\prime},j)`.

* The Hamiltonian governing the interactions among all the lattice atomic spins is

  .. math::
    H &=
     \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
    \braket{\,S_{mi}\,|\, \boldsymbol{J}_{\boldsymbol{d}ij}\,|\, S_{m+d_{ij},j}\, }
    + \,\sum_{m,i}\,\braket{\,S_{mi}\,|\,\boldsymbol{A}_i\,|\,S_{mi}}
    + \mu_B \sum_{m,i}\, g_i\,\braket{\,h\,|\, S_{mi}\,}\\
    &=
    \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
    \braket{\,S_{mi}\,|\, x\,y\,z\,}
    \braket{\,x\,y\,z\,|\, \boldsymbol{J}_{\boldsymbol{d}ij}\,|\, x\,y\,z\,}
    \braket{\,x\,y\,z\,|\, S_{m+d_{ij},j}\, }
    + \,\sum_{m,i}\,\braket{\,S_{mi}\,|\,x\,y\,z\,}\,\braket{\,x\,y\,z\,|\,
    \boldsymbol{A}_i\,|\,x\,y\,z\,}\braket{\,x\,y\,z\,|\,S_{mi}}
    + \mu_B \braket{\,h\,|\, x\,y\,z\,}\,\sum_{m,i}\, g_i
    \braket{\, x\,y\,z\,|\, S_{mi}\,}
    \\ &=
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i\ne j\vert_{\boldsymbol{d}_{ij}} = \boldsymbol{0}}
    \,^z\boldsymbol{S}_{mi}^\dagger\,
    ^z\boldsymbol{J}_{\boldsymbol{d}ij}\,
    ^z\boldsymbol{S}_{m+d_{ij},j}\,
    + \,\sum_{m,i}\,
    ^z\boldsymbol{S}_{mi}^\dagger\,
    ^z\boldsymbol{A}_i\,
    ^z\boldsymbol{S}_{mi}\,
    +\,
    \mu_B\,^z\boldsymbol{h}^\dagger\,
    \sum_{m,i}\, g_i\, ^z\boldsymbol{S}_{mi}

  where the first sum runs over all the lattice bonds
  :math:`(m,i;m+\boldsymbol{d}_{ij},j)`: index :math:`m` runs over all cells of the
  lattice, indices :math:`i` and :math:`j` run over the atoms in each cell and the
  vector :math:`\boldsymbol{d}_{ij} = \boldsymbol{r}_{m+d_{ij}} - \boldsymbol{r}_m`
  runs over all the neighbors of atom :math:`(m,i)` up to a certain cutoff distance.
  Note that the vector :math:`\boldsymbol{d}_{ij}` is defined as a difference of two
  lattice vectors, and hence it is a lattice vector itself.

* The exchange tensor :math:`^z\boldsymbol{J}_{\boldsymbol{d}ij}` is a :math:`3\times3`
  matrix written in the :math:`\ket{xyz}` reference frame.  The exchange tensor
  is split into isotropic exchange, as well as into traceless symmetric
  and anti-symmetric anisotropy matrices as follows:

  .. math::
    ^z\boldsymbol{J}_{\boldsymbol{d}ij}
    =
    J_{ij}^{I}\,\boldsymbol{I}
    +
    \boldsymbol{J^{S}}_{\boldsymbol{d}ij}
    +
    \boldsymbol{J^{A}}_{\boldsymbol{d}ij}

  where :math:`\boldsymbol{I}` is a :math:`3\times 3` identity matrix.

  * The isotropic exchange is:

  .. math::
    J_{\boldsymbol{d}ij}^{I}
    =
    \dfrac{\mathrm{Tr}(\boldsymbol{^zJ}_{\boldsymbol{d}ij})}{3}

  * The traceless symmetric anisotropy is:

    .. math::
      \boldsymbol{J^{S}}_{\boldsymbol{d}ij}
      =
      \dfrac{^z\boldsymbol{J}_{\boldsymbol{d}ij}
      +
      ^z\boldsymbol{J}_{\boldsymbol{d}ij}^T}{2}
      -
      J_{\boldsymbol{d}ij}^{I}\,\boldsymbol{I}
      =
      \begin{pmatrix}
        S_{\boldsymbol{d}ij}^{xx} & S_{\boldsymbol{d}ij}^{xy} & S_{\boldsymbol{d}ij}^{xz} \\
        S_{\boldsymbol{d}ij}^{yx} & S_{\boldsymbol{d}ij}^{yy} & S_{\boldsymbol{d}ij}^{yz} \\
        S_{\boldsymbol{d}ij}^{zx} & S_{\boldsymbol{d}ij}^{zy} & S_{\boldsymbol{d}ij}^{zz} \\
      \end{pmatrix}

    where
    :math:`S^{xx}_{\boldsymbol{d}ij}+S^{yy}_{\boldsymbol{d}ij}+S^{zz}_{\boldsymbol{d}ij}=0`.

  * The antisymmetric anisotropy that encapsulates the Dzyaloshinskii-Moriya
    (DM) Interaction is:

    .. math::
      \boldsymbol{J^{A}}_{\boldsymbol{d}ij}
      =
      \dfrac{^z\boldsymbol{J}_{\boldsymbol{d}ij}
      -
      \,^z\boldsymbol{J}_{\boldsymbol{d}ij}^T}{2}
      =
      \begin{pmatrix}
        0                       & D^z_{\boldsymbol{d}ij}  & -D^y_{\boldsymbol{d}ij} \\
        -D^z_{\boldsymbol{d}ij} & 0                       & D^x_{\boldsymbol{d}ij}  \\
        D^y_{\boldsymbol{d}ij}  & -D^x_{\boldsymbol{d}ij} & 0                       \\
      \end{pmatrix}

    :math:`\boldsymbol{J^{A}}_{\boldsymbol{d}ij}` is often recast in terms of the DM
    vector :math:`\boldsymbol{D}_{\boldsymbol{d}ij} = (D^x_{\boldsymbol{d}ij},\,D^y_{\boldsymbol{d}ij},\,D^z_{\boldsymbol{d}ij})^T`.

* The intra-atomic anisotropy tensor :math:`\boldsymbol{A}_i` is a symmetric
  :math:`3\times3` matrix.

* The final term describes the Zeeman interaction of an external magnetic field
  :math:`\boldsymbol{h}` with the atomic spins where the interaction strength is
  given by the atomic g-factors :math:`g_i`.

* The spin Hamiltonian can be recast in the simplified form

  .. include:: repeated-formulas/hamiltonian-main-any.inc

  by defining :math:`\dfrac{1}{2}\,^z\boldsymbol{J}_{\boldsymbol{0},ii}\,=\,^z\boldsymbol{A}_i`


* The exchange tensors obey the following symmetry property, that ensures that the spin
  Hamiltonian is hermitian:

  .. include:: repeated-formulas/spinham-parameter-symmetries.inc

.. note::

  The summation in the exchange piece of the Hamiltonian double-counts each bond,
  because both :math:`(m,i; m+d_{ij},j)` and :math:`(m+d_{ij},j; m,i)` are included in
  the sum.
