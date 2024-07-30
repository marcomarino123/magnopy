.. _user-guide_methods_lswt:

************************
Linear Spin-Wave Theory
************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/matrices.inc
  * .. include:: ../page-notations/quantum-operators.inc
  * .. include:: ../page-notations/bra-ket.inc

=================================
Bosonic tight-binding Hamiltonian
=================================

The LSWT Hamiltonian introduced :ref:`here <user-guide_methods_quantum-hamiltonian>`
can be rearranged into a tight-binding-like form

.. math::
  {\cal H}^{LSWT}
  =
  \frac{1}{2}\,\sum_{\boldsymbol{m,d_{ij}} i, j} \,
  \Big(&
  \,(E_{mdij}+E_{mdij}^*)\,a_{mi}^\dagger\,a_{mi}
  +T_{mdij}\, a_{mi}^\dagger\,a_{m+d_{ij}\,j} +
  T_{mdij}^*\,a_{mi}\,a_{m+d_{ij}\,j}^\dagger
  \\&+
  \Delta_{mdij}\,b_{m+d_{ij}\,j}\,b_{mi} +
  \Delta_{mdij}^*\,b_{mi}^\dagger\,b_{m+d_{ij}\,j}^\dagger
  \Big)

The on-site, hopping and off-diagonal parameters are expanded in
terms of higher harmonics as described :ref:`here <user-guide_methods_exchange-tensor>`

.. math::
  E_{mdij} =&\,
             -S_j\,\boldsymbol{\tilde{J}}_{dij}^{f,00} =
             \sum_{\nu=0,\pm 1,\pm 2}\,(-S_j)\,^{sf}\tilde{J}_{dij}^{f\nu,00}\,
              e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}=
              \sum_{\nu=0,\pm 1,\pm 2}
              E_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
             \\\\
  T_{mdij} =&\,
             (S_i\,S_j)^{1/2}\,
            \boldsymbol{\tilde{J}}_{dij}^{f,--}=
            \sum_{\nu=0,\pm 1,\pm 2}(S_i\,S_j)^{1/2}\,
            ^{sf}\tilde{J}_{dij}^{f\nu,--}
            e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}=
            \sum_{\nu=0,\pm 1,\pm 2}
              T_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
              \\\\
  \Delta_{mdij} =&\,
               (S_i\,S_j)^{1/2}\,
                  \boldsymbol{\tilde{J}}_{dij}^{f,+-}\,=
                  \sum_{\nu=0,\pm 1,\pm 2}\,
                  ^{sf}\tilde{J}_{dij}^{f\nu,+-}
                  \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}  =
                  \sum_{\nu=0,\pm 1,\pm 2}
                  \Delta_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

where the cell-independent matrix elements :math:`^{sf}\tilde{J}_{dij}^{\alpha\beta,\nu}` and have been
written out explicitly in this :ref:`section <user-guide_methods_matrix-elements>`.
Altogether, the LSWT Hamiltonian can be rewritten as a series summation of a conventional
LSWT term and higher harmonics as follows

.. math::
  {\cal H}^{LSWT}=&\frac{M}{2}\,\sum_i \,(T_{\boldsymbol{d}_{ij}=0,ii}^0)^*+
  \sum_{\nu=0,\pm 1,\pm 2}\, {\cal H^\nu}\\
  {\cal H^\nu}=&
    \frac{1}{2}\,\sum_{\boldsymbol{d_{ij}}, i, j} \,
   \Big(
  \,\left(E_{dij}^\nu+(E_{dij}^\nu)^*\right)\,{\cal E^{\nu}_{i}}
  +T_{dij}^\nu\,{\cal T_{dij}^\nu} + (T_{dij}^\nu\,{\cal T_{dij}^\nu})^\dagger
  +
  \Delta_{dij}^\nu\,{\cal D_{dij}^\nu}+(\Delta_{dij}^\nu\,{\cal D_{dij}^\nu})^\dagger
  \Big)

where

.. math::
  {\cal E_i^\nu}=& \sum_m a_{mi}^\dagger\,a_{mi}\,
     e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\\
  {\cal T_{dij}^\nu}=& \sum_m a_{mi}^\dagger\,a_{m+d_{ij}\,j}
  \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}} \\
  {\cal D_{dij}^\nu}=&\sum_m  a_{m+d_{ij}\,j}\,a_{mi} \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

