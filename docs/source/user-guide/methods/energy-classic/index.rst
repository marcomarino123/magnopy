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

=================================
Re-written Heisenberg Hamiltonian
=================================
We have shown in :ref:`the previous section <user-guide_methods_spherical-rf>` that the
classical Heisenberg Hamiltonian can be written in the spherical reference frame
:math:`(u^+\, u^-\, n)` as follows:

.. include:: ../repeated-formulas/hamiltonian-main-spherical.inc

where the spin vectors are

.. math::
  \boldsymbol{S}_{mi}^s
  =
  \boldsymbol{R}_m^s\, \boldsymbol{S}^s_i
  =
  S_i\, \boldsymbol{R}_m^s\, \boldsymbol{\hat{f}}_i^s
  =
  S_i\,\boldsymbol{R}_m^s
  \begin{pmatrix}
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{- i \phi_i} \\
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{+ i \phi_i} \\
     \cos\theta_i
  \end{pmatrix}

the inter-cell rotation matrix is

.. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.inc

and the exchange constant matrix is

.. math::
  \boldsymbol{J}^s_{ij}(\boldsymbol{d}_{ij})
  =
  \boldsymbol{J}^s_{\boldsymbol{d}ij}
  =
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{++} & J_{\boldsymbol{d}ij}^{+-} & J_{\boldsymbol{d}ij}^{+n} \\
    J_{\boldsymbol{d}ij}^{-+} & J_{\boldsymbol{d}ij}^{--} & J_{\boldsymbol{d}ij}^{-n} \\
    J_{\boldsymbol{d}ij}^{n+} & J_{\boldsymbol{d}ij}^{n-} & J_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}

By inserting the above expressions into the Hamiltonian, we find

.. math::
  H=&
  \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,
  (\boldsymbol{S}^{s})^{\dagger}_i\, (\boldsymbol{R}_m^s)^{\dagger}\,
  \boldsymbol{J}^s_{\boldsymbol{d}ij}\, \boldsymbol{R}_{m+d_{ij}}^s
  \boldsymbol{S}^s_j
  +
  \mu_B\,(\boldsymbol{h}^{s})^{\dagger}\,
  \sum_{m,i}\, g_i\, \boldsymbol{R}_m^s\, \boldsymbol{S}^s_i
  \\=&
  \dfrac{1}{2} \sum_{m,\boldsymbol{d}_{ij}, i, j}\,
  (\boldsymbol{S}^{s})^{\dagger}_i\, \boldsymbol{\tilde{J}}^s_{m\boldsymbol{d}ij}\,
  \boldsymbol{S}^s_j
  +
  \mu_B\, (\boldsymbol{h}^{s})^{\dagger}\,
  \sum_{m,i}\, g_i\, \boldsymbol{R}_m^s\, \boldsymbol{S}^s_i

where we introduce the notation for the "rotated" exchange matrices written in
:ref:`spherical basis <user-guide_methods_spherical-rf>`

.. math::
  \boldsymbol{\tilde{J}}^s_{mdij}
  =
  (\boldsymbol{R}_m^s)^{\dagger}\,
  \boldsymbol{J}^s_{\boldsymbol{d}ij}\,
  \boldsymbol{R}_{m+d_{ij}}^s

Futhermore, we group the part of the sum that depends on the index :math:`m` as we
will compute it explicitly below

.. math::
  H=
  \dfrac{1}{2}
  \sum_{\boldsymbol{d}_{ij}, i, j}\,
  (\boldsymbol{S}^{s})^{\dagger}_i\,
  \boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}\,
  \boldsymbol{S}^s_j
  +
  \mu_B\, (\boldsymbol{h}^{s})^{\dagger}\,
  \sum_{i}\, g_i\, \left(\sum_m\boldsymbol{R}_m^s\right)\, \boldsymbol{S}^s_i

where

.. math::
  \boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}
  =
  \sum_m\,
  \boldsymbol{\tilde{J}}^s_{mdij}
  =
  \sum_m\,
  (\boldsymbol{R}_m^s)^{\dagger}\,
  \boldsymbol{J}^s_{\boldsymbol{d}ij}\,
  \boldsymbol{R}_{m+d_{ij}}^s


