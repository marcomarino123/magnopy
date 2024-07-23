.. _user-guide_methods_magnetic-BZ:

***********************
Magnetic Brillouin Zone
***********************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/exchange-tensor.inc

==========
Motivation
==========




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
