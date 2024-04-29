This expression of the exchange Hamiltonian cuts all terms having more than
four bosonic operators. In particular

* Five-operator terms:

  .. math::
    &\dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    \biggl[
      \dfrac{1}{4}S_i^{-1/2}
      \Bigl(
        \boldsymbol{\tilde{J}}_{mdij}^{pf}\,
        n_{mi}\, a_{mi}\, n_{m + d_{ij},j}
        +
        \boldsymbol{\tilde{J}}_{mdij}^{tf}\,
        a_{mi}^{\dagger}\, n_{mi}\, n_{m + d_{ij},j}
      \Bigr)
      +\\&\phantom{\dfrac{1}{2}\sum_{m, \boldsymbol{d}_{ij}, i, j}\biggl[}+
      \dfrac{1}{4S_j^{1/2}}
      \Bigl(
        \boldsymbol{\tilde{J}}_{mdij}^{fp}\,
        n_{mi}\, a_{m + d_{ij},j}^{\dagger}\, n_{m + d_{ij},j}
        +
        \boldsymbol{\tilde{J}}_{mdij}^{ft}\,
        n_{mi}\, n_{m + d_{ij},j}\, a_{m + d_{ij},j}
      \Bigr)
    \Biggr]

* Six operator terms

  .. math::
    &\dfrac{1}{2}
    \sum_{m, \boldsymbol{d}_{ij}, i, j}
    \dfrac{(S_iS_j)^{-1/2}}{16}
    \biggl[
      \boldsymbol{\tilde{J}}_{mdij}^{pp}\,
      n_{mi}\, a_{mi}\, a_{m + d_{ij},j}^{\dagger}\, n_{m + d_{ij},j}
      +
      \boldsymbol{\tilde{J}}_{mdij}^{pt}\,
      n_{mi}\, a_{mi}\, n_{m + d_{ij},j}\, a_{m + d_{ij},j}
      +\\&\phantom{\dfrac{1}{2}\sum_{m, \boldsymbol{d}_{ij}, i, j}\biggl[\dfrac{(S_iS_j)^{-1/2}}{16}}+
      \boldsymbol{\tilde{J}}_{mdij}^{tp}\,
      a_{mi}^{\dagger}\, n_{mi}\, a_{m + d_{ij},j}^{\dagger}\, n_{m + d_{ij},j}
      +
      \boldsymbol{\tilde{J}}_{mdij}^{tt}\,
      a_{mi}^{\dagger}\, n_{mi}\, n_{m + d_{ij},j}\, a_{m + d_{ij},j}^{\dagger}
    \Biggr]


that correspond to terms of order smaller than :math:`1/S^2`
(if one assumes :math:`S_i = S_j = S`).

.. note::
  In order to fully account for more than 4 operator terms one need to expand the square
  root in the HP transformation up to higher degrees in :math:`1/S`.

The last omitted terms are one-operator terms:

.. math::
  &\dfrac{1}{2}
  \sum_{m, \boldsymbol{d}_{ij}, i, j}
  \biggl[
    S_iS_j^{1/2}
    \Bigl(
      \boldsymbol{\tilde{J}}_{mdij}^{fp}\, a_{m+d_{ij},j}^{\dagger}
      +
      \boldsymbol{\tilde{J}}_{mdij}^{ft}\, a_{m+d_{ij},j}
    \Bigr)
    +
    S_i^{1/2}S_j
    \Bigl(
      \boldsymbol{\tilde{J}}_{mdij}^{pf}\, a_{mi}
      +
      \boldsymbol{\tilde{J}}_{mdij}^{tf}\, a_{mi}^{\dagger}
    \Bigr)
  \Biggr]
  +\\&+
  \mu_B \boldsymbol{h}^{\dagger}\,
  \sum_{m,i}\, g_i\, S_i^{1/2}\,
  \boldsymbol{R_m}\,
  \left(
    \boldsymbol{\hat{p}}_i^s
    {\cal a}_{mi}^{\dagger}
    +
    \boldsymbol{\hat{t}}_i^s
    {\cal a}_{mi}
  \right)
