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
  \ket{\,n^+\,n^-\,n\,}&=\boldsymbol{T}\,\ket{\,u\,v\,n\,}\\
  \ket{\,f^+_i\,f^-_i\,f_i\,}&=\boldsymbol{T}\,\ket{\,p_i\,t_i\,n_i\,}

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

Spin vectors in the :math:`(\,n^+\,n^-\,n\,)` basis look like

.. math::
  \ket{S_i}=  \ket{\,n^+\,n^-\,n\,}\,\braket{\,n^+\,n^-\,n\,|\,u\,v\,n\,}\,
             \braket{\,u\,v\,n\,|\,S_i\,}
           = \ket{\,n^+\,n^-\,n\,}\,T^\dagger\,\, ^n\boldsymbol{S_i}=
           \ket{\,n^+\,n^-\,n\,}\,\,^{sn}\boldsymbol{S_i}

where the vector components are

.. math::
  ^{sn}\boldsymbol{S_i}=
  \begin{pmatrix}\frac{1}{\sqrt{2}}\,(S^u_i-i \,S^v_i)\\
                 \frac{1}{\sqrt{2}}\,(S^u_i-i \,S^v_i)\\
                 S_i^n
  \end{pmatrix}=
  S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{-i \,\phi_i}\\
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{i \,\phi_i}\\
           \cos \theta_i
           \end{pmatrix}

Spin vectors in the :math:`(\,f_i^+\,f_i^-\,f_i\,)` basis look like

.. math::
  \ket{\tilde{S}_i}=  \ket{\,f_i^+\,f_i^-\,f_i\,}\,
              \braket{\,f_i^+\,f_i^-\,f_i\,|\,p_i\,t_i\,f_i\,}\,
             \braket{\,p_i\,t_i\,f_i\,|\,\tilde{S}_i\,}
           = \ket{\,f_i^+\,f_i^-\,f_i\,}\,T^\dagger\,\, ^f\boldsymbol{\tilde{S}_i}=
           \ket{\,f_i^+\,f_i^-\,f_i\,}\,\,^{sf}\boldsymbol{\tilde{S}_i}

where the vector components are

.. math::
  ^{sf}\boldsymbol{\tilde{S}_i}=
  S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\delta S^-_i\\
           \frac{1}{\sqrt{2}}\,\delta S^+_i\\
           \cos \theta_i
           \end{pmatrix}

with :math:`\delta{S}_i^\pm=\frac{1}{\sqrt{2}}\,(\delta S^p_i\pm i \,\delta S^t_i)`

------------------------------------------------------------------------------------
Intra-cell rotation matrix :math:`\boldsymbol{R}_i\,\rightarrow\,^s\boldsymbol{R_i}`
------------------------------------------------------------------------------------

.. dropdown:: Reminder on the :math:`\,^n\boldsymbol{R}_i` matrix

  .. include:: repeated-formulas/spin-rotation-matrix-uvn.inc

The :math:`\boldsymbol{R}_i` matrix elements in the spherical :math:`(\,n^+\,n^-\,n\,)` basis are

.. math::
    ^{n,s}\boldsymbol{R_i}
       &=
       \bra{\,n^+\,n^-\,n\,}\,\boldsymbol{R_i}\,\ket{\,n^+\,n^-\,n\,}
         \,=\,\boldsymbol{T}^\dagger\,^n\boldsymbol{R_i}\,\boldsymbol{T}\\
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

.. dropdown:: Details

  .. math::
    ^{n,s}\boldsymbol{R}_i
    =
    \braket{\, u^+\, u^-\, n\, |\, \boldsymbol{R}_i\, |\, u^+\, u^-\, n\, }
    =
    \braket{\, u^+\, u^-\, n\, |\, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, \boldsymbol{R}_i\, |\, \, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, u^+\, u^-\, n\, }
    =
    \boldsymbol{T}^{\dagger}\, \boldsymbol{R}_i\, \boldsymbol{T}

------------------------------------------------------------------------------------------------------------------
Inter-cell rotation matrix :math:`\boldsymbol{R}_m(\boldsymbol{q})\rightarrow\,^s\boldsymbol{R}_m(\boldsymbol{q})`
------------------------------------------------------------------------------------------------------------------

.. dropdown:: Reminder on the :math:`\,^n\boldsymbol{R}_m` matrix

  .. include:: repeated-formulas/spiral-rotation-matrix-uvn.inc

The inter-cell rotation :math:`\boldsymbol{R}_m` matrix elements in the spherical :math:`(\,n^+\,n^-\,n\,)`
basis are

.. math::
  ^{n,s}\boldsymbol{R}_m
  =
  \begin{pmatrix}
    e^{-i\boldsymbol{q} \cdot \boldsymbol{r_m}} & 0                  & 0 \\
    0                   & e^{i\boldsymbol{q} \cdot \boldsymbol{r_m}} & 0 \\
    0                   & 0                                          & 1 \\
  \end{pmatrix}

