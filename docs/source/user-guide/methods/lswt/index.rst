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
  \frac{1}{2}\,\sum_{\boldsymbol{m,d_{ij}}, i, j} \,
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
             \sum_{\nu=0,\pm 1,\pm 2}\,(-S_j)\,\tilde{J}_{dij}^{f\nu,00}\,
              e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}=
              \sum_{\nu=0,\pm 1,\pm 2}
              E_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
             \\\\
  T_{mdij} =&\,
             (S_i\,S_j)^{1/2}\,
            \boldsymbol{\tilde{J}}_{dij}^{f,--}=
            \sum_{\nu=0,\pm 1,\pm 2}(S_i\,S_j)^{1/2}\,
            \tilde{J}_{dij}^{f\nu,--}
            e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}=
            \sum_{\nu=0,\pm 1,\pm 2}
              T_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
              \\\\
  \Delta_{mdij} =&\,
               (S_i\,S_j)^{1/2}\,
                  \boldsymbol{\tilde{J}}_{dij}^{f,+-}\,=
                  \sum_{\nu=0,\pm 1,\pm 2}\,
                  \tilde{J}_{dij}^{f\nu,+-}
                  \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}  =
                  \sum_{\nu=0,\pm 1,\pm 2}
                  \Delta_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

where the cell-independent matrix elements :math:`^{sf}\tilde{J}_{dij}^{\alpha\beta,\nu}` and have been
written out explicitly in this :ref:`section <user-guide_methods_matrix-elements>`.
Altogether, the LSWT Hamiltonian can be rewritten as a series summation of a conventional
LSWT term and higher harmonics as follows

.. math::
  {\cal H}^{LSWT}=&E^{QC-LSWT}+\sum_{\nu=0,\pm 1,\pm 2}\, {\cal H^\nu}\\
  E^{QC-LSWT}=&-\frac{M}{2}\,\sum_{\boldsymbol{d}_{ij},i,j} \,
  \left(E_{\boldsymbol{d}ij}^0+\delta_{\boldsymbol{q},0}\,
  (E_{\boldsymbol{d}ij}^1+E_{\boldsymbol{d}ij}^{-1}+E_{\boldsymbol{d}ij}^2+E_{\boldsymbol{d}ij}^{-2})\right)^*\\
  {\cal H^\nu}=&
    \frac{1}{2}\,\sum_{\boldsymbol{d_{ij}}, i, j} \,
   \Big(
  \,E_{dij}^\nu\,{\cal E}^{\nu,1}_{i}+(E_{dij}^\nu)^*\,{\cal E}^{\nu,2}_{i}
  +T_{dij}^\nu\,{\cal T}_{dij}^{\nu,1} + (T_{dij}^\nu)^*\,{\cal T}_{dij}^{\nu,2}
  +
  \Delta_{dij}^\nu\,{\cal D}_{dij}^{\nu,1}+(\Delta_{dij}^\nu)^*\,{\cal D}_{dij}^{\nu,2}
  \Big)

where

