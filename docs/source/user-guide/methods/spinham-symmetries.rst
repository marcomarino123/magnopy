.. _user-guide_methods_spinham-symmetries:

***********************************
Spin Hamiltonian and its symmetries
***********************************


Before we define the Hamiltonian let us discuss some notation:

* Let :math:`\vec{r}_m` :math:`(m = 1, ..., M)` be the Bravais lattice vectors that define
  the position of each cell.
* Each unit cell contains a set of :math:`N` atoms, located at the positions
  :math:`\vec{r}_a` :math:`(a = 1, ..., N)` with respect to the position of the cell. Therefore,
  each atom is located at the position :math:`\vec{r}_{ma} = \vec{r}_m + \vec{r}_a`.
* Each atom is characterized by the spin :math:`\vec{S}_{ma} = \hbar S_a \hat{S}_{ma}`,
  where :math:`\hat{S}_{ma}` is a unit vector.

The Hamiltonian is usually given in some coordinate frame, which we call
a global :math:`\vert xyz \rangle` frame. Then the Hamiltonian is given by:

.. math::
  H = \dfrac{1}{2} \sum_{m, \vec{d}, a\ne b\vert_{\vec{d}= \vec{0}}} \vec{S}_{ma}^T J_{ab}(d_{ab})\vec{S}_{m+d,b}
  + \sum_{m,a} \vec{S}_{ma}^T A_a \vec{S}_{ma}
  + \mu_B\vec{H}^T\sum_{m,a} g_a \vec{S}_{ma}

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \vec{d}, a\ne b\vert_{\vec{d}= \vec{0}}} \langle S_{ma}\vert xyz\rangle
    \langle xyz \vert J_{ab}(d_{ab}) \vert xyz \rangle
    \langle xyz \vert S_{m+d,b}\rangle
    + \sum_{m,a} \langle S_{ma} \vert xyz \rangle
    \langle xyz \vert A_a \vert xyz\rangle
    \langle xyz \vert S_{ma} \rangle
    + \mu_B\langle H\vert xyz\rangle\sum_{m,a} g_a
    \langle xyz \vert S_{ma}\rangle

where vector :math:`\vec{d}_{ab} = \vec{r}_{m+d} - \vec{r}_m`  runs over the neighbors.
:math:`J_{ab}(d_{ab})` is a :math:`3\times3` exchange matrix.
:math:`A_a` is a :math:`3\times3` on-site anisotropy matrix.
The third term describe the Zeeman interaction with the external magnetic field.

.. note::

  * The double counting is explicitly present in the summation:
    for the pair :math:`(m,a; m+d,b)` the pair :math:`(m+d,b; m,a)` is included.
  * Spin vectors are not normalized.

For the simplicity of the latter discussion we combine the exchange and anisotropy
under one sum, defining :math:`A_a = \dfrac{1}{2}J_{aa}(\vec{d}=\vec{0})`, than the Hamiltonian
is written as:

.. math::
  H = \dfrac{1}{2} \sum_{m, \vec{d}, a, b} \vec{S}_{ma}^T J_{ab}(d_{ab})\vec{S}_{m+d,b}
  + \mu_B\vec{H}^T\sum_{m,a} g_a \vec{S}_{ma}

.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \vec{d}, a, b}
    \langle S_{ma}\vert xyz\rangle
    \langle xyz \vert J_{ab}(d_{ab})\vert xyz \rangle
    \langle xyz \vert S_{m+d,b} \rangle
    + \mu_B \langle H \vert xyz\rangle\sum_{m,a} g_a
    \langle xyz\vert S_{ma} \rangle

Symmetries of the Hamiltonian
=============================

The Hamiltonian has the following symmetries:

.. math::
  J_{ab}(d_{ab}) = J_{ba}^T(d_{ba}) = J_{ba}^T(-d_{ab})
