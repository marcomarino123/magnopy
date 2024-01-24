.. _user-guide_methods_spin-fourier:

**********************
Fourier transformation
**********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/parentheses.txt
  * .. include:: page-notations/kronecker-delta.txt

As it is evident at the end, the reference frame :math:`\vert u^+u^-n \rangle`
is the most convenient one for the fourier transformation. First, we recall the
coordinate representation of the spin vector :math:`\vert S_{mi} \rangle`
from :ref:`previous section <user-guide_methods_spherical-rf>`:

.. include:: repeated-formulas/spin-spherical.txt

We compute the fourier transform of it:

.. dropdown:: Details

  .. math::
      \vert S_{ka} \rangle
      =
      \dfrac{1}{M}\sum_{m} e^{-i\boldsymbol{k}\boldsymbol{r_m}} \vert S_{mi} \rangle
      &=
      S_i
      \cdot
      \Biggl[
        \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}}
        \vert u^+\rangle
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\boldsymbol{r_m}(\boldsymbol{k}+\boldsymbol{q})}
        \right)
        +\\&+
        \dfrac{\sin\theta_i\cdot e^{i\phi_i}}{\sqrt{2}}
        \vert u^-\rangle
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
        \vert v \rangle
      \Biggr]

  where :math:`m = 1, ..., M`

.. math::
  \vert S_{ka} \rangle
  =
  S_i
  \cdot
  \left[
    \delta_{\boldsymbol{k}, -\boldsymbol{q}}
    \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}}
    \vert u^+\rangle
    +
    \delta_{\boldsymbol{k}, \boldsymbol{q}}
    \dfrac{\sin\theta_i\cdot e^{i\phi_i}}{\sqrt{2}}
    \vert u^-\rangle
    +
    \delta_{\boldsymbol{k}, \boldsymbol{0}}
    \cdot
    \cos\theta
    \vert v \rangle
  \right]

Structural factor in the :math:`\vert u^+u^-n\rangle` reference frame:

.. math::
  \langle u^+u^-n \vert S_{ka} \rangle
  =
  S_i
  \cdot
  \begin{pmatrix}
    \dfrac{\sin\theta_i\cdot e^{-i\phi_i}}{\sqrt{2}} \delta_{\boldsymbol{k}, -\boldsymbol{q}} \\
    \dfrac{\sin\theta_i\cdot e^{ i\phi_i}}{\sqrt{2}} \delta_{\boldsymbol{k},  \boldsymbol{q}} \\
    \cos\theta \delta_{\boldsymbol{k}, \boldsymbol{0}}                                        \\
  \end{pmatrix}

Structural factor in the :math:`\vert uvn\rangle` reference frame:

.. math::
  \langle uvn\vert S_{ka} \rangle
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
