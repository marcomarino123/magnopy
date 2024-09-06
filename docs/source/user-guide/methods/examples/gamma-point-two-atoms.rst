.. _user-guide_methods_examples_gamma-point-two-atoms:

*************************************************************
Gamma-point solution Z-axis solution, two atoms per unit cell
*************************************************************

This section discusses the Spin Wave Theory of two magnetic atoms A and B
in the unit cell whose spins are oriented along the Z-axis in either
a parallel (ferromagnetic, FM) or anti-parallel (antiferromagnetic, AFM)
fashion. These two configurations can be described by choosing
:math:`  b \boldsymbol{q}=0`, and performing a rotation of :math:`\pm \pi` degrees
of the z-axis about a unit vector :math:`\boldsymbol{\hat{r}}` lying in the XY-plane.

===================================
:math:`(u\, v\, n)` reference frame
===================================

We choose here :math:`\boldsymbol{\hat{r}}` to be oriented along the positive
y-axis as is illustrated in the left panel of the figure shown below.

.. raw:: html
  :file: ../../../images/two-atoms.jpg

.. rst-class:: plotly-figure-caption

  **Figure 1** : Left, generation of the :math:`(u\, v\, n)` reference frame. Right, generation of the :math:`(p\, t\, f)` reference frame.

This is accomplished mathematically by selecting :math:`\beta=0`, and :math:`\alpha=\pi/2`
so that :math:`\boldsymbol{\hat{r}}=\boldsymbol{\hat{z}}\times \boldsymbol{\hat{n}}`.
The rotation matrix is then

.. math::
  ^z\boldsymbol{R_r}(\pi/2,0)=e^{-i\,\pi/2\,\boldsymbol{\hat{r}}\,\times}=
  \begin{pmatrix}0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{pmatrix}

Accordingly, the rotated exchange tensor becomes in the cartesian and the spherical bases

.. math::
  ^n\boldsymbol{J}_{\boldsymbol{d}_{ij}}&\,=\,
  \begin{pmatrix}
  J^{zz} & - J^{zy} & - J^{zx} \\ - J^{yz} & J^{yy} & J^{yx} \\ -J^{xz} & J^{xy} & J^{xx}
  \end{pmatrix}
  \\\\
  ^{sn}\boldsymbol{J}_{\boldsymbol{d}ij}&\,=\,
    \begin{pmatrix}
    J^{n,++}_{\boldsymbol{d}ij} & J^{n,+-}_{\boldsymbol{d}ij} & J^{n,+0}_{\boldsymbol{d}ij} \\
    J^{n,-+}_{\boldsymbol{d}ij} & J^{n,--}_{\boldsymbol{d}ij} & J^{n,-0}_{\boldsymbol{d}ij} \\
    J^{n,0+}_{\boldsymbol{d}ij} & J^{n,0-}_{\boldsymbol{d}ij} & J^{n,00}_{\boldsymbol{d}ij} \\
    \end{pmatrix}\\
    &\,=\,
    \begin{pmatrix}
      J^{zy,+}_{\boldsymbol{d}ij} + i D^x_{\boldsymbol{d}ij} &
      J^{zy,-}_{\boldsymbol{d}ij} + i S^x_{\boldsymbol{d}ij} &
      \frac{1}{\sqrt{2}}\,\left(-J^{zx}_{\boldsymbol{d}ij} - i J^{yx}_{\boldsymbol{d}ij}\right)
      \\
      J^{zy,-}_{\boldsymbol{d}ij} - i S^x_{\boldsymbol{d}ij} &
      J^{zy,+}_{\boldsymbol{d}ij} - i D^x_{\boldsymbol{d}ij} &
      \frac{1}{\sqrt{2}}\,\left(-J^{zx}_{\boldsymbol{d}ij} + i J^{yx}_{\boldsymbol{d}ij}\right)
      \\
      \frac{1}{\sqrt{2}}\,\left(-J^{xz}_{\boldsymbol{d}ij} + i J^{xy}_{\boldsymbol{d}ij}\right) &
      \frac{1}{\sqrt{2}}\,\left(-J^{xz}_{\boldsymbol{d}ij} - i J^{xy}_{\boldsymbol{d}ij}\right) &
      J^{xx}_{\boldsymbol{d}ij}
    \end{pmatrix}
  \,+\,2\,\delta_{i,j}\,\delta_{\boldsymbol{d}_{ij},0}\,
    \begin{pmatrix}
      A^{zy,+}_i & A^{zy,-}_i + i A^{yz}_i & -\frac{1}{\sqrt{2}}\,\left(A^{zx}_i + i A^{yx}_i\right)
      \\
      A^{zy,-}_i - i A^{yz}_i & A^{yz,+}_i - i A^{yz}_i &
      \frac{1}{\sqrt{2}}\,\left(-A^{zx}_i - i A^{yx}_i\right)
      \\
      \frac{1}{\sqrt{2}}\,\left(-A^{xz}_i + i A^{xy}_i\right) &
      \frac{1}{\sqrt{2}}\,\left(-A^{xz}_i + i A^{xy}_i\right) &
      A^{xx}_i
    \end{pmatrix}

