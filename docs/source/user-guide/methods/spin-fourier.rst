.. _user-guide_methods_spin-fourier:

**********************
Fourier transformation
**********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/parentheses.inc
  * .. include:: page-notations/kronecker-delta.inc
  * .. include:: page-notations/uvn-or-spherical.inc

As it is evident at the end, the reference frame :math:`\vert u^+u^-n \rangle`
is the most convenient one for the fourier transformation. First, we recall the
coordinate representation of the spin vector :math:`\vert S_{mi} \rangle`
from :ref:`previous section <user-guide_methods_spherical-rf>`:

.. include:: repeated-formulas/spin-spherical.inc

We compute the fourier transform of it:

.. dropdown:: Details

  .. math::
      \boldsymbol{S_{ki}^s}
      =
      \dfrac{1}{M}\sum_{m} e^{-i\boldsymbol{k}\boldsymbol{r_m}} \boldsymbol{S_{mi}^s}
      &=
      S_i
      \cdot
      \Biggl[
        \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}}
        \boldsymbol{\hat{u}^+}
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{r_m}(\boldsymbol{k}+\boldsymbol{q})}
        \right)
        +\\&+
        \dfrac{\sin\theta_i\cdot e^{i\phi_i}}{\sqrt{2}}
        \boldsymbol{\hat{u}^-}
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{r_m}(\boldsymbol{k}-\boldsymbol{q})}
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

.. math::
  \boldsymbol{S_{ki}^s}
  =
  S_i
  \cdot
  \left[
    \delta_{\boldsymbol{k}, -\boldsymbol{q}}
    \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}}
    \boldsymbol{\hat{u}^+}
    +
    \delta_{\boldsymbol{k}, \boldsymbol{q}}
    \dfrac{\sin\theta_i\cdot e^{i\phi_i}}{\sqrt{2}}
    \boldsymbol{\hat{u}^-}
    +
    \delta_{\boldsymbol{k}, \boldsymbol{0}}
    \cdot
    \cos\theta
    \boldsymbol{\hat{v}}
  \right]

Structural factor in the :math:`(\,u^+\,u^-\,n\,)` reference frame:

.. math::
  \boldsymbol{S_{ki}^s}
  =
  S_i
  \cdot
  \begin{pmatrix}
    \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}} \delta_{\boldsymbol{k}, -\boldsymbol{q}} \\
    \dfrac{\sin\theta_i\cdot e^{ i\phi_i}}{\sqrt{2}} \delta_{\boldsymbol{k},  \boldsymbol{q}} \\
    \cos\theta \delta_{\boldsymbol{k}, \boldsymbol{0}}                                        \\
  \end{pmatrix}

Structural factor in the :math:`(\,u\,v\,n\,)` reference frame:

.. math::
  \boldsymbol{S_{ki}}
  =
  S_i
  \cdot
  \begin{pmatrix}
    \dfrac{\sin\theta_i}{2}
    \left(
      e^{-i\phi_i}\delta_{\boldsymbol{k}, -\boldsymbol{q}}
      +
      e^{i\phi_i}\delta_{\boldsymbol{k}, \boldsymbol{q}}
    \right) \\
    \dfrac{i\sin\theta_i}{2}
    \left(
      e^{-i\phi_i}\delta_{\boldsymbol{k}, -\boldsymbol{q}}
      -
      e^{i\phi_i}\delta_{\boldsymbol{k}, \boldsymbol{q}}
    \right) \\
    \cos\theta \delta_{\boldsymbol{k}, \boldsymbol{0}}
  \end{pmatrix}