.. math::
  {\cal E}_i^{\nu,1}&=& \sum_m a_{mi}^\dagger\,a_{mi}\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\quad\quad
  {\cal E}_i^{\nu,2}&=& \sum_m a_{mi}\,a_{mi}^\dagger\,e^{-i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\\\\
  {\cal T}_{dij}^{\nu,1}&=& \sum_m a_{mi}^\dagger\,a_{m+d_{ij}\,j}\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\quad\quad
  {\cal T}_{dij}^{\nu,2}&=& \sum_m a_{mi}\,a_{m+d_{ij}\,j}^\dagger\,e^{-i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\\\\
  {\cal D}_{dij}^{\nu,1}&=&\sum_m  a_{mi}\,a_{m+d_{ij}\,j} \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\quad\quad
  {\cal D}_{dij}^{\nu,2}&=&\sum_m  a_{mi}^\dagger \,a_{m+d_{ij}\,j}^\dagger\,e^{-i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

The LSWT energy term :math:`E^{QC-LSWT}` is a quantum correction that must be added to the classical energy.
Further corrections arise from higher-order pieces of the Hamiltonian.

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
  {\cal E}_i^{\nu,1}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,a_{\boldsymbol{k} i}\,\quad\quad
  {\cal E}_i^{\nu,2}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}\,a_{\boldsymbol{k} i}^\dagger\\\\
  {\cal T}_{dij}^{\nu,1}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,a_{\boldsymbol{k} j}\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}\quad\quad
  {\cal T}_{dij}^{\nu,2}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}\,a_{\boldsymbol{k} j}^\dagger\,
  e^{-i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}
  \\\\
  {\cal D}_{dij}^{\nu,1}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}\,a_{\boldsymbol{k} j}\,
  e^{i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}\quad\quad
  {\cal D}_{dij}^{\nu,2}&=&\sum_k\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,a_{\boldsymbol{k} j}^\dagger\,
  e^{-i\,\boldsymbol{k}\cdot \boldsymbol{d_{ij}}}

where we have assumed that two operators :math:`a_{\boldsymbol{k}i}` and
:math:`a_{\boldsymbol{k+G},i}` destroy the same particle (or rather quasi-particle). We define now
the :math:`\boldsymbol{k}`-space onsite, hopping and pairing terms as follows

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

and define :math:`T_{ii}^\nu=\sum_j E_{ij}^\nu`. Then, extending the sum to include the
elements :math:`i=j`, the Hamiltonian is finally rewritten as

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, i, j} \,
   \Big(&
  T_{ij}^\nu(\boldsymbol{k})\,a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}^\dagger\,
  a_{\boldsymbol{k} j}\,+
   (T_{ij}^\nu(\boldsymbol{k}))^*\,  a_{\boldsymbol{k}+\nu\,\boldsymbol{q}, i}\,a_{\boldsymbol{k} j}^\dagger\,
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

where :math:`t` indicates transpose. The LSWT Hamiltonian can be written in compact form as follows

.. math::
  {\cal H}^{LSWT} &=E^{QC-LSWT}+
    \frac{1}{2}\,\sum_{\nu, \boldsymbol{k}}\,
    \left(B_{\boldsymbol{k}+\nu\,\boldsymbol{q}}^\dagger\,T^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +\tilde{B}_{\boldsymbol{k}+\nu\,\boldsymbol{q}}\,(T^\nu(\boldsymbol{k}))^*\,\tilde{B}_\boldsymbol{k}^\dagger
    +\tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}\,\Delta^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_\boldsymbol{k}^\dagger\,(\Delta^\nu(\boldsymbol{k})^\dagger\,
    \tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}^\dagger\right)\\
    &=E^{QC-LSWT}+
    \frac{1}{2}\,\sum_{\nu, \boldsymbol{k}}\,
    \left(B_{\boldsymbol{k}+\nu\,\boldsymbol{q}}^\dagger\,T^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +\tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}\,(T^{-\nu}(-\boldsymbol{k}))^*\,\tilde{B}_{-\boldsymbol{k}}^\dagger
    +\tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}\,\Delta^\nu(\boldsymbol{k})\,B_\boldsymbol{k}
    +B_\boldsymbol{k}^\dagger\,(\Delta^\nu(\boldsymbol{k})^\dagger\,
    \tilde{B}_{-(\boldsymbol{k}+\nu\,\boldsymbol{q})}^\dagger\right)

where :math:`T^\nu` and :math:`\Delta^\nu` are matrices comprising all the hopping and pairing matrix elements.

The final expression for the LSWT Hamiltonian highlights that higher harmonics generated by
the spiral spin arrangement introduces couplings among different reciprocal lattice vectors. In other
words, the LSWT Hamiltonian is not diagonal in reciprocal space. A way around to diagonalize the
Hamiltonian is to enlarge the pristine Brillouin Zone and define the Magnetic Brillouin Zone, that
will discussed next.
