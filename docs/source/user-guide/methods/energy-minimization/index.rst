.. _user-guide_methods_energy-minimization:

************************************
Minimization of the classical energy
************************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/kronecker-delta.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc

Let us recall the expression for the classical energy:

.. include:: ../repeated-formulas/classic-total-energy.inc

In order to minimize this equation and find ground state we split all possible cases into
three distinct ones:

* :math:`\boldsymbol{q} = \boldsymbol{G}` - ferromagnetic alignment.
* :math:`\boldsymbol{q} = \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - antiferromagnetic cone.
* :math:`\boldsymbol{q} \ne \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - spiral state.

For each case the general equation is simplified and minimized. Then the true
ground state is defined by the comparison of the three obtained minimums.

Before we proceed to the detailed discussion about each of the three cases
let us recall the equation for the spin vector in the :math:`uvn`
reference frame:

.. include:: ../repeated-formulas/spin-uvn.inc

.. include:: ferromagnetic-case.inc

.. include:: afm-cone-case.inc

.. include:: spiral-case.inc

Minimization strategy
=====================

* We note, that for ferromagnetic case and antiferromagnetic cone case the choice of
  :math:`(uvn)` is arbitrary, therefore for those two cases we choose :math:`(uvn) = (xyz)`,
  which means that we do not need to minimize against :math:`\alpha` and :math:`\beta` angles.
* For the spiral case the minimization with respect to the angles :math:`\alpha` and :math:`\beta`
  (for any given set of other parameters) can be formulated as:

  .. math::
    \min_{||\boldsymbol{n}|| = 1}
    \left(
      \boldsymbol{n}^T
      \boldsymbol{C}
      \boldsymbol{n}
      +
      \boldsymbol{b}^T
      \boldsymbol{n}
    \right)

  Where matrix :math:`\boldsymbol{C}` and vector :math:`\boldsymbol{b}` are defined as

  .. math::
    \boldsymbol{C}
    =
    \dfrac{1}{2}
    \sum_{i, j, \boldsymbol{d_{ij}}}
    \boldsymbol{J_{ij}^S}(\boldsymbol{d_{ij}})
    S_iS_j
    \Biggl[
      \cos\theta_i\cos\theta_j
      -
      \sin\theta_i\sin\theta_j
      \cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
    \Biggr]

  .. math::
    \boldsymbol{b}
    =
    \dfrac{1}{2}
    \sum_{i, j, \boldsymbol{d_{ij}}}
    \boldsymbol{D_{ij}}(\boldsymbol{d_{ij}})
    S_iS_j
    \sin\theta_i\sin\theta_j
    \sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