with

.. math::
  J^{zy,\pm}_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{zz}_{\boldsymbol{d}ij}\pm J^{yy}_{\boldsymbol{d}ij}\right)\\
  S^z_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{xy}_{\boldsymbol{d}ij}+ J^{yx}_{\boldsymbol{d}ij}\right)\\
  D^z_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{xy}_{\boldsymbol{d}ij}- J^{yx}_{\boldsymbol{d}ij}\right)\\
  A^{xy,\pm}_i&=\frac{1}{2}\,\left(A^{xx}_i\pm A^{yy}_i\right)

==============================================================
Exchange tensor :math:`^{sn}\boldsymbol{J}_{\boldsymbol{d}ij}`
==============================================================
This kind of solutions narrow the parameter space, since the cone angles
:math:`\alpha=\beta=0` so that the bases :math:`(\,u\,v\,n\,)\,=\,(\,x\,y\,z\,=`).
Furthermore, the spiral vector :math:`\boldsymbol{q}=0` and the intracell
angles are all set to zero also, :math:`\theta_i=\phi_i=0`.
Therefore that exchange tensor simplifies to

.. math::
  ^{sz}\boldsymbol{J}_{\boldsymbol{d}ij}\,=\,^{sn}\boldsymbol{J}_{\boldsymbol{d}ij}=
  	\begin{pmatrix}
  		J^{xy,+}_{\boldsymbol{d}ij} + i D^z_{\boldsymbol{d}ij} &
  		J^{xy,-}_{\boldsymbol{d}ij} - i S^z_{\boldsymbol{d}ij} &
  		\frac{1}{\sqrt{2}}\,\left(J^{xz}_{\boldsymbol{d}ij} - i J^{yz}_{\boldsymbol{d}ij}\right)
  		\\
  		J^{xy,-}_{\boldsymbol{d}ij} + i S^z_{\boldsymbol{d}ij} &
  		J^{xy,+}_{\boldsymbol{d}ij} - i D^z_{\boldsymbol{d}ij} &
  		\frac{1}{\sqrt{2}}\,\left(J^{xz}_{\boldsymbol{d}ij} + i J^{yz}_{\boldsymbol{d}ij}\right)
  		\\
  		\frac{1}{\sqrt{2}}\,\left(J^{zx}_{\boldsymbol{d}ij} + i J^{zy}_{\boldsymbol{d}ij}\right) &
  		\frac{1}{\sqrt{2}}\,\left(J^{zx}_{\boldsymbol{d}ij} - i J^{zy}_{\boldsymbol{d}ij}\right) &
  		J^{zz}_{\boldsymbol{d}ij}
  	\end{pmatrix}
  \,+\,2\,\delta_{i,j}\,\delta_{\boldsymbol{d}_{ij},0}\,
  	\begin{pmatrix}
  		A^{xy,+}_i & A^{xy,-}_i - i A^{xy}_i & \frac{1}{\sqrt{2}}\,\left(A^{xz}_i - i A^{yz}_i\right)
  		\\
  		A^{xy,-}_i - i A^{xy}_i & A^{xy,+}_i &
  		\frac{1}{\sqrt{2}}\,\left(A^{xz}_i + i A^{yz}_i\right)
  		\\
  		\frac{1}{\sqrt{2}}\,\left(A^{xz}_i + i A^{yz}_i\right) &
  		\frac{1}{\sqrt{2}}\,\left(A^{xz}_i - i A^{yz}_i\right) &
  		0
  	\end{pmatrix}

with

