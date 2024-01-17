.. _user-guide_methods_energy-classic:

****************
Classical energy
****************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/reference-frame.txt
  * .. include:: ../page-notations/transpose-complex-conjugate.txt
  * .. include:: ../page-notations/in-spherical.txt
  * .. include:: ../page-notations/parentheses.txt


Let us recall the Hamiltonian:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any.txt


Let us separate the summation over cites in unit cell and over unit cells:

.. note::
    Ferromagnetic spin does not depend on the unit cell index:

    .. math::
        \vec{S}_{ma}^{ferro}
        =
        (0, 0, S_a )^T
        =
        \vec{S}_a^{ferro}

    We assume that magnetic field can vary over the space:

    .. math::
        \vec{H} = \vec{H}(\vec{r_{ma}}) = \vec{H}_{ma}

.. math::
  H
  =
  \dfrac{1}{2}
  \sum_{a, b}
  (\vec{S}_a^{ferro})^{\dagger}
  \boldsymbol{R}^{\dagger}(\theta_a,\phi_a)
  \sum_{\vec{d}_{ab}}
  \left[
  \sum_{m}
  \boldsymbol{R}^{\dagger}(\theta_m)
  \boldsymbol{J_{ab}}(\vec{d}_{ab})
  \boldsymbol{R}(\theta_{m+d_{ab}})
  \right]
  \boldsymbol{R}(\theta_b,\phi_b)
  \vec{S}_b^{ferro}
  +
  \mu_B
  \sum_{a}
  g_a
  \left[
  \sum_{m}
  \vec{H}^{\dagger}_{ma}
  \boldsymbol{R}(\theta_m)
  \right]
  \boldsymbol{R}(\theta_a,\phi_a)
  \vec{S}_{a}^{ferro}

We focus our attention on the expressions in the square brackets:

Exchange energy
===============

We recall
:ref:`exchange matrix in a spherical reference frame <user-guide_methods_spinham-spherical>`
and
:ref:`rotation matrix in a spherical reference frame <user-guide_methods_spherical-rf>`:
from previous sections:

.. include:: ../repeated-formulas/exchange-matrix-spherical.txt

.. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.txt

Next we write the expression under the sum explicitly:

.. dropdown:: Details

  .. include:: exchange-matrix-spiral-rotated-details.txt


.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-uvn.txt

Next we write back the sum over :math:`m`, and using the facts that:

* :math:`\vec{d} = \sum_{i}\vec{a}_in_i`, where :math:`\vec{a}_i` are the lattice vectors
  and :math:`n_i \in \mathbb{Z}`, :math:`i = 1,2,3`.
* :math:`\boldsymbol{J_{ab}}(\vec{d}_{ab})`
  does not depend on the index :math:`m`
* :math:`\sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\vec{G}}`
  and
  :math:`\sum_{r_m}e^{\pm 2i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\frac{\vec{G}}{2}}`

  .. dropdown:: Details [1]_

    .. include:: exchange-details-on-fourier-identities.txt

we get an expression for the sum:

.. dropdown:: Details

  .. include:: exchange-matrix-sum-over-m-details.txt

.. include:: ../repeated-formulas/exchange-matrix-rotated-and-summed-over-m.txt

Which leads to the expression for the exchange part of total energy:

.. dropdown:: Details

  First, we recall the rotation matrix in the spherical reference frame:

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.txt

  Then we compute:

  .. include:: exchange-energy-left-part.txt

  and

  .. include:: exchange-energy-right-part.txt

  Finally, we compute the exchange energy:

  .. include:: exchange-energy-not-simplified.txt


  Now we simplify each term of the sum separately:

  .. include:: exchange-energy-simplify-ppmm.txt

  .. include:: exchange-energy-simplify-pmmp.txt

  .. include:: exchange-energy-simplify-pnmn.txt

  .. include:: exchange-energy-simplify-npnm.txt

.. include:: ../repeated-formulas/classic-exchange-energy.txt