This form of the Hamiltonian shows that the classical energy corresponding to any
given spin configuration
:math:`E(\boldsymbol{\hat{n}},\,\boldsymbol{q},\theta_i,\,\phi_i)`
is a function of the cone axis :math:`\boldsymbol{\hat{n}}`, the spiral vector
:math:`\boldsymbol{q}`, and all the angles :math:`\theta_i,\,\phi_i`.
The minimum-energy configuration is therefore obtained by minimizing :math:`E` with
respect to all those parameters.

=====================================================================
Exchange constant :math:`\boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}`
=====================================================================

The exchange constant :math:`\boldsymbol{\tilde{J}}^s_{m\boldsymbol{d}ij}` can be
written as a sum of five matrices in terms of zero-, first- and second-harmonics as
follows:

.. math::
  \boldsymbol{\tilde{J}}_{m\boldsymbol{d}ij}^s
  =
  \sum_{l=0,\pm 1,\pm 2}\,
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
  \cdot
  e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

and where

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^0
  =
  \begin{pmatrix}
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{++} & 0 & 0 \\
    0 & e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{--}  & 0 \\
    0 & 0 & J_{\boldsymbol{d}ij}^{nn}
  \end{pmatrix}

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^1
  =
  \begin{pmatrix}
    0 & 0 & J_{\boldsymbol{d}ij}^{+n} \\
    0 & 0 & 0 \\
    0 & e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{n-} & 0
  \end{pmatrix}

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-1}
  =
  \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & J_{\boldsymbol{d}ij}^{-n} \\
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}ij}^{n+} & 0 & 0
  \end{pmatrix}

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^2
  =
  \begin{pmatrix}
    0  &  e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{+-} & 0  \\
    0  &  0                                                                & 0  \\
    0  &  0                                                                & 0
  \end{pmatrix}

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-2}
  =
  \begin{pmatrix}
    0                                                                 &  0  &  0  \\
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{-+} &  0  &  0  \\
    0                                                                 &  0  &  0
  \end{pmatrix}

The above expression helps to perform the summation over index :math:`m` needed to
determine the exchange constant

.. math::
  \boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}
  =
  M\,
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
    :math:`\boldsymbol{q}=0`. This is **ferromagnetic** case where no spiral is formed.
    Note, that the each spin in the unit cell can be oriented in any direction, but all
    cells are replicas of each other.

2.  Only the zeroth- and second-order terms contribute to the energy if the spiral vector
    :math:`\boldsymbol{q}=\boldsymbol{G}/2`. This is the **anti-ferromagnetic** case where
    the spins can rotate between two different cells, but the angle of rotation is
    :math:`n_m \pi/2`.

3. Only the zero harmonic contributes to the energy if the spiral vector
   :math:`\boldsymbol{q}\neq 0,\,\boldsymbol{G}/2`. This is the **spiral** case where the
   spins rotate between the cells.

This means that it proves more transparent to write separate expressions for the spin
vectors and energies for the three cases.

--------------------
Ferromagnetic energy
--------------------
The spin vectors look like

.. math::
  \boldsymbol{S}_{mi}^s
    =S_i\,
  \begin{pmatrix}
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{- i \phi_i} \\
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{ i \phi_i} \\
     \cos\theta_i
  \end{pmatrix}

and the total energy per unit cell is

.. math::
  E^{C,FM}=&
  \frac{1}{2}\,\sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\,S_j\,\left(
  \cos\theta_i\,\cos\theta_j\,J_{ij}^{nn}
  +\sin\theta_i\,\sin\theta_j\,J_{ij}^{F-AF}
  +\cos\theta_i\,\sin\theta_j\,J_{ij}^{F,1}
  +\sin\theta_i\,\cos\theta_j\,J_{ij}^{F,2}
  \right)\\
  &+\mu_B\,
  \sum_i\,g_i\,  S_i\,\left(\,\cos\theta_i\,h^n\,+\,
  \sin\theta_i\,
  \left(h^u\,\cos\phi_i+h^v\,\sin\phi_i\,\right)
  \right)

