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

  and fulfills the hermiticity property

  .. math::
    ((\boldsymbol{R_m^s})^{\dagger}
    \boldsymbol{J_{ij}^s}(\boldsymbol{d_{ij}})
    \boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    =
    (\boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    (\boldsymbol{J_{ij}^s})^{\dagger}(\boldsymbol{d_{ij}})
    \boldsymbol{R_m^s}
    =
    (\boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    \boldsymbol{J_{ji}^s}(\boldsymbol{d_{ji}})
    \boldsymbol{R_m^s}

  Before we proceed with derivation let us demonstrate hermicity of the Hamiltonian.
  The easiest way to do so is to write two entries of the same bond for arbitrary bond
  and show that their sum is unchanged under the application of the hermitian conjugate.

  We write the part of the Hamiltonian for the bond between atoms
  :math:`1` and :math:`2`,
  with first atom being located in the unit cell :math:`0` and the second in
  the unit cell :math:`0+d`. Then two entries of the bond are:

  * :math:`1 \Rightarrow 2` (:math:`{\cal H}_{12}`)

    - :math:`a = 1`
    - :math:`b = 2`
    - :math:`\boldsymbol{d_{ij}} = \boldsymbol{d}`
    - :math:`m = 0`
  * :math:`2 \Rightarrow 1` (:math:`{\cal H}_{21}`)

    - :math:`a = 2`
    - :math:`b = 1`
    - :math:`\boldsymbol{d_{ij}} = -\boldsymbol{d}`
    - :math:`m = 0+d`

  Then

  .. include:: hermicity-two-bond-part.txt

  and

  .. include:: hermicity-two-bond-part-hc.txt

  By comparison of two formulas above we see that
  :math:`{\cal H}_{12}={\cal H}_{21}^{\dagger}`, therefore:

  .. math::
    ({\cal H}_{12} + {\cal H}_{21})^{\dagger}
    =
    {\cal H}_{12}^{\dagger} + {\cal H}_{21}^{\dagger}
    =
    {\cal H}_{21} + {\cal H}_{12}
    =
    {\cal H}_{12} + {\cal H}_{21}


Fourier transformation
======================
The LSWT Hamiltonian can be rearranged into a more convenient form
by noting that each bond is counted twice, and taking advantage of the
hermiticy relations for the exchange matrix :math:`\boldsymbol{\tilde{J}_{mdij}^s}`

.. math::
  {\cal H}^{LSWT}=
  \frac{1}{2}\,\sum_{m, \boldsymbol{d_{ij}}, i, j} \,
   \Big(&
  \,(E_{mdij}+E_{mdij}^*)\,a_{mi}^\dagger\,a_{mi}
  \\&+
  T_{mdij}\, a_{mi}^\dagger\,a_{m+d_{ij}\,j} +
  T_{mdij}^*\,a_{m+d_{ij}\,j}^\dagger\,a_{mi}
  \\&+
  \Delta_{mdij}\,b_{m+d_{ij}\,j}\,b_{mi} +
  \Delta_{mdij}^*\,b_{mi}^\dagger\,b_{m+d_{ij}\,j}^\dagger
  \Big)

where on-site, hopping and off-diagonal energy terms are

.. math::
  E_{mdij} =&
             S_j\,(\boldsymbol{f_i^s})^\dagger\,
             \boldsymbol{\tilde{J}_{mdij}^s}\,\boldsymbol{f_j^s}\,
             \\\\
  T_{mdij} =&
             S_i^{1/2}\,S_j^{1/2}\,
            (\boldsymbol{p_i^s})^\dagger\,
             \boldsymbol{\tilde{J}_{mdij}^s}\,
              \boldsymbol{p_j^s}
              \\\\
  \Delta_{mdij} =&
               S_i^{1/2}\,S_j^{1/2}\,
                  (\boldsymbol{p_i^s})^\dagger\,
                  \boldsymbol{\tilde{J}_{mdij}^s}\,
                  \boldsymbol{t_j^s}\,

In order to describe collective exitations we apply Fourier transformation to the local
bosonic operators :math:`a_{mi}` and move to the collective bosonic operators
:math:`a_{ka}`:

.. math::
  a_{mi}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  a_{ka}
  e^{i\boldsymbol{\boldsymbol{k}}\boldsymbol{r_m}}
  \\
  a_{m+d_{ij},j}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  a_{kb}
  e^{i(\boldsymbol{\boldsymbol{k}}\boldsymbol{r_m}+\boldsymbol{d_{ij}})}
  \\
  a_{mi}^{\dagger}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  a_{ka}^{\dagger}
  e^{-i\boldsymbol{\boldsymbol{k}}\boldsymbol{r_m}}
  \\
  a_{m+d_{ij},j}^{\dagger}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  a_{kb}^{\dagger}
  e^{-i(\boldsymbol{\boldsymbol{k}}\boldsymbol{r_m}+\boldsymbol{d_{ij}})}

.. dropdown:: Details

  .. include:: fourier-hamiltonian-grouping-details.txt

.. include:: fourier-hamiltonian-grouping.txt

After we apply the rotated matrix separation to each term in the round parentheses
we end up with the number of the sums over :math:`m` of the following form:

.. math::
  \dfrac{1}{M}\sum_m e^{i(h(\boldsymbol{k}, \boldsymbol{k}^{\prime})+\tilde{h}(\boldsymbol{q}))\boldsymbol{r_m}}

where :math:`h(\boldsymbol{k}, \boldsymbol{k}^{\prime})` and :math:`\tilde{h}(\boldsymbol{q})` are corresponding functions of
the vectors.

As was discussed in the :ref:`classical energy <user-guide_methods_energy-classic_sum-over-m-condition>`
section the sums of this form can be simplified:

.. math::
  \dfrac{1}{M}\sum_m e^{i(h(\boldsymbol{k}, \boldsymbol{k}^{\prime})+\tilde{h}(\boldsymbol{q}))\boldsymbol{r_m}}
  =
  \delta_{h(\boldsymbol{k}, \boldsymbol{k}^{\prime})+\tilde{h}(\boldsymbol{q}), \boldsymbol{G}}

where :math:`\boldsymbol{G}` is a reciprocal lattice vector.


Now we focus on each term of the sum separately:

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
