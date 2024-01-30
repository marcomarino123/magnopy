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

This section discusses basis changes, that are more easily understood and checked
using Dirac's vector notation.
The :ref:`previous section <user-guide_methods_single-q>` has shown
how each lattice spin with components

.. include:: repeated-formulas/spin-uvn.txt

in the :math:`(\,u\,v\,n\,)` reference frame can be obtained
from a local collinear reference frame by

.. include:: repeated-formulas/spin-from-ferro-any.txt

where all atomic vectors
are collinear :math:`\boldsymbol{S^n_{mi}}=S_i\,\boldsymbol{n}`.

Coordinate system with circular polarization
============================================
The spin algebra indicates that spin waves are often circularly polarized,
so this section discusses its proper reference frame that is termed
the spherical reference frame :math:`(\,u^+\,v,u^-\,n\,)` where the basis
vectors are

.. math::
  \begin{matrix}
    \ket{u^{\pm}} = \dfrac{\ket{u} \pm i \ket{v}}{\sqrt{2}}
    & \text{and} &
    \ket{n}=\ket{n}
  \end{matrix}

The basis transformation matrix

.. math::
  \ket{\, u^+\,u^-\,n\,}=\boldsymbol{T} \, \ket{\,u\,v\,n\,}

is

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

.. dropdown:: Unitary check

  .. math::
    \begin{matrix}
      \boldsymbol{T}\,\boldsymbol{T}^{\dagger} = \dfrac{1}{2}
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
      \boldsymbol{T}^{\dagger}\,\boldsymbol{T} = \dfrac{1}{2}
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

The spin vector :math:`\boldsymbol{S_{mi}^s}` can be written
in the spherical reference frame as

.. math::
  \boldsymbol{S_{mi}^s}
  =&
  \begin{pmatrix}
    S_{mi}^{-} \\
    S_{mi}^{+} \\
    S_{mi}^{n} \\
  \end{pmatrix}
   =\, \boldsymbol{T}^\dagger\,\boldsymbol{S_{mi}}\\
   =&
   \begin{pmatrix}
    \frac{1}{\sqrt{2}}\,(S_{mi}^u-S_{mi}^v) \\
    \frac{1}{\sqrt{2}}\,(S_{mi}^u+S_{mi}^v) \\
     S_{mi}^{n} \\
   \end{pmatrix}
  =
  \,S_i
  \,
  \begin{pmatrix}
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{- i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)} \\
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{+ i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)} \\
     \cos\theta_i                                                                 \\
  \end{pmatrix}

.. dropdown:: Details

  .. math::
    \braket{\,u^+\,u^-\,n \,|\, S_{mi}\,}
    =
    \braket{\,u^+\,u^-\, n \,|\, u\, v\, n\,} \,
    \braket{\,u\, v\, n\,|\, S_{mi}\,}
    =
    \braket{\,u\, v\, n\,|\, T^{\dagger} \,|\,u\, v\, n\,} \,
    \braket{\,u\, v\, n\, | \,S_{mi}\,}

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

  where

  .. math::
      S_{mi}^{\pm}
      =&
      \dfrac{S_{mi}^u \pm iS_{mi}^v}{\sqrt{2}}
      =
      S_i\,\dfrac{
        \sin\theta_i[
          \cos(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)
          \pm
          i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)]}{\sqrt{2}}
      =\\
      =&
      S_i\,\dfrac{\sin\theta_i}{\sqrt{2}}
      \,e^{\pm i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)}

Intra-atomic rotation matrix :math:`\boldsymbol{R^s_i}`
-------------------------------------------------------------
The matrix elements of the rotation matrix :math:`\boldsymbol{R_i}`
in the spherical basis can be obtained from the expression

.. math::
  \boldsymbol{R_i^{s}}=\boldsymbol{T}^\dagger\,\boldsymbol{R_i}\,\boldsymbol{T}
  =\dfrac{1}{2}
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

.. dropdown:: Details

  .. math::
    \braket{\,u^+\,u^-\,n\,| \, R_i\, |\, u^+\,u^-\,n\,}
    &=
    \braket{\,u^+\,u^-\,n\,| \, u\,v\,n\,} \,
    \braket{\, u\,v\,n\,|\, R_i \,|\, u\,v\,n\,} \,
    \braket{\, u\,v\,n\,|\, u^+\,u^-\,n\,}
    \\&=
    \braket{\,u\,v\,n\,|\, T^{\dagger} \,|\, u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\,  R_i \,|\, u\,v\,n\,} \,
    \braket{\,u\,v\,n \,|\, T\,|\, u\,v\,n\, }

    where the rotation matrix in the :math:`(\,u\,v\,n\,)\` reference frame is

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.txt

Inter-cell rotation matrix :math:`\boldsymbol{R_m^s}(\boldsymbol{q})`
---------------------------------------------------------------------
The matrix elements of the rotation matrix :math:`\boldsymbol{R_m}`
in the spherical basis can be obtained from the expression

.. math::
  \boldsymbol{R_m^{s}}=\boldsymbol{T}^\dagger\,\boldsymbol{R_m}\,\boldsymbol{T}
  =
  \begin{pmatrix}
    e^{-i\boldsymbol{q}\cdot\boldsymbol{r_m}} & 0                          & 0 \\
    0                           & e^{i\boldsymbol{q}\cdot\boldsymbol{r_m}} & 0 \\
    0                           & 0                          & 1 \\
  \end{pmatrix}

.. dropdown:: Details

  First we recall the rotation matrix in the :math:`\vert uvn\rangle` reference frame:

  .. include:: repeated-formulas/spiral-rotation-matrix-uvn.txt

  Then we compute the transformation:

  .. math::
    \langle u^+u^-n \vert R(\phi_m) \vert u^+u^-n \rangle
    &=
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
    \begin{pmatrix}
      e^{-i\phi_m} & 0              & 0 \\
      0               & e^{i\phi_m} & 0 \\
      0               & 0              & 1 \\
    \end{pmatrix}