with

.. math::
  J_{ij}^{F-AF}=&
   (J_{ij}^{uu}\,\cos\phi_i\,\cos\phi_j+
  J_{ij}^{vv}\,\sin\phi_i\,\sin\phi_j+
  J_{ij}^{uv}\,\cos\phi_i\,\sin\phi_j+
  J_{ij}^{vu}\,\sin\phi_i\,\cos\phi_j)\\
  J_{ij}^{F,1}=&
  (J_{ij}^{nu}\,\cos\phi_j+J_{ij}^{nv}\,\sin\phi_j)\\
  J_{ij}^{F,2}=&(J_{ij}^{un}\,\cos\phi_i+J_{ij}^{vn}\,\sin\phi_i)

------------------------
Antiferromagnetic energy
------------------------
If :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1`,
then :math:`\boldsymbol{q}\,\boldsymbol{r_m} = \pi\, n_m` always.
Thus :math:`\cos(\boldsymbol{q}\cdot\boldsymbol{r}_m)=(-1)^{mod(n_m,2)}`.
Thus, the spin vector is simplified to

.. math::
  \boldsymbol{S}_{mi}^s
  = S_i\,
  \begin{pmatrix}
    \sin\theta_i\,e^{-i(\pi n_m+\phi_i)} \\
    \sin\theta_i\,e^{i(\pi n_{m}+\phi_i)} \\
    \cos\theta_i                    \\
  \end{pmatrix}
  =
  S_i\,
    \begin{pmatrix}
      (-1)^{mod(n_m,2)}\,\sin\theta_i\,e^{-i\phi_i} \\
      (-1)^{mod(n_m,2)}\,\sin\theta_i\,e^{i\phi_i} \\
      \cos\theta_i             \\
    \end{pmatrix}

Similarly, :math:`\boldsymbol{q}\,\boldsymbol{d}_{ij} = \pi \,n_{ij}`. Then
:math:`\cos(\boldsymbol{q}\,\boldsymbol{d}_{ij})=(-1)^{mod(n_{ij},2)}`,
so the classical energy per unit cell becomes

.. math::
  E^{C,AF}=
  \frac{1}{2}\,\sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\,S_j\,\left(
  \cos\theta_i\,\cos\theta_j\,J_{ij}^{nn}
  +(-1)^{mod(n_{ij},2)}\,\sin\theta_i\,\sin\theta_j\,
  J_{ij}^{F-AF}\right)
  +\mu_B\,\sum_i\,g_i\, S_i\,\cos\theta_i\,h^n

---------------------------
Generic spiral state energy
---------------------------
The spin vectors assume the generic form

.. math::
  \boldsymbol{S}_{mi}^s
    =S_i\,
  \begin{pmatrix}
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{- i \phi_{mi}} \\
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{ i \phi_{mi}} \\
     \cos\theta_i
  \end{pmatrix}

where

.. math::
  \phi_{mi}(q) = \phi_m(\boldsymbol{q}) + \phi_i(\boldsymbol{q})
               = \boldsymbol{q}\cdot\boldsymbol{r_m} +
                  \boldsymbol{q}\cdot\boldsymbol{r_i}+ \Delta\phi_i
               = \boldsymbol{q}\cdot\boldsymbol{r_{mi}} + \Delta\phi_i

and the classical energy per unit cell is

.. math::
   E^{C,SP}=
   \frac{1}{2}\,\sum_{i, j, \boldsymbol{d_{ij}}}
    S_i\,S_j\,\left(
      \,\cos\theta_i\,\cos\theta_j\,J_{ij}^{nn}+
      \sin\theta_i\,\sin\theta_j\,J_{ij}^{SP}\right)+
      \mu_B\,\sum_i\,g_i\,  S_i\,\cos\theta_i\,h^n

with

.. math::
  J_{ij}^{SP}=
       J_{ij}^+\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)+
         D_{ij}^{n}\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)