.. dropdown:: Details

  .. math::
    ^{n,s}\boldsymbol{R}_m
    =
    \braket{\, u^+\, u^-\, n\, |\, \boldsymbol{R}_m\, |\, u^+\, u^-\, n\, }
    =
    \braket{\, u^+\, u^-\, n\, |\, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, \boldsymbol{R}_m\, |\, \, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, u^+\, u^-\, n\, }
    =
    \boldsymbol{T}^{\dagger}\, \boldsymbol{R}_m\, \boldsymbol{T}

-----------------------------------------------------------------------------------------------------------
Exchange tensor :math:`\boldsymbol{J_{\boldsymbol{d}ij}}\,\rightarrow\,^s\boldsymbol{J_{\boldsymbol{d}ij}}`
-----------------------------------------------------------------------------------------------------------
The exchange matrix elements in the :math:`(\,n^+\,n^-\,n\,)` reference frame are


.. include:: repeated-formulas/exchange-matrix-decomposed-spherical.inc

.. dropdown:: Details

  .. math::
    \braket{\, u^+\, u^-\, n\, |\, J_{\boldsymbol{d}ij}\, |\, u^+\, u^-\, n\, }
    =&
    \braket{\, u^+\, u^-\, n\, |\, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, J_{\boldsymbol{d}ij}\, |\, u\, v \, n\, }
    \braket{\, u\, v\, n\, |\, u^+\, u^-\, n\, }
    =\\=&
    \braket{\, u\, v\, n\, |\, T^{\dagger}\,|\, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, J_{\boldsymbol{d}ij}\, |\, u\, v\, n\, }
    \braket{\, u\, v\, n\, |\, T\, |\, u\, v\, n\, }

  .. math::
    &\braket{\, u^+\, u^-\, n\, |\, J_{\boldsymbol{d}ij}\, |\, u^+\, u^-\, n\, }
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      J_{\boldsymbol{d}ij}^{uu} & J_{\boldsymbol{d}ij}^{uv} & J_{\boldsymbol{d}ij}^{un} \\
      J_{\boldsymbol{d}ij}^{vu} & J_{\boldsymbol{d}ij}^{vv} & J_{\boldsymbol{d}ij}^{vn} \\
      J_{\boldsymbol{d}ij}^{nu} & J_{\boldsymbol{d}ij}^{nv} & J_{\boldsymbol{d}ij}^{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      J_{\boldsymbol{d}ij}^{uu} - i J_{\boldsymbol{d}ij}^{vu} &
      J_{\boldsymbol{d}ij}^{uv} - i J_{\boldsymbol{d}ij}^{vv} &
      J_{\boldsymbol{d}ij}^{un} - i J_{\boldsymbol{d}ij}^{vn} \\
      J_{\boldsymbol{d}ij}^{uu} + i J_{\boldsymbol{d}ij}^{vu} &
      J_{\boldsymbol{d}ij}^{uv} + i J_{\boldsymbol{d}ij}^{vv} &
      J_{\boldsymbol{d}ij}^{un} + i J_{\boldsymbol{d}ij}^{vn} \\
      \sqrt{2}J_{\boldsymbol{d}ij}^{nu} &
      \sqrt{2}J_{\boldsymbol{d}ij}^{nv} &
      \sqrt{2}J_{\boldsymbol{d}ij}^{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      (J_{\boldsymbol{d}ij}^{uu} + J_{\boldsymbol{d}ij}^{vv}) + i(J_{\boldsymbol{d}ij}^{uv} - J_{\boldsymbol{d}ij}^{vu}) &
      (J_{\boldsymbol{d}ij}^{uu} - J_{\boldsymbol{d}ij}^{vv}) - i(J_{\boldsymbol{d}ij}^{uv} + J_{\boldsymbol{d}ij}^{vu}) &
      \sqrt{2}(J_{\boldsymbol{d}ij}^{un} - iJ_{\boldsymbol{d}ij}^{vn})             \\
      (J_{\boldsymbol{d}ij}^{uu} - J_{\boldsymbol{d}ij}^{vv}) + i(J_{\boldsymbol{d}ij}^{uv} + J_{\boldsymbol{d}ij}^{vu}) &
      (J_{\boldsymbol{d}ij}^{uu} + J_{\boldsymbol{d}ij}^{vv}) - i(J_{\boldsymbol{d}ij}^{uv} - J_{\boldsymbol{d}ij}^{vu}) &
      \sqrt{2}(J_{\boldsymbol{d}ij}^{un} + iJ_{\boldsymbol{d}ij}^{vn})             \\
      \sqrt{2}(J_{\boldsymbol{d}ij}^{nu} + iJ_{\boldsymbol{d}ij}^{nv})             &
      \sqrt{2}(J_{\boldsymbol{d}ij}^{nu} - iJ_{\boldsymbol{d}ij}^{nv})             &
      2J_{\boldsymbol{d}ij}^{nn}
    \end{pmatrix}

  Which gives:

  .. math::
    \braket{\, u^+\, u^-\, n\, |\, J_{\boldsymbol{d}ij}\, |\, u^+\, u^-\, n\, }
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      2J^I_{\boldsymbol{d}ij} + S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv} + 2iD_{\boldsymbol{d}ij}^n      &
      S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv} - 2iS_{\boldsymbol{d}ij}^{uv}                                 &
      \sqrt{2}(S_{\boldsymbol{d}ij}^{un} - iS_{\boldsymbol{d}ij}^{vn} - D_{\boldsymbol{d}ij}^v - iD_{\boldsymbol{d}ij}^u) \\
      S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv} + 2iS_{\boldsymbol{d}ij}^{uv}                                 &
      2J^I_{\boldsymbol{d}ij} + S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv} - 2iD_{\boldsymbol{d}ij}^n      &
      \sqrt{2}(S_{\boldsymbol{d}ij}^{un} + iS_{\boldsymbol{d}ij}^{vn} - D_{\boldsymbol{d}ij}^v + iD_{\boldsymbol{d}ij}^u) \\
      \sqrt{2}(S_{\boldsymbol{d}ij}^{un} + iS_{\boldsymbol{d}ij}^{vn} + D_{\boldsymbol{d}ij}^v - iD_{\boldsymbol{d}ij}^u) &
      \sqrt{2}(S_{\boldsymbol{d}ij}^{un} - iS_{\boldsymbol{d}ij}^{vn} + D_{\boldsymbol{d}ij}^v + iD_{\boldsymbol{d}ij}^u) &
      2J^I_{\boldsymbol{d}ij} + 2S_{\boldsymbol{d}ij}^{nn}
    \end{pmatrix}

