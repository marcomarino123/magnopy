.. _user-guide_methods_energy-classic_spiral:

***********
Spiral case
***********

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: ../page-notations/reference-frame.inc
  * .. include:: ../page-notations/transpose-complex-conjugate.inc
  * .. include:: ../page-notations/exchange-tensor.inc


============
Spin vectors
============

First we recall the most general form of the spin vectors in :math:`(u\, v\, n)` basis:

.. include:: ../repeated-formulas/spin-from-ferro-uvn.inc

where

.. include:: ../repeated-formulas/full-azimuth-angle.inc

In the spiral case full expression of the spin vector remains unchanged.


============
Total energy
============

Considering :math:`\delta_{\boldsymbol{q}, \, \boldsymbol{G}} = 0` and
:math:`\delta_{\boldsymbol{2q}, \, \boldsymbol{G}} = 0` we get an expression for the
total energy of the true spiral state:

.. math::
  E^{SP}
  &=
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \Biggl[
    \cos\theta_i\, \cos\theta_j\, (J_{\boldsymbol{d}ij}^I + S^{nn}_{\boldsymbol{d}ij})
    +\\&\phantom{=\frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \sin\theta_j\,
    (
      J_{\boldsymbol{d}ij}^I
      -
      \dfrac{S^{nn}_{\boldsymbol{d}ij}}{2}
    )
    \cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij} + \phi_j - \phi_i)
    +\\&\phantom{=\frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \sin\theta_j\, D_{\boldsymbol{d}ij}^n
    \sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \Biggr]
  +\\&+
  \mu_B\,
  \sum_i\, g_i\, S_i\,
  h^n\, \cos\theta_i


========
Examples
========

# TODO

=====================
Minimization strategy
=====================

Let us rewrite the expression for the total energy, using following relations and using
the fact that isotropic part of the exchange matrix does not depend on the choice of
the basis.

.. math::
  D_{\boldsymbol{d}ij}^n
  =
  (\boldsymbol{D}_{\boldsymbol{d}ij}^{xyz})^\dagger\cdot\boldsymbol{\hat{n}}
  =
  \boldsymbol{\hat{n}}^\dagger\cdot \boldsymbol{D}_{\boldsymbol{d}ij}^{xyz}
  =
  D_{\boldsymbol{d}ij}^x\, \sin\alpha\, \cos\beta
  +
  D_{\boldsymbol{d}ij}^y\, \sin\alpha\, \sin\beta
  +
  D_{\boldsymbol{d}ij}^z\, \cos\alpha

.. math::
  S_{\boldsymbol{d}ij}^{nn}
  =
  \boldsymbol{\hat{n}}^\dagger\,
  \boldsymbol{J}_{\boldsymbol{d}ij}^{\boldsymbol{S},xyz}\,
  \boldsymbol{\hat{n}}
  =&\,
  S_{\boldsymbol{d}ij}^{xx}(\cos^2(\beta)\, \sin^2(\alpha) - \cos^2(\alpha))
  +\\&+
  S_{\boldsymbol{d}ij}^{yy}(\sin^2(\beta)\, \sin^2(\alpha) - \cos^2(\alpha))
  +\\&+
  S_{\boldsymbol{d}ij}^{xy}\, \sin^2(\alpha)\, \sin(2\beta)
  +\\&+
  S_{\boldsymbol{d}ij}^{xz}\, \cos(\beta)\, \sin(2\alpha)
  +\\&+
  S_{\boldsymbol{d}ij}^{yz}\, \sin(\beta)\, \sin(2\alpha)

.. math::

  h^n = \boldsymbol{h}^{xyz}\cdot \boldsymbol{\hat{n}}

Now we define a scalar:

.. math::
  E_I
  =
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  J_{\boldsymbol{d}ij}^{I}
  \Biggl[
    \cos\theta_i\, \cos\theta_j\,
    +
    \sin\theta_i\, \sin\theta_j\,
    \cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \Biggr]

a matrix:

.. math::
  \boldsymbol{E_S}
  =
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \boldsymbol{J}_{\boldsymbol{d}ij}^{\boldsymbol{S},xyz}
  \Biggl[
    \cos\theta_i\, \cos\theta_j\,
    -
    \dfrac{\sin\theta_i\, \sin\theta_j}{2}
    \cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \Biggr]


and two vectors:

.. math::
  \boldsymbol{E_D}
  =
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \boldsymbol{D}_{\boldsymbol{d}ij}^{xyz}
  \sin\theta_i\, \sin\theta_j\,
  \sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij} + \phi_j - \phi_i)

.. math::
  \boldsymbol{E_Z}
  =
  \mu_B\,
  \sum_i\, g_i\, S_i\,
  \boldsymbol{h}^{xyz}\, \cos\theta_i


and write energy in a simplified manner:

.. math::
  E^{SP}
  =
  E_I
  +
  \boldsymbol{\hat{n}}^\dagger\,
  \boldsymbol{E_S}\,
  \boldsymbol{\hat{n}}
  +
  \boldsymbol{\hat{n}}^\dagger
  \cdot
  \boldsymbol{E_D}
  +
  \boldsymbol{\hat{n}}^\dagger
  \cdot
  \boldsymbol{E_Z}

In order to minimize this equation we need to minimize the following expression

.. math::
  \boldsymbol{\hat{n}}^\dagger\,
  \boldsymbol{E_S}\,
  \boldsymbol{\hat{n}}
  +
  \boldsymbol{\hat{n}}^\dagger
  \cdot
  (\boldsymbol{E_D} + \boldsymbol{E_Z})

with respect to the direction of the unit vector :math:`\boldsymbol{\hat{n}}` for each
set of intracell angles :math:`\phi_i`, :math:`\theta_i`
