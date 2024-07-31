.. _user-guide_methods_examples_gamma-point:

***************************************************************
Gamma-point solution solution with spins lying along the Z-axis
***************************************************************

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
  E_{Cl} = \frac{1}{2}\,\sum_{\boldsymbol{d}_{ij}, i, j} S_i\,S_j\,J_{\boldsymbol{d}ij}^{zz} + \sum_i\,A_i^{zz}\,S_i^2

==========
LSW theory
==========
The quantum correction, kinetic and pairing terms of the Hamiltonian are

.. math::
  E^{QC-LSWT} &\,=\,M\,\sum_i\,S_i\,A_i^{zz}+\frac{M}{2}\,
              \sum_{\boldsymbol{d}_{ij},i, j} S_{j}\,J_{\boldsymbol{d}ij}^{zz}\\\\
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

where we have introduced the notation

.. math::
  J_{ij}^{\alpha\beta}(\boldsymbol{k})= \sum_{\boldsymbol{d}_{ij}}\,
      J^{\alpha\beta}_{\boldsymbol{d}ij}\, e^{i\,\boldsymbol{k}\cdot\boldsymbol{d}_{ij}}

The LSWT Hamiltonian is

.. math::
  H^{LSWT} = E^{QC-LSWT}+
  			 \frac{1}{2}\,\sum_\boldsymbol{k}\,\cal{\boldsymbol{B}}(\boldsymbol{k})^\dagger\,
  			 \begin{pmatrix}
  			 \boldsymbol{T}(\boldsymbol{k})&\boldsymbol{\Delta}(\boldsymbol{k})\\
  			 \boldsymbol{\Delta}(\boldsymbol{k})^\dagger&\boldsymbol{T}(-\boldsymbol{k})^*
  			 \end{pmatrix}
  			 \cal{\boldsymbol{B}}(\boldsymbol{k})

=============================================================
Simplification: single atom per unit cell with spin :math:`S`
=============================================================
A notable simplification happens here because the :math:`i` and :math:`j` sub-indices dissapear.
The classical energy is

.. math::
   E_{Cl} = M\,S^2\,\left(A^{zz}+\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0) \right)

The quantum correction, kinetic and pairing terms simplify to

.. math::
  \frac{E^{QC-LSWT}}{S}&\,=\,M\,\left(A^{zz}+\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)\right)\\
  \frac{T(\boldsymbol{k})}{S}&\,=\,A^{xx}+A^{yy}-2\,A^{zz}+
  \frac{J^{xx}(\boldsymbol{k})+J^{yy}(\boldsymbol{k})}{2}-J^{zz}(\boldsymbol{k=0})-i D^z(\boldsymbol{k})\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=\,A^{xx}-A^{yy}-2 i A^{xy}+
  \frac{J^{xx}(\boldsymbol{k})-J^{yy}(\boldsymbol{k})}{2}-i J^{xy}(\boldsymbol{k})

A last simpification comes about if :math:`J^{xx}=J^{yy}`, :math:`A^{xx}=A^{yy}`, and
:math:`J^{xy}=D^z=A^{xy}=0`. Then

.. math::
  \frac{E^{QC-LSWT}}{S}&\,=\,M\,\left(A^{zz}+\frac{1}{2}\,J^{zz}(\boldsymbol{k}=0)\right)\\
  \frac{T(\boldsymbol{k})}{S}&\,=\,2\,(A^{xx}-A^{zz})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\\
  \frac{\Delta(\boldsymbol{k})}{S}&\,=0

whereby the LSWT spin wave dispersion relation becomes

.. math::
  \omega(\boldsymbol{k})\,=\,S\,\left(\,2\,(A^{xx}-A^{zz})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\,\right)

and the LSWT Hamiltonian

.. math::
  H^{LSWT} &\,=\, E^{QC-LSWT}+\frac{1}{2}\,\sum_{\boldsymbol{k}}\,\omega(-\boldsymbol{k})
  +\sum_{\boldsymbol{k}}\,\omega(\boldsymbol{k})\,\gamma_\boldsymbol{k}^\dagger\,\gamma(\boldsymbol{k})\\
  &\,=\,M\,S\,A^{xx}
  +\sum_{\boldsymbol{k}}\,\omega(\boldsymbol{k})\,\gamma_\boldsymbol{k}^\dagger\,\gamma(\boldsymbol{k})

The constant piece is finally added to the expression for the classical energy and the LSWT Hamiltonian
becomes finally

.. math::
  H^{LSWT}=\sum_{\boldsymbol{k}}\,\omega(\boldsymbol{k})\,a_\boldsymbol{k}^\dagger\,a(\boldsymbol{k})

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
  J^{f\nu,00}_{\boldsymbol{d}_{ii}=0}&=A^{xx}-A^{yy}-2\,i\,A^{xy}

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

=============================
Renormalized Spin Wave Theory
=============================

The full interacting Hamiltonian becomes

.. math::
  H=S\,\sum_{\boldsymbol{k}}\,\left(\,2\,(A^{xx}-A^{zz})\,(1-\frac{1}{2\,S})+J^{xx}(\boldsymbol{k})-J^{zz}(\boldsymbol{k}=0)\,\right)+
          \frac{1}{2\,M}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2},\boldsymbol{p}}\,\left(J^{zz}(\boldsymbol{p})-2\,A^{xx}-
          \frac{J^{xx}(\boldsymbol{k_1})+J^{xx}(\boldsymbol{k_1+p})}{2}\right)\,
          a_{\boldsymbol{k_1+p}}^\dagger\,a_{\boldsymbol{k_2-p}}^\dagger\,a_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}

The four-boson interaction is decoupled in the Mean-Field approximation as follows

.. math::
  a_{\boldsymbol{k_1+p}}^\dagger\,a_{\boldsymbol{k_2-p}}^\dagger\,a_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}=
  \delta_{\boldsymbol{p},0}\,(n_{\boldsymbol{k_1}}\,a_{\boldsymbol{k_2}}^\dagger\,a_{\boldsymbol{k_2}}+
  n_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}^\dagger\,a_{\boldsymbol{k_1}})+
  \delta_{\boldsymbol{p},\boldsymbol{k_2-k_1}}\,(n_{\boldsymbol{k_1}}\,a_{\boldsymbol{k_2}}^\dagger\,a_{\boldsymbol{k_2}}+
  n_{\boldsymbol{k_2}}\,a_{\boldsymbol{k_1}}^\dagger\,a_{\boldsymbol{k_1}})
