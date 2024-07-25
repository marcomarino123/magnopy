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
and the Hamiltonian rewritten as

.. math::
  {\cal H}^{Cubic}=-\frac{1}{M^{1/2}}\, \sum_{i, j,\nu}\,\sum_{\boldsymbol{k}_1,\boldsymbol{k}_2}\,
  \left(
  \frac{S_j}{S_i^{1/2}}\, C_{ij}^{1,\nu}(\boldsymbol{q}) \,
  a_\boldsymbol{k_1}+\boldsymbol{k_2}+\boldsymbol{q},i}\,a_{\boldsymbol{k_1},i}\,a_{\boldsymbol{k_2},i}
  +
  S_i^{1/2}\, C_{ij}^{2,\nu}(\boldsymbol{k_1},\boldsymbol{q}) \,
  a_\boldsymbol{k_1}+\boldsymbol{k_2}+\boldsymbol{q},i}\,a_{\boldsymbol{k_1},i}\,a_{\boldsymbol{k_2},i}
  \right)

==================================
Bi-quadratic Spin-Wave Hamiltonian
==================================
Similarly, the bi-quadratic piece of the Spin-Wave Hamiltonian can be rewritten as follows:

.. math::
