.. _user-guide_methods_rewritten-spinham:

*********************************
Re-written Heisenberg Hamiltonian
*********************************

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


We have shown in :ref:`section <user-guide_methods_spherical-rf>` that the
classical Heisenberg Hamiltonian can be written in the spherical reference frame
:math:`(u^+\, u^-\, n)` as follows:

.. include:: ../repeated-formulas/hamiltonian-main-spherical.inc

where the spin vectors are

.. math::
  ^{n,s}\boldsymbol{S}_{mi}
  \,=\,
  ^{n,s}\boldsymbol{R}_m\, ^{n,s}\boldsymbol{S}_i

By inserting the above expressions into the Hamiltonian, we find

.. math::
  H=&
  \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,
  ^{n,s}\boldsymbol{S}^{\dagger}_i\, ^{n,s}\boldsymbol{R}_m^{\dagger}\,
  ^{n,s}\boldsymbol{J}_{\boldsymbol{d}ij}\, ^{n,s}\boldsymbol{R}_{m+d_{ij}}
  ^{n,s}\boldsymbol{S}_j
  +
  \mu_B\,^{n,s}\boldsymbol{h}^{\dagger}\,
  \sum_{m,i}\, g_i\, ^{n,s}\boldsymbol{R}_m\, ^{n,s}\boldsymbol{S}_i
  \\=&
  \dfrac{1}{2} \sum_{m,\boldsymbol{d}_{ij}, i, j}\,
  ^{n,s}\boldsymbol{S}^{\dagger}_i\, ^{n,s}\boldsymbol{\tilde{J}}_{m\boldsymbol{d}ij}\,
  ^{n,s}\boldsymbol{S}_j
  +
  \mu_B\, ^{n,s}\boldsymbol{h}^{\dagger}\,
  \sum_{m,i}\, g_i\, ^{n,s}\boldsymbol{R}_m\, ^{n,s}\boldsymbol{S}_i

where we introduce the notation for the "rotated" exchange matrices written in
:ref:`spherical basis <user-guide_methods_spherical-rf>`

.. include:: ../repeated-formulas/exchange-matrix-rotated-definition-spherical.inc

Futhermore, we factor the :math:`m`-summation as follows

.. math::
  ^{n,s}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}
  &=
  \sum_m\,
  ^{n,s}\boldsymbol{\tilde{J}}^s_{mdij}
  =
  \sum_m\,
  ^{n,s}\boldsymbol{R}_m^\dagger\,
  ^{n,s}\boldsymbol{J}_{\boldsymbol{d}ij}\,
  ^{n,s}\boldsymbol{R}_{m+d_{ij}}\\
  ^{n,s}\boldsymbol{R}_0&=\sum_m\,^{n,s}\boldsymbol{R}_m

As a consequence, the Hamiltonian looks as follows:

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

=====================================================================
Exchange constant :math:`\boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}`
=====================================================================

The exchange constant :math:`\boldsymbol{\tilde{J}}^s_{m\boldsymbol{d}ij}` can be
written as a sum of five matrices in terms of zero-, first- and second-harmonics as
follows:

.. include:: ../repeated-formulas/exchange-matrix-rotated-split-spherical.inc

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
