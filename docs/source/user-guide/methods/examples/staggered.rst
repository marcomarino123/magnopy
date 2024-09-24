.. _user-guide_methods_examples_staggered:

*********
Staggered
*********

This section discusses the Spin Wave Theory of a square/cubic lattice
of lattice constant :math:`a`, displaying a staggered solution
:math:`\boldsymbol{q}\,a=(\pi,\,\pi)\,\mathrm{or}\,(\pi,\,\pi,\,\pi)`.
All :math:`I` atoms inside each unit cell are assumed to point likewise and
along the :math:`z`-axis. We take reciprocal lattice units of
:math:`2\,\pi\,/\,a` in the remainder of this example.

=========
Rotations
=========

The cone axis vector :math:`\boldsymbol{n}` is chosen to lie along the
positive :math:`x`-axis as indicated in the figure below. This is
achieved by choosing :math:`\beta=0` and :math:`\alpha=\pi/2`. Then
:math:`\boldsymbol{\hat{r}}=\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}=\boldsymbol{\hat{y}}`,
and

.. math::
  ^z\boldsymbol{R}=e^{-i\,\frac{\pi}{2}\,\boldsymbol{\hat{r}}\times}=
          \begin{pmatrix}0&0&1\\0&1&0\\-1&0&0\end{pmatrix}

.. image::
  ../../../../images/staggered.jpg

We choose a cell rotation vector :math:`\boldsymbol{\hat{r}_i}`
pointing along the negative
:math:`\boldsymbol{\hat{v}}=\boldsymbol{\hat{y}}`-axis. This
is accomplished by choosing intra-cell rotation azimut
angle :math:`\phi_i=\pi`, and then the intra-cell polar angle is
:math:`\theta_i=\pi`. The rotation matrix is

.. math::
  ^n\boldsymbol{R}_i\,=\,e^{-i\,\pi\,\boldsymbol{\hat{r}_i}\,\times}=
  \begin{pmatrix}0&0&-1\\0&1&0\\1&0&0\end{pmatrix}\\
  ^{sn}\boldsymbol{R}_i\,=\,\frac{1}{2}\,
  \begin{pmatrix}1&-1&-\sqrt{2}\\-1&1&-\sqrt{2}\\\sqrt{2}&\sqrt{2}&0\end{pmatrix}

The intercell rotation is governed by the azimut angle
:math:`\phi_m=\boldsymbol{q}\cdot\boldsymbol{r}_m=n_m\,\pi`. Then

.. math::
  ^\boldsymbol{n}\boldsymbol{R}_m\,=e^{-i\,\pi\,n_m\,\boldsymbol{\hat{n}}\,\times}=
  \begin{pmatrix}s_m&0&0\\0&s_m&0\\0&0&1\end{pmatrix}

where :math:`s_\boldsymbol{m}=(-1)^{\mathrm{mod}(n_m,2)}`.

The magnetization is

.. math::
  \boldsymbol{S}_{mi}=^z\boldsymbol{R}\,^n\boldsymbol{R}_m\,\boldsymbol{R}_i\,
  \begin{pmatrix}0\\0\\S_i\end{pmatrix}=\begin{pmatrix}0\\0\\s_m\,S_i\end{pmatrix}

The exchange tensor is

.. math::
  ^{sn}\boldsymbol{J}_{\boldsymbol{d}ij}=
  \begin{pmatrix}
  J^{zy,+}_{\boldsymbol{d}ij}+i\,D^x_{\boldsymbol{d}ij}&
  J^{zy,-}_{\boldsymbol{d}ij}+i\,S^x_{\boldsymbol{d}ij}&
  \frac{1}{\sqrt{2}}(-J^{zx}_{\boldsymbol{d}ij}-i\,J^{yx}_{\boldsymbol{d}ij})\\
  J^{zy,-}_{\boldsymbol{d}ij}-i\,S^x_{\boldsymbol{d}ij}&
  J^{zy,+}_{\boldsymbol{d}ij}-i\,D^x_{\boldsymbol{d}ij}&
  \frac{1}{\sqrt{2}}(-J^{zx}_{\boldsymbol{d}ij}+i\,J^{yx}_{\boldsymbol{d}ij})\\
  \frac{1}{\sqrt{2}}(-J^{xz}_{\boldsymbol{d}ij}+i\,J^{xy}_{\boldsymbol{d}ij})&
  \frac{1}{\sqrt{2}}(-J^{xz}_{\boldsymbol{d}ij}-i\,J^{xy}_{\boldsymbol{d}ij})
  &J^{xx}_{\boldsymbol{d}ij}\\
  \end{pmatrix}+2\,\delta_{i,j}\,\delta_{\boldsymbol{d}_{ij},0}\,
  \begin{pmatrix}
  A^{zy,+}_i&A^{zy,-}_i+i\,A^{yz}_i&\frac{1}{\sqrt{2}}\,(-A_i^{xz}-i\,A_i^{xy})\\
  A^{zy,-}_i-i\,A^{yz}_i&A^{zy,+}_i&\frac{1}{\sqrt{2}}\,(-A_i^{xz}+i\,A_i^{xy})\\
  \frac{1}{\sqrt{2}}\,(-A_i^{xz}+i\,A_i^{xy})&\frac{1}{\sqrt{2}}\,(-A_i^{xz}-i\,A_i^{xy})&0
  \end{pmatrix}

