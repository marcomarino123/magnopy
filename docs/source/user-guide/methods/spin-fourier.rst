.. _user-guide_methods_spin-fourier:

**********************
Fourier transfromation
**********************

.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
  * Bra-ket notation for vectors. With few exceptions:

    - :math:`\vec{v_1}\cdot\vec{v}_2 = \langle v_1\vert v_2\rangle`
  * Parentheses () and brackets [] are equivalent.

From the :ref:`previous section <user-guide_methods_single-q>` we recall:

.. math::
  \vert S_{ma}\rangle = R(\theta_m)R(\theta_a,\phi_a)\vert S_{ma}^{ferro}\rangle
  = R_{ma}\vert S_{ma}^{ferro}\rangle

.. math::
  \langle uvn\vert S_{ma}\rangle =
  \begin{pmatrix}
      \sin\theta_a\cos(\vec{Q}\cdot\vec{r}_m + \phi_a) \\
      \sin\theta_a\sin(\vec{Q}\cdot\vec{r}_m + \phi_a) \\
      \cos\theta_a                                     \\
  \end{pmatrix} =
  \begin{pmatrix}
      S_{ma}^u\\
      S_{ma}^v\\
      S_{ma}^n\\
  \end{pmatrix}

.. math::
  \vert S_{ma}\rangle
  = \sin\theta_a\cos(\vec{Q}\cdot\vec{r}_m + \phi_a) \vert u \rangle
  + \sin\theta_a\sin(\vec{Q}\cdot\vec{r}_m + \phi_a) \vert v \rangle
  + \cos\theta_a \vert n \rangle

Now we define:

.. math::
  \vert u^{\pm} \rangle = \dfrac{\vert u \rangle \pm i\vert v \rangle }{\sqrt{2}}

and

.. math::
  \begin{multline}
    S_{ma}^{\pm} = \dfrac{S_{ma}^u \pm iS_{ma}^v}{\sqrt{2}} =
    \dfrac{\sin\theta_a[\cos(\vec{Q}\cdot\vec{r}_m + \phi_a)
    \pm i\sin(\vec{Q}\cdot\vec{r}_m + \phi_a)]}{\sqrt{2}} \\
    = \dfrac{\sin(\theta_a)}{\sqrt{2}}\cdot e^{\mp i (\vec{Q}\cdot\vec{r}_m + \phi_a)}
  \end{multline}

than

.. math::
  \begin{matrix}
    \vert u \rangle = \dfrac{\vert u^+ \rangle + \vert u^- \rangle }{\sqrt{2}} &
    \text{ and } &
    \vert v \rangle = \dfrac{\vert u^+ \rangle - \vert u^- \rangle }{i\sqrt{2}}
  \end{matrix}

and

.. math::
  \begin{multline}
    \vert S_{ma}\rangle
    = S_{ma}^u
    \left(\dfrac{\vert u^+ \rangle + \vert u^- \rangle }{\sqrt{2}}\right)
    + S_{ma}^v
    \left(\dfrac{\vert u^+ \rangle - \vert u^- \rangle }{i\sqrt{2}}\right)
    + S_{ma}^n \vert n \rangle \\
    =
    \left(\dfrac{S_{ma}^u - iS_{ma}^v}{\sqrt{2}}\right)
    \vert u^+\rangle +
    \left(\dfrac{S_{ma}^u + iS_{ma}^v}{\sqrt{2}}\right)
    \vert u^-\rangle
    + S_{ma}^n \vert n \rangle\\
    =
    \dfrac{\sin(\theta_a)}{\sqrt{2}}\cdot e^{+ i (\vec{Q}\cdot\vec{r}_m + \phi_a)}
    \vert u^+\rangle +
    \dfrac{\sin(\theta_a)}{\sqrt{2}}\cdot e^{- i (\vec{Q}\cdot\vec{r}_m + \phi_a)}
    \vert u^-\rangle
    + \cos\theta_a \vert n \rangle
  \end{multline}

Next we compute the fourier transform (:math:`m = 1, ..., M`):

.. math::
  \begin{multline}
    \vert S_{ka} \rangle
    = \dfrac{1}{M}\sum_{m} e^{-i\vec{k}\vec{r_m}} \vert S_{ma} \rangle
    = \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}} \vert u^+\rangle
    \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{r}_m(\vec{k}+\vec{Q})}\right)\\
    + \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}} \vert u^-\rangle
    \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{r}_m(\vec{k}-\vec{Q})}\right)
    + \cos\theta \left(\dfrac{1}{M}\sum_{m}e^{-i\vec{k}\vec{r}_m}\right) \vert v \rangle
  \end{multline}

Which gives the final result:

.. math::
  \vert S_{ka} \rangle
  = \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
  \delta_{\vec{k}, -\vec{Q}} \vert u^+\rangle
  + \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
  \delta_{\vec{k}, \vec{Q}} \vert u^-\rangle
  + \cos\theta \delta_{\vec{k}, \vec{0}} \vert v \rangle

Coordinates in the :math:`\vert u^+u^-n\rangle` reference frame:

.. math::
  \langle u^+u^-n\vert S_{ka} \rangle
  = \begin{pmatrix}
    \dfrac{\sin\theta_a\cdot e^{i\phi_a}}{\sqrt{2}}
    \delta_{\vec{k}, -\vec{Q}} \\
    \dfrac{\sin\theta_a\cdot e^{-i\phi_a}}{\sqrt{2}}
    \delta_{\vec{k}, \vec{Q}} \\
    \cos\theta \delta_{\vec{k}, \vec{0}}
  \end{pmatrix}

Coordinates in the :math:`\vert uvn\rangle` reference frame:

.. math::
  \langle uvn\vert S_{ka} \rangle
  = \begin{pmatrix}
    \dfrac{\sin\theta_a}{2}
    \left(e^{i\phi_a}\delta_{\vec{k}, -\vec{Q}} +
    e^{-i\phi_a}\delta_{\vec{k}, \vec{Q}}\right) \\
    \dfrac{i\sin\theta_a}{2}
    \left(e^{i\phi_a}\delta_{\vec{k}, -\vec{Q}} -
    e^{-i\phi_a}\delta_{\vec{k}, \vec{Q}}\right) \\
    \cos\theta \delta_{\vec{k}, \vec{0}}
  \end{pmatrix}
