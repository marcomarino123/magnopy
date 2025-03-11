.. _user-guide_methods_hp-higher:

*********************************************************
Higher-order pieces of the Holstein-Primakoff Hamiltonian
*********************************************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/quantum-operators.inc
  * .. include:: page-notations/bra-ket.inc

===========================
Cubic Spin-Wave Hamiltonian
===========================
The cubic piece of the Spin-Wave Hamiltonian introduced
:ref:`previously <user-guide_methods_quantum-hamiltonian>` can be Fourier-transformed
and the normal-ordered Hamiltonian is

.. math::
  {\cal H}^{Cubic}=-\frac{1}{M^{1/2}}\, \sum_{i, j,\nu}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2}}\,
  \left(
  \frac{S_j}{S_i^{1/2}}\, C_{ij}^{1,\nu}(\boldsymbol{q}) \,
  a_{\boldsymbol{k_1}+\boldsymbol{k_2}+\nu\,\boldsymbol{q},i}^\dagger
  \,a_{\boldsymbol{k_2},i}\,a_{\boldsymbol{k_1},i}
  +
  S_i^{1/2}\, C_{ij}^{2,\nu}(\boldsymbol{k_1},\boldsymbol{q}) \,
  a_{\boldsymbol{k_1}+\boldsymbol{k_2}+\nu\,\boldsymbol{q},j}^\dagger
  \,a_{\boldsymbol{k_2},j}\,a_{\boldsymbol{k_1},i}\right) + h.c.

where :math:`h.c.` means hermitian conjugate, and the coupling constants are

.. math::
  C_{ij}^{1,\nu}(\boldsymbol{q})&=\sum_{\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}_{ij}}^{f\nu,+0}\\
  C_{ij}^{2,\nu}(\boldsymbol{q})&=\sum_{\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}_{ij}}^{f\nu,+0}\,
                                  e^{-i\,(\boldsymbol{k_1}+\nu\,\boldsymbol{q})}

==================================
Biquadratic Spin-Wave Hamiltonian
==================================
Similarly, the bi-quadratic piece of the Spin-Wave Hamiltonian can be rewritten as follows:

.. math::
  {\cal H}^{Biquadratic}\,=\,&
  \frac{1}{2}\, \sum_{i,\nu,\boldsymbol{k}} \left(
  \left(J_{\boldsymbol{d}_{ii}=0}^{f\nu,00}\,-\,J_{\boldsymbol{d}_{ii}=0}^{f\nu,++}\right)\,
  a_{\boldsymbol{k}+\nu\,\boldsymbol{q},i}^\dagger\,a_{\boldsymbol{k},i}-
  \frac{1}{2}\,\left(J_{\boldsymbol{d}_{ii}=0}^{f\nu,+-}\,
  a_{-(\boldsymbol{k}+\nu\,\boldsymbol{q}),i}\,a_{\boldsymbol{k},i}+h.c.\right)\right)\\
  &+\frac{1}{2\,M}\, \sum_{i, j,\nu}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2},\boldsymbol{p}}\,
  \Big( D_{ij}^{1,\nu}(\boldsymbol{p},\boldsymbol{q})\,
  a_{\boldsymbol{k_2}+\boldsymbol{p}+\nu\,\boldsymbol{q},i}^\dagger\,
  a_{\boldsymbol{k_1}-\boldsymbol{p},j}^\dagger\,
  a_{\boldsymbol{k_2},i}\,a_{\boldsymbol{k_1},j}\\
  &-\frac{1}{4\,M}\, \sum_{i, j,\nu}\,\sum_{\boldsymbol{k_1},\boldsymbol{k_2},\boldsymbol{p}}\,
  \left(\frac{S_i}{S_j}\right)^{1/2}\,
  \left(\left(D_{ij}^{2,\nu}(\boldsymbol{k_1},\boldsymbol{q})\,
  a_{\boldsymbol{k_1}+\boldsymbol{p}+\nu\,\boldsymbol{q},j}^\dagger
  \,a_{\boldsymbol{k_2}-\boldsymbol{p},j}^\dagger\,
  a_{\boldsymbol{k_2},j}\,a_{\boldsymbol{k_1},i}+
  D_{ij}^{3,\nu}(\boldsymbol{k_1},\boldsymbol{q})\,
  a_{\boldsymbol{k_1}+\boldsymbol{p}+\nu\,\boldsymbol{q},j}^\dagger
  \,a_{-\boldsymbol{k_2}+\boldsymbol{p},j}\,
  a_{\boldsymbol{k_2},j}\,a_{\boldsymbol{k_1},i}
  \right)\,+\,h.c.\right)

where normal ordering results in five additional bilinear pieces. Here, the coupling constants are

.. math::
  D_{ij}^{1,\nu}(\boldsymbol{q})&=\sum_{\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}_{ij}}^{f\nu,00}
                                  e^{i\,(\boldsymbol{k_1}-\boldsymbol{k_3})}\\
  D_{ij}^{2,\nu}(\boldsymbol{q})&=\sum_{\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}_{ij}}^{f\nu,++}\,
                                  e^{-i\,(\boldsymbol{k_1}+\nu\,\boldsymbol{q})}\\
  D_{ij}^{3,\nu}(\boldsymbol{q})&=\sum_{\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}_{ij}}^{f\nu,+-}\,
                                  e^{-i\,(\boldsymbol{k_1}+\nu\,\boldsymbol{q})}
