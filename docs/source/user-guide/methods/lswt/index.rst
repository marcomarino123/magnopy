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
  E^{QC-LSWT}+
  \frac{1}{2}\,\sum_{\boldsymbol{m,d_{ij}} i, j} \,
  \Big(&
  \,E_{mdij}\,a_{mi}^\dagger\,a_{mi}+E_{mdij}^*\,a_{mi}\,a_{mi}^\dagger
  \\
  &+T_{mdij}\, a_{mi}^\dagger\,a_{m+d_{ij}\,j} +
  T_{mdij}^*\,a_{m+d_{ij}\,j}^\dagger\,a_{mi}
  \\&+
  \Delta_{mdij}\,b_{m+d_{ij}\,j}\,b_{mi} +
  \Delta_{mdij}^*\,b_{mi}^\dagger\,b_{m+d_{ij}\,j}^\dagger
  \Big)

where

.. math::
  E^{QC-LSWT}=-\frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij} i, j}} \,E_{mdij}^*

is a quantum correction to the classical ground state
energy. Higher-order quantum corrections shall also appear from the bi-quadratic
piece of the Hamiltonian.
The on-site, hopping and off-diagonal parameters are expanded in
terms of higher harmonics as described :ref:`here <user-guide_methods_exchange-tensor>`

.. math::
  E_{mdij} =&\,
             -S_j\,\boldsymbol{\tilde{J}}_{dij}^{f,00} =
             \sum_{\nu=0,\pm 1,\pm 2}\,(-S_j)\,^{sf}\tilde{J}_{dij}^{00,\nu}\,
              e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
              \sum_{\nu=0,\pm 1,\pm 2}
              E_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
             \\\\
  T_{mdij} =&\,
             (S_i\,S_j)^{1/2}\,
            \boldsymbol{\tilde{J}}_{dij}^{f,--}=
            \sum_{\nu=0,\pm 1,\pm 2}(S_i\,S_j)^{1/2}\,
            ^{sf}\tilde{J}_{dij}^{--,\nu}
            e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}=
            \sum_{\nu=0,\pm 1,\pm 2}
              T_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}
              \\\\
  \Delta_{mdij} =&\,
               (S_i\,S_j)^{1/2}\,
                  \boldsymbol{\tilde{J}}_{dij}^{f,+-}\,=
                  \sum_{\nu=0,\pm 1,\pm 2}\,
                  ^{sf}\tilde{J}_{dij}^{+-,\nu}
                  \,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}  =
                  \sum_{\nu=0,\pm 1,\pm 2}
                  \Delta_{dij}^\nu\,e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}

where the cell-independent matrix elements :math:`^{sf}\tilde{J}_{dij}^{\alpha\beta,\nu}` and have been
written out explicitly in this :ref:`section <user-guide_methods_matrix-elements>`.
Altogether, the LSWT Hamiltonian can be rewritten as a series summation of a conventional
LSWT term and higher harmonics as follows

.. math::
  {\cal H}^{LSWT}=E^{QC-LSWT}+\sum_{\nu=0,\pm 1,\pm 2}\, {\cal H^\nu}

with

.. math::
  {\cal H^\nu}=
    \frac{1}{2}\,\sum_{\boldsymbol{d_{ij}}, i, j} \,
   \Big(&
  \,E_{dij}^\nu\,{\cal E^{\nu}_{i}}+(E_{dij}^\nu\,{\cal {E^{\nu}_{i}}})^\dagger
  +T_{dij}^\nu\,{\cal T_{dij}^\nu} + (T_{dij}^\nu\,{\cal T_{dij}^\nu})^\dagger
  \\&+
  \Delta_{dij}^\nu\,{\cal D_{dij}^\nu}+(\Delta_{dij}^\nu\,{\cal D_{dij}^\nu})^\dagger
  \Big)

where

.. math::
  {\cal E_i^{\nu 1}}=& \sum_m a_{mi}^\dagger\,a_{mi}\,
     e^{i\,\nu\,\boldsymbol{q}\cdot\boldsymbol{r_m}}\\
  {\cal E_i^{\nu 2}}=& \sum_m \,a_{mi}\,a_{mi}^\dagger\,
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
  {\cal E_i^{\nu}}=&\sum_k\,a_{\boldsymbol{k} i}^\dagger\,
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
the Brillouin zone. Inserting the operators back into the Hamiltonian harmonic pieces

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, i, j} \,
   \Big(&
  \,E_{ij}^\nu\,
  a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, i}
   +(\,E_{ij}^\nu)^*\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, i}
  \,a_{\boldsymbol{k} i}^\dagger
  \\&+
  T_{ij}^\nu\,a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}\,+
   (T_{ij}^\nu)^*\,  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}^\dagger\,
   a_{\boldsymbol{k} i}
  \\&+
  \Delta_{dij}^\nu\,a_{\boldsymbol{k} i}\,a_{\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q}, j}
  +(\Delta_{dij}^\nu)^*\,a_{\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q}, j}^\dagger
  \,a_{\boldsymbol{k} i}\dagger
  \Big)

