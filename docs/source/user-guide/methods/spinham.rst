.. _user-guide_methods_spinham:

****************
Spin Hamiltonian
****************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/unit-vector.txt
  * .. include:: page-notations/spin-unit-vector-operator.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/transpose-complex-conjugate.txt
  * .. include:: page-notations/trace.txt

Before we define the Hamiltonian let us define the system, which we are solving:

* Let :math:`\vec{r}_m` :math:`(m = 1, ..., M)` be the Bravais lattice vectors
  that define the position of each cell.
* Each unit cell contains a set of :math:`N` atoms, located at the positions
  :math:`\vec{r}_a` :math:`(a = 1, ..., N)` with respect to the position of the cell.
  Therefore, each atom is located at the position
  :math:`\vec{r}_{ma} = \vec{r}_m + \vec{r}_a`.
* Each atom is characterized by the spin :math:`\vec{S}_{ma} = \hbar S_a \hat{S}_{ma}`.

The Hamiltonian is usually given in some coordinate frame, which we call
a global :math:`xyz` reference frame. Then the Hamiltonian is given by:

.. math::
  H
  =
  \dfrac{1}{2} \sum_{m, \vec{d}_{ab}, a\ne b\vert_{\vec{d}_{ab} = \vec{0}}}
  \vec{S}_{ma}^{\dagger} \boldsymbol{J_{ab}}(\vec{d}_{ab})\vec{S}_{m+d,b}
  + \sum_{m,a} \vec{S}_{ma}^{\dagger} \boldsymbol{A_a} \vec{S}_{ma}
  + \mu_B\vec{H}^{\dagger}\sum_{m,a} g_a \vec{S}_{ma}

.. dropdown:: Bra-ket notation

  .. math::
    H
    =
    \dfrac{1}{2} \sum_{m, \vec{d}_{ab}, a\ne b\vert_{\vec{d}_{ab} = \vec{0}}}
    \langle S_{ma}\vert xyz\rangle
    \langle xyz \vert J_{ab}(\vec{d}_{ab}) \vert xyz \rangle
    \langle xyz \vert S_{m+d,b}\rangle
    +
    \sum_{m,a} \langle S_{ma} \vert xyz \rangle
    \langle xyz \vert A_a \vert xyz\rangle
    \langle xyz \vert S_{ma} \rangle
    +
    \mu_B\langle H\vert xyz\rangle\sum_{m,a} g_a
    \langle xyz \vert S_{ma}\rangle

where vector :math:`\vec{d}_{ab} = \vec{r}_{m+d} - \vec{r}_m`  runs over the neighbors.
:math:`\boldsymbol{J_{ab}}(\vec{d}_{ab})` is a :math:`3\times3` exchange matrix, which includes:

* Isotropic exchange:

  .. math::

    J_{ab}^{iso} = \dfrac{\mathrm{Tr}(\boldsymbol{J_{ab}})}{3}

* Symmetric anisotropy:

  .. math::

    \boldsymbol{J_{ab}^{aniso-symm}} = \dfrac{\boldsymbol{J_{ab}} + \boldsymbol{J_{ab}}^T}{2} - J_{ab}^{iso}\cdot \boldsymbol{I}

  where :math:`\boldsymbol{I}` is a :math:`3\times3` identity matrix.

* Antisymmetric anisotropy (Dzyaloshinskii-Moriya Interaction, DMI)

  .. math::

    \boldsymbol{J_{ab}^{aniso-asymm}} = \dfrac{\boldsymbol{J_{ab}} - \boldsymbol{J_{ab}}^T}{2}
    =
    \begin{pmatrix}
      0    & D_z  & -D_y \\
      -D_z & 0    & D_x  \\
      D_y  & -D_x & 0    \\
    \end{pmatrix}

  It is often described by the vector :math:`\vec{D} = (D_x,D_y,D_z)^T`.

:math:`\boldsymbol{A_a}` is a :math:`3\times3` on-site anisotropy matrix.
The third term describes the Zeeman interaction with the external magnetic field.

.. note::

  * The double counting is explicitly present in the summation:
    for the pair :math:`(m,a; m+d,b)` the pair :math:`(m+d,b; m,a)` is included.
  * Spin vectors are not normalized.

For the simplicity of the latter discussion we combine the exchange and anisotropy terms
under one sum, defining
:math:`\boldsymbol{A_a} = \dfrac{1}{2}\boldsymbol{J_{aa}}(\vec{d}_{aa}=\vec{0})`,
then the Hamiltonian is written as:

.. include:: repeated-formulas/hamiltonian-main-any.txt

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \vec{d}_{ab}, a, b}
    \langle S_{ma}\vert xyz\rangle
    \langle xyz \vert J_{ab}(\vec{d}_{ab})\vert xyz \rangle
    \langle xyz \vert S_{m+d,b} \rangle
    + \mu_B \langle H \vert xyz\rangle\sum_{m,a} g_a
    \langle xyz\vert S_{ma} \rangle

Symmetries of the Hamiltonian
=============================

The Hamiltonian has the following symmetries:

.. include:: repeated-formulas/spinham-parameter-symmetries.txt