with

.. math::
  J^{zy,\pm}_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{zz}_{\boldsymbol{d}ij}\pm J^{yy}_{\boldsymbol{d}ij}\right)\\
  S^x_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{yz}_{\boldsymbol{d}ij}+ J^{zy}_{\boldsymbol{d}ij}\right)\\
  D^x_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{yz}_{\boldsymbol{d}ij}- J^{zy}_{\boldsymbol{d}ij}\right)\\
  A^{zy,\pm}_i&=\frac{1}{2}\,\left(A^{zz}_i\pm A^{yy}_i\right)

================
Classical energy
================

The expression for the classical energy is

.. math::
  E^{0,cl}=\frac{1}{2}\,\sum_{\boldsymbol{d}_{ij},i,j}\,S_i\,S_j\,s_d\,J^{zz}_{\boldsymbol{d}ij}

=======================
Magnetic Brillouin Zone
=======================
We have that :math:`M_q=2`, so that :math:`M_q\,\boldsymbol{q}=(1,\,1)=\boldsymbol{G}`.
We take new primitive unit vectors :math:`\boldsymbol{g}_\parallel=\frac{1}{2}(1,\,1)` and
:math:`\boldsymbol{g}_\perp=\frac{1}{2}(-1,\,1)`, and reshape the Brillouin Zone as shown in the
left panel of the figure below, so that
:math:`\boldsymbol{k}=k_\parallel\, \boldsymbol{g}_\parallel+k_\perp\, \boldsymbol{g}_\perp` with
:math:`k_{\parallel\,/\perp}\,\in\,[-1/2,\,1/2)`. The Magnetic Brillouin Zone includes all points
:math:`\boldsymbol{k}=\boldsymbol{k}_1` and :math:`\boldsymbol{k}_2=\boldsymbol{k}_1+\boldsymbol{q}`,
as illustrated in the right panel of the figure below.

.. image::
  ../../../../images/MBZ.jpg

================
LSWT Hamiltonian
================
The :math:`I` unit-cell boson fields are arranged as the bosonic vector field
:math:`\tilde{B}_n(\boldsymbol{k})=(a_{n,1}(\boldsymbol{k}),\,\dots,\,a_{n,I}(\boldsymbol{k}))`,
where the tilde indicates that the vector is transposed, and then the bosonic vector fields are
also arranged as

.. math::
  \cal{\boldsymbol{B}}(\boldsymbol{k})=
  \begin{pmatrix}
    B_{-1/2}(\boldsymbol{k})\\\tilde{B}_{1/2}^\dagger(-\boldsymbol{k})\\
    B_{1/2}(\boldsymbol{k})\\\tilde{B}_{-1/2}^\dagger(-\boldsymbol{k})
  \end{pmatrix}

The LSWT Hamiltonian is then

