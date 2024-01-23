.. _user-guide_methods_lswt:

************************
Linear Spin-Wave Theory
************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/operators.txt
  * .. include:: ../page-notations/spin-unit-vector-operator.txt
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
  (\boldsymbol{R}^{\dagger}(\theta_m)
  \boldsymbol{J_{ab}}(\vec{d}_{ab})
  \boldsymbol{R}(\theta_{m+d_{ab}}))^{\dagger}
  =
  \boldsymbol{R}^{\dagger}(\theta_{m+d_{ab}})
  \boldsymbol{J_{ab}}^{\dagger}(\vec{d}_{ab})
  \boldsymbol{R}(\theta_m)
  =
  \boldsymbol{R}^{\dagger}(\theta_{m+d_{ab}})
  \boldsymbol{J_{ba}}(\vec{d}_{ba})
  \boldsymbol{R}(\theta_m)


Hermicity
=========

Before we proceed with derivation let us demonstrate hermicity of the Hamiltonian.
The easiest way to do so is to write two entries of the same bond for arbitrary bond
and show that their sum is unchanged under the application of the hermitian conjugate.

We write the part of the Hamiltonian for the bond between atoms :math:`1` and :math:`2`,
with first atom being located in the unit cell :math:`0` and the second in the unit cell
:math:`0+d`. Then two entries of the bond are:

* :math:`1 \Rightarrow 2` (:math:`H_{12}`)

  - :math:`a = 1`
  - :math:`b = 2`
  - :math:`\vec{d}_{ab} = \vec{d}`
  - :math:`m = 0`
* :math:`2 \Rightarrow 1` (:math:`H_{21}`)

  - :math:`a = 2`
  - :math:`b = 1`
  - :math:`\vec{d}_{ab} = -\vec{d}`
  - :math:`m = 0+d`

.. dropdown:: Part of the Hamiltonian

  .. include:: hermicity-two-bond-part.txt

.. dropdown:: It's Hermitian conjugate

  .. include:: hermicity-two-bond-part-hc.txt

By comparison of two formulas above we see that :math:`H_{12}=H_{21}^{\dagger}`, therefore:

.. math::
  (H_{12} + H_{21})^{\dagger}
  =
  H_{12}^{\dagger} + H_{21}^{\dagger}
  =
  H_{21} + H_{12}
  =
  H_{12} + H_{21}

Therefor full Hamiltonian :math:`H^{LSWT}` is a sum of hermitian terms and is hermitian
by itself.














IGNORE

Finally, we separate the matrix into five terms as it will be convenient later:

.. include:: J-abmd-separation.txt

Fourier transformation
======================

In order to describe collective exitations we apply Fourier transformation to the local
bosonic operators :math:`\hat{a}_{ma}` and move to the collective bosonic operators
:math:`\hat{a}_{ka}`:

.. math::
  \hat{a}_{ma}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  \hat{a}_{ka}
  e^{i\vec{\vec{k}}\vec{r}_m}
  \\
  \hat{a}_{m+d_{ab},b}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  \hat{a}_{kb}
  e^{i(\vec{\vec{k}}\vec{r}_m+\vec{d}_{ab})}
  \\
  \hat{a}_{ma}^{\dagger}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  \hat{a}_{ka}^{\dagger}
  e^{-i\vec{\vec{k}}\vec{r}_m}
  \\
  \hat{a}_{m+d_{ab},b}^{\dagger}
  &=
  \dfrac{1}{\sqrt{M}}
  \sum_{k}
  \hat{a}_{kb}^{\dagger}
  e^{-i(\vec{\vec{k}}\vec{r}_m+\vec{d}_{ab})}

.. dropdown:: Details

  .. include:: fourier-hamiltonian-grouping-details.txt

.. include:: fourier-hamiltonian-grouping.txt

After we apply the rotated matrix separation to each term in the round parentheses
we end up with the number of the sums over :math:`m` of the following form:

.. math::
  \dfrac{1}{M}\sum_m e^{i(h(\vec{k}, \vec{k}^{\prime})+\tilde{h}(\vec{Q}))\vec{r}_m}

where :math:`h(\vec{k}, \vec{k}^{\prime})` and :math:`\tilde{h}(\vec{Q})` are corresponding functions of
the vectors.

As was discussed in the :ref:`classical energy <user-guide_methods_energy-classic_sum-over-m-condition>`
section the sums of this form can be simplified:

.. math::
  \dfrac{1}{M}\sum_m e^{i(h(\vec{k}, \vec{k}^{\prime})+\tilde{h}(\vec{Q}))\vec{r}_m}
  =
  \delta_{h(\vec{k}, \vec{k}^{\prime})+\tilde{h}(\vec{Q}), \vec{G}}

where :math:`\vec{G}` is a reciprocal lattice vector.


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
