.. _user-guide_methods_spherical-rf:

*************************
Spherical reference frame
*************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/parentheses.inc
  * .. include:: page-notations/uvn-or-spherical.inc

The :ref:`previous section <user-guide_methods_single-q>` has shown
how each lattice spin of the spiral conical state can be generated from a global
ferromagnetic state, where all spins are aligned along the direction of
:math:`\boldsymbol{n}`:

.. include:: repeated-formulas/spin-from-ferro-uvn.inc

This section is devoted to translation of these spin vectors and matrices to spherical
basis, that is more convenient in several instances.

============================================
Coordinate system with circular polarization
============================================
The spin algebra indicates that spin waves are often circularly polarized,
so this section discusses its proper reference frame that is termed
the spherical reference frame :math:`(\,u^+\,u^-\,n\,)` where the basis
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

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.inc

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

.. hint::
  Introduction of this spherical reference frame caused the change of the transposition
  sign ":math:`^T`" to the hermitian conjugate ":math:`^{\dagger}`" in the formulas across
  the whole documentation.

=============================
Change to the spherical basis
=============================

--------------------------------------------------------------------------------
Intra-cell rotation matrix :math:`\boldsymbol{R}_i\rightarrow\boldsymbol{R}^s_i`
--------------------------------------------------------------------------------

.. dropdown:: :math:`\boldsymbol{R}_i\text{ in }(\,u,\,v,\,n)\text{ basis}`

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.inc

The matrix elements of the rotation matrix
:math:`\boldsymbol{R}_i=(\boldsymbol{\hat{p}}_i\,\boldsymbol{\hat{t}}_i\,\boldsymbol{\hat{f}}_i)`
in the spherical basis can be obtained from the expression

.. math::
  \boldsymbol{R}_i^s
  =\boldsymbol{T}^\dagger\,\boldsymbol{R}_i\,\boldsymbol{T}
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

The above expression also defines the vectors :math:`\boldsymbol{\hat{p}}_i`,
:math:`\boldsymbol{\hat{t}}_i`, and :math:`\boldsymbol{\hat{f}}_i` in the spherical basis:

.. math::
  \boldsymbol{\hat{p}}^s_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{\hat{p}}_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\boldsymbol{\hat{u}}
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\,\boldsymbol{T}\boldsymbol{T}^{\dagger}\,\boldsymbol{\hat{u}}
  =
  &\boldsymbol{R}_i^s\,\boldsymbol{\hat{u}}^+
  =
  \dfrac{1}{2}
  \begin{pmatrix}
    1+\cos\theta_i                     \\
    (\cos\theta_i - 1)e^{2i\phi_i}     \\
    -\sqrt{2}\sin\theta_i e^{i\phi_i}
  \end{pmatrix}
  \\\\
  \boldsymbol{\hat{t}}^s_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{\hat{t}}_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\boldsymbol{\hat{v}}
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\,\boldsymbol{T}\boldsymbol{T}^{\dagger}\,\boldsymbol{\hat{v}}
  =
  &\boldsymbol{R}_i^s\,\boldsymbol{\hat{u}}^+
  =
  \dfrac{1}{2}
  \begin{pmatrix}
    (\cos\theta_i-1)e^{-2i\phi_i}     \\
    1 + \cos\theta_i                  \\
    -\sqrt{2}\sin\theta_i e^{-i\phi_i}
  \end{pmatrix}
  \\\\
  \boldsymbol{\hat{f}}^s_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{\hat{f}}_i
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\boldsymbol{\hat{n}}
  =
  \boldsymbol{T}^{\dagger}\boldsymbol{R}_i\,\boldsymbol{T}\boldsymbol{T}^{\dagger}\,\boldsymbol{\hat{n}}
  =
  &\boldsymbol{R}_i^s\,\boldsymbol{\hat{n}}
  =
  \dfrac{1}{2}
  \begin{pmatrix}
    \sqrt{2}\sin\theta_i e^{-i\phi_i}  \\
    \sqrt{2}\sin\theta_i e^{i\phi_i}   \\
    2\cos\theta_i                      \\
  \end{pmatrix}

----------------------------------------------------------------------------------------------------------------
Inter-cell rotation matrix :math:`\boldsymbol{R}_m(\boldsymbol{q})\rightarrow\boldsymbol{R}_m^s(\boldsymbol{q})`
----------------------------------------------------------------------------------------------------------------

.. dropdown:: :math:`\boldsymbol{R}_m\text{ in }(\,u,\,v,\,n)\text{ basis}`

  .. include:: repeated-formulas/spiral-rotation-matrix-uvn.inc

The matrix elements of the rotation matrix :math:`\boldsymbol{R}_m`
in the spherical basis can be obtained from the expression

.. include:: repeated-formulas/spiral-rotation-matrix-spherical.inc

-----------------------------------------------------------------------
Spin vector :math:`\boldsymbol{S}_{mi}\rightarrow\boldsymbol{S}_{mi}^s`
-----------------------------------------------------------------------
The spin vector :math:`\boldsymbol{S}_{mi}` can be written
in the spherical basis as