Magnetic field energy
=====================

Next we turn our attention to the Zeeman term:

.. math::
  \mu_B
  \sum_{a}
  g_a
  \left[
  \sum_{m}
  \vec{H}^{\dagger}_{ma}
  \boldsymbol{R}(\theta_m)
  \right]
  \boldsymbol{R}(\theta_a,\phi_a)
  \vec{S}_{a}^{ferro}

Let us compute part of the expression:

.. math::
  \boldsymbol{R}(\theta_a,\phi_a)
  \vec{S}_a^{ferro}
  =
  S_a
  \begin{pmatrix}
    \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}} \\
    \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}}  \\
    \cos\theta_a                                \\
  \end{pmatrix}

Magnetic field in the spherical reference frame is written as:

.. dropdown:: Details

  Magnetic field in the :math:`uvn` reference frame is written as:

  .. math::
    \langle uvn \vert H_{ma}\rangle
    =
    \left(H_{ma}^u, H_{ma}^v, H_{ma}^n\right)^{\dagger}

  Let us recall the transformation matrix:

  .. include:: ../repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

  And compute the magnetic field in the spherical reference frame:

  .. math::
    \langle u^+u^-n \vert H_{ma} \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert H_{ma} \rangle
    =
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert H_{ma} \rangle

  Which leads to the expression:

.. math::
  \dfrac{1}{\sqrt{2}}
  \begin{pmatrix}
    1 & -i & 0        \\
    1 &  i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}
  \begin{pmatrix}
    H_{ma}^u \\
    H_{ma}^v \\
    H_{ma}^n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{H_{ma}^u - iH_{ma}^v}{\sqrt{2}} \\
    \dfrac{H_{ma}^u + iH_{ma}^v}{\sqrt{2}} \\
    H_{ma}^n     \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{H_{ma}^{-}}{\sqrt{2}}       \\
    \dfrac{H_{ma}^{+}}{\sqrt{2}}       \\
    H_{ma}^n \\
  \end{pmatrix}

Then the energy is:

.. dropdown:: Details

  .. include:: field-energy-details.txt

.. math::
  \mu_B
  \sum_{a}
  g_a  S_a
  \sum_{m}
  \left[
  \sin\theta_a
  \left(
    H_{ma}^u\cos(\vec{Q}\cdot\vec{r}_m+\phi_a)
    +
    H_{ma}^v\sin(\vec{Q}\cdot\vec{r}_m+\phi_a)
  \right)
  +
  H_{ma}^n\cos\theta_a
  \right]

Let us set each component of the magnetic field to be a harmonic function in the
:math:`uvn` reference frame:

.. math::
  \begin{aligned}
    H_{ma}^u
    &=
    H^u\cos(\vec{Q^u}(\vec{r}_m+\vec{r}_a)+\varphi^u)
    =
    H^u\cos(\vec{Q}^u\vec{r}_m+\phi_a^u) \\
    H_{ma}^v
    &=
    H^v\cos(\vec{Q^v}(\vec{r}_m+\vec{r}_a)+\varphi^v)
    =
    H^v\cos(\vec{Q}^v\vec{r}_m+\phi_a^v) \\
    H_{ma}^n
    &=
    H^n\cos(\vec{Q^n}(\vec{r}_m+\vec{r}_a)+\varphi^n)
    =
    H^n\cos(\vec{Q}^n\vec{r}_m+\phi_a^n) \\
  \end{aligned}

Then we can write:

.. dropdown:: Details

  * :math:`\hat{u}` component

    .. include:: field-sum-u-component-details.txt

  * :math:`\hat{v}` component

    .. include:: field-sum-v-component-details.txt

  * :math:`\hat{n}` component

    .. include:: field-sum-n-component-details.txt

.. include:: ../repeated-formulas/classic-zeeman-energy.txt

Total energy
============

Finally, we can write the total classical energy:

.. include:: ../repeated-formulas/classic-total-energy.txt