Let us note a few symmetries of the exchange matrix in a spherical reference frame:

.. include:: repeated-formulas/exchange-matrix-symmetries-spherical.inc

.. dropdown:: Alternative way to write the matrix

  If we define:

  .. math::
    \begin{matrix}
        D^{\pm}_{\boldsymbol{d}ij}
        =
        \dfrac{D_{\boldsymbol{d}ij}^v \pm iD_{\boldsymbol{d}ij}^u}{\sqrt{2}};
      &
        S^{\pm}_{\boldsymbol{d}ij}
        =
        \dfrac{S_{\boldsymbol{d}ij}^{un} \pm iS_{\boldsymbol{d}ij}^{vn}}{\sqrt{2}}
      \\
    \end{matrix}

  Then we can write the exchange matrix in the spherical reference frame as:

  .. math::
    \begin{pmatrix}
      J_{\boldsymbol{d}ij}^I + \dfrac{S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv}}{2} + iD_{\boldsymbol{d}ij}^n &
      \dfrac{S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv}}{2} - iS_{\boldsymbol{d}ij}^{uv}        &
      S_{\boldsymbol{d}ij}^- - D_{\boldsymbol{d}ij}^+                                   \\
      \dfrac{S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv}}{2} + iS_{\boldsymbol{d}ij}^{uv}        &
      J_{\boldsymbol{d}ij}^I + \dfrac{S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv}}{2} - iD_{\boldsymbol{d}ij}^n &
      S_{\boldsymbol{d}ij}^+ - D_{\boldsymbol{d}ij}^-                                   \\
      S_{\boldsymbol{d}ij}^+ + D_{\boldsymbol{d}ij}^-                                   &
      S_{\boldsymbol{d}ij}^- + D_{\boldsymbol{d}ij}^+                                   &
      J_{\boldsymbol{d}ij}^I + S_{\boldsymbol{d}ij}^{nn}                            \\
    \end{pmatrix}

.. _user-guide_methods_spherical-rf_change_magnetic-field:

------------------------------------------------------------------
Magnetic field :math:`\,^s\boldsymbol{h}\rightarrow\boldsymbol{h}`
------------------------------------------------------------------
The magnetic field vector :math:`\boldsymbol{h}` can be written
in the global spherical basis :math:`(\,n^+\,n^-\,n\,)` as

.. math::
  ^{n,s}\boldsymbol{h}=\braket{\,n^+\,n^-\,n\,|\,h\,}
  =
  \begin{pmatrix}
     h^{-} \\
     h^{+} \\
     h^n
  \end{pmatrix}

.. dropdown:: Details

  The magnetic field vector in the :math:`(u\, v\, n)` reference frame is written as

  .. math::
    ^n\boldsymbol{h_{mi}}
    =
    \begin{pmatrix}
      h^u \\
      h^v \\
      h^n \\
    \end{pmatrix}

============================================
Hamiltonian in the spherical reference frame
============================================
The Heisenberg Hamiltonian can be written now in the global spherical basis :math:`(\,n^+\,n^-\,n\,)`
as follows

.. include:: repeated-formulas/hamiltonian-main-spherical.inc