.. math::
  J^{xy,\pm}_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{xx}_{\boldsymbol{d}ij}\pm J^{yy}_{\boldsymbol{d}ij}\right)\\
  S^z_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{xy}_{\boldsymbol{d}ij}+ J^{yx}_{\boldsymbol{d}ij}\right)\\
  D^z_{\boldsymbol{d}ij}&=\frac{1}{2}\,\left(J^{xy}_{\boldsymbol{d}ij}- J^{yx}_{\boldsymbol{d}ij}\right)\\
  A^{xy,\pm}_i&=\frac{1}{2}\,\left(A^{xx}_i\pm A^{yy}_i\right)

================
Classical energy
================
The classical energy is in this case

.. math::
  E^{0,cl} = \frac{1}{2}\,\sum_{\boldsymbol{d}_{ij}, i, j} S_i\,S_j\,J_{\boldsymbol{d}ij}^{zz} + \sum_i\,A_i^{zz}\,S_i^2

==========
LSW theory
==========
The LSWT Hamiltonian is

.. math::
  \boldsymbol{H}^{LSWT}&\,=\,
  E^{LSWT,1}\,+\,\frac{1}{2}\,\sum_\boldsymbol{k}\,\begin{pmatrix}\boldsymbol{B}_\boldsymbol{k}^\dagger&
  \boldsymbol{\tilde{B}}_{-\boldsymbol{k}}\end{pmatrix}\,
  \begin{pmatrix}\boldsymbol{T}(\boldsymbol{k})&\boldsymbol{\Delta}(\boldsymbol{k})\\
                  \boldsymbol{\Delta}^\dagger(\boldsymbol{k})&\boldsymbol{T}^*(\boldsymbol{k})
  \end{pmatrix}
  \begin{pmatrix}\boldsymbol{B}_\boldsymbol{k}\\
  \boldsymbol{\tilde{B}}_{-\boldsymbol{k}}^\dagger\end{pmatrix}

where the super-vectors :math:`\boldsymbol{B}_\boldsymbol{k}` and :math:`\boldsymbol{\tilde{B}}_{-\boldsymbol{k}}`
collect all the bosonic spin-wave fields :math:`a_{\boldsymbol{k},i}`.
The different pieces of the Hamiltonian are

.. math::
  E^{LSWT,1} &\,=
            M\,\left(\frac{1}{2}\,\sum_{\boldsymbol{d}_{ij},i, j} S_{j}\,J_{\boldsymbol{d}ij}^{zz}+
            \,\sum_i\,S_i\,A_i^{zz}\right)
           \\\\
  T_{ij}(\boldsymbol{k})&\,=\,\delta_{ij}\,\left(\left(A_i^{xx}+A_i^{yy}-2\,A_i^{zz}\right)\,S_i-
  				 \sum_{\boldsymbol{d}_{ij'}, j'} S_{j'}\,J_{\boldsymbol{d}ij'}^{zz}\right)+
  				 \left(S_i\,S_j\right)^{1/2}\,
  				 \left(\frac{J^{xx}_{\boldsymbol{d}ij}(\boldsymbol{k})+
  				 J^{yy}_{\boldsymbol{d}ij}(\boldsymbol{k})}{2}
  				 -i D^z_{\boldsymbol{d}ij}(\boldsymbol{k})\right)
  				 \\\\
  \Delta_{ij}(\boldsymbol{k})&\,=\,\delta_{ij}\,\left(A_i^{xx}-A_i^{yy}-2 i A_i^{xy}\right)\,S_i+
  \left(S_i\,S_j\right)^{1/2}\,\sum_{\boldsymbol{d}_{ij}}\,
  				 \left(\frac{J^{xx}_{\boldsymbol{d}ij}(\boldsymbol{k})- J^{yy}_{\boldsymbol{d}ij}(\boldsymbol{k})}{2}
					-i J^{xy}_{\boldsymbol{d}ij}(\boldsymbol{k})\right)

Here, we have introduced the notation

.. math::
  J_{ij}^{\alpha\beta}(\boldsymbol{k})= \sum_{\boldsymbol{d}_{ij}}\,
      J^{\alpha\beta}_{\boldsymbol{d}ij}\, e^{i\,\boldsymbol{k}\cdot\boldsymbol{d}_{ij}}


=============================================================
Simplification: single atom per unit cell with spin :math:`S`
=============================================================
A notable simplification happens here because the :math:`i` and :math:`j` sub-indices dissapear.
Furhtermore, there is a single bosonic field per unit cell, so that
:math:`\boldsymbol{B}_\boldsymbol{k}=a_\boldsymbol{k}`
The classical energy is

.. math::
   E^{0,cl} = M\,S^2\,\left(\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)+A^{zz} \right)

