.. _user-guide_methods_spherical-rf:

*************************
Spherical reference frame
*************************

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

Now we write the :math:`\vert S_{mi}\rangle` in the :math:`\vert u^+u^-n\rangle`
reference frame:

.. math::
  \langle u^+u^-n \vert S_{mi} \rangle
  =
  \langle u^+u^-n \vert uvn \rangle
  \langle uvn \vert S_{mi} \rangle
  =
  \langle uvn \vert T^{\dagger} \vert uvn \rangle
  \langle uvn \vert S_{mi} \rangle

.. dropdown:: Details

  .. math::
    = \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2}
    \end{pmatrix}
    \begin{pmatrix}
      S_{mi}^{u} \\
      S_{mi}^{v} \\
      S_{mi}^{n} \\
    \end{pmatrix}
    = \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      S_{mi}^{u} - iS_{mi}^{u} \\
      S_{mi}^{v} + iS_{mi}^{u} \\
      \sqrt{2}S_{mi}^{n}
    \end{pmatrix}
    =
    \begin{pmatrix}
      S_{mi}^{-} \\
      S_{mi}^{+} \\
      S_{mi}^{n}
    \end{pmatrix}

  where we defined:

  .. math::
    \begin{multline}
      S_{mi}^{\pm}
      =
      \dfrac{S_{mi}^u \pm iS_{mi}^v}{\sqrt{2}}
      =
      S_i
      \cdot
      \dfrac{
        \sin\theta_i[
          \cos(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)
          \pm
          i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)
        ]
      }{\sqrt{2}}
      =\\=
      S_i
      \cdot
      \dfrac{
        \sin\theta_i[
          \cos(\pm\boldsymbol{q}\cdot\boldsymbol{r_m} \pm \phi_i)
          +
          i\sin(\pm\boldsymbol{q}\cdot\boldsymbol{r_m} \pm \phi_i)
        ]
      }{\sqrt{2}}
      =
      S_i
      \cdot
      \dfrac{\sin\theta_i}{\sqrt{2}}
      \cdot
      e^{\pm i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)}
    \end{multline}

.. include:: repeated-formulas/spin-spherical.txt

Rotation matrix :math:`\boldsymbol{R}(\theta_i,\phi_i)`
-------------------------------------------------------

.. dropdown:: Details

  First we recall the rotation matrix in the :math:`\vert uvn\rangle` reference frame:

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.txt

  Then we compute the transformation:

  .. math::
    &\langle u^+u^-n \vert R_i \vert u^+u^-n \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert R_i \vert uvn \rangle
    \langle uvn \vert u^+u^-n \rangle
    =\\&=
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert R_i \vert uvn \rangle
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
      \cos\theta_i + \sin^2\phi_i(1-\cos\theta_i) &
      -\sin\phi_i\cos\phi_i(1-\cos\theta_i)       &
      \cos\phi_i\sin\theta_i                      \\
      -\sin\phi_i\cos\phi_i(1-\cos\theta_i)       &
      \cos\theta_i + \cos^2\phi_i(1-\cos\theta_i) &
      \sin\phi_i\sin\theta_i                      \\
      -\cos\phi_i\sin\theta_i                     &
      -\sin\phi_i\sin\theta_i                     &
      \cos\theta_i                                \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      \cos\theta_i + \sin\phi_i(1-\cos\theta_i)(\sin\phi_i + i\cos\phi_i)   &
      -i\cos\theta_i - \cos\phi_i(1-\cos\theta_i)(\sin\phi_i + i\cos\phi_i) &
      \sin\theta_i(\cos\phi_i - i\sin\phi_i)                                \\
      \cos\theta_i + \sin\phi_i(1-\cos\theta_i)(\sin\phi_i - i\cos\phi_i)   &
      i\cos\theta_i - \cos\phi_i(1-\cos\theta_i)(\sin\phi_i - i\cos\phi_i)  &
      \sin\theta_i(\cos\phi_i + i\sin\phi_i)                                \\
      -\sqrt{2}\sin\theta_i\cos\phi_i                                       &
      -\sqrt{2}\sin\theta_i\sin\phi_i                                       &
      \sqrt{2}\cos\theta_i                                                  \\
    \end{pmatrix}
    \begin{pmatrix}
      1 & 1 & 0         \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      1+\cos\theta_i                     &
      (\cos\theta_i-1)e^{-2i\phi_i}      &
      \sqrt{2}\sin\theta_i e^{-i\phi_i}  \\
      (\cos\theta_i - 1)e^{2i\phi_i}     &
      1 + \cos\theta_i                   &
      \sqrt{2}\sin\theta_i e^{i\phi_i}   \\
      -\sqrt{2}\sin\theta_i e^{i\phi_i}  &
      -\sqrt{2}\sin\theta_i e^{-i\phi_i} &
      2\cos\theta_i                      \\
    \end{pmatrix}

.. include:: repeated-formulas/spin-rotation-matrix-spherical.txt

Rotation matrix :math:`\boldsymbol{R}(\phi_m)`
------------------------------------------------

.. dropdown:: Details

  First we recall the rotation matrix in the :math:`\vert uvn\rangle` reference frame:

  .. include:: repeated-formulas/spiral-rotation-matrix-uvn.txt

  Then we compute the transformation:

  .. math::
    &\langle u^+u^-n \vert R(\phi_m) \vert u^+u^-n \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert R(\phi_m) \vert uvn \rangle
    \langle uvn \vert u^+u^-n \rangle
    =\\&=
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert R(\phi_m) \vert uvn \rangle
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
      \cos(\phi_m) & -\sin(\phi_m) & 0 \\
      \sin(\phi_m) & \cos(\phi_m)  & 0 \\
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
      \cos\phi_m - i\sin\phi_m  &
      -\sin\phi_m - i\cos\phi_m &
      0                             \\
      \cos\phi_m + i\sin\phi_m  &
      -\sin\phi_m + i\cos\phi_m &
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
      2e^{-i\phi_m} & 0              & 0 \\
      0               & 2e^{i\phi_m} & 0 \\
      0               & 0              & 2 \\
    \end{pmatrix}

.. include:: repeated-formulas/spiral-rotation-matrix-spherical.txt
