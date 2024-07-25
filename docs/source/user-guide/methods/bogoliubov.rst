.. _user-guide_methods_bogoliubov:

*************************************
Generalized Bogoliubov Transformation
*************************************

This section discusses how to diagonzalize block bilinear Hamiltonians.
The section is based on references [1]_ and [2]_

=======================
Matrix diagonalization
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
  \boldsymbol{C}_\boldsymbol{k}&=\begin{pmatrix}c_{\boldsymbol{k},1}\\c_{\boldsymbol{k},2}\\\vdots\\c_{\boldsymbol{k},m}\end{pmatrix}\\
  \boldsymbol{\tilde{C}}_\boldsymbol{k}&=\begin{pmatrix}c_{\boldsymbol{k},1}&c_{\boldsymbol{k},2}&\cdots&c_{\boldsymbol{k},m}\end{pmatrix}

Arrange those block vectors into the super-vector

.. math::
  \boldsymbol{\cal{C}}_\boldsymbol{k}=\begin{pmatrix}\boldsymbol{C}_\boldsymbol{k}\\\boldsymbol{\tilde{C}}_{-\boldsymbol{k}}\end{pmatrix}

Then, the bosonic and fermionic commutation relations are, respectively

.. math::
  \left[\,\boldsymbol{\cal{C}}_\boldsymbol{k},\,\boldsymbol{\cal{C}}_\boldsymbol{k}^\dagger\,\right]_\eta \,= \,\delta_{k,k'}\,{\boldsymbol \tau}_\eta

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

:math:`\gamma_{\boldsymbol{k},i}` destroys "quasi-particles" henceforth. Let us perform a basis transformation
with the aid of the derivative matrix :math:`P_\boldsymbol{k}`

.. math::
 \boldsymbol{\cal{C}}_\boldsymbol{k}&=P_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}\\
 P_\boldsymbol{k}&=\begin{pmatrix}A_\boldsymbol{k}&B_{-\boldsymbol{k}}^*\\B_\boldsymbol{k}&A_{-\boldsymbol{k}}^*\end{pmatrix}

The requirement that the new quasi-particles obey the same statistics as the pristine ones is spelled as

.. math::
  \left[\,\boldsymbol{\cal{C}}_\boldsymbol{k},\,\boldsymbol{\cal{C}}_\boldsymbol{k}^\dagger\,\right]_\eta \,=
  P_\boldsymbol{k}\,\left[\,\boldsymbol{\Gamma}_\boldsymbol{k},\,\boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,\right]_\eta \,P_\boldsymbol{k}^\dagger\,=
  \,\delta_{k,k'}\,{\boldsymbol \tau}_\eta

meaning that the derivative matrix must obey

.. math::
  \tau_\eta\,P_\boldsymbol{k}\,\tau_\eta\,P_\boldsymbol{k}^+\,=\,{\cal I}_m

This requirement implies for fermions that the :math:`P_\boldsymbol{k}` be unitary, or

.. math::
  A_\boldsymbol{k}\,A_\boldsymbol{k}^*+B_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}}^* &\,=\, {\cal I}_m\\
  A_\boldsymbol{k}\,B_\boldsymbol{k}^*+A_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}}^* &\,=\, 0

The requirement for bosons is spelled as

.. math::
  A_\boldsymbol{k}\,A_\boldsymbol{k}^*-B_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}}^* &\,=\, {\cal I}_m\\
  A_\boldsymbol{k}\,B_\boldsymbol{k}^*-A_{-\boldsymbol{k}} \,B_{-\boldsymbol{k}}^* &\,=\, 0

and leads to the Bogoluibov analysis and transformation [3]_.

========================================
Diagonalization of bilinear Hamiltonians
========================================
Let be the following bilinear Hamiltonian

.. math::
  \boldsymbol{H}_\boldsymbol{k}^{BL}&\,=\,
  -\frac{\eta}{2}\,Tr(T)+\frac{1}{2}\,\boldsymbol{\cal{C}}_\boldsymbol{k}^+\,
  \cal{\boldsymbol{H}}_\boldsymbol{k}\,\boldsymbol{\cal{C}}_\boldsymbol{k}\\
  \cal{\boldsymbol{H}}_\boldsymbol{k}&\,=\,
  \begin{pmatrix}\boldsymbol{T}_\boldsymbol{k}&\boldsymbol{\Delta}_\boldsymbol{k}\\
                  \boldsymbol{\Delta}_\boldsymbol{k}^\dagger&\eta\,\boldsymbol{T}_{\boldsymbol{-k}}^*
  \end{pmatrix}

