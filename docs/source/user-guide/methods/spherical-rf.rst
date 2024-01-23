.. _user-guide_methods_spherical-rf:

***************************
"Spherical" reference frame
***************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/in-uvn.txt
  * .. include:: page-notations/parentheses.txt

From the :ref:`previous section <user-guide_methods_single-q>` we recall:

.. include:: repeated-formulas/spin-from-ferro-any.txt

.. include:: repeated-formulas/spin-uvn.txt

Coordinate system with circular polarization
============================================

Later we use the reference frame with circular polarized :math:`\vert u \rangle` and
:math:`\vert v \rangle` vectors. Here we present the algebra for this
reference frame. First of all, we define the transformation matrix as:

.. math::
  \boldsymbol{T} \vert uvn \rangle
  =
  \vert u^+u^-n \rangle

The transformation matrix is designed as follows:

.. math::
  \begin{matrix}
    \vert u^{\pm} \rangle
    =
    \dfrac{\vert u \rangle \pm i \vert v \rangle }{\sqrt{2}}
    & \text{and} &
    \vert n \rangle
    =
    \vert n \rangle
  \end{matrix}

Which results in the unitary transformation matrix:

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

.. dropdown:: Unitary check

  .. math::
    \begin{matrix}
      \boldsymbol{T}\boldsymbol{T}^{\dagger} = \dfrac{1}{2}
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
      \boldsymbol{T}^{\dagger}\boldsymbol{T} = \dfrac{1}{2}
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
    \boldsymbol{T}^{\dagger} = \boldsymbol{T}^{-1}

Change to the spherical basis
=============================

Spin vector
-----------

Now we write the :math:`\vert S_{ma}\rangle` in the :math:`\vert u^+u^-n\rangle`
reference frame:

.. math::
  \langle u^+u^-n \vert S_{ma} \rangle
  =
  \langle u^+u^-n \vert uvn \rangle
  \langle uvn \vert S_{ma} \rangle
  =
  \langle uvn \vert T^{\dagger} \vert uvn \rangle
  \langle uvn \vert S_{ma} \rangle

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
      S_{ma}^{\pm}
      =
      \dfrac{S_{ma}^u \pm iS_{ma}^v}{\sqrt{2}}
      =
      S_a
      \cdot
      \dfrac{
        \sin\theta_a[
          \cos(\boldsymbol{q}\cdot\boldsymbol{r}_m + \phi_a)
          \pm
          i\sin(\boldsymbol{q}\cdot\boldsymbol{r}_m + \phi_a)
        ]
      }{\sqrt{2}}
      =\\=
      S_a
      \cdot
      \dfrac{
        \sin\theta_a[
          \cos(\pm\boldsymbol{q}\cdot\boldsymbol{r}_m \pm \phi_a)
          +
          i\sin(\pm\boldsymbol{q}\cdot\boldsymbol{r}_m \pm \phi_a)
        ]
      }{\sqrt{2}}
      =
      S_a
      \cdot
      \dfrac{\sin\theta_a}{\sqrt{2}}
      \cdot
      e^{\pm i (\boldsymbol{q}\cdot\boldsymbol{r}_m + \phi_a)}
    \end{multline}

.. include:: repeated-formulas/spin-spherical.txt

Rotation matrix :math:`\boldsymbol{R}(\theta_a,\phi_a)`
-------------------------------------------------------

.. dropdown:: Details

  First we recall the rotation matrix in the :math:`\vert uvn\rangle` reference frame:

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.txt

  Then we compute the transformation:

  .. math::
    &\langle u^+u^-n \vert R_a \vert u^+u^-n \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert R_a \vert uvn \rangle
    \langle uvn \vert u^+u^-n \rangle
    =\\&=
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert R_a \vert uvn \rangle
    \langle uvn \vert T\vert uvn \rangle

  The exact form of this matrix will be useful later:

  .. math::
    &\dfrac{1}{2}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      \cos\theta_a + \sin^2\phi_a(1-\cos\theta_a) &
      -\sin\phi_a\cos\phi_a(1-\cos\theta_a)       &
      \cos\phi_a\sin\theta_a                      \\
      -\sin\phi_a\cos\phi_a(1-\cos\theta_a)       &
      \cos\theta_a + \cos^2\phi_a(1-\cos\theta_a) &
      \sin\phi_a\sin\theta_a                      \\
      -\cos\phi_a\sin\theta_a                     &
      -\sin\phi_a\sin\theta_a                     &
      \cos\theta_a                                \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      \cos\theta_a + \sin\phi_a(1-\cos\theta_a)(\sin\phi_a + i\cos\phi_a)   &
      -i\cos\theta_a - \cos\phi_a(1-\cos\theta_a)(\sin\phi_a + i\cos\phi_a) &
      \sin\theta_a(\cos\phi_a - i\sin\phi_a)                                \\
      \cos\theta_a + \sin\phi_a(1-\cos\theta_a)(\sin\phi_a - i\cos\phi_a)   &
      i\cos\theta_a - \cos\phi_a(1-\cos\theta_a)(\sin\phi_a - i\cos\phi_a)  &
      \sin\theta_a(\cos\phi_a + i\sin\phi_a)                                \\
      -\sqrt{2}\sin\theta_a\cos\phi_a                                       &
      -\sqrt{2}\sin\theta_a\sin\phi_a                                       &
      \sqrt{2}\cos\theta_a                                                  \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      1+\cos\theta_a                     &
      (\cos\theta_a-1)e^{-2i\phi_a}      &
      \sqrt{2}\sin\theta_a e^{-i\phi_a}  \\
      (\cos\theta_a - 1)e^{2i\phi_a}     &
      1 + \cos\theta_a                   &
      \sqrt{2}\sin\theta_a e^{i\phi_a}   \\
      -\sqrt{2}\sin\theta_a e^{i\phi_a}  &
      -\sqrt{2}\sin\theta_a e^{-i\phi_a} &
      2\cos\theta_a                      \\
    \end{pmatrix}

.. include:: repeated-formulas/spin-rotation-matrix-spherical.txt

Rotation matrix :math:`\boldsymbol{R}(\theta_m)`
------------------------------------------------

.. dropdown:: Details

  First we recall the rotation matrix in the :math:`\vert uvn\rangle` reference frame:

  .. include:: repeated-formulas/spiral-rotation-matrix-uvn.txt

  Then we compute the transformation:

  .. math::
    &\langle u^+u^-n \vert R(\theta_m) \vert u^+u^-n \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert R(\theta_m) \vert uvn \rangle
    \langle uvn \vert u^+u^-n \rangle
    =\\&=
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert R(\theta_m) \vert uvn \rangle
    \langle uvn \vert T \vert uvn \rangle

  The exact form of this matrix will be useful later:

  .. math::
    &\dfrac{1}{2}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      \cos(\theta_m) & -\sin(\theta_m) & 0 \\
      \sin(\theta_m) & \cos(\theta_m)  & 0 \\
      0              & 0               & 1 \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      \cos\theta_m - i\sin\theta_m  &
      -\sin\theta_m - i\cos\theta_m &
      0                             \\
      \cos\theta_m + i\sin\theta_m  &
      -\sin\theta_m + i\cos\theta_m &
      0                             \\
      0                             &
      0                             &
      \sqrt{2}                      \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      2e^{-i\theta_m} & 0              & 0 \\
      0               & 2e^{i\theta_m} & 0 \\
      0               & 0              & 2 \\
    \end{pmatrix}

.. include:: repeated-formulas/spiral-rotation-matrix-spherical.txt
