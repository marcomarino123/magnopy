.. _user-guide_methods_spinham:

****************
Spin Hamiltonian
****************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/unit-vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/transpose-complex-conjugate.txt
  * .. include:: page-notations/trace.txt

Before we define the Hamiltonian let us define the system, which we are solving:

* Let :math:`\boldsymbol{r_m}` :math:`(m = 1, ..., M)` be the Bravais lattice vectors
  that define the position of each cell.
* Each unit cell contains a set of :math:`N` atoms, located at the positions
  :math:`\boldsymbol{r_i}` :math:`(i = 1, ..., N)` with respect to the position of the cell.
  Therefore, each atom is located at the position
  :math:`\boldsymbol{r_{mi}} = \boldsymbol{r_m} + \boldsymbol{r_i}`.
* Each atom is characterized by the spin vector
  :math:`\boldsymbol{S_{mi}} = \hbar S_i \boldsymbol{\hat{S}_{mi}}`.

The Hamiltonian is usually given in some coordinate frame, which we call
a global :math:`xyz` reference frame. Then the Hamiltonian is written as

.. math::
  H
  =
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i\ne j\vert_{\boldsymbol{d_{ij}} = \boldsymbol{0}}}
  \boldsymbol{S_{mi}}^{\dagger}
  \boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})
  \boldsymbol{S_{m+d_{ij},j}}
  + \sum_{m,i}
  \boldsymbol{S_{mi}}^{\dagger}
  \boldsymbol{A_i}
  \boldsymbol{S_{mi}}
  +
  \mu_B\boldsymbol{h}^{\dagger}
  \sum_{m,i} g_i \boldsymbol{S_{mi}}

.. dropdown:: Bra-ket notation

  .. math::
    H
    =
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d_{ij}}, i\ne j\vert_{\boldsymbol{d_{ij}} = \boldsymbol{0}}}
    \langle S_{mi}\vert xyz\rangle
    \langle xyz \vert J_{ij}(\boldsymbol{d_{ij}}) \vert xyz \rangle
    \langle xyz \vert S_{m+d_{ij},j}\rangle
    +
    \sum_{m,i} \langle S_{mi} \vert xyz \rangle
    \langle xyz \vert A_i \vert xyz\rangle
    \langle xyz \vert S_{mi} \rangle
    +
    \mu_B\langle H\vert xyz\rangle
    \sum_{m,i} g_i
    \langle xyz \vert S_{mi}\rangle

where vector :math:`\boldsymbol{d_{ij}} = \boldsymbol{r}_{m+d_{ij}} - \boldsymbol{r_m}`  runs over the neighbors.
:math:`\boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})` is a :math:`3\times3` exchange matrix, which includes:

* Isotropic exchange:

  .. math::

    J_{ij}^{iso} = \dfrac{\mathrm{Tr}(\boldsymbol{J_{ij}})}{3}

* Symmetric anisotropy:

  .. math::

    \boldsymbol{J_{ij}^{aniso-symm}} = \dfrac{\boldsymbol{J_{ij}} + \boldsymbol{J_{ij}}^T}{2} - J_{ij}^{iso}\cdot \boldsymbol{I}

  where :math:`\boldsymbol{I}` is a :math:`3\times3` identity matrix.

* Antisymmetric anisotropy (Dzyaloshinskii-Moriya Interaction, DMI)

  .. math::

    \boldsymbol{J_{ij}^{aniso-asymm}} = \dfrac{\boldsymbol{J_{ij}} - \boldsymbol{J_{ij}}^T}{2}
    =
    \begin{pmatrix}
      0    & D^z  & -D^y \\
      -D^z & 0    & D^x  \\
      D^y  & -D^x & 0    \\
    \end{pmatrix}

  It is often described by the vector :math:`\boldsymbol{D} = (D^x,D^y,D^z)^T`.

:math:`\boldsymbol{A_i}` is a :math:`3\times3` on-site anisotropy matrix.
Third term describes the Zeeman interaction with the external magnetic field.

.. note::

  * The double counting is explicitly present in the summation:
    for the pair :math:`(m,i; m+d_{ij},j)` the pair :math:`(m+d_{ij},j; m,i)` is included.
  * Spin vectors are not normalized.

For the simplicity of the latter discussion we combine the exchange and anisotropy terms
under one sum, defining
:math:`\boldsymbol{A_i} = \dfrac{1}{2}\boldsymbol{J_{ii}}(\boldsymbol{d}_{ii}=\boldsymbol{0})`,
then the Hamiltonian is written as

.. include:: repeated-formulas/hamiltonian-main-any.txt

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \boldsymbol{d_{ij}}, i, j}
    \langle S_{mi}\vert xyz\rangle
    \langle xyz \vert J_{ij}(\boldsymbol{d_{ij}})\vert xyz \rangle
    \langle xyz \vert S_{m+d_{ij},j} \rangle
    + \mu_B \langle H \vert xyz\rangle\sum_{m,i} g_i
    \langle xyz\vert S_{mi} \rangle

Symmetries of the Hamiltonian
=============================

The Hamiltonian has the following symmetries:

.. include:: repeated-formulas/spinham-parameter-symmetries.txt
