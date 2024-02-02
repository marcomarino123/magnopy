.. _user-guide_methods_lswt:

************************
Linear Spin-Wave Theory
************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/operators.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/kronecker-delta.inc


This section discusses the LSWT Hamiltonian :math:`{\cal H}^{LSWT}`
introduced :ref:`here <user-guide_methods_hp-bosons>`

.. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.inc

Rotated exchange matrix
=======================
The rotated exchange matrix :math:`\boldsymbol{J_{ij}^s}(\boldsymbol{d_{ij}})`
that was introduced :ref:`here <user-guide_methods_spherical-rf>`
can be split into the following five pieces

.. include:: J-abmd-separation.txt

.. dropdown:: Matrix elements in the spherical reference frame

  .. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.inc

  .. include:: ../repeated-formulas/exchange-matrix-spherical.inc

.. dropdown:: Hermiticity properties of the rotated exchange matrix

  .. include:: ../repeated-formulas/spinham-parameter-symmetries.inc

.. dropdown:: Proof of Hermiticities in the LSWT Hamiltonian

  .. include:: ../repeated-formulas/hermiticity.inc

Hamiltonian reordering
======================
The LSWT Hamiltonian can be rearranged into a more convenient form
by noting that each bond is counted twice, and taking advantage of the
hermiticy relations for the exchange matrix :math:`\boldsymbol{\tilde{J}_{mdij}^s}`

.. math::
  {\cal H}^{LSWT}
  =
  \frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij}} i, j} \,
   \Big(&
  \,(E_{mdij}+E_{mdij}^*)\,\,a_{mi}^\dagger\,a_{mi}
  \\&+
  T_{mdij}\, a_{mi}^\dagger\,a_{m+d_{ij}\,j} +
  T_{mdij}^*\,a_{m+d_{ij}\,j}^\dagger\,a_{mi}
  \\&+
  \Delta_{mdij}\,b_{m+d_{ij}\,j}\,b_{mi} +
  \Delta_{mdij}^*\,b_{mi}^\dagger\,b_{m+d_{ij}\,j}^\dagger
  \Big)

The first term in the sum is better rearranged to make it explicitly hermitian

.. math::
  \frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij}} i, j} \,
  \,(E_{mdij}+E_{mdij}^*)\,\,a_{mi}^\dagger\,a_{mi}
    =
  E^{QC-LSWT}+
  \frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij}} i, j} \,
  \,(E_{mdij}\,a_{mi}^\dagger\,a_{mi}+E_{mdij}^*\,a_{mi}\,a_{mi}^\dagger)

where

.. math::
  E^{QC-LSWT}=-\frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij} i, j}} \,E_{mdij}^*

is a quantum correction to the classical ground state
energy. Higher-order quantum corrections shall also appear from the bi-quadratic
piece of the Hamiltonian.
The on-site, hopping and off-diagonal energy terms can be expanded in higher
harmonics as follows

.. math::
  E_{mdij} =&\,
             S_j\,(\boldsymbol{f_i^s})^\dagger\,
             \boldsymbol{\tilde{J}_{mdij}^s}\,\boldsymbol{f_j^s} =
              \sum_{\nu=0,\pm 1,\pm 2}
              E_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
             \\\\
  T_{mdij} =&\,
             S_i^{1/2}\,S_j^{1/2}\,
            (\boldsymbol{p_i^s})^\dagger\,\boldsymbol{\tilde{J}_{mdij}^s}\,\boldsymbol{p_j^s}=
            \sum_{\nu=0,\pm 1,\pm 2}
              T_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
              \\\\
  \Delta_{mdij} =&\,
               S_i^{1/2}\,S_j^{1/2}\,
                  (\boldsymbol{p_i^s})^\dagger\,\boldsymbol{\tilde{J}_{mdij}^s}\,
                  \boldsymbol{t_j^s}\,=
                  \sum_{\nu=0,\pm 1,\pm 2}
                  \Delta_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

where the matrix elements are independent of the site :math:`m` now,

.. math::
  E_{dij}^\nu =&\,
        S_j\,(\boldsymbol{f_i^s})^\dagger\,\boldsymbol{\tilde{J}_{dij}^\nu}\,\boldsymbol{f_j^s}\\
  T_{dij}^\nu =&\,
        S_i^{1/2}\,S_j^{1/2}\,
            (\boldsymbol{p_i^s})^\dagger\,\boldsymbol{\tilde{J}_{dij}^\nu}\,\boldsymbol{p_j^s}\\
  \Delta_{dij}^\nu=&\,
        S_i^{1/2}\,S_j^{1/2}\,
                  (\boldsymbol{p_i^s})^\dagger\,\boldsymbol{\tilde{J}_{dij}^\nu}\,\boldsymbol{t_j^s}

Altogether, the LSWT Hamiltonian can be rewritten as a series summation of a conventional
LSWT term and higher harmonics as follows

