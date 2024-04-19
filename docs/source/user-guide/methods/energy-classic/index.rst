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

  .. include:: exchange-details-on-fourier-identities.inc

===============
Exchange energy
===============
The exchange energy **per unit cell** (i.e. divided by :math:`M`) can be found by
inserting the previous expression for the exchange constant into the Hamiltonian,
that leads to:

.. math::
  E^{X}
  =
  E^{\text{zero}}
  +
  \delta_{\boldsymbol{q}, \, \boldsymbol{G}}\, E^{\text{first}}
  +
  \delta_{\boldsymbol{2q}, \, \boldsymbol{G}}\, E^{\text{second}}

where the zeroth-, first- and second-order harmonic exchange contributions are

.. math::
  E^{\text{zero}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left(
    \cos\theta_i\, \cos\theta_j\, (J_{dij}^I+S_{dij}^{nn})
    +
    \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{zero}}
  \right)
  \\\\
  E^{\text{first}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left(
    \cos\theta_i\, \cos\theta_j\, J_{dij}^{\text{first},1}+
    \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{first},2}
  \right)
  \\\\
  E^{\text{second}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\, \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{second}}

and

.. math::
  J_{dij}^{\text{zero}}
  =&
  (J^I_{dij} - \frac{1}{2}S_{dij}^{nn})\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  +
  D_{dij}^{n}\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \\\\
  J_{dij}^{\text{first},1}
  =&
  (S_{dij}^{un} + D_{dij}^v)\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  +
  (S_{dij}^{vn} - D_{dij}^u)\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  \\\\
  J_{dij}^{\text{first}, 2}
  =&
  (S_{dij}^{un} - D_{dij}^v)\, \cos(\phi_i) + (S_{dij}^{vn} + D_{dij}^u)\, \sin(\phi_i)
  \\\\
  J_{dij}^{\text{second}}
  =&
  \frac{S_{dij}^{uu} - S_{dij}^{vv}}{2}\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)
  +
  S_{dij}^{uv}\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)

where we used the decomposition of exchange matrix into isotropic, symmetric anisotropic
and asymmetric parts

.. math::
  \begin{pmatrix}
      J_{dij}^{uu} & J_{dij}^{uv} & J_{dij}^{un} \\
      J_{dij}^{vu} & J_{dij}^{vv} & J_{dij}^{vn} \\
      J_{dij}^{nu} & J_{dij}^{nv} & J_{dij}^{nn} \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    J_{dij}^I + S_{dij}^{uu}             &             S_{dij}^{uv} + D_{dij}^n &             S_{dij}^{un} - D_{dij}^v \\
                S_{dij}^{uv} - D_{dij}^n & J_{dij}^I + S_{dij}^{vv}             &             S_{dij}^{vn} + D_{dij}^u \\
                S_{dij}^{un} + D_{dij}^v &             S_{dij}^{vn} - D_{dij}^u & J_{dij}^I + S_{dij}^{nn}             \\
  \end{pmatrix}

with :math:`J_{dij}^I = \dfrac{1}{3}(J_{dij}^{uu} + J_{dij}^{vv} + J_{dij}^{nn})`
and :math:`S_{dij}^{uu} + S_{dij}^{vv} + S_{dij}^{nn} = 0`.


=====================
Magnetic field energy
=====================

Next we turn our attention to the Zeeman term, where we assume henceforth that the
magnetic field

.. math::
  \boldsymbol{h}
  =
  (\frac{1}{\sqrt{2}}\, h^+, \frac{1}{\sqrt{2}}\, h^-, h^n)^{\dagger}

is uniform. The Zeeman Hamiltonian can be written as follows:

.. math::
  H_{Z}=\mu_B
  \sum_i
  g_i\, \sum_{m}\,
  (\boldsymbol{h}^s)^{\dagger}\, \boldsymbol{R}_m^s\, \boldsymbol{S}_{i}^s

The sum over lattice sites is performed by taking into account that only the
:math:`\boldsymbol{R}_m^s` depend on :math:`m`:

.. math::
  \sum_{m}\, \boldsymbol{R_m^s}
  =
  M
  \begin{pmatrix}
    \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0                           & 0 \\
    0                           & \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0 \\
    0                           & 0                                       & 1 \\
  \end{pmatrix}

Then the Zeeman contribution to the energy **per unit cell** is:

.. math::
  E^Z =\mu_B\,
  \sum_i\, g_i\, S_i\,
  \left[
    h^n\, \cos\theta_i
    +
    \delta_{\boldsymbol{q}, \boldsymbol{G}}\, \sin\theta_i\,
    \left( h^u\, \cos\phi_i + h^v\, \sin\phi_i\, \right)
  \right]

=================================================================================
Ferromagnetic, antiferromagnetic and conical spin arrangements and their energies
=================================================================================
The above expressions demonstrate that all harmonics contribute to the total classical
energy for ferromagnetic spin arrangements, where :math:`\boldsymbol{q}=0`. In contrast,
the zeroth- and second-order terms but not the first contribute to the exchange energy
for anti-ferromagnetic spin configurations where :math:`\boldsymbol{q}=\boldsymbol{G}/2`.
Finally, only the lowest harmonic contributes to the energy if the spiral vector
:math:`\boldsymbol{q}\neq 0,\,\boldsymbol{G}/2`.

This means that it proves more transparent to write separate expressions for the spin
vectors and energies for the three cases. These are

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
  \boldsymbol{S}_{mi}
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
