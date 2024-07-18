.. _user-guide_methods_rewritten-spinham:

**************************
Rewritten Spin Hamiltonian
**************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/uvn-or-spherical.inc
  * .. include:: page-notations/exchange-tensor.inc

===========
Hamiltonian
===========

The Spin Hamiltonian is

.. math::
  H =
   \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
   \braket{\,\tilde{S}_{mi}\,|\, \boldsymbol{J}_{\boldsymbol{d}ij}\,|\, \tilde{S}_{m+d_{ij},j}\, }
   + \mu_B \sum_{m,i}\, g_i\,\braket{\,h\,|\, \tilde{S}_{mi}\,}

where the tilde indicates that the spin vectors include also fluctuations about the
ground-state. We rewrite this Hamiltonian in the spherical basis

.. math::
  H =
     \dfrac{1}{2}
    \sum_{\boldsymbol{d}_{ij}, i, j}\,
    ^{sf}\boldsymbol{\tilde{S}_{mi}}^\dagger\,
    ^{sf}\boldsymbol{\tilde{J}_{\boldsymbol{d}ij}}\,
    ^{sf}\boldsymbol{\tilde{S}_{d_{ij},j}}
    +
    \mu_B\, \sum_{m,i}\, g_i \,^{sn}\boldsymbol{h}^\dagger\,
    ^{sn}\boldsymbol{R}_m\, ^{sn}\boldsymbol{R_i}\, ^{sf}\boldsymbol{\tilde{S}_{mi}}

where the exchange tensor

.. math::
  ^{sf}\boldsymbol{\tilde{J}_{\boldsymbol{d}ij}}=
    \braket{\,f_i^+\,f_i^-\,f_i\,|\,\tilde{J}_{\boldsymbol{d}ij}\,|\,f_i^+\,f_i^-\,f_i\,}

======================================================================
Exchange tensor :math:`^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}`
======================================================================

The exchange  :math:`\boldsymbol{\tilde{J}}^s_{m\boldsymbol{d}ij}` can be
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
