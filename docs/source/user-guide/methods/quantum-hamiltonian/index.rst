.. _user-guide_methods_quantum-hamiltonian:

*******************
Quantum Hamiltonian
*******************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/operators.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc

The quantum Heisenberg Hamiltonian looks exactly the same as its classical
counterpart, where all the classical spin vectors are replaced by quantum
spins.

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any-quantum.inc

The Hamiltonian can be rewritten as follows (as it was done
:ref:`here <user-guide_methods_energy-classic>` for the classical Hamiltonian)

.. math::
  {\cal H}
  =
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  (\boldsymbol{{\cal S}}_{mi}^s)^\dagger\,
  \boldsymbol{\tilde{J}}_{ij}^s(m,\boldsymbol{d}_{ij})\,
  \boldsymbol{{\cal S}}_{m+d_{ij} j}^s
  +
  \mu_B\, \boldsymbol{h}^{\dagger}\,
  \sum_{m,i}\, g_i\,
  \boldsymbol{R_m}\,
  \boldsymbol{{\cal S}}_{mi}^s

where (see section
:ref:`Quantum spin fluctuations <user-guide_methods_quantum-spin-fluctuations>`)

.. include:: ../repeated-formulas/spin-expansion-rotated-spherical-quantum.inc

and

.. math::

  \boldsymbol{{\cal S}}_{m+d_{ij}, j}^s=
  \boldsymbol{R}_j^s\,\boldsymbol{{\cal S}}_{m+d_{ij}, j}^{F,s}\approx&\,
  S_j\,\boldsymbol{\hat{f}}^s_{j}+S_j^{1/2}\,
  (a_{m+d_{ij}, j}^\dagger\,\boldsymbol{\hat p}^s_j+a_{m+d_{ij}, j}\,
  \boldsymbol{\hat t}^s_j)
  -n_{m+d_{ij}, j}\,\boldsymbol{\hat{f}}^s_j\\
  &-\frac{1}{4\,S_j^{1/2}}\,
  (a_{m+d_{ij}, j}^\dagger\,n_{m+d_{ij}, j}\,\boldsymbol{\hat p}^s_j+
  a_{m+d_{ij}, j}\,n_{m+d_{ij}, j}\,\boldsymbol{\hat t}^s_j)

and

.. include:: ../repeated-formulas/exchange-matrix-rotated-definition-spherical.inc

================
Exchange kernels
================
We define the following nine exchange kernels

.. math::
  \boldsymbol{\tilde{J}}_{mdij}^{ff}=&
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{tt}=&
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{pp}=&
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{tp}=&
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{pt}=&
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{fp}=&
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{pf}=&
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{ft}=&
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s\\
  \boldsymbol{\tilde{J}}_{mdij}^{tf}=&
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\

=====================
Hamiltonian splitting
=====================
The exchange part of the Hamiltonian can be decomposed into different pieces
according to their order in a :math:`1/S` expansion by assuming that
:math:`S_i = S_j = S`. The different pieces also correspond to terms having
zero, two, three and four bosons fields. Terms containing more than four boson
terms are dropped, that is equivalent to dropping terms beyond :math:`1/S^2`
in the conventional :math:`1/S` expansion. Then

.. math::
  {\cal H}^{exchange}=E^C+{\cal H}^{LSWT}
                      +{\cal H}^{Cubic}+{\cal H}^{Biquadratic}

* The classical energy piece

  .. math::
    E^{C}=\dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    S_i\,S_j\,\boldsymbol{\tilde{J}}_{mdij}^{ff}

  has been determined in section
  :ref:`Total energy of the classical Hamiltonian <user-guide_methods_energy-classic>`.

* The Linear Spin Wave Theory (LSWT) piece contains bilinear bosonic terms

  .. math::
    {\cal H}^{LSWT}=
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    &\left(
     - \,\boldsymbol{\tilde{J}}_{mdij}^{ff}\,
        \left(S_j\,n_{mi}\,+S_i\,n_{m+d_{ij},j}^\dagger\right)
        \right.
    \\&+
        (S_i\,S_j)^{1/2}\left(
       \boldsymbol{\tilde{J}}_{mdij}^{pp}\,
       \,a_{mi}\,a_{m+d_{ij},j}^\dagger
       +
       \boldsymbol{\tilde{J}}_{mdij}^{tt}\,
       \,a_{mi}^\dagger\,a_{m+d_{ij},j}\right)
      \\&+
      (S_i\,S_j)^{1/2}
      \left.\left(
      \boldsymbol{\tilde{J}}_{mdij}^{pt}\,
      \,a_{mi}\,a_{m+d_{ij},j}
      +
      \boldsymbol{\tilde{J}}_{mdij}^{tp}\,
      \,a_{mi}^{\dagger}\,a_{m+d_{ij},j}^{\dagger}
    \right)\right)

* The cubic piece contains cubic terms contains three-boson terms

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-cubic-part.inc

* And the biquadratic piece contains four-boson terms

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-biquadratic-part.inc


.. important::
  We keep the magnitude of each atomic spin :math:`S_i,\,S_j` in the above expressions.
  Note that if the unit cell spins have different spin magnitudes, then
  the :math:`1/S` expansion becomes anbiguous. For example, the magnitude of
  a cubic term
  could be similar to some terms at LSWT order, so one should judiciously
  evaluate which terms should be kept for a particular system of interest.

.. dropdown:: Omitted terms

  .. include:: omitted-terms.inc
