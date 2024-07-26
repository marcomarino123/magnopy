.. _user-guide_methods_rewritten-spinham:

**************************
Rewritten Spin Hamiltonian
**************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/exchange-tensor.inc

===========
Hamiltonian
===========

The Spin Hamiltonian is

.. math::
  H \,=\,H_{exc}+H_Z\,=\,
   \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
   \braket{\,S_{mi}\,|\, \boldsymbol{J}_{\boldsymbol{d}ij}\,|\, S_{m+d_{ij},j}\, }
   + \mu_B \sum_{m,i}\, g_i\,\braket{\,h\,|\, S_{mi}\,}

It is convenient to split the inter-cell rotation matrix from the spin vectors,
:math:`\ket{S_{mi}}=\boldsymbol{R_m}\,\ket{\tilde{S}_{mi}}`, as described
:ref:`here <user-guide_methods_single-q>`, and define a renormalized exchange
tensor

.. math::
  \boldsymbol{\tilde{J}}_{\boldsymbol{d}_{ij}}=
  \boldsymbol{R_m}^\dagger\,\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,\boldsymbol{R_{m+d_{ij}}}

Then,

.. math::
  H_{exc} \,=\,&
   \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}
   \braket{\,\tilde{S}_{mi}\,|\, \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,|\, \tilde{S}_{m+d_{ij},j}\, }\,=\,
    \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,
   ^{sf}\boldsymbol{\tilde{S}_{mi}}\,^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,
   ^{sf}\boldsymbol{\tilde{S}_{m+d_{ij},j}}\\
  H_Z  \,=\,&
     \mu_B \sum_{m,i}\, g_i\,\braket{\,h\,|\, \boldsymbol{R_m}\,|\,\tilde{S}_{mi}\,}
   \,=\, \mu_B \sum_{m,i}\, g_i\,^{sf}\boldsymbol{h}\, ^{sf}\boldsymbol{R_m}\,^{sf}\boldsymbol{\tilde{S}_{mi}}


The exchange tensor :math:`^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}` is described in the next section.