===============================
Fourier-transformed Hamiltonian
===============================

The above Hamiltonian simplifies by Fourier-transforming the local
bosonic operators

.. math::
  a_{mi}=\dfrac{1}{\sqrt{M}}\,\sum_{k}\,a_{\boldsymbol{k} i}
  \,e^{i\,\boldsymbol{\boldsymbol{k}}\cdot\boldsymbol{r_m}}

where the wave-vectors belong to the reciprocal lattice, e.g.:
:math:`\boldsymbol{k}=\frac{k_1}{M_1}\,\boldsymbol{b}_1+\frac{k_2}{M_2}\,\boldsymbol{b}_2+\frac{k_3}{M_3}\,\boldsymbol{b}_3`, with :math:`k_i\,\in {\cal Z}`.
We assume now that the spiral wave-vector :math:`\boldsymbol{q}` also belongs also the
reciprocal lattice. Then, using the identity

.. math::
  \dfrac{1}{M}\sum_m e^{i\,(\pm(\boldsymbol{k'}\pm \boldsymbol{k})+
  \nu\,\boldsymbol{q})\cdot\boldsymbol{r_m}}
  =
  \delta_{\pm(\boldsymbol{k'}\pm \boldsymbol{k})+
  \nu\,\boldsymbol{q},\, \boldsymbol{G}}

where
:math:`\boldsymbol{G}=n_1\,\boldsymbol{b}_1+n_2\,\boldsymbol{b}_2+n_3\,\boldsymbol{b}_3`,
are wave vectors belonging to the Bravais reciprocal lattice, e. g.: :math:`k_i,\,\in {\cal Z}`.
Then the operators above become

.. math::
  {\cal E_i^{\nu}}=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,
  a_{\boldsymbol{k} i}\,
  \\
  {\cal T_{dij}^\nu}=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,
  a_{\boldsymbol{k} j}\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}
  \\
  {\cal D_{dij}^\nu}=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}\,a_{\boldsymbol{k} j}\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}

where we have assumed that two operators :math:`a_{\boldsymbol{k}i}` and
:math:`a_{\boldsymbol{k+G},i}` destroy the same particle (or rather quasi-particle).
Inserting the operators back into the Hamiltonian harmonic pieces, we find

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, i, j} \,
   \Big(&
  \,\left(E_{ij}^\nu\,+(E_{ij}^\nu)^*\right)
  a_{\boldsymbol{k}+\nu\,\boldsymbol{q},, i}^\dagger\,
  a_{\boldsymbol{k} i}
  +
  T_{ij}^\nu\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,
  a_{\boldsymbol{k} j}\,+
   (T_{ij}^\nu)^*\,  a_{\boldsymbol{k} j}^\dagger\,
   a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}
  \\&+
  \Delta_{dij}^\nu\,a_{-(\boldsymbol{k}+\nu\,\boldsymbol{q}), i}\,a_{\boldsymbol{k} j}
  +(\Delta_{dij}^\nu)^*\,a_{\boldsymbol{k} j}^\dagger
  \,a_{-(\boldsymbol{k}+\nu\,\boldsymbol{q}), i}^\dagger
  \Big)

with

.. math::
  E_{ij}^\nu =& \sum_{\boldsymbol{d_{ij}}} \,E_{dij}^\nu=(-S_j)\,\sum_{\boldsymbol{d_{ij}}}\,
  \tilde{J}_{dij}^{f\nu,00}
  \\
  T_{ij}^\nu(\boldsymbol{k}) =& \sum_{\boldsymbol{d_{ij}}} \,T_{dij}^\nu\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}
  =(S_i\,S_j)^{1/2}\,\sum_{\boldsymbol{d_{ij}}}\,\tilde{J}_{dij}^{f\nu,--}\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}
  \\
  \Delta_{ij}^\nu(\boldsymbol{k}) =&\sum_{\boldsymbol{d_{ij}}} \,\Delta_{dij}^\nu\,
     e^{-i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}=
     (S_i\,S_j)^{1/2}\,\sum_{\boldsymbol{d_{ij}}}\,\tilde{J}_{dij}^{f\nu,+-}\,
     e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}

