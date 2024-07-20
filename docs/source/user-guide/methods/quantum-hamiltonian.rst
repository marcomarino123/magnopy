.. _user-guide_methods_quantum-hamiltonian:

*******************
Quantum Hamiltonian
*******************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/quantum-operators.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc

The quantum Heisenberg Hamiltonian looks exactly the same as its classical
counterpart, where all the classical spin vectors are replaced by quantum
spins

.. math::
    {\cal H}=
   \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,
   \boldsymbol{\cal{S}_{mi}}\,^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,
   ^{sf}\boldsymbol{\cal{S}_{m+d_{ij},j}}
   + \mu_B \sum_{m,i}\, g_i\,^{sf}\boldsymbol{h}\, ^{sf}\boldsymbol{R_m}\,^{sf}\boldsymbol{\cal{S}_{mi}}

with

.. math::
  \tilde{J}_{d_{ij}}^{f,\alpha\,\beta}
          =\sum_{l=0,\pm 1,\pm 2}\,
          (^{sn}\boldsymbol{\hat{f}_i^\alpha})^\dagger\,^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
            \,^{sn}\boldsymbol{\hat{f}_i^\beta}\,\,\,
              e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

and where the quantum spin vector operators are

.. math::
  \boldsymbol{\cal S}_{mi}
  \approx
  \begin{pmatrix}
    0 \\ 0 \\
    S_i
  \end{pmatrix}
   +
  S_i^{1/2}\,
  \begin{pmatrix}
    a^\dagger_{mi}  \\a_{mi} \\ 0
  \end{pmatrix}
  +
  S_i\,
  \begin{pmatrix}
    0 \\ 0 \\ - n_{mi}
  \end{pmatrix}
  +\frac{1}{4\,S_i^{1/2}}\,
  \begin{pmatrix}
   -a^\dagger_{mi} \,n_{mi} \\
    -n_{mi}\,a_{mi} \\
    0
  \end{pmatrix}

.. math::
  \boldsymbol{\cal S}_{m+d_{ij},j}
  \approx
  \begin{pmatrix}
    0 \\ 0 \\
    S_j
  \end{pmatrix}
   +
  S_j^{1/2}\,
  \begin{pmatrix}
    a^\dagger_{m+d_{ij},j}  \\a_{m+d_{ij},j} \\ 0
  \end{pmatrix}
  +
  S_j\,
  \begin{pmatrix}
    0 \\ 0 \\ - n_{m+d_{ij},j}
  \end{pmatrix}
  +\frac{1}{4\,S_j^{1/2}}\,
  \begin{pmatrix}
   -a^\dagger_{m+d_{ij},j} \,n_{m+d_{ij},j} \\
    -n_{m+d_{ij},j}\,a_{m+d_{ij},j} \\
    0
  \end{pmatrix}

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
  E^0 + {\cal H}^{LSWT} + {\cal H}^{Cubic} + {\cal H}^{Biquadratic}

* The classical energy piece corresponds to
  one of the energy minima of the classical Hamiltonian as discussed in this
  :ref:`section <user-guide_methods_energy-classic>`

  .. math::
    E^0
    =
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    S_i\, S_j\, \boldsymbol{\tilde{J}}_{dij}^{f,00}
    +
    \mu_B \,^{sn}\boldsymbol{h}^{\dagger}\,^{sn}\boldsymbol{R_0}\,
    \sum_i\, g_i\,^{sn}\boldsymbol{S}_i

* The Linear Spin Wave Theory (LSWT) piece contains
  bilinear bosonic terms and will be discussed in the next :ref:`section <user-guide_methods_lswt>`

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.inc

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
