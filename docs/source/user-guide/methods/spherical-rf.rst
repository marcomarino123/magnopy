.. _user-guide_methods_spherical-rf:

***************************
"Spherical" reference frame
***************************

.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
  * Bra-ket notation for vectors. With one exception:

    - :math:`\vec{v_1}\cdot\vec{v}_2 = \langle v_1\vert v_2\rangle`
  * Parentheses () and brackets [] are equivalent.
  * :math:`S_a` - is length of the spin vector :math:`\vert S_{ma}\rangle`

    .. math::
      \langle uvn\vert S_{ma}^{ferro}\rangle =
      \begin{pmatrix}
        0 \\
        0 \\
        S_a \\
      \end{pmatrix}

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

Coordinate system with circular polarization
============================================

Later we will find useful the usage of the new reference frame
with circularry polarized :math:`\vert u \rangle` and
:math:`\vert v \rangle` vectors. Here we present the algebra of this
reference frame. First of all, we define the transformation matrix as:

.. math::
  T \vert uvn \rangle = \vert u^+u^-n\rangle

The transformation matrix is designed as follows:

.. math::
  \begin{matrix}
    \vert u^{\pm} \rangle = \dfrac{\vert u \rangle \pm i\vert v \rangle }{\sqrt{2}} &
    \text{and} &
    \vert n \rangle = \vert n \rangle
  \end{matrix}

Which results in the unitary transformation matrix:

.. math::
  \langle uvn\vert T\vert uvn \rangle
  = \langle uvn \vert u^+u^-n\rangle
  = \dfrac{1}{\sqrt{2}}
  \begin{pmatrix}
    1 &  1 & 0        \\
    i & -i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}

.. dropdown:: Unitary check

  .. math::
    \begin{matrix}
      TT^{\dagger} = \dfrac{1}{2}
      \begin{pmatrix}
        1 &  1 & 0        \\
        i & -i & 0        \\
        0 &  0 & \sqrt{2} \\
      \end{pmatrix}
      \begin{pmatrix}
        1 & -i & 0        \\
        1 & i  & 0        \\
        0 & 0  & \sqrt{2} \\
      \end{pmatrix}
      =
      \begin{pmatrix}
        1 & 0 & 0\\
        0 & 1 & 0\\
        0 & 0 & 1\\
      \end{pmatrix} \\
      T^{\dagger}T = \dfrac{1}{2}
      \begin{pmatrix}
        1 & -i & 0        \\
        1 & i  & 0        \\
        0 & 0  & \sqrt{2} \\
      \end{pmatrix}
      \begin{pmatrix}
        1 & 1  & 0        \\
        i & -i & 0        \\
        0 & 0  & \sqrt{2} \\
      \end{pmatrix}
      =
      \begin{pmatrix}
        1 & 0 & 0\\
        0 & 1 & 0\\
        0 & 0 & 1\\
      \end{pmatrix}
    \end{matrix}
    \Rightarrow
    T^{\dagger} = T^{-1}

Cahnge to the spherical basis
==============================

Spin vector
-----------

Now we write the :math:`\vert S_{ma}\rangle` in the :math:`\vert u^+u^-n\rangle`
reference frame:

.. math::
  \langle u^+u^-n\vert S_{ma}\rangle
  = \langle u^+u^-n\vert uvn \rangle\langle uvn\vert S_{ma}\rangle
  = \langle uvn\vert T^{\dagger}\vert uvn\rangle\langle uvn\vert S_{ma}\rangle

.. dropdown:: Details

  .. math::
    = \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2}
    \end{pmatrix}
    \begin{pmatrix}
      S_{ma}^{u} \\
      S_{ma}^{v} \\
      S_{ma}^{n} \\
    \end{pmatrix}
    = \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      S_{ma}^{u} - iS_{ma}^{u} \\
      S_{ma}^{v} + iS_{ma}^{u} \\
      \sqrt{2}S_{ma}^{n}
    \end{pmatrix}
    =
    \begin{pmatrix}
      S_{ma}^{-} \\
      S_{ma}^{+} \\
      S_{ma}^{n}
    \end{pmatrix}


  where we defined:

  .. math::
    \begin{multline}
      S_{ma}^{\pm} = \dfrac{S_{ma}^u \pm iS_{ma}^v}{\sqrt{2}} =
      \dfrac{\sin\theta_a[\cos(\vec{Q}\cdot\vec{r}_m + \phi_a)
      \pm i\sin(\vec{Q}\cdot\vec{r}_m + \phi_a)]}{\sqrt{2}} \\
      =\dfrac{\sin\theta_a[\cos(\pm\vec{Q}\cdot\vec{r}_m \pm \phi_a)
      + i\sin(\pm\vec{Q}\cdot\vec{r}_m \pm \phi_a)]}{\sqrt{2}}
      = \dfrac{\sin\theta_a}{\sqrt{2}}\cdot e^{\pm i (\vec{Q}\cdot\vec{r}_m + \phi_a)}
    \end{multline}

.. math::
  \langle u^+u^-n\vert S_{ma}\rangle
  =
  \begin{pmatrix}
    S_{ma}^{-} \\
    S_{ma}^{+} \\
    S_{ma}^{n}
  \end{pmatrix}
  =
  \begin{pmatrix}
     \dfrac{\sin\theta_a}{\sqrt{2}}\cdot e^{- i (\vec{Q}\cdot\vec{r}_m + \phi_a)} \\
     \dfrac{\sin\theta_a}{\sqrt{2}}\cdot e^{+ i (\vec{Q}\cdot\vec{r}_m + \phi_a)} \\
     \cos\theta_a
  \end{pmatrix}
