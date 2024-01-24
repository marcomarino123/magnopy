.. _user-guide_methods_lswt:

************************
Linear Spin-Wave Theory
************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/operators.txt
  * .. include:: ../page-notations/bra-ket.txt
  * .. include:: ../page-notations/kronecker-delta.txt


The part of Hamiltonian, which is discussed in this page is

.. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.txt

Rotated exchange matrices
=========================

Before we proceed with the solution of the Hamiltonian we take a close look at the rotated
exchange matrices:

.. include:: ../repeated-formulas/J-abmd-matrix-definition-any.txt

.. dropdown:: Relevant matrices in the spherical reference frame

    .. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.txt

    .. include:: ../repeated-formulas/exchange-matrix-spherical.txt

First of all we recall it's form in the
:ref:`spherical basis <user-guide_methods_spherical-rf>`:

.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-uvn.txt

Next we derive symmetry of the rotated exchange matrices.
We recall the symmetries of the exchange matrices:

.. include:: ../repeated-formulas/spinham-parameter-symmetries.txt

And then apply hermitian conjugate to the whole expression:

.. math::
  (\boldsymbol{R}^{\dagger}(\phi_m)
  \boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})
  \boldsymbol{R}(\phi_{m+d_{ij}}))^{\dagger}
  =
  \boldsymbol{R}^{\dagger}(\phi_{m+d_{ij}})
  \boldsymbol{J_{ij}}^{\dagger}(\boldsymbol{d_{ij}})
  \boldsymbol{R}(\phi_m)
  =
  \boldsymbol{R}^{\dagger}(\phi_{m+d_{ij}})
  \boldsymbol{J_{ji}}(\boldsymbol{d_{ji}})
  \boldsymbol{R}(\phi_m)


Hermicity
=========

Before we proceed with derivation let us demonstrate hermicity of the Hamiltonian.
The easiest way to do so is to write two entries of the same bond for arbitrary bond
and show that their sum is unchanged under the application of the hermitian conjugate.

We write the part of the Hamiltonian for the bond between atoms :math:`1` and :math:`2`,
with first atom being located in the unit cell :math:`0` and the second in the unit cell
:math:`0+d`. Then two entries of the bond are:

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

.. dropdown:: Part of the Hamiltonian

  .. include:: hermicity-two-bond-part.txt

.. dropdown:: It's Hermitian conjugate

  .. include:: hermicity-two-bond-part-hc.txt

By comparison of two formulas above we see that :math:`{\cal H}_{12}={\cal H}_{21}^{\dagger}`, therefore:

.. math::
  ({\cal H}_{12} + {\cal H}_{21})^{\dagger}
  =
  {\cal H}_{12}^{\dagger} + {\cal H}_{21}^{\dagger}
  =
  {\cal H}_{21} + {\cal H}_{12}
  =
  {\cal H}_{12} + {\cal H}_{21}

Therefor full Hamiltonian :math:`H^{LSWT}` is a sum of hermitian terms and is hermitian
by itself.














IGNORE

Finally, we separate the matrix into five terms as it will be convenient later:

.. include:: J-abmd-separation.txt

Fourier transformation
======================

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
