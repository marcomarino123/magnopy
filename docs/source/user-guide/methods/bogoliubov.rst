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
  \tilde{C}_\boldsymbol{k}=\begin{pmatrix}c_{\boldsymbol{k},1}&c_{\boldsymbol{k},2}&\cdots&c_{\boldsymbol{k},m}\end{pmatrix}

Arrange those block vectors into the supervector

.. math::
  \boldsymbol{C}_\boldsymbol{k}=\begin{pmatrix}C_\boldsymbol{k}\\\tilde{C}_{-\boldsymbol{k}}\end{pmatrix}

Then, the bosonic and fermionic commutation relations are, respectively

.. math::
  \left[\,\boldsymbol{C}_\boldsymbol{k},\,\boldsymbol{C}_\boldsymbol{k}^\dagger\,\right]_\eta \,= \,\delta_{k,k'}\,{\boldsymbol \tau}_\eta

where :math:`\boldsymbol{\tau}_\eta= {\cal I}_m\otimes\tau_\eta`, with :math:`{\cal I}_m` being the
:math:`m\times m` identity matrix, and

.. math::
  \tau_\eta =\begin{pmatrix}1&0\\0&\eta\end{pmatrix}

Here :math:`\eta` is +1 for fermions and -1 for bosons.

=============
Basis changes
=============
Let us define the new basis

.. math::
  \boldsymbol{\Gamma}_\boldsymbol{k}&=\begin{pmatrix}\Gamma_\boldsymbol{k}\\\tilde{\Gamma}_\boldsymbol{-k}\end{pmatrix}\\
  \Gamma_\boldsymbol{k}&=\begin{pmatrix}\gamma_{\boldsymbol{k},1}\\\gamma_{\boldsymbol{k},2}\\\vdots\\\gamma_{\boldsymbol{k},m}\end{pmatrix}\\
  \tilde{\Gamma}_\boldsymbol{k}&=\begin{pmatrix}\gamma_{\boldsymbol{k},1}&\gamma_{\boldsymbol{k},2}&\cdots&\gamma_{\boldsymbol{k},m}\end{pmatrix}

:math:`\gamma_{\boldsymbol{k},i}` are called henceforth quasi-particles. Let us perform a basis transformation
with the aid of the derivative matrix :math:`P_\boldsymbol{k}`

.. math::
 \boldsymbol{C}_\boldsymbol{k}&=P_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}\\
 P_\boldsymbol{k}&=\begin{pmatrix}A_\boldsymbol{k}&B_{\boldsymbol{k}}^*\\B_\boldsymbol{k}&A_{-\boldsymbol{k}}^*\end{pmatrix}

The requirement that the new quasi-particles obey the same statistics as the pristine ones is spelled as

.. math::
  \left[\,\boldsymbol{C}_\boldsymbol{k},\,\boldsymbol{C}_\boldsymbol{k}^\dagger\,\right]_\eta \,=
  P_\boldsymbol{k}\,\left[\,\boldsymbol{\Gamma}_\boldsymbol{k},\,\boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,\right]_\eta \,P_\boldsymbol{k}^\dagger\,=
  \,\delta_{k,k'}\,{\boldsymbol \tau}_\eta

meaning that the derivative matrix must obey

.. math::
  \tau_\eta\,P_\boldsymbol{k}\,\tau_\eta\,P_\boldsymbol{k}^+\,=\,{\cal I}_m

This requirement implies for fermions that the :math:`P_\boldsymbol{k}` be unitary, or

.. math::
  A_\boldsymbol{k}\,A_\boldsymbol{k}^*+B_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}^* = {\cal I}_m\\
  A_\boldsymbol{k}\,B_\boldsymbol{k}^*+A_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}^* = 0

The requirement for bosons is that :math:`\tau_3\,P_\boldsymbol{k}` be unitary, that is spelled as


and leads to the Bogoluibov analysis and transformation [3]_.



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

.. [3] Bogoliubov
       Bla bla