We perform a basis transformation oriented to diagonalize the Hamiltonian. Then

.. math::
  \boldsymbol{\cal{C}}_\boldsymbol{k}^+\,
  \cal{\boldsymbol{H}}_\boldsymbol{k}\,\boldsymbol{\cal{C}}_\boldsymbol{k}\,=\,
  \boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,P_\boldsymbol{k}^\dagger\,
  \cal{\boldsymbol{H}}_\boldsymbol{k}\,P_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}
  \,=\,
  \boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,\tau_\eta\,P_\boldsymbol{k}^{-1}\,\tau_\eta\,
  \cal{\boldsymbol{H}}_\boldsymbol{k}\,P_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}
  \,=\,
  \boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,
  \boldsymbol{\cal E}_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}

meaning that we require the matrix :math:`\boldsymbol{\cal E}_\boldsymbol{k}` to be diagonal. Here

.. math::
  \boldsymbol{\cal M}_\boldsymbol{k}&\,=\,\tau_\eta\,\cal{\boldsymbol{H}}_\boldsymbol{k}\\
  \boldsymbol{\cal D}_\boldsymbol{k}&\,=\,P_\boldsymbol{k}^{-1}\,\cal{\boldsymbol{M}}_\boldsymbol{k}\\
  \boldsymbol{\cal E}_\boldsymbol{k}&\,=\,\tau_\eta\,\boldsymbol{\cal D}_\boldsymbol{k}

The dynamic matrix

.. math::
  \boldsymbol{\cal M}_\boldsymbol{k}\,=\,
  \begin{pmatrix}\boldsymbol{T}_\boldsymbol{k}&\boldsymbol{\Delta}_\boldsymbol{k}\\
                  \eta\,\boldsymbol{\Delta}_\boldsymbol{k}^\dagger&\boldsymbol{T}_{\boldsymbol{-k}}^*
  \end{pmatrix}

is not hermitian if :math:`\eta=-1`, e.g.: for bosons. If
:math:`\boldsymbol{\cal M}_\boldsymbol{k}` is diagonalizable by :math:`P_\boldsymbol{k}`
then

.. math::
  \boldsymbol{\cal D}_\boldsymbol{k}&\,=\,
      \begin{pmatrix}
        \boldsymbol{\omega}_\boldsymbol{k}&0\\0&-\boldsymbol{\omega}_{-\boldsymbol{k}}
      \end{pmatrix}\\\\
   \boldsymbol{\omega}_\boldsymbol{k}&\,=\,
   diag(\omega_{\boldsymbol{k},1},\,\omega_{\boldsymbol{k},2},\,\cdots,\,\omega_{\boldsymbol{k},m})

and the dynamic matrix is made of the eigenvectors of :math:`\boldsymbol{\cal D}_\boldsymbol{k}`:

.. math::
  \boldsymbol{\cal D}_\boldsymbol{k}=
    (\boldsymbol{v}(\omega_{\boldsymbol{k},1}),\,\,\cdots,\,\boldsymbol{v}(\omega_{\boldsymbol{k},m}),\,
    \boldsymbol{v}(-\omega_{-\boldsymbol{k},1}),\,\cdots,\,\boldsymbol{v}(-\omega_{-\boldsymbol{k},m}))

with normalization condition

.. math::
  \boldsymbol{\cal D}_\boldsymbol{k}^\dagger\,\tau_\eta\,\boldsymbol{\cal D}_\boldsymbol{k}\,=\,
    \begin{pmatrix}1&0\\0&-\eta\end{pmatrix}

========================
Diagonalized Hamiltonian
========================
The Hamiltonian can be manipulated to look as

.. math::
  \boldsymbol{H}_\boldsymbol{k}^{BL}\,=\,
  -\frac{\eta}{2}\,Tr(T)+\frac{1}{2}\,\boldsymbol{\Gamma}_\boldsymbol{k}^\dagger\,
  \boldsymbol{\cal E}_\boldsymbol{k}\,\boldsymbol{\Gamma}_\boldsymbol{k}\,=\,
  -\frac{\eta}{2}\,Tr(T)
  +\frac{1}{2}\,\Gamma_\boldsymbol{k}^\dagger\,\boldsymbol{\omega}_\boldsymbol{k}\,\Gamma_\boldsymbol{k}
  +\frac{1}{2}\,\Gamma_{\boldsymbol{-k}}^\dagger\,\boldsymbol{\omega}_{\boldsymbol{-k}}\,\Gamma_{\boldsymbol{-k}}

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