.. math::
  \boldsymbol{S}_{mi}^s
   =&
   \, \boldsymbol{T}^\dagger\,\boldsymbol{S}_{mi}
   =\boldsymbol{T}^\dagger\,\boldsymbol{R}_m\,\boldsymbol{R}_i\,\boldsymbol{S^F}_{mi}
   \\\\
   =&\,
   \boldsymbol{R}_m^s\,\boldsymbol{R}_i^s\,\boldsymbol{S^{F,s}}_{i}=
     \boldsymbol{R}_m^s\,\boldsymbol{S}_i^s\,=
     S_i\,\boldsymbol{R}_m^s\,\boldsymbol{\hat{f}}_{i}^s\,\\\\
    =&
  \,S_i
  \,
  \begin{pmatrix}
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{- i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)} \\
     \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{+ i (\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)} \\
     \cos\theta_i                                                                 \\
  \end{pmatrix}

---------------------------------------------------------------------------
Exchange tensor :math:`\boldsymbol{J_{ij}}\rightarrow\boldsymbol{J_{ij}^s}`
---------------------------------------------------------------------------
The exchange matrix in the spherical reference frame is obtained through

.. math:: \boldsymbol{J_{ij}}^s =&
  \begin{pmatrix}
    J_{ij}^{++} & J_{ij}^{+-} & J_{ij}^{+n} \\
    J_{ij}^{-+} & J_{ij}^{--} & J_{ij}^{-n} \\
    J_{ij}^{n+} & J_{ij}^{n-} & J_{ij}^{nn} \\
  \end{pmatrix}\,=\,
  \boldsymbol{T}^\dagger\,\boldsymbol{J_{ij}}\,\boldsymbol{T}\,
  \\\\=&
  \begin{pmatrix}
    J^{I} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} + iD_{ij}^n                       &
    \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} - iS_{ij}^{uv}                              &
    \dfrac{S_{ij}^{un} - iS_{ij}^{vn}}{\sqrt{2}} - \dfrac{D_{ij}^v + iD_{ij}^u}{\sqrt{2}} \\
    \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} + iS_{ij}^{uv}                              &
    J^{I} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} - iD_{ij}^n                       &
    \dfrac{S_{ij}^{un} + iS_{ij}^{vn}}{\sqrt{2}} - \dfrac{D_{ij}^v - iD_{ij}^u}{\sqrt{2}} \\
    \dfrac{S_{ij}^{un} + iS_{ij}^{vn}}{\sqrt{2}} + \dfrac{D_{ij}^v - iD_{ij}^u}{\sqrt{2}} &
    \dfrac{S_{ij}^{un} - iS_{ij}^{vn}}{\sqrt{2}} + \dfrac{D_{ij}^v + iD_{ij}^u}{\sqrt{2}} &
    J^{I} + S_{ij}^{nn}                                                  \\
  \end{pmatrix}


