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
  \boldsymbol{\tilde{J}}_{m\boldsymbol{d}ij}^s\,
  \boldsymbol{{\cal S}}_{m+d_{ij} j}^s
  +
  \mu_B\, \boldsymbol{h}^{\dagger}\,
  \sum_{m,i}\, g_i\,
  \boldsymbol{R_m}\,
  \boldsymbol{{\cal S}}_{mi}^s

where (see section
:ref:`Quantum spin fluctuations <user-guide_methods_quantum-spin-fluctuations>`)

.. include:: ../repeated-formulas/spin-expansion-rotated-spherical-quantum.inc

.. math::
  (\boldsymbol{\cal S}^s_{mi})^{\dagger}
  &\approx
  S_i\, (\boldsymbol{\hat{f}}^s_i)^{\dagger}
  +
  S_i^{1/2}\, (
    a_{mi}\, (\boldsymbol{\hat p}^s_i)^{\dagger}
    +
    a_{mi}^\dagger\, (\boldsymbol{\hat t}^s_i)^{\dagger}
  )
  -
  n_{mi}\, (\boldsymbol{\hat{f}}^s_i)^{\dagger}
  -\\&-
  \frac{1}{4}\, S_i^{-1/2}(
    n_{mi}\, a_{mi}\, (\boldsymbol{\hat p}^s_i)^{\dagger}
    +
    a_{mi}^{\dagger}\, n_{mi}\, (\boldsymbol{\hat t}^s_i)^{\dagger}
  )

and

.. math::
  \boldsymbol{\cal S}^s_{m+d_{ij},j}
  &\approx
  S_j\, \boldsymbol{\hat{f}}^s_j
  +
  S_j^{1/2}\, (
    a_{m+d_{ij},j}^\dagger\, \boldsymbol{\hat p}^s_j
    +
    a_{m+d_{ij},j}\, \boldsymbol{\hat t}^s_j
  )
  -
  n_{m+d_{ij},j}\, \boldsymbol{\hat{f}}^s_j
  -\\&-
  \frac{1}{4\, S_j^{1/2}}\, (
    a_{m+d_{ij},j}^\dagger\, n_{m+d_{ij},j}\, \boldsymbol{\hat p}^s_j
    +
    n_{m+d_{ij},j}\, a_{m+d_{ij},j}\, \boldsymbol{\hat t}^s_j
  )


and

.. include:: ../repeated-formulas/exchange-matrix-rotated-definition-spherical.inc

====================
Exchange ??kernels??
====================
For further convenience we define a shorten notation for the products of two vectors
and exchange matrix as follows:

.. math::
  &\boldsymbol{\tilde{J}}_{mdij}^{pp}&=
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{pt}&=
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{pf}&=
    (\boldsymbol{\hat{p}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\
  &\boldsymbol{\tilde{J}}_{mdij}^{tp}&=
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{tt}&=
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{tf}&=
    (\boldsymbol{\hat{t}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\
  &\boldsymbol{\tilde{J}}_{mdij}^{fp}&=
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{p}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{ft}&=
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{t}}_j^s \quad\quad\quad
  &\boldsymbol{\tilde{J}}_{mdij}^{ff}&=
    (\boldsymbol{\hat{f}}_i^s)^\dagger\,\boldsymbol{\tilde{J}}_{mdij}^s\,
    \boldsymbol{\hat{f}}_j^s\\

=====================
Hamiltonian splitting
=====================
The exchange part of the Hamiltonian can be decomposed into different pieces
according to their order in a :math:`1/S` expansion by assuming that
:math:`S_i = S_j = S`. The different pieces also correspond to terms having
zero, two, three and four bosons fields. Terms containing more than four boson
terms are dropped, that is equivalent to dropping terms beyond :math:`1/S^2`
in the Hamiltonian. Then

.. math::
  {\cal H}^{exchange}
  =
  E^{Classic} + {\cal H}^{LSWT} + {\cal H}^{Cubic} + {\cal H}^{Biquadratic}

* :ref:`The classical energy piece <user-guide_methods_energy-classic>`

  .. math::
    E^{Classic}
    =
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    S_i\, S_j\, \boldsymbol{\tilde{J}}_{mdij}^{ff}
    +
    \mu_B \boldsymbol{h}^{\dagger}\,
    \sum_{m,i}\, g_i\, S_i\,
    \boldsymbol{R_m}\,
    \boldsymbol{\hat{f}}_i^s

* :ref:`The Linear Spin Wave Theory (LSWT) piece <user-guide_methods_lswt>` contains
  bilinear bosonic terms

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.inc

  .. hint::

    .. math::

      {\cal n}_{mi}^{\dagger} = {\cal n}_{mi}
      \quad\quad\text{and}\quad\quad
      {\cal n}_{m+d_{ij},j}^{\dagger} = {\cal n}_{m+d_{ij},j}

* The cubic piece contains three-boson terms

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
