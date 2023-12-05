.. _user-guide_methods_spin-fourier:

**********************
Fourier transfromation
**********************

.. dropdown:: Notation used on this page

  * Bra-ket notation for vectors. With one exception:

    - :math:`\vec{v_1}\cdot\vec{v}_2 = \langle v_1\vert v_2\rangle`

As it is evident at the end, the reference frame :math:`\vert u^+u^-n\rangle`
is the most convinient one for the fourier transformation. First, we recall the
coordinate representation of the spin vector :math:`\vert S_{ma}\rangle`
from :ref:`previous section <user-guide_methods_spherical-rf>`:

.. math::
  \langle u^+u^-n\vert S_{ma}\rangle
  =
  \begin{pmatrix}
    \dfrac{\sin\theta_a}{\sqrt{2}}\cdot e^{- i (\vec{Q}\cdot\vec{r}_m + \phi_a)} \\
    \dfrac{\sin\theta_a}{\sqrt{2}}\cdot e^{+ i (\vec{Q}\cdot\vec{r}_m + \phi_a)} \\
    \cos\theta_a
  \end{pmatrix}

We compute the fourier transform of it:

.. dropdown:: Details

  .. math::
    \begin{multline}
      \vert S_{ka} \rangle
      = \dfrac{1}{M}\sum_{m} e^{-i\vec{k}\vec{r_m}} \vert S_{ma} \rangle
      = \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}} \vert u^+\rangle
      \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{r}_m(\vec{k}+\vec{Q})}\right)\\
      + \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}} \vert u^-\rangle
      \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{r}_m(\vec{k}-\vec{Q})}\right)
      + \cos\theta \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{k}\vec{r}_m}\right) \vert v \rangle
    \end{multline}

  where :math:`m = 1, ..., M`

.. math::
  \vert S_{ka} \rangle
  = \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
  \delta_{\vec{k}, -\vec{Q}} \vert u^+\rangle
  + \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
  \delta_{\vec{k}, \vec{Q}} \vert u^-\rangle
  + \cos\theta \delta_{\vec{k}, \vec{0}} \vert v \rangle

Structural factor in the :math:`\vert u^+u^-n\rangle` reference frame:

.. math::
  \langle u^+u^-n\vert S_{ka} \rangle
  =
  \begin{pmatrix}
    \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
    \delta_{\vec{k}, -\vec{Q}} \\
    \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
    \delta_{\vec{k}, \vec{Q}} \\
    \cos\theta \delta_{\vec{k}, \vec{0}}
  \end{pmatrix}

Structural factor in the :math:`\vert uvn\rangle` reference frame:

.. math::
  \langle uvn\vert S_{ka} \rangle
  =
  \begin{pmatrix}
    \dfrac{\sin\theta_a}{2}
    \left(e^{-i\phi_a}\delta_{\vec{k}, -\vec{Q}} +
    e^{i\phi_a}\delta_{\vec{k}, \vec{Q}}\right) \\
    \dfrac{i\sin\theta_a}{2}
    \left(e^{-i\phi_a}\delta_{\vec{k}, -\vec{Q}} -
    e^{i\phi_a}\delta_{\vec{k}, \vec{Q}}\right) \\
    \cos\theta \delta_{\vec{k}, \vec{0}}
  \end{pmatrix}
