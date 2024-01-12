.. _user-guide_methods_spin-fourier:

**********************
Fourier transformation
**********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/parentheses.txt

As it is evident at the end, the reference frame :math:`\vert u^+u^-n \rangle`
is the most convenient one for the fourier transformation. First, we recall the
coordinate representation of the spin vector :math:`\vert S_{ma} \rangle`
from :ref:`previous section <user-guide_methods_spherical-rf>`:

.. include:: repeated-formulas/spin-spherical.txt

We compute the fourier transform of it:

.. dropdown:: Details

  .. math::
      \vert S_{ka} \rangle
      =
      \dfrac{1}{M}\sum_{m} e^{-i\vec{k}\vec{r_m}} \vert S_{ma} \rangle
      &=
      S_a
      \cdot
      \Biggl[
        \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
        \vert u^+\rangle
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\vec{r}_m(\vec{k}+\vec{Q})}
        \right)
        \\&+
        \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
        \vert u^-\rangle
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\vec{r}_m(\vec{k}-\vec{Q})}
        \right)
        \\&+
        \cos\theta
        \left(
          \dfrac{1}{M}
          \sum_{m}e^{-i\vec{k}\vec{r}_m}
        \right)
        \vert v \rangle
      \Biggr]

  where :math:`m = 1, ..., M`

.. math::
  \vert S_{ka} \rangle
  =
  S_a
  \cdot
  \left[
    \delta_{\vec{k}, -\vec{Q}}
    \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
    \vert u^+\rangle
    +
    \delta_{\vec{k}, \vec{Q}}
    \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
    \vert u^-\rangle
    +
    \delta_{\vec{k}, \vec{0}}
    \cdot
    \cos\theta
    \vert v \rangle
  \right]

Structural factor in the :math:`\vert u^+u^-n\rangle` reference frame:

.. math::
  \langle u^+u^-n \vert S_{ka} \rangle
  =
  S_a
  \cdot
  \begin{pmatrix}
    \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}} \delta_{\vec{k}, -\vec{Q}} \\
    \dfrac{\sin\theta_a\cdot e^{ i\phi_a}}{\sqrt{2}} \delta_{\vec{k},  \vec{Q}} \\
    \cos\theta \delta_{\vec{k}, \vec{0}}                                        \\
  \end{pmatrix}

Structural factor in the :math:`\vert uvn\rangle` reference frame:

.. math::
  \langle uvn\vert S_{ka} \rangle
  =
  S_a
  \cdot
  \begin{pmatrix}
    \dfrac{\sin\theta_a}{2}
    \left(
      e^{-i\phi_a}\delta_{\vec{k}, -\vec{Q}}
      +
      e^{i\phi_a}\delta_{\vec{k}, \vec{Q}}
    \right) \\
    \dfrac{i\sin\theta_a}{2}
    \left(
      e^{-i\phi_a}\delta_{\vec{k}, -\vec{Q}}
      -
      e^{i\phi_a}\delta_{\vec{k}, \vec{Q}}
    \right) \\
    \cos\theta \delta_{\vec{k}, \vec{0}}
  \end{pmatrix}