.. math::
  H^{LSWT}&\,=\,-\frac{1}{2}\,\sum_{k}\,(T^0(\boldsymbol{k}))^\dagger+
  \frac{1}{4}\,\sum_{k}\,\cal{\boldsymbol{B}}^\dagger(\boldsymbol{k})\,
  \cal{\boldsymbol{H}}(\boldsymbol{k})\,\cal{\boldsymbol{B}}(\boldsymbol{k})\\
  \cal{\boldsymbol{H}}(\boldsymbol{k})&\,=\,
  \begin{pmatrix}
  T_{-1/2}^0(\boldsymbol{k})+T_{-1/2}^{-2}(\boldsymbol{k})+T_{-1/2}^2(\boldsymbol{k})&
  T_{1/2}^{-1}(\boldsymbol{k})+T_{1/2}^1(\boldsymbol{k})&
  \left(\Delta_{-1/2}^0(\boldsymbol{k})+\Delta_{-1/2}^{-2}(\boldsymbol{k})+\Delta_{-1/2}^2(\boldsymbol{k})\right)^\dagger&
  \left(\Delta_{-1/2}^{-1}(\boldsymbol{k})+\Delta_{-1/2}^1(\boldsymbol{k})\right)^\dagger\\
  T_{-1/2}^{-1}(\boldsymbol{k})+T_{-1/2}^{1}(\boldsymbol{k})&
  T_{1/2}^{0}(\boldsymbol{k})+T_{1/2}^{-2}(\boldsymbol{k})+T_{1/2}^2(\boldsymbol{k})&
  \left(\Delta_{1/2}^{-1}(\boldsymbol{k})+\Delta_{1/2}^1(\boldsymbol{k})\right)^\dagger&
  \left(\Delta_{1/2}^0(\boldsymbol{k})+\Delta_{1/2}^{-2}(\boldsymbol{k})+\Delta_{1/2}^2(\boldsymbol{k})\right)^\dagger\\
  \Delta_{-1/2}^0(\boldsymbol{k})+\Delta_{-1/2}^{-2}(\boldsymbol{k})+\Delta_{-1/2}^2(\boldsymbol{k})&
  \Delta_{1/2}^{-1}(\boldsymbol{k})+\Delta_{1/2}^1(\boldsymbol{k})&
  \left(T_{1/2}^{0}(-\boldsymbol{k})+T_{1/2}^{-2}(-\boldsymbol{k})+T_{1/2}^2(-\boldsymbol{k})\right)^*&
   \left(T_{-1/2}^{-1}(-\boldsymbol{k})+T_{-1/2}^{1}(-\boldsymbol{k})\right)^*\\
  \Delta_{-1/2}^{-1}(\boldsymbol{k})+\Delta_{-1/2}^1(\boldsymbol{k})&
  \Delta_{1/2}^0(\boldsymbol{k})+\Delta_{1/2}^{-2}(\boldsymbol{k})+\Delta_{1/2}^2(\boldsymbol{k})&
   \left(T_{1/2}^{-1}(-\boldsymbol{k})+T_{1/2}^{1}(-\boldsymbol{k})\right)^*&
   \left(T_{-1/2}^{0}(-\boldsymbol{k})+T_{-1/2}^{-2}(-\boldsymbol{k})+T_{-1/2}^2(-\boldsymbol{k})\right)^*
  \end{pmatrix}

The above expression is too complex, so we perform several simplifications. First, we assume a
single atom per unit cell. Second, we assume that interactions run only to first neighbors that
are labelled by :math:`\boldsymbol{d}`, and that they are isotropic in space, so that the
:math:`\boldsymbol{d}`-subindex can be dropped. Third, we suppose that :math:`J^{xx}=J^{yy}`,
:math:`A^{xx}=A^{yy}` and that :math:`S^{x}=0`. Then

.. math::
  T_{\pm 1/2}^0(\boldsymbol{k})+T_{\pm 1/2}^{-2}(\boldsymbol{k})+T_{\pm 1/2}^2(\boldsymbol{k}&\,=\,
  S\,\sum_\boldsymbol{d}\,
  \left(\mp\frac{J^{xx}-J^{yy}}{2}\,e^{i\,\boldsymbol{k}\cdot\boldsymbol{d}}-s_d\,J^{zz}\right)\\
  T_{\pm 1/2}^{-1}(\boldsymbol{k})+T_{\pm 1/2}^1(\boldsymbol{k}&\,=\,
  \mp\,i\,S\,\sum_\boldsymbol{d}\,D^z\,e^{i\,\boldsymbol{k}\cdot\boldsymbol{d}}\\
  \Delta_{\mp 1/2}^0(\boldsymbol{k})+\Delta_{\mp 1/2}^{-2}(\boldsymbol{k})
  +\Delta_{\mp 1/2}^2(\boldsymbol{k})&\,=\,\\
  \Delta_{\mp 1/2}^{-1}(\boldsymbol{k})+\Delta_{\mp 1/2}^1(\boldsymbol{k})&\,=\
