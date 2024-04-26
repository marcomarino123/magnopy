This expression of the exchange Hamiltonian cuts all terms having more than
four bosonic operators. This corresponed to terms of order smaller than
:math:`1/S^2` (if one assumes :math:`S_i = S_j = S`). Examples are:

.. math::
  \dfrac{1}{4S_iS_j^{3/2}}
  \Bigl[
    &(\boldsymbol{f_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{p_j^s}
    \,a_{mi}^{\dagger}\,\,a_{mi}\,\,a_{m+d_{ij},j}^{\dagger}\,\,a_{m+d_{ij},j}^{\dagger}\,\,a_{m+d_{ij},j}
    +
    (\boldsymbol{f_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{t_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}\,a_{m+d_{ij},j}
    +\\&+
    (\boldsymbol{p_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{f_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}
    +
    (\boldsymbol{t_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{f_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}^{\dagger}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}
  \Bigr]
  +\\+
  \dfrac{1}{16S_i^{3/2}S_j^{3/2}}
  \Bigl[
    &(\boldsymbol{p_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{p_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}
    +
    (\boldsymbol{p_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{t_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}\,a_{m+d_{ij},j}
    +\\&+
    (\boldsymbol{t_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{p_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}^{\dagger}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}
    +
    (\boldsymbol{t_i^s})^\dagger\,
    \boldsymbol{\tilde{J}_{mdij}^s}\,
    \boldsymbol{t_j^s}
    \,a_{mi}^{\dagger}\,a_{mi}^{\dagger}\,a_{mi}\,a_{m+d_{ij},j}^{\dagger}\,a_{m+d_{ij},j}\,a_{m+d_{ij},j}
  \Bigr]

.. note::
  In order to fully account for more than 4 operator terms one need to expand the square root
  in the HP transformation up to higher degrees in :math:`1/S`.

The last omitted terms are one-operator terms:

.. math::
  &\dfrac{1}{2}
  \sum_{m, \boldsymbol{d}_{ij}, i, j}
  \biggl[
    S_iS_j^{1/2}
    \Bigl(
      \boldsymbol{\tilde{J}_{mdij}^{fp}}\,
      \,
      \,a_{m+d_{ij},j}^{\dagger}
      +
      \boldsymbol{\tilde{J}_{mdij}^{ft}}\,
      \,
      \,a_{m+d_{ij},j}
    \Bigr)
    +\\&\phantom{\dfrac{1}{2}\sum_{m, \boldsymbol{d}_{ij}, i, j}\biggl[}+
    S_i^{1/2}S_j
    \Bigl(
      \boldsymbol{\tilde{J}_{mdij}^{pf}}\,
      \,
      \,a_{mi}
      +
      \boldsymbol{\tilde{J}_{mdij}^{tf}}\,
      \,
      \,a_{mi}^{\dagger}
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