The LSWT first correction, kinetic and pairing terms simplify to

.. math::
  \frac{E^{LSWT,1}}{S}&\,=\,M\,\left(\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)+A^{zz}\right)\\
  \frac{T(\boldsymbol{k})}{S}&\,=\,A^{xx}+A^{yy}-2\,A^{zz}+
  \frac{J^{xx}(\boldsymbol{k})+J^{yy}(\boldsymbol{k})}{2}-J^{zz}(\boldsymbol{k=0})-i D^z(\boldsymbol{k})\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=\,A^{xx}-A^{yy}-2 i A^{xy}+
  \frac{J^{xx}(\boldsymbol{k})-J^{yy}(\boldsymbol{k})}{2}-i J^{xy}(\boldsymbol{k})

A last simpification comes about if :math:`J^{xx}=J^{yy}`, :math:`A^{xx}=A^{yy}`, and
:math:`J^{xy}=D^z=A^{xy}=0`. Then

.. math::
  \frac{E^{LSWT,1}}{S}&\,=\,M\,\left(\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)+A^{zz}\right)\\
  \frac{T(\boldsymbol{k})}{S}&\,=\,2\,(A^{xx}-A^{zz})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=0

Then the LSWT Hamiltonian becomes

.. math::
  \boldsymbol{H}_\boldsymbol{k}^{LSWT}&\,=\,
  E^{LSWT,1}\,+\,\frac{1}{2}\,\sum_\boldsymbol{k}\,
  \begin{pmatrix}a_\boldsymbol{k}^\dagger&a_{-\boldsymbol{k}}\end{pmatrix}\,
  \begin{pmatrix}T(\boldsymbol{k})&0\\&T(\boldsymbol{-k})
  \end{pmatrix}
  \begin{pmatrix}a_\boldsymbol{k}\\a_{-\boldsymbol{k}}^\dagger\end{pmatrix}\\\\
  &\,=\,E^{LSWT,1}\,+\,\sum_\boldsymbol{k}\,\omega^{LSWT}(-\boldsymbol{k}) +
 \sum_\boldsymbol{k}  \omega^{LSWT}(\boldsymbol{k}) \, a_\boldsymbol{k}^\dagger\,a_\boldsymbol{k}

with

.. math::
  \omega^{LSWT}(\boldsymbol{k})\,=\,T(\boldsymbol{k})\,=
  \,S\,\left(\,2\,(A^{xx}-A^{zz})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\,\right)

The full Hamiltonian to LSWT order is

.. math::
  H \,&=\, E^0+
   \sum_{\boldsymbol{k}}\,\omega^{LSWT}(\boldsymbol{k})\,a_\boldsymbol{k}^\dagger\,a(\boldsymbol{k})\\\\
   E^0\,&=E^{0,cl}+E^{LSWT,1}+\sum_\boldsymbol{k}\,\omega^{LSWT}(-\boldsymbol{k})\,=
   \,M\,S^2\,\left(\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)+A^{zz}\right)+M\,S\,A^{xx}

===============================================================
Higher-order pieces of the Hamiltonian for the single-atom case
===============================================================

The bosonic cubic term in the SWT Hamiltonian has been written explicitly :ref:`here <user-guide_methods_hp-higher>`,
where the coupling constants for the single-atom case are

.. math::
  C^{1,\nu}(\boldsymbol{q})&=J_{\boldsymbol{d}_{ij}}^{f\nu,+0}(\boldsymbol{q=0})
            =\sqrt{2}\,(A^{xz} - i\, A^{yz})+\frac{1}{\sqrt{2}}\,\left(J^{xz}(\boldsymbol{q}=0)-i \,J^{yz}(\boldsymbol{q}=0)\right) \\
  C^{2,\nu}(\boldsymbol{q})&= J_{\boldsymbol{d}_{ij}}^{f\nu,+0}(\boldsymbol{q})=
            \sqrt{2}\,(A^{xz}+i\, A^{yz})+\frac{1}{\sqrt{2}}\,\left(J^{xz}(\boldsymbol{q})-i \,J^{yz}(\boldsymbol{q})\right)

These two coupling constants are zero if there exists a single atom per unit cell, and
:math:`J^{xz}=J^{yz}=A^{xz}=A^{yz}=0`, so that :math:`H^{Cubic}=0`.

The bosonic biquadratic has also been written :ref:`here <user-guide_methods_hp-higher>`, where the
three coupling constants and on-site exchange tensors for a single atom per unit cell are

