.. _user-guide_methods_spinham:

****************
Spin Hamiltonian
****************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/transpose-complex-conjugate.inc
  * .. include:: page-notations/trace.inc
  * .. include:: page-notations/exchange-tensor.inc

* Let be a Bravais lattice that is described by the Bravais vectors
  :math:`\boldsymbol{r_m}` :math:`(m = 1, ..., M)` with primitive vectors
  :math:`\{\boldsymbol{a_1},\boldsymbol{a_2},\boldsymbol{a_3}\}`.

* Let each unit cell contain a set of :math:`I` atoms, where each atomic position
  :math:`\boldsymbol{r_i}` is measured  with respec to the cell origin.

* Let an atom at site :math:`i` in cell :math:`m` be denoted by :math:`(m,i)`.
  Then its atom position is
  :math:`\boldsymbol{r_{mi}} = \boldsymbol{r_m} + \boldsymbol{r_i}`.

* Each atomic site in the lattice is populated with its own spin vector
  :math:`\boldsymbol{S_{mi}} = \hbar \,S_i\, \boldsymbol{\hat{S}_{mi}}`,
  where :math:`S_i` is the spin modulus. :math:`\hbar` is henceforth set to 1.

* The bond between atoms :math:`(m,i)` and :math:`(m^{\prime},j)` is denoted by
  :math:`(m,i;m^{\prime},j)`.

* The Hamiltonian governing the interactions among all the lattice atomic spins is

  .. include:: repeated-formulas/hamiltonian-on-site-separate-any-classic.inc

  where the first sum runs over all the lattice bonds
  :math:`(m,i;m+\boldsymbol{d}_{ij},j)`: index :math:`m` runs over all cells of the
  lattice, indices :math:`i` and :math:`j` run over the atoms in each cell and the
  vector :math:`\boldsymbol{d}_{ij} = \boldsymbol{r}_{m+d_{ij}} - \boldsymbol{r}_m`
  runs over all the neighbors of atom :math:`(m,i)` up to a given cutoff distance.
  Note that the vector :math:`\boldsymbol{d}_{ij}` is defined as a difference of two
  lattice vectors, and hence it is a lattice vector itself.

* The exchange tensor :math:`\boldsymbol{J}_{ij}(\boldsymbol{d}_{ij})` is a
  :math:`3\times3` matrix that is split into isotropic exchange, as well as into
  traceless symmetric  and anti-symmetric anisotropy matrices as follows:

  .. math::
    \boldsymbol{J}_{\boldsymbol{d}ij}
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
    \dfrac{\mathrm{Tr}(\boldsymbol{J}_{\boldsymbol{d}ij})}{3}

  * The traceless symmetric anisotropy is:

    .. math::
      \boldsymbol{J^{S}}_{\boldsymbol{d}ij}
      =
      \dfrac{\boldsymbol{J}_{\boldsymbol{d}ij}
      +
      \boldsymbol{J}_{\boldsymbol{d}ij}^T}{2}
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
      \dfrac{\boldsymbol{J}_{\boldsymbol{d}ij}
      -
      \boldsymbol{J}_{\boldsymbol{d}ij}^T}{2}
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

  by defining
  :math:`\dfrac{1}{2}\boldsymbol{J}_{ii}(\boldsymbol{d}_{ii}=\boldsymbol{0})=\boldsymbol{A}_i`


* The exchange tensors possess the symmetry property, that ensures that the spin
  Hamiltonian is hermitian:

  .. include:: repeated-formulas/spinham-parameter-symmetries.inc

.. note::

  The summation in the exchange piece of the Hamiltonian double-counts each bond,
  because both :math:`(m,i; m+d_{ij},j)` and
  :math:`(m+d_{ij},j; m,i)` are included in it.

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
    \langle S_{mi}\vert xyz\rangle
    \langle xyz \vert J_{ij}(\boldsymbol{d_{ij}})\vert xyz \rangle
    \langle xyz \vert S_{m+d_{ij},j} \rangle
    + \mu_B \langle H \vert xyz\rangle\sum_{m,i} g_i
    \langle xyz\vert S_{mi} \rangle