with

.. math::
  E_{ij}^\nu =& \sum_{\boldsymbol{d_{ij}}} \,E_{dij}^\nu
  \\
  T_{ij}^\nu(\boldsymbol{k}) =& \sum_{\boldsymbol{d_{ij}}} \,T_{dij}^\nu\,
  e^{i\,(\boldsymbol{k}+\boldsymbol{G}-\nu \boldsymbol{q})\cdot \boldsymbol{d_{ij}}}
  \\
  \Delta_{ij}^\nu(\boldsymbol{k}) =&\sum_{\boldsymbol{d_{ij}}} \,\Delta_{dij}^\nu\,
     e^{-i\,(\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q})\cdot \boldsymbol{d_{ij}}}

By defining :math:`T_{ii}^\nu=\sum_j E_{ij}^\nu` the above Hamiltonian is finally rewritten as
and arranging all Hamiltonian matrix elements as

.. math::
  {\cal H}^\nu =
    \frac{1}{2}\,\sum_{\boldsymbol{k}, i, j} \,
   \Big(&
  T_{ij}^\nu\,a_{\boldsymbol{k} i}^\dagger\,
  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}\,+
   (T_{ij}^\nu)^*\,  a_{\boldsymbol{k}+\boldsymbol{G}-\nu\,\boldsymbol{q}, j}^\dagger\,
   a_{\boldsymbol{k} i}
  \\&+
  \Delta_{dij}^\nu\,a_{\boldsymbol{k} i}\,a_{\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q}, j}
  +(\Delta_{dij}^\nu)^*\,a_{\boldsymbol{k}+\boldsymbol{G}+\nu\,\boldsymbol{q}, j}^\dagger
  \,a_{\boldsymbol{k} i}\dagger
  \Big)

==========================
Harmonic block Hamiltonian
==========================
Block bosonic operators can be defined by grouping together all bosonic operators referring to
the :math:`I` atoms in a unit cell

.. math::
  B_\boldsymbol{k} =\begin{pmatrix} a_{\boldsymbol{k},1}\\a_{\boldsymbol{k},2}
         \\\vdots\\a_{\boldsymbol{k},I}\end{pmatrix}

and then arranging together particle and hole block boson operators

.. math::
  {\cal B}_\boldsymbol{k} =\begin{pmatrix} B_\boldsymbol{k}\\B_{-\boldsymbol{k}}^\dagger\end{pmatrix}

The final expression for the LSWT hamiltonian is

.. math::
  {\cal H}^{LSWT} =
    \frac{1}{2}\,\sum_{\nu, \boldsymbol{k}}\,
    {\cal B}_\boldsymbol{k}^\dagger\,
    \begin{pmatrix} T^\nu(\boldsymbol{k}) & \Delta^\nu(\boldsymbol{k})\\
                   (\Delta^\nu(\boldsymbol{k}))^\dagger & (T^\nu(-\boldsymbol{k}))^\dagger
    \end{pmatrix}\,
    {\cal B}_{\boldsymbol{k}+\nu \boldsymbol{q}+\boldsymbol{G} }

where

.. math::
  T^\nu(\boldsymbol{k})
         =&
          \begin{pmatrix}
          T^\nu_{11}(\boldsymbol{k}) &T^\nu_{12}(\boldsymbol{k})&\cdots&T^\nu_{1I}(\boldsymbol{k})\\
          T^\nu_{21}(\boldsymbol{k}) &T^\nu_{22}(\boldsymbol{k})&\cdots&T^\nu_{2I}(\boldsymbol{k})\\
          &&\cdots& \\
           T^\nu_{I1}(\boldsymbol{k}) &T^\nu_{I2}(\boldsymbol{k})&\cdots&T^\nu_{II}(\boldsymbol{k})
           \end{pmatrix}
        \\\\
  \Delta^\nu(\boldsymbol{k})=&
          \begin{pmatrix}
          \Delta^\nu_{11}(\boldsymbol{k}) &\Delta^\nu_{12}(\boldsymbol{k})&\cdots&\Delta^\nu_{1I}(\boldsymbol{k})\\
          \Delta^\nu_{21}(\boldsymbol{k}) &\Delta^\nu_{22}(\boldsymbol{k})&\cdots&\Delta^\nu_{2I}(\boldsymbol{k})\\
          &&\cdots& \\
           \Delta^\nu_{I1}(\boldsymbol{k}) &\Delta^\nu_{I2}(\boldsymbol{k})&\cdots&\Delta^\nu_{II}(\boldsymbol{k})
           \end{pmatrix}

.. dropdown:: Hopping mattrix elements

  .. include:: hopping.txt

.. dropdown:: Off-diagonal matrix elements

  .. include:: off-diagonal.txt
