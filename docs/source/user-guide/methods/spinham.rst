.. _user-guide_methods_spinham:

****************
Spin Hamiltonian
****************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/transpose-complex-conjugate.inc
  * .. include:: page-notations/trace.inc

* Let be a Bravais lattice that is described by the Bravais vectors
  :math:`\boldsymbol{r_m}` :math:`(m = 1, ..., M)`.

* Let each unit cell contain a set of :math:`I` atoms, where each atomic position
  :math:`\boldsymbol{r_i}` is measured  with respecto to the cell origin.

* Let an atom at site :math:`i` in cell :math:`m` be denoted by :math:`(m,i)`.
  Then its atom position is
  :math:`\boldsymbol{r_{mi}} = \boldsymbol{r_m} + \boldsymbol{r_i}`.

* Each atomic site in the lattice is populated with its own spin vector
  :math:`\boldsymbol{S_{mi}} = \hbar \,S_i\, \boldsymbol{\hat{S}_{mi}}`,
  where :math:`S_i` is the spin modulus. :math:`\hbar` is henceforth set to 1.

* The bond between atoms (m,i) and (m',j) is denoted by (m,i;m',j).

* The Hamiltonian governing the interactions among all the lattice atomic spins is

  .. include:: repeated-formulas/hamiltonian-on-site-separate-any-classic.inc

  where the first sum runs over all the lattice bonds
  :math:`(m,i;m+\boldsymbol{d_{i j}},j)` and the vector
  :math:`\boldsymbol{d_{ij}} = \boldsymbol{r}_{m+d_{ij}} - \boldsymbol{r_m}`
  runs over all the neighbors of atom :math:`(m,i)` up to a given cutoff distance.

* The exchange tensor :math:`\boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})` is a :math:`3\times3` matrix that
  is split into isotropic exchange, as well as into traceless symmetric  and anti-symmetric
  anisotropy matrices as follows:

  .. math::
    \boldsymbol{J}_{ij} = J_{ij}^{I}\,\boldsymbol{I}+\boldsymbol{J_{ij}^{S}}+\boldsymbol{J_{ij}^{A}}

  where :math:`\boldsymbol{I}` is a :math:`3\times 3` identity matrix.

  * The isotropic exchange is:

  .. math::
    J_{ij}^{I} = \dfrac{\mathrm{Tr}(\boldsymbol{J_{ij}})}{3}

  * The symmetric anisotropy is:

    .. math::
      \boldsymbol{J_{ij}^{S}} = \dfrac{\boldsymbol{J_{ij}} + \boldsymbol{J_{ij}}^T}{2} - J_{ij}^{I}\, \boldsymbol{I}
      =
      \begin{pmatrix}
        S_{ij}^{xx} & S_{ij}^{xy} & S_{ij}^{xz} \\
        S_{ij}^{yx} & S_{ij}^{yy} & S_{ij}^{yz} \\
        S_{ij}^{zx} & S_{ij}^{zy} & S_{ij}^{zz} \\
      \end{pmatrix}

    where :math:`S^{xx}_{ij}+S^{yy}_{ij}+S^{zz}_{ij}=0`.

  * The antisymmetric anisotropy that encapsulates the Dzyaloshinskii-Moriya
    (DM) Interaction is:

    .. math::
      \boldsymbol{J_{ij}^{A}} = \dfrac{\boldsymbol{J_{ij}} - \boldsymbol{J_{ij}}^T}{2}
      =
      \begin{pmatrix}
        0    & D^z  & -D^y \\
        -D^z & 0    & D^x  \\
        D^y  & -D^x & 0    \\
      \end{pmatrix}

    :math:`\boldsymbol{J_{ij}^{A}}` is often recast in terms of the DM
    vector :math:`\boldsymbol{D} = (D^x,\,D^y,\,D^z)^T`.

* The intra-atomic anisotropy tensor :math:`\boldsymbol{A_i}` is symmetric
  :math:`3\times3` matrix.

* The final term describes the Zeeman interaction of an external magnetic field
  :math:`\boldsymbol{h}` with the atomic spins where the interaction strength is
  given by the atomic g-factors :math:`g_i`.

* The spin Hamiltonian can be recast in the simplified form

  .. include:: repeated-formulas/hamiltonian-main-any.inc

  by defining
  :math:`\dfrac{1}{2}\boldsymbol{J_{ii}}(\boldsymbol{d}_{ii}=\boldsymbol{0})=\boldsymbol{A_i}`


* The Spin Hamiltonian possesses the symmetry property

  .. include:: repeated-formulas/spinham-parameter-symmetries.inc

.. note::

  The summation in the exchange piece of the Hamiltonian double-counts each bond,
  because both :math:`(m,i; m+d_{ij},j)` and
  :math:`(m+d_{ij},j; m,i)` are included in it.

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \boldsymbol{d_{ij}}, i, j}
    \langle S_{mi}\vert xyz\rangle
    \langle xyz \vert J_{ij}(\boldsymbol{d_{ij}})\vert xyz \rangle
    \langle xyz \vert S_{m+d_{ij},j} \rangle
    + \mu_B \langle H \vert xyz\rangle\sum_{m,i} g_i
    \langle xyz\vert S_{mi} \rangle