.. math::
  D^{1,\nu}(\boldsymbol{q})&= J^{f\nu,00}(\boldsymbol{q})=J^{zz}(\boldsymbol{q})\\
  D^{2,\nu}(\boldsymbol{q})&= J^{f\nu,++}(\boldsymbol{q})=A^{xx}+A^{yy}+
                                    \frac{J^{xx}(\boldsymbol{q})+J^{yy}(\boldsymbol{q})}{2}+i\,D^z(\boldsymbol{q})\\
  D^{3,\nu}(\boldsymbol{q})&= J^{f\nu,+-}(\boldsymbol{q})=A^{xx}-A^{yy}-2\,i\,A^{xy}+
                                    \frac{J^{xx}(\boldsymbol{q})-J^{yy}(\boldsymbol{q})-
                                    i\,\left(J^{xy}(\boldsymbol{q})+J^{yx}(\boldsymbol{q})\right)}{2}\\
  J^{f\nu,00}_{\boldsymbol{d}_{ii}=0}&=2 \,A^{zz}\\
  J^{f\nu,++}_{\boldsymbol{d}_{ii}=0}&=A^{xx}+A^{yy}\\
  J^{f\nu,+-}_{\boldsymbol{d}_{ii}=0}&=A^{xx}-A^{yy}-2\,i\,A^{xy}

We assume now that :math:`J^{xx}=J^{yy}` and :math:`J^{xy}=A^{xy}=D^z=0`. Then

.. math::
  D^{1,\nu}(\boldsymbol{q})&=J^{zz}(\boldsymbol{q})\\
  D^{2,\nu}(\boldsymbol{q})&=2\,A^{xx}+J^{xx}(\boldsymbol{q})\\
  D^{3,\nu}(\boldsymbol{q})&=0\\
  J^{f\nu,00}_{\boldsymbol{d}_{ii}=0}&=2 \,A^{zz}\\
  J^{f\nu,++}_{\boldsymbol{d}_{ii}=0}&=2 \,A^{xx}\\
  J^{f\nu,+-}_{\boldsymbol{d}_{ii}=0}&=0

As a consequence, the interacting biquadratic Hamiltonian becomes

.. math::
  H^{Biquadratic}=
       & -(A^{xx}-A^{zz})\,\sum_{\boldsymbol{k}}\,a_{\boldsymbol{k}}^\dagger\,a_{\boldsymbol{k}}\\
       &+ \frac{1}{2\,M}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2},\boldsymbol{p}}\,\left(J^{zz}(\boldsymbol{p})-2\,A^{xx}-
                      \frac{J^{xx}(\boldsymbol{k_1})+J^{xx}(\boldsymbol{k_1+p})}{2}\right)\,
                      a_{\boldsymbol{k_1+p}}^\dagger\,a_{\boldsymbol{k_2-p}}^\dagger\,a_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}

And the full interacting Hamiltonian is

.. math::
  H\,=\,\,E^0+
  \sum_{\boldsymbol{k}}\,\omega(\boldsymbol{k})\,a_{\boldsymbol{k}}^\dagger\,a_{\boldsymbol{k}}
          +\frac{1}{2\,M}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2},\boldsymbol{p}}\,
          \,\lambda(\boldsymbol{k_1},\boldsymbol{p})\,
          a_{\boldsymbol{k_1+p}}^\dagger\,a_{\boldsymbol{k_2-p}}^\dagger\,a_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}

with the following shifted spin-wave frequency and coupling contant

.. math::
  \omega(\boldsymbol{k})&\,=\,\omega^{LSWT}(\boldsymbol{k})-(A^{xx}-A^{zz})=
  S\,\left(\,2\,(A^{xx}-A^{zz})\,(1-\frac{1}{2\,S})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\,\right)\\\\
  \lambda(\boldsymbol{k_1},\boldsymbol{p})&\,=\,
          J^{zz}(\boldsymbol{p})-2\,A^{xx}-\frac{J^{xx}(\boldsymbol{k_1})+J^{xx}(\boldsymbol{k_1+p})}{2}

=============================
Renormalized Spin Wave Theory
=============================

The four-boson interaction is decoupled in the Mean-Field approximation as follows

