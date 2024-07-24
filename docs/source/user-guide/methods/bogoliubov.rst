.. _user-guide_methods_bogoliubov:

*************************************
Generalized Bogoliubov Transformation
*************************************

This section discusses how to diagonzalize block bilinear Hamiltonians.
The section is based on references [1]_ and [2]_

=======================
Matrix diagonzalization
=======================
Let :math:`M` be a :math:`m\times m` matrix. Then :math:`M` is diagonalizable if there
exists a diagonal matrix :math:`D` and an invertible matrix :math:`P`, both of size
:math:`m\times m`, such that :math:`M=P\, D\, P^{-1}`. Finding :math:`D` and :math:`P`
is called diagonalizing the matrix :math:`M`. Let

.. math::
  M\,\boldsymbol{p}_i=d_i\,\boldsymbol{p}_i

with :math:`i = 1,\,2\,\cdots,\,m`, where :math:`d_i` is ordered arbitrarily. Then
the matrices :math:`M` and :math:`P` are

.. math::
  D \,=\,& diag(d_1,\,d_2,\,\cdots,\,d_m)\\
  P \,=\,&(\boldsymbol{p}_1,\,\boldsymbol{p}_1,\,\cdots,\,\boldsymbol{p}_m)

and

.. math::
  M\, P = P\, D\,\implies\,M=P\,D\,P^{-1}

=============================================
Block boson and fermion commutation relations
=============================================
Let a physical system be defined by the operators :math:`\{c_{\boldsymbol{k},\alpha},\alpha=1,\,2,\,\cdots,\,m\}`.
Arrange these operators as the block vectors

.. math::
  C_\boldsymbol{k}=\begin{pmatrix}c_{\boldsymbol{k},1}\\c_{\boldsymbol{k},2}\\\vdots\\c_{\boldsymbol{k},m}\end{pmatrix},\,\,\,
  \tilde{C}_\boldsymbol{k}=\begin{pmatrix}c_{\boldsymbol{k},1}&c_{\boldsymbol{k},2}&\vdots&c_{\boldsymbol{k},m}\end{pmatrix}

Arrange those block vectors into the supervector

.. math::
  \boldsymbol{C}_\boldsymbol{k}=\begin{pmatrix}C_\boldsymbol{k}\\\tilde{C}_{-\boldsymbol{k}}\end{pmatrix}

Then, the bosonic and fermionic commutation relations are, respectively

.. math::
  \left[\,\boldsymbol{C}_\boldsymbol{k},\,\boldsymbol{C}_\boldsymbol{k}^\dagger\,\right]_- \,=& \,\delta_{k,k'}\,{\boldsymbol \tau}_3\\
  \left[\,\boldsymbol{C}_\boldsymbol{k},\,\boldsymbol{C}_\boldsymbol{k}^\dagger\,\right]_+ \,=& \,\delta_{k,k'}\,{\boldsymbol \tau}_0\\

where :math:`\boldsymbol{\tau}_{0,3}= {\cal I}_m\otimes\tau_{0,3}`, :math:`{\cal I}_m` and :math:`\tau_{0,3}`
are the :math:`m\times m` identity matrix, the :math:`2\times 2` identity matrix and the third Pauli matrix, respectively.

==========
References
==========

.. [1] Ming-wen Xiao.
       Theory of transformation for the diagonalization of quadratic Hamiltonians.
       arXiv:0908.0787v1.

.. [2] Terumichi Ohashi, Shingo Kobayashi, and Yuki Kawaguchi.
	   Generalized Berry phase for a bosonic Bogoliubov system with
	   exceptional points.
	   Phys. Rev. A 101, 013625 (2020).
