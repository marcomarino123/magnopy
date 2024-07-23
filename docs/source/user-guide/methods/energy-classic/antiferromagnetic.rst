.. _user-guide_methods_energy-classic_antiferromagnetic:

**********************
Antiferromagnetic case
**********************

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


In the antiferromagnetic case we have
:math:`\boldsymbol{q} = \boldsymbol{G} \ne \boldsymbol{G}/2`,
therefore, product with the lattice vectors would have the form:

One can always write :math:`q` in a basis of reciprocal lattice vectors:

.. math::
  \boldsymbol{q}
  =
  \dfrac{n_1\boldsymbol{b}_1}{2}
  +
  \dfrac{n_2\boldsymbol{b}_2}{2}
  +
  \dfrac{n_3\boldsymbol{b}_3}{2}

Then, we can write any lattice vector (as well as any :math:`\boldsymbol{d}_ij`) in a
basis of lattice vectors:

.. math::
  \boldsymbol{r}_m
  =
  m_1\boldsymbol{a}_1
  +
  m_2\boldsymbol{a}_2
  +
  m_3\boldsymbol{a}_3

Then the scalar products will have the form:


.. math::

  \boldsymbol{q} \cdot \boldsymbol{r}_m
  =
  \boldsymbol{q} \cdot \boldsymbol{d}_{ij}
  =
  \pi (n_1m_1 + n_2m_2 + n_3m_3)

Those scalar product enters in the expression under the harmonic functions, therefore
we can always add arbitrary amount of :math:`2\pi`. That means that it is enough to
consider :math:`n_i = \{-1,0,1\}` as if :math:`|n_i| > 2`, then it is either even and
results in the phase proportional to :math:`2\pi` or odd and can be written as
:math:`n_i^{\prime} + 1`, where :math:`n_i^{\prime}` is even or zero, therefore, gives
phase proportional to :math:`2\pi` and this case is equivalent to the :math:`n_i = 1`.

Finally, we only need to test 26 sets of :math:`n_i` (the one where all equals to zero
falls into the :ref:`user-guide_methods_energy-classic_ferromagnetic`). Effectively we
restrict the q vector to the first Brillouin zone.

One should note, that for :math:`\boldsymbol{r}_i` the :math:`\boldsymbol{q}` vector
from the first and second Brillouin zone are not equivalent. However, since we would
minimize with respect to arbitrary :math:`\Delta\phi_i`, then we can assume the
difference to be absorbed there.


The spin vectors would have the form

.. math::
  \boldsymbol{S}_{mi}
  =
  S_i
  \begin{pmatrix}
    (-1)^{mod(n_m,2)}\sin\theta_i\, \cos\Delta\phi_i \\
    (-1)^{mod(n_m,2)}\sin\theta_i\, \sin\Delta\phi_i \\
    \cos\theta_i
  \end{pmatrix}

Note, that the spin arrangement is not fully antiferromagnetic, it rather resembles an
"antiferromagnetic cone".


============
Total energy
============

For the total energy only :math:`E^{(0)}` and :math:`E^{(2)}` contribute:

.. math::
  E^{AFM}
  &=
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \Biggl[
    \cos\theta_i\, \cos\theta_j\, (J_{\boldsymbol{d}ij}^I + S^{nn}_{\boldsymbol{d}ij})
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \sin\theta_j\,
    (-1)^{mod(n_{ij},2)}
    \operatorname{Re}\left(
      J_{\boldsymbol{d}ij}^{++} e^{-i(\Delta\phi_j - \Delta\phi_i)}
      +
      J_{\boldsymbol{d}ij}^{+-} e^{i(\Delta\phi_j + \Delta\phi_i)}
    \right)
  \Biggr]
  \\&+
  \mu_B\,
  \sum_i\, g_i\, S_i\, h^n\, \cos\theta_i


with

.. math::
  \operatorname{Re}\left(
      J_{\boldsymbol{d}ij}^{++} e^{-i(\Delta\phi_j - \Delta\phi_i)}
      +
      J_{\boldsymbol{d}ij}^{+-} e^{i(\Delta\phi_j + \Delta\phi_i)}
  \right)
  &=
  J^{uu}_{\boldsymbol{d}ij}\, \cos\Delta\phi_i\, \cos\Delta\phi_j
  +
  J^{uv}_{\boldsymbol{d}ij}\, \cos\Delta\phi_i\, \sin\Delta\phi_j
  +\\&+
  J^{vu}_{\boldsymbol{d}ij}\, \sin\Delta\phi_i\, \cos\Delta\phi_j
  +
  J^{vv}_{\boldsymbol{d}ij}\, \sin\Delta\phi_i\, \sin\Delta\phi_j


========
Examples
========

#TODO


=====================
Minimization strategy
=====================

Numerical minimization with respect to the :math:`2+2I` parameters for 25 discrete
cases.
