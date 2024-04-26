.. _user-guide_methods_spin-fourier:

**********************
Fourier transformation
**********************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/parentheses.inc
  * .. include:: page-notations/kronecker-delta.inc
  * .. include:: page-notations/uvn-or-spherical.inc

The spherical reference frame :math:`(u^+\, u^-\, n)` is convenient for analyzing the
fourier-transformed spin vectors. Notice that the components of the spin vector
:math:`\boldsymbol{S}_{mi}^s` in the spherical reference frame are

.. include:: repeated-formulas/spin-spherical.inc

whose Fourier transform is

.. math::
  \boldsymbol{S}_{ki}^s
  =
  S_i
  \begin{pmatrix}
    \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}} \\
    \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{ i\phi_i}\, \delta_{\boldsymbol{k},  \boldsymbol{q}} \\
    \cos\theta\, \delta_{\boldsymbol{k}, \boldsymbol{0}}                                     \\
  \end{pmatrix}

.. dropdown:: Details

  .. math::
      \boldsymbol{S}_{ki}^s
      =
      \dfrac{1}{M}\sum_{m} e^{-i\boldsymbol{k}\boldsymbol{r_m}} \boldsymbol{S_{mi}^s}
      =
      S_i
      \cdot
      \Biggl[
        &\dfrac{\sin\theta_i \cdot e^{-i\phi_i}}{\sqrt{2}}
        \boldsymbol{\hat{u}^+}
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{r_m}(\boldsymbol{k} + \boldsymbol{q})}
        \right)
        +\\&+
        \dfrac{\sin\theta_i \cdot e^{i\phi_i}}{\sqrt{2}}
        \boldsymbol{\hat{u}^-}
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{r_m}(\boldsymbol{k} - \boldsymbol{q})}
        \right)
        +\\&+
        \cos\theta
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{k}\boldsymbol{r_m}}
        \right)
        \boldsymbol{\hat{v}}
      \Biggr]

  where :math:`m = 1, ..., M`


This structural factor can be written in the :math:`(u\, v\, n)` reference frame as follows:

.. math::
  \boldsymbol{S}_{ki}
  =
  S_i
  \begin{pmatrix}
      \dfrac{\sin\theta_i}{2}\,
      \left(
        e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}}
        +
        e^{i\phi_i}\, \delta_{\boldsymbol{k}, \boldsymbol{q}}
      \right)
    \\
      \dfrac{i\sin\theta_i}{2}\,
      \left(
        e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}}
        -
        e^{i\phi_i}\, \delta_{\boldsymbol{k}, \boldsymbol{q}}
      \right)
    \\
      \cos\theta \, \delta_{\boldsymbol{k}, \boldsymbol{0}}
  \end{pmatrix}
