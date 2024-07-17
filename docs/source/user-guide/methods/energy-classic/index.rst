.. _user-guide_methods_energy-classic:

*****************************************
Total energy of the classical Hamiltonian
*****************************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/reference-frame.inc
  * .. include:: ../page-notations/transpose-complex-conjugate.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/kronecker-delta.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc
  * .. include:: ../page-notations/exchange-tensor.inc


We have shown in the previous :ref:`section <user-guide_methods_spinham>` that the Hamiltonian
can be written as follows

.. math::
  H=
  \dfrac{1}{2}
  \sum_{\boldsymbol{d}_{ij}, i, j}\,
  ^{n,s}\boldsymbol{S}^\dagger_i\,
  ^{n,s}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,
  ^{n,s}\boldsymbol{S}_j
  +
  \mu_B\, ^{n,s}\boldsymbol{h}^\dagger\,^{n,s}\boldsymbol{R}_0\,
  \sum_{i}\, g_i\, ^{n,s}\boldsymbol{S}_i

where

.. math::
  ^{n,s}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}&=\sum_m\,
  ^{n,s}\boldsymbol{\tilde{J}}_{m\boldsymbol{d}ij}
  =
  \sum_{l=0,\pm 1,\pm 2}\,
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
  \cdot
  \sum_m\,e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}\\
   &= M\,
  \left(
    \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^0
    +
    \delta_{\boldsymbol{q}, \, \boldsymbol{G}}\,
    \left[
      \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^1
      +
      \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-1}
    \right]
    +
    \delta_{\boldsymbol{2q}, \, \boldsymbol{G}}\,
    \left[
      \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^2
      +
      \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-2}
    \right]
  \right)


This form of the Hamiltonian shows that the classical energy corresponding to any
given spin configuration
:math:`E(\boldsymbol{\hat{n}},\,\boldsymbol{q},\theta_i,\,\phi_i)`
is a function of the cone axis :math:`\boldsymbol{\hat{n}}`, the spiral vector
:math:`\boldsymbol{q}`, and all the angles :math:`\theta_i,\,\phi_i`.
The minimum-energy configuration is therefore obtained by minimizing :math:`E` with
respect to all those parameters.

.. dropdown:: Details

  .. math::
    \boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}
    =
    \sum_{l=0,\pm 1,\pm 2}\,
    \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
    \cdot
    \sum_m
    e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

  Therefore, one needs to compute the values of the sums of exponential

  .. math::
    \sum_m
    e^{i\, l\, \boldsymbol{q} \cdot \boldsymbol{r}_m}

  .. include:: details-on-fourier-identities.inc

===============
Exchange energy
===============

.. include:: exchange-energy.inc

=====================
Magnetic field energy
=====================

.. include:: magnetic-field-energy.inc


================
Three main cases
================

Base on the equation for the total energy we can classify all possible states into three
big groups based on the harmonics that contribute to the energy in each of them.

1.  All harmonics contribute to the total energy if the spiral vector
    :math:`\boldsymbol{q} = \boldsymbol{G}`. This is **ferromagnetic** case where no
    spiral is formed. Note, that the each spin in the unit cell can be oriented in any
    direction, but all cells are replicas of each other.

2.  Only the zeroth- and second-order terms contribute to the energy if the spiral
    vector :math:`\boldsymbol{q}=\boldsymbol{G}/2` and
    :math:`\boldsymbol{q}\ne\boldsymbol{G}`. This is the **anti-ferromagnetic** case
    where the spins can rotate between two different cells, but the angle of rotation
    is :math:`n_m \pi/2`.

3. Only the zero harmonic contributes to the energy if the spiral vector
   :math:`\boldsymbol{q}\neq \boldsymbol{G},\,\boldsymbol{G}/2`. This is the true
   **spiral** case where the spins rotate between the cells.


In the three following pages we consider minimization for each case separately:

.. toctree::
  :maxdepth: 1
  :caption: Minimization strategy

  ferromagnetic
  antiferromagnetic
  spiral