By defining :math:`T_{ii}^\nu=\sum_j E_{ij}^\nu` and extending the sum to include the
elements :math:`i=j`, the above Hamiltonian is finally rewritten as
and arranging all Hamiltonian matrix elements as

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, i, j} \,
   \Big(&
  T_{ij}^\nu(\boldsymbol{k})\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,
  a_{\boldsymbol{k} j}\,+
   (T_{ij}^\nu(\boldsymbol{k}))^*\,  a_{\boldsymbol{k} j}^\dagger\,
   a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}
  \\&+
  \Delta_{dij}^\nu(\boldsymbol{k})\,a_{-(\boldsymbol{k}+\nu\,\boldsymbol{q}), i}\,a_{\boldsymbol{k} j}
  +(\Delta_{dij}^\nu(\boldsymbol{k}))^*\,a_{\boldsymbol{k} j}^\dagger
  \,a_{-(\boldsymbol{k}+\nu\,\boldsymbol{q}), i}^\dagger
  \Big)

WARNING: I CANNOT FIND MY NOTES FOR THE EQUATIONS BELOW, CANNOT CHECK THEM NOW!!!

.. dropdown:: Hopping matrix elements

  .. include:: hopping.txt

.. dropdown:: Off-diagonal matrix elements

  .. include:: off-diagonal.txt

==========================
Harmonic block Hamiltonian
==========================
Block bosonic operators can be defined by grouping together all bosonic operators referring to
the :math:`I` atoms in a unit cell

.. math::
  B_\boldsymbol{k} =\begin{pmatrix} a_{\boldsymbol{k},1}\\a_{\boldsymbol{k},2}
         \\\vdots\\a_{\boldsymbol{k},I}\end{pmatrix},\,\,\,\tilde{B}_\boldsymbol{k}=B_\boldsymbol{k}^t

where :math:`t` indicates transpose. The Hamiltonian can be written in compact form as follows

.. math::
  {\cal H}^{LSWT} &=\frac{M}{2}\,\sum_i \,T_{\boldsymbol{d}_{ij}=0}^0+
    \frac{1}{2}\,\sum_{\nu, \boldsymbol{k}}\,
    \left(B_{\boldsymbol{k}+\nu\,\boldsymbol{q}}^\dagger\,T^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_\boldsymbol{k}^\dagger\,(T^\nu(\boldsymbol{k}))^\dagger\,B_{\boldsymbol{k}+\nu\,\boldsymbol{q}}
    +\tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}\,\Delta^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_\boldsymbol{k}^\dagger\,(\Delta^\nu(\boldsymbol{k})^\dagger\,
    \tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}^\dagger\right)\\
    &=E^{QC-LSWT}+
    \frac{1}{2}\,\sum_{\nu, \boldsymbol{k}}\,
    \left(B_{\boldsymbol{k}+\nu\,\boldsymbol{q}}^\dagger\,T^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_{-\boldsymbol{k}}^\dagger\,(T^{-\nu}(-\boldsymbol{k}))^\dagger\,B_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}
    +\tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}\,\Delta^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_\boldsymbol{k}^\dagger\,(\Delta^\nu(\boldsymbol{k})^\dagger\,
    \tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}^\dagger\right)

where :math:`T^\nu` and :math:`\Delta^\nu` are matrices comprising all the hopping and pairing matrix elements.
The LSWT energy term

.. math::
  E^{QC-LSWT}= -\frac{1}{2}\,\sum_{\boldsymbol{k}}\,T^0(\boldsymbol{k})

is a quantum correction that must be added to the classical energy. Further corrections arise from
higher-order pieces of the Hamiltonian.

The final expression for the LSWT Hamiltonian highlights that higher harmonics generated by
the spiral spin arrangement introduces couplings among different reciprocal lattice vectors. In other
words, the LSWT Hamiltonian is not diagonal in reciprocal space. A way around to diagonalize the
Hamiltonian is to enlarge the pristine Brillouin Zone and define the Magnetic Brillouin Zone, that
will discussed next.
