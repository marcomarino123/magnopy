.. _user-guide_methods_examples_gamma-point:

***************************************************************
Gamma-point solution solution with spins lying along the Z-axis
***************************************************************

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

The classical energy is in this case

.. math::
  E_{Cl} = \frac{1}{2}\,\sum_{\boldsymbol{d}_{ij}, i, j} S_i\,S_j\,
  	\left(J_{\boldsymbol{d}ij}^{zz} + 2 \,\delta_{i,j}\,\delta_{\boldsymbol{d}_{ij},0}\,A_i^{zz}\right)

We introduce the notation

.. math::
  J_{ij}^{\alpha\beta}(\boldsymbol{k})= \sum_{\boldsymbol{d}_{ij}}\,
  		J^{\alpha\beta}_{\boldsymbol{d}ij}\, e^{i\,\boldsymbol{k}\cdot\boldsymbol{d}_{ij}}

Then, the kinetic and pairing terms of the Hamiltonian are

.. math::
  T_{ij}(\boldsymbol{k})&\,=\,\delta_{ij}\,\left(\left(A_i^{xx}+A_i^{yy}+2\,A_i^{zz}\right)\,S_i-
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

and the Hamiltonian is

.. math::
  H^{LSWT} = -\frac{1}{2}\,\sum_\boldsymbol{k} \, \boldsymbol{T}(\boldsymbol{k})+
  			 \frac{1}{2}\,\sum_\boldsymbol{k}\,\cal{\boldsymbol{B}}(\boldsymbol{k})^\dagger\,
  			 \begin{pmatrix}
  			 \boldsymbol{T}(\boldsymbol{k})&\boldsymbol{\Delta}(\boldsymbol{k})\\
  			 \boldsymbol{\Delta}(\boldsymbol{k})^\dagger&\boldsymbol{T}(-\boldsymbol{k})^*
  			 \end{pmatrix}
  			 \cal{\boldsymbol{B}}(\boldsymbol{k})

=============================================================
Simplification: single atom per unit cell with spin :math:`S`
=============================================================
A notation simplification happens because the :math:`i\, j` sub-indices dissapear.
The kinetic and pairing terms simplify to

.. math::
  \frac{T(\boldsymbol{k})}{S}&\,=\,A^{xx}+A^{yy}+
  \frac{J^{xx}(\boldsymbol{k})+J^{yy}(\boldsymbol{k})}{2}-J^{zz}(\boldsymbol{k=0})-i D^z(\boldsymbol{k})\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=\,A^{xx}-A^{yy}-2 i A^{xy}+
  \frac{J^{xx}(\boldsymbol{k})-J^{yy}(\boldsymbol{k})}{2}-i J^{xy}(\boldsymbol{k})

A last simpification comes about if :math:`J^{xx}=J^{yy}`, :math:`A^{xx}=A^{yy}=A`, and
:math:`J^{xy}=D^z=A^{xy}=0`. Then

.. math::
  \frac{T(\boldsymbol{k})}{S}&\,=\,2\,A+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=0

whereby the LSWT magnon dispersion relationship is

.. math::
  \omega(\boldsymbol{k})=S\,\left(\,2\,A+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\,\right)

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

The bosonic biquadratic has also been written :ref:`here <user-guide_methods_hp-higher>`, where the three coupling constants for
a single atom per unit cell are

.. math::
  D^{1,\nu}(\boldsymbol{q})&= J^{f\nu,00}(\boldsymbol{q})=J^{zz}(\boldsymbol{q})\\
  D^{2,\nu}(\boldsymbol{q})&= J^{f\nu,++}(\boldsymbol{q})=A^{xx}+A^{yy}+
                                    \frac{J^{xx}(\boldsymbol{q})+J^{yy}(\boldsymbol{q})}{2}+i\,D^z(\boldsymbol{q})\\
  D^{3,\nu}(\boldsymbol{q})&= J^{f\nu,+-}(\boldsymbol{q})=A^{xx}-A^{yy}-2\,i\,A^{xy}+
                                    \frac{J^{xx}(\boldsymbol{q})-J^{yy}(\boldsymbol{q})-
                                    i\,\left(J^{xy}(\boldsymbol{q})+J^{yx}(\boldsymbol{q})\right)}{2}

We assume now that :math:`J^{xx}=J^{yy}` and :math:`J^{xy}=A^{xy}=D^z=0`. Then

.. math::
  D^{1,\nu}(\boldsymbol{q})&=J^{zz}(\boldsymbol{q})\\
  D^{2,\nu}(\boldsymbol{q})&=2\,A^{xx}+J^{xx}(\boldsymbol{q})\\
  D^{3,\nu}(\boldsymbol{q})&=0

As a consequence, the interacting biquadratic Hamiltonian becomes

.. math::
  H^{Biquadratic}=\frac{1}{2\,M}\,\sum_{\boldsymbol{k1},\boldsymbol{k2},\boldsymbol{p}}\,\left(J^{zz}(\boldsymbol{p})-2\,A^{xx}-
                      \frac{J^{xx}(\boldsymbol{k1})+J^{xx}(\boldsymbol{k1+p})}{2}\right)\,
                      a_{\boldsymbol{k1+p}}^\dagger\,a_{\boldsymbol{k2-p}}^\dagger\,a_{\boldsymbol{k2}}\,a_{\boldsymbol{k1}}