.. math::
  {\cal H}^{LSWT}=E^{QC-LSWT}+\sum_{\nu=0,\pm 1,\pm 2}\, {\cal H^\nu}

with

.. math::
  {\cal H^\nu}=
    \frac{1}{2}\,\sum_{\boldsymbol{d_{ij}}, i, j} \,
   \Big(&
  \,E_{dij}^\nu\,{\cal E^\nu_{i}}+(E_{dij}^\nu\,{\cal E^\nu_{i}})^\dagger
  +T_{dij}^\nu\,{\cal T_{dij}^\nu} + (T_{dij}^\nu\,{\cal T_{dij}^\nu})^\dagger
  \\&+
  \Delta_{dij}^\nu\,{\cal D_{dij}^\nu}+(\Delta_{dij}^\nu\,{\cal D_{dij}^\nu})^\dagger
  \Big)

where

.. math::
  {\cal E_{mi}^\nu}=& \sum_m \big(a_{mi}^\dagger\,a_{mi}\,
     e^{i\,n\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\,\big)\\
  {\cal T_{dij}^\nu}=& \sum_m \big(a_{mi}^\dagger\,a_{m+d_{ij}\,j}
  \,e^{i\,n\,\boldsymbol{q}\cdot\boldsymbol{r_m}} \big)\\
  {\cal D_{dij}^\nu}=&\sum_m \big( a_{m+d_{ij}\,j}\,a_{mi} \,e^{i\,n\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\big)

Fourier-transformed Hamiltonian
===============================

The above Hamiltonian simplifies by Fourier-transforming the local
bosonic operators

.. math::
  a_{mi}=\dfrac{1}{\sqrt{M}}\,\sum_{k}\,a_{\boldsymbol{k} i}
  \,e^{i\,\boldsymbol{\boldsymbol{k}}\cdot\boldsymbol{r_m}}

and using the identity

.. math::
  \dfrac{1}{M}\sum_m e^{i\,(\pm(\boldsymbol{k'}\pm \boldsymbol{k})+
  \nu\,\boldsymbol{q})\cdot\boldsymbol{r_m}}
  =
  \delta_{\pm(\boldsymbol{k'}\pm \boldsymbol{k})+
  \nu\,\boldsymbol{q},\, \boldsymbol{G}}

where :math:`\boldsymbol{G}` is a reciprocal lattice vector.
Then the operators become

.. math::
  {\cal E_{mi}^\nu}=&\sum_k\,a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, i}\,
  \\
  {\cal T_{dij}^\nu}=&\sum_k\,a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}\,
  e^{i\,(\boldsymbol{k}+\boldsymbol{G}-\nu \boldsymbol{q})\cdot \boldsymbol{d_{ij}}}
  \\
  {\cal D_{dij}^\nu}=&\sum_k\,a_{\boldsymbol{k} i}\,a_{\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q}, j}\,
  e^{-i\,(\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q})\cdot \boldsymbol{d_{ij}}}

where :math:`\boldsymbol{G}` is chosen to bring sums bak to the First Brillouin zone.
:math:`\boldsymbol{G}` will be dropped henceforth, with the implicit understanding
that :math:`\boldsymbol{k}+\nu\,\boldsymbol{q}` summations must stay always inside
the Brillouin zone.

Each harmonic piece of the LSWT Hamiltonian can be written

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, \boldsymbol{d_{ij}}, i, j} \,
   \Big(&
  \,E_{dij}^\nu\,
  a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, i}
   +(\,E_{dij}^\nu\,
  a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, i})^\dagger\\
  &+T_{dij}^\nu\,a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}\,
  e^{i\,(\boldsymbol{k}+\boldsymbol{G}-\nu \boldsymbol{q})\cdot \boldsymbol{d_{ij}}}
  {\cal T_{dij}^\nu} + (T_{dij}^\nu)^*\,({\cal T_{dij}^\nu})^\dagger
  \\&+
  \Delta_{dij}^\nu\,{\cal D_{dij}^\nu}+(\Delta_{dij}^\nu)^*\,({\cal D_{dij}^\nu})^\dagger
  \Big)


.. dropdown:: First term

  .. include:: first-term.txt

.. dropdown:: Second term

  .. include:: second-term.txt

.. dropdown:: Third term

  .. include:: third-term.txt

.. dropdown:: Fourth term

  .. include:: fourth-term.txt

.. dropdown:: Fifth terms

  .. include:: fifth-term.txt

.. dropdown:: Sixth terms

  .. include:: sixth-term.txt

Now we organize the terms with respect to the parts of the exchange matrix:

.. math::
  H^{LSWT}
  =
  H^{LSWT}_0
  +
  H^{LSWT}_1
  +
  H^{LSWT}_2
  +
  H^{LSWT}_3
  +
  H^{LSWT}_4

and work with those terms separately:


.. include:: hamiltonian-organized-k.txt
