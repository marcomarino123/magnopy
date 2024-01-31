.. _user-guide_methods_energy-classic:

****************
Classical energy
****************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/reference-frame.inc
  * .. include:: ../page-notations/transpose-complex-conjugate.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/kronecker-delta.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc


Let us recall the Hamiltonian:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any-classic.inc

In the classical picture the Hamiltonian describes the total energy of the system,
therefore, we write :math:`E` instead of :math:`H`, where appropriate.


Let us separate the summation over cites in unit cell and over unit cells:

.. note::
    Ferromagnetic classical spin vector does not depend on the unit cell index:

    .. math::
        \boldsymbol{S_{mi}^{F}}
        =
        (0, 0, S_i )^T
        =
        S_i \boldsymbol{\hat{n}}
        =
        \boldsymbol{S_i^{F}}

    We assume that magnetic field is uniform in space:

    .. math::
        \boldsymbol{h} = (h^u, h^v, h^n)^{\dagger}


It os convenient to wcompute the expression for the classical energy in the spherical reference frame:

.. math::
  H
  =
  \dfrac{1}{2}
  \sum_{a, b}
  (\boldsymbol{S_i^{F,s}})^{\dagger}
  (\boldsymbol{R_i^s})^{\dagger}
  \sum_{\boldsymbol{d_{ij}}}
  \left[
  \sum_{m}
  (\boldsymbol{R_m^s})^{\dagger}(\boldsymbol{q})
  \boldsymbol{J_{ij}^s}(\boldsymbol{d_{ij}})
  \boldsymbol{R_{m+d_{ij}}^s}(\boldsymbol{q})
  \right]
  \boldsymbol{R_j^s}
  \boldsymbol{S_j^{F, s}}
  +
  \mu_B
  \sum_i
  g_i
  (\boldsymbol{h^s})^{\dagger}
  \left[
  \sum_{m}
  \boldsymbol{R_m^s}(\boldsymbol{q})
  \right]
  \boldsymbol{R_i^s}
  \boldsymbol{S_{i}^{F,s}}

We focus our attention on the expressions in the square brackets:

===============
Exchange energy
===============

We recall
:ref:`exchange matrix in a spherical reference frame <user-guide_methods_spherical-rf_exchange-tensor>`
and
:ref:`rotation matrix in a spherical reference frame <user-guide_methods_spherical-rf>`
from previous sections:

.. include:: ../repeated-formulas/exchange-matrix-spherical.inc

.. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.inc

Next we write the expression under the sum explicitly:

.. dropdown:: Details

  .. include:: exchange-matrix-spiral-rotated-details.inc


.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-spherical.inc

.. _user-guide_methods_energy-classic_sum-over-m-condition:

Next we write back the sum over :math:`m`, and using the facts that:

* :math:`\boldsymbol{d_{ij}} = \sum_{i}\boldsymbol{a}_in_i`, where :math:`\boldsymbol{a}_i` are the lattice vectors
  and :math:`n_i \in \mathbb{Z}`, :math:`i = 1,2,3`.
* :math:`\boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})`
  does not depend on the index :math:`m`
* :math:`\sum_{r_m}e^{\pm i\boldsymbol{q}\boldsymbol{r_m}} = M\delta_{\boldsymbol{q},\boldsymbol{G}}`
  and
  :math:`\sum_{r_m}e^{\pm 2i\boldsymbol{q}\boldsymbol{r_m}} = M\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}}`

  .. dropdown:: Details [1]_

    .. include:: exchange-details-on-fourier-identities.inc

we get an expression for the sum:

.. dropdown:: Details

  .. include:: exchange-matrix-sum-over-m-details.inc

.. include:: ../repeated-formulas/exchange-matrix-rotated-and-summed-over-m.inc

Which leads to the expression for the exchange part of total energy:

.. dropdown:: Details

  First, we recall the rotation matrix in the spherical reference frame:

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.inc

  Then we compute:

  .. include:: exchange-energy-left-part.inc

  and

  .. include:: exchange-energy-right-part.inc

  Finally, we compute the exchange energy:

  .. include:: exchange-energy-not-simplified.inc


  Now we simplify each term of the sum separately:

  .. include:: exchange-energy-simplify-ppmm.inc

  .. include:: exchange-energy-simplify-pmmp.inc

  .. include:: exchange-energy-simplify-pnmn.inc

  .. include:: exchange-energy-simplify-npnm.inc

.. include:: ../repeated-formulas/classic-exchange-energy.inc

=====================
Magnetic field energy
=====================

Next we turn our attention to the Zeeman term:

.. math::
  \mu_B
  \sum_i
  g_i
  \left[
  \sum_{m}
  (\boldsymbol{h^s})^{\dagger}
  \boldsymbol{R_m^s}
  \right]
  \boldsymbol{R_i^s}
  \boldsymbol{S_{i}^{F,s}}

Let us compute part of the expression:

.. math::
  \boldsymbol{R_i^s}
  \boldsymbol{S_i^{F,s}}
  =
  S_i
  \begin{pmatrix}
    \dfrac{\sin\theta_i e^{-i\phi_i}}{\sqrt{2}} \\
    \dfrac{\sin\theta_i e^{i\phi_i}}{\sqrt{2}}  \\
    \cos\theta_i                                \\
  \end{pmatrix}

Magnetic field in the spherical reference frame is written as:

.. include:: ../repeated-formulas/magnetic-field-spherical.inc

Before we compute the expression for energy work with the sum over :math:`m`:

.. math::
  \sum_{m}
  \boldsymbol{R_m^s}
  =
  \begin{pmatrix}
    \sum_{m}e^{-i\boldsymbol{q}\cdot\boldsymbol{r_m}} & 0                          & 0 \\
    0                           & \sum_{m}e^{i\boldsymbol{q}\cdot\boldsymbol{r_m}} & 0 \\
    0                           & 0                          & \sum_{m}1 \\
  \end{pmatrix}
  =
  M
  \begin{pmatrix}
    \delta_{\boldsymbol{q},\boldsymbol{G}} & 0                           & 0 \\
    0                           & \delta_{\boldsymbol{q},\boldsymbol{G}} & 0 \\
    0                           & 0                          & 1             \\
  \end{pmatrix}

Then the energy is:

.. dropdown:: Details

  .. include:: field-energy-details.inc

.. include:: ../repeated-formulas/classic-zeeman-energy.inc


Total energy
============

Finally, we can write the total classical energy:

.. include:: ../repeated-formulas/classic-total-energy.inc
