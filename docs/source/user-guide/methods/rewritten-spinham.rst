.. _user-guide_methods_rewritten-spinham:

**************************
Higher-harmonic generation
**************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/transpose-complex-conjugate.inc
  * .. include:: page-notations/parentheses.inc
  * .. include:: page-notations/kronecker-delta.inc
  * .. include:: page-notations/uvn-or-spherical.inc
  * .. include:: page-notations/exchange-tensor.inc

=================================
Re-written Heisenberg Hamiltonian
=================================

We have shown in :ref:`section <user-guide_methods_spherical-rf>` that the
classical Heisenberg Hamiltonian can be written in the spherical reference frame
:math:`(u^+\, u^-\, n)` as follows:

.. include:: ./repeated-formulas/hamiltonian-main-spherical.inc

where the spin vectors are

.. math::
  ^{n,s}\boldsymbol{S}_{mi}
  \,=\,
  ^{n,s}\boldsymbol{R}_m\, ^{n,s}\boldsymbol{S}_i

The above expressions are inserted and the Hamiltonian regrouped as follows

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

=====================================================================
Exchange constant :math:`\boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}`
=====================================================================

The exchange constant :math:`\boldsymbol{\tilde{J}}^s_{m\boldsymbol{d}ij}` can be
written as a sum of five matrices in terms of zero-, first- and second-harmonics as
follows:

.. include:: repeated-formulas/exchange-matrix-rotated-split-spherical.inc

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