.. math::
  a_{\boldsymbol{k_1+p}}^\dagger\,a_{\boldsymbol{k_2-p}}^\dagger\,a_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}=
  \delta_{\boldsymbol{p},0}\,(n_{\boldsymbol{k_1}}\,a_{\boldsymbol{k_2}}^\dagger\,a_{\boldsymbol{k_2}}+
  n_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}^\dagger\,a_{\boldsymbol{k_1}})+
  \delta_{\boldsymbol{p},\boldsymbol{k_2-k_1}}\,(n_{\boldsymbol{k_1}}\,a_{\boldsymbol{k_2}}^\dagger\,a_{\boldsymbol{k_2}}+
  n_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}^\dagger\,a_{\boldsymbol{k_1}})

where the boson ocupation factor

.. math::
  n_\boldsymbol{k}=\langle\,a_{\boldsymbol{k}}^\dagger\,a_{\boldsymbol{k}}\,\rangle=
  \frac{1}{e^{\beta\,\Omega(\boldsymbol{k})}-1}

depends on the renormalized spin wave frequency :math:`\Omega(\boldsymbol{k})` and must be
calculated self-consistently. The
resulting renormalized Hamiltonian is

.. math::
  H^{RSWT}&\,=\,\,E^0\,+\,
  \sum_{\boldsymbol{k}}\,\Omega(\boldsymbol{k})\,a_{\boldsymbol{k}}^\dagger\,a_{\boldsymbol{k}}\\\\
  \Omega(\boldsymbol{k})&\,=\,\omega(\boldsymbol{k})+\frac{1}{2\,M}\,\sum_{\boldsymbol{k'}}\,
  \left(\lambda(\boldsymbol{k},0)+\lambda(\boldsymbol{k'},0)+
  \lambda(\boldsymbol{k},\boldsymbol{k-k'})+\lambda(\boldsymbol{k'},\boldsymbol{k-k'})\right)\\
  &\,=\,\omega(\boldsymbol{k})-
  \frac{1}{M}\,\sum_{\boldsymbol{k'}}\,\left(4\,A^{xx}+J^{xx}(\boldsymbol{k})+J^{xx}(\boldsymbol{k'})
  -J^{zz}(\boldsymbol{0})-J^{zz}(\boldsymbol{k-k'}\right)\,n_{\boldsymbol{k'}}\\
  &\,=\,\,\omega(\boldsymbol{k})+
  \left(J^{zz}(\boldsymbol{0})-4\,A^{xx}-J^{xx}(\boldsymbol{k})\right)\,n_0+\frac{1}{M}\,
  \sum_{\boldsymbol{k'}}\,\left(J^{zz}(\boldsymbol{k-k'})-J^{xx}(\boldsymbol{k'})\right)\,n_{\boldsymbol{k'}}

with the average boson occupation being defined by
:math:`n_0=\frac{1}{M}\,\sum_\boldsymbol{k}\,n_{\boldsymbol{k}}`. Further progress can be made for an
hyper-cubic lattice if the exchange constants are isotropic, and reach only nearest neighbors
sites at lattice vectors :math:`\boldsymbol{\delta}`. Then
:math:`J^{xx,zz}(\boldsymbol{k})=J^{xx,zz}\,\gamma(\boldsymbol{k})` with

.. math::
  \gamma(\boldsymbol{k})\,=\,\sum_{\boldsymbol{\delta}}\,e^{i\,\boldsymbol{k}\cdot\boldsymbol{\delta}}
                      \,=\,\sum_{\boldsymbol{\delta}}\,\cos(\boldsymbol{k}\cdot\boldsymbol{\delta})

and the renormalized frequency simplifies to

.. math::
  \Omega(\boldsymbol{k})\,=\,
  2\,S\,(A^{xx}-A^{zz})\,-\,4\,A^{xx}\,+\,(S-n_0)\,
   (J^{zz}\,\gamma(\boldsymbol{0})-J^{xx}\,\gamma(\boldsymbol{k}))+
  n_1\,\left(J^{zz}\,\gamma(\boldsymbol{k})-J^{xx}\,\gamma(\boldsymbol{0})\right)

with :math:`n_1=\frac{1}{M}\,\sum_\boldsymbol{k}\,\cos(k_x)\,n_{\boldsymbol{k}}`. If there
is no magnetic anisotropy, :math:`A^{xx}=A^{zz}=0` and :math:`J=J^{xx}=J^{zz}` so that
the renormalized frequency becomes

.. math::
  \Omega(\boldsymbol{k})\,=\,J\,(\,\gamma(\boldsymbol{k})-\gamma(\boldsymbol{0})\,)\,(S-(n_0-n_1))