.. dropdown:: Details

  .. math::
    \braket{ \,u^+\,u^-\,n\, |\, J_{ij} \,|\, u^+\,u^-\,n\,}
    =&
    \braket{\,u^+\,u^-\,n \,|\,u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, J_{ij}\,|\, u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, u^+\,u^-\,n\,}
    =\\=&
    \braket{\,u\,v\,n\,|\, T^{\dagger}\,|\, u\,v\,n\,}\,
    \braket{\,u\,v\,n\,|\, J_{ij}\,|\,u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, T\,|\, u\,v\,n\,}

  .. math::
    &\langle u^+u^-n \vert J_{ij}(\boldsymbol{d_{ij}}) \vert u^+u^-n \rangle
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      J_{ij}^{uu} & J_{ij}^{uv} & J_{ij}^{un} \\
      J_{ij}^{vu} & J_{ij}^{vv} & J_{ij}^{vn} \\
      J_{ij}^{nu} & J_{ij}^{nv} & J_{ij}^{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      J_{ij}^{uu} - i J_{ij}^{vu} & J_{ij}^{uv} - i J_{ij}^{vv} & J_{ij}^{un} - i J_{ij}^{vn} \\
      J_{ij}^{uu} + i J_{ij}^{vu} & J_{ij}^{uv} + i J_{ij}^{vv} & J_{ij}^{un} + i J_{ij}^{vn} \\
      \sqrt{2}J_{ij}^{nu}    & \sqrt{2}J_{ij}^{nv}    & \sqrt{2}J_{ij}^{nn}    \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      (J_{ij}^{uu} + J_{ij}^{vv}) + i(J_{ij}^{uv} - J_{ij}^{vu}) &
      (J_{ij}^{uu} - J_{ij}^{vv}) - i(J_{ij}^{uv} + J_{ij}^{vu}) &
      \sqrt{2}(J_{ij}^{un} - iJ_{ij}^{vn})             \\
      (J_{ij}^{uu} - J_{ij}^{vv}) + i(J_{ij}^{uv} + J_{ij}^{vu}) &
      (J_{ij}^{uu} + J_{ij}^{vv}) - i(J_{ij}^{uv} - J_{ij}^{vu}) &
      \sqrt{2}(J_{ij}^{un} + iJ_{ij}^{vn})             \\
      \sqrt{2}(J_{ij}^{nu} + iJ_{ij}^{nv})             &
      \sqrt{2}(J_{ij}^{nu} - iJ_{ij}^{nv})             &
      2J_{ij}^{nn}                                \\
    \end{pmatrix}

  Which gives:

  .. math::
    \langle u^+u^-n \vert J_{ij}(\boldsymbol{d_{ij}})\vert u^+u^-n \rangle
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      2J^{iso} + S_{ij}^{uu} + S_{ij}^{vv} + 2iD_{ij}^n      &
      S_{ij}^{uu} - S_{ij}^{vv} - 2iS_{ij}^{uv}              &
      \sqrt{2}(S_{ij}^{un} - iS_{ij}^{vn} - D_{ij}^v - iD_{ij}^u) \\
      S_{ij}^{uu} - S_{ij}^{vv} + 2iS_{ij}^{uv}              &
      2J^{iso} + S_{ij}^{uu} + S_{ij}^{vv} - 2iD_{ij}^n      &
      \sqrt{2}(S_{ij}^{un} + iS_{ij}^{vn} - D_{ij}^v + iD_{ij}^u) \\
      \sqrt{2}(S_{ij}^{un} + iS_{ij}^{vn} + D_{ij}^v - iD_{ij}^u) &
      \sqrt{2}(S_{ij}^{un} - iS_{ij}^{vn} + D_{ij}^v + iD_{ij}^u) &
      2J^{iso} + 2S_{ij}^{nn}                      \\
    \end{pmatrix}

Let us note a few symmetries of the exchange matrix in a spherical reference frame:

.. include:: repeated-formulas/exchange-matrix-symmetries-spherical.inc

.. dropdown:: Alternative way to write the matrix

  If we define:

  .. math::
    \begin{matrix}
      D^{\pm} = \dfrac{D_{ij}^v \pm iD_{ij}^u}{\sqrt{2}};      &
      S^{\pm} = \dfrac{S_{ij}^{un} \pm iS_{ij}^{vn}}{\sqrt{2}} \\
    \end{matrix}

  Then we can write the exchange matrix in the spherical reference frame as:

  .. math::
    \begin{pmatrix}
      J_{ij}^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} + iD_{ij}^n &
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} - iS_{ij}^{uv}        &
      S_{ij}^- - D_{ij}^+                                   \\
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} + iS_{ij}^{uv}        &
      J_{ij}^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} - iD_{ij}^n &
      S_{ij}^+ - D_{ij}^-                                   \\
      S_{ij}^+ + D_{ij}^-                                   &
      S_{ij}^- + D_{ij}^+                                   &
      J_{ij}^{iso} + S_{ij}^{nn}                            \\
    \end{pmatrix}

----------------------------------------------------------------
Magnetic field :math:`\boldsymbol{h}\rightarrow\boldsymbol{h}^s`
----------------------------------------------------------------
The magnetic field vector :math:`\boldsymbol{h}` can be written
in the spherical reference frame as

.. include:: repeated-formulas/magnetic-field-spherical.inc

.. dropdown:: Details

  Magnetic field in the :math:`uvn` reference frame is written as:

  .. math::
    \boldsymbol{h_{mi}}
    =
    \begin{pmatrix}
      h^u \\
      h^v \\
      h^n \\
    \end{pmatrix}

  Let us compute the magnetic field in the spherical reference frame:

  .. math::
    \langle u^+u^-n \vert h \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert h \rangle
    =
    \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert h \rangle

  Which leads to the expression:

  .. math::
    \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      h^u \\
      h^v \\
      h^n \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      \frac{1}{\sqrt{2}}\,(h^u - ih^v) \\
      \frac{1}{\sqrt{2}}\,(h^u + ih^v) \\
      h^n     \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      \frac{1}{\sqrt{2}}\,h^{-} \\
      \frac{1}{\sqrt{2}}\,h^{+} \\
      h^n                        \\
    \end{pmatrix}

============================================
Hamiltonian in the spherical reference frame
============================================
The Heisenberg Hamiltonian can be written now in the spherical reference frame as follows

.. math::
  H
  =
  \dfrac{1}{2} \sum_{m, \boldsymbol{d_{ij}}, i, j}\,
  \boldsymbol{S}^{s,\dagger}_{mi}\,
  \boldsymbol{J}^s_{ij}(\boldsymbol{d}_{ij})\,
  \boldsymbol{S}^s_{m+d_{ij},j}
  +
  \mu_B\,\boldsymbol{h}^{s,\dagger}\,
  \sum_{m,i}\,g_i \,\boldsymbol{S}^s_{mi}
