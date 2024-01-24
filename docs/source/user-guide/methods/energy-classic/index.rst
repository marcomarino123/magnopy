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
  * .. include:: ../page-notations/kronecker-delta.txt


Let us recall the Hamiltonian:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any.txt


Let us separate the summation over cites in unit cell and over unit cells:

.. note::
    Ferromagnetic spin does not depend on the unit cell index:

    .. math::
        \boldsymbol{S_{mi}^{ferro}}
        =
        (0, 0, S_i )^T
        =
        \boldsymbol{S_i^{ferro}}

    We assume that magnetic field can vary in space:

    .. math::
        \boldsymbol{h} = \boldsymbol{h}(\boldsymbol{r_{mi}}) = \boldsymbol{h_{mi}}

.. math::
  H
  =
  \dfrac{1}{2}
  \sum_{a, b}
  (\boldsymbol{S_i^{ferro}})^{\dagger}
  \boldsymbol{R}^{\dagger}(\theta_i,\phi_i)
  \sum_{\boldsymbol{d_{ij}}}
  \left[
  \sum_{m}
  \boldsymbol{R}^{\dagger}(\theta_m)
  \boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})
  \boldsymbol{R}(\theta_{m+d_{ij}})
  \right]
  \boldsymbol{R}(\theta_j,\phi_j)
  \boldsymbol{S_j^{ferro}}
  +
  \mu_B
  \sum_i
  g_i
  \left[
  \sum_{m}
  \boldsymbol{h_{mi}}^{\dagger}
  \boldsymbol{R}(\theta_m)
  \right]
  \boldsymbol{R}(\theta_i,\phi_i)
  \boldsymbol{S_{i}^{ferro}}

We focus our attention on the expressions in the square brackets:

Exchange energy
===============

We recall
:ref:`exchange matrix in a spherical reference frame <user-guide_methods_spinham-spherical>`
and
:ref:`rotation matrix in a spherical reference frame <user-guide_methods_spherical-rf>`
from previous sections:

.. include:: ../repeated-formulas/exchange-matrix-spherical.txt

.. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.txt

Next we write the expression under the sum explicitly:

.. dropdown:: Details

  .. include:: exchange-matrix-spiral-rotated-details.txt


.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-uvn.txt

.. _user-guide_methods_energy-classic_sum-over-m-condition:

Next we write back the sum over :math:`m`, and using the facts that:

* :math:`\boldsymbol{d} = \sum_{i}\boldsymbol{a}_in_i`, where :math:`\boldsymbol{a}_i` are the lattice vectors
  and :math:`n_i \in \mathbb{Z}`, :math:`i = 1,2,3`.
* :math:`\boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})`
  does not depend on the index :math:`m`
* :math:`\sum_{r_m}e^{\pm i\boldsymbol{q}\boldsymbol{r_m}} = M\delta_{\boldsymbol{q},\boldsymbol{G}}`
  and
  :math:`\sum_{r_m}e^{\pm 2i\boldsymbol{q}\boldsymbol{r_m}} = M\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}}`

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
  \sum_i
  g_i
  \left[
  \sum_{m}
  \boldsymbol{h_{mi}}^{\dagger}
  \boldsymbol{R}(\theta_m)
  \right]
  \boldsymbol{R}(\theta_i,\phi_i)
  \boldsymbol{S_{i}^{ferro}}

Let us compute part of the expression:

.. math::
  \boldsymbol{R}(\theta_i,\phi_i)
  \boldsymbol{S_i^{ferro}}
  =
  S_i
  \begin{pmatrix}
    \dfrac{\sin\theta_i e^{-i\phi_i}}{\sqrt{2}} \\
    \dfrac{\sin\theta_i e^{i\phi_i}}{\sqrt{2}}  \\
    \cos\theta_i                                \\
  \end{pmatrix}

Magnetic field in the spherical reference frame is written as:

.. dropdown:: Details

  Magnetic field in the :math:`uvn` reference frame is written as:

  .. math::
    \langle uvn \vert h_{mi}\rangle
    =
    \left(h_{mi}^u, h_{mi}^v, h_{mi}^n\right)^{\dagger}

  Let us recall the transformation matrix:

  .. include:: ../repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

  And compute the magnetic field in the spherical reference frame:

  .. math::
    \langle u^+u^-n \vert h_{mi} \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert h_{mi} \rangle
    =
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert h_{mi} \rangle

  Which leads to the expression:

.. math::
  \dfrac{1}{\sqrt{2}}
  \begin{pmatrix}
    1 & -i & 0        \\
    1 &  i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}
  \begin{pmatrix}
    h_{mi}^u \\
    h_{mi}^v \\
    h_{mi}^n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{h_{mi}^u - ih_{mi}^v}{\sqrt{2}} \\
    \dfrac{h_{mi}^u + ih_{mi}^v}{\sqrt{2}} \\
    h_{mi}^n     \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{h_{mi}^{-}}{\sqrt{2}}       \\
    \dfrac{h_{mi}^{+}}{\sqrt{2}}       \\
    h_{mi}^n \\
  \end{pmatrix}

Then the energy is:

.. dropdown:: Details

  .. include:: field-energy-details.txt

.. math::
  \mu_B
  \sum_i
  g_i  S_i
  \sum_{m}
  \left[
  \sin\theta_i
  \left(
    h_{mi}^u\cos(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)
    +
    h_{mi}^v\sin(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)
  \right)
  +
  h_{mi}^n\cos\theta_i
  \right]

Let us set each component of the magnetic field to be a harmonic function in the
:math:`uvn` reference frame:

.. math::
  \begin{aligned}
    h_{mi}^u
    &=
    h^u\cos(\boldsymbol{q^u}(\boldsymbol{r_m}+\boldsymbol{r_i})+\varphi^u)
    =
    h^u\cos(\boldsymbol{q^u}\boldsymbol{r_m}+\phi_i^u) \\
    h_{mi}^v
    &=
    h^v\cos(\boldsymbol{q^v}(\boldsymbol{r_m}+\boldsymbol{r_i})+\varphi^v)
    =
    h^v\cos(\boldsymbol{q^v}\boldsymbol{r_m}+\phi_i^v) \\
    h_{mi}^n
    &=
    h^n\cos(\boldsymbol{q^n}(\boldsymbol{r_m}+\boldsymbol{r_i})+\varphi^n)
    =
    h^n\cos(\boldsymbol{q^n}\boldsymbol{r_m}+\phi_i^n) \\
  \end{aligned}

Then we can write:

.. dropdown:: Details

  * :math:`\boldsymbol{\hat{u}}` component

    .. include:: field-sum-u-component-details.txt

  * :math:`\boldsymbol{\hat{v}}` component

    .. include:: field-sum-v-component-details.txt

  * :math:`\boldsymbol{\hat{n}}` component

    .. include:: field-sum-n-component-details.txt

.. include:: ../repeated-formulas/classic-zeeman-energy.txt

Total energy
============

Finally, we can write the total classical energy:

.. include:: ../repeated-formulas/classic-total-energy.txt
