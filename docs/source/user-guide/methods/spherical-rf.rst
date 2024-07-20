.. _user-guide_methods_spherical-rf:

**************************
Spherical reference frames
**************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/rotations.inc

Much of quantum spin algebra is written in a spherical basis. Furthermore, spin-waves
are frequently circularly polarized.
This section is devoted to translating spin vector components and matrix elements
to spherical bases.

===============
Spherical bases
===============

We perform the transformations

.. math::
  \ket{\,n^+\,n^-\,n\,}&=\ket{\,u\,v\,n\,}\,\boldsymbol{T}\\
  \ket{\,f^+_i\,f^-_i\,f_i\,}&=\ket{\,p_i\,t_i\,n_i\,}\,\boldsymbol{T}

where the transformation matrix is basis-independent and given by

.. math::
  \boldsymbol{T}=\braket{\,u\,v\,n\,|\,n^+\,n^-\,n\,}=\braket{\,p_i\,t_i\,f_i\,|\,f_i^+\,f_i^-\,f_i}
          =\frac{1}{\sqrt{2}}\,\begin{pmatrix} 1 & 1 & 0\\ i & -i & 0\\ 0& 0 & \sqrt{2}\end{pmatrix}

so that

.. math::
  \begin{matrix}
    \ket{\, n^{\pm}\, } &= \dfrac{\ket{\, u\, } \pm i\, \ket{\, v\, }}{\sqrt{2}}\\
    \ket{\, n\, } &= \ket{\, n\, }\\
    \ket{\, f_i^{\pm}\, } &= \dfrac{\ket{\, p_i\, } \pm i\, \ket{\, t_i\, }}{\sqrt{2}}\\
    \ket{\, f_i\, } &= \ket{\, f_i\, }
  \end{matrix}

============
Spin vectors
============

Ground-state spin vectors in the :math:`(\,n^+\,n^-\,n\,)` basis look like

.. math::
  \ket{S_i^0}=&  \ket{\,n^+\,n^-\,n\,}\,\braket{\,n^+\,n^-\,n\,|\,u\,v\,n\,}\,
             \braket{\,u\,v\,n\,|\,S_i\,}\\
           =& \ket{\,n^+\,n^-\,n\,}\,T^\dagger\,\, ^n\boldsymbol{S_i}=
           \ket{\,n^+\,n^-\,n\,}\,\,^{sn}\boldsymbol{S_i}

where the vector components are

.. math::
  ^{sn}\boldsymbol{S_i}
    =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\,S_{mi}^{uv,-} \\
    \frac{1}{\sqrt{2}}\,S_{mi}^{uv,+} \\
    S_{mi}^{n} \\
  \end{pmatrix}
  =
  S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{-i \,\phi_i}\\
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{i \,\phi_i}\\
           \cos \theta_i
           \end{pmatrix}

where :math:`S_i^{uv,\pm}=S^u_i\pm \,i \,S^v_i`.

-----------------------------------
Operator :math:`\boldsymbol{R_i^s}`
-----------------------------------

The basis change :math:`(\,n^+\,n^-\,n\,)` to :math:`(\,f_i^+\,f_i^-\,f_i\,)`
is achieved by the rotation operator

.. math::
  \boldsymbol{R_i^s}=
  \ket{\,f_i^+\,f_i^-\,f_i\,}\,\bra{\,n^+\,n^-\,n\,}=
    \boldsymbol{T}^\dagger\,\ket{\,p_i\,t_i\,f_i\,}\,\bra{\,u\,v\,n\,}\,\boldsymbol{T}=
  \boldsymbol{T}^\dagger\,\boldsymbol{R_i}\,\boldsymbol{T}

with matrix elements

.. math::
    ^{sn}\boldsymbol{R_i}
       &=
       \bra{\,n^+\,n^-\,n\,}\,\boldsymbol{R_i^s}\,\ket{\,n^+\,n^-\,n\,}
         \,=
         \,\boldsymbol{T}^\dagger\,^n\boldsymbol{R_i}\,\boldsymbol{T}\\
       &=
      \dfrac{1}{2}
      \begin{pmatrix}
          1 + \cos\theta_i                        &
          (\cos\theta_i - 1)\, e^{-2i\phi_i}      &
          \sqrt{2}\, \sin\theta_i\, e^{-i\phi_i}  \\
          (\cos\theta_i - 1)\, e^{2i\phi_i}       &
          1 + \cos\theta_i                        &
          \sqrt{2}\, \sin\theta_i\, e^{i\phi_i}   \\
          -\sqrt{2}\, \sin\theta_i\, e^{i\phi_i}  &
          -\sqrt{2}\, \sin\theta_i\, e^{-i\phi_i} &
          2\cos\theta_i
      \end{pmatrix}

.. dropdown:: Reminder on the :math:`\,^n\boldsymbol{R}_i` matrix

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.inc
