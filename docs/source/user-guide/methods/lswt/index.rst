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

Now we focus on each term in the round parenthesis:

.. dropdown:: First term

  .. include:: sum-over-m-pa-pb.txt

.. dropdown:: Second term

  .. include:: sum-over-m-pa-tb.txt

.. dropdown:: Third term

  .. include:: sum-over-m-ta-pb.txt

.. dropdown:: Fourth term

  .. include:: sum-over-m-ta-tb.txt

.. dropdown:: Fifth and Sixth terms

  .. include:: sum-over-m-fa-fb.txt
