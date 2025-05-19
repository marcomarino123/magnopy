.. _user-guide_methods_energy-classic_ferromagnetic:

******************
Ferromagnetic case
******************

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

Since :math:`\boldsymbol{q} = \boldsymbol{G}`, then
:math:`\boldsymbol{q} \cdot \boldsymbol{r}_m = 2\pi n_m` and
:math:`\boldsymbol{q} \cdot \boldsymbol{d}_{ij} = 2\pi n_{ij}` always, where :math:`n_m`
and :math:`n_{ij}` are integers. Thus, the spin vectors do not depend on the index
:math:`m` and are given by

.. math::
  \boldsymbol{S}_{mi}
  =
  S_i
  \begin{pmatrix}
    \sin\theta_i\, \cos(\Delta\phi_{i}) \\
    \sin\theta_i\, \sin(\Delta\phi_{i}) \\
    \cos\theta_i
  \end{pmatrix}
  \equiv
  \boldsymbol{S}_{i}

.. note::
  Formally total azimuthal angle is given by
  :math:`\Delta\phi_i = \Delta\phi_i + \boldsymbol{G} \cdot \boldsymbol{r}_i`.
  Since :math:`\boldsymbol{r}_i` is not a lattice vector we can not just drop the term
  :math:`\boldsymbol{G} \cdot \boldsymbol{r}_i`. However, we can absorb it in the
  :math:`\Delta\phi_i` term if :math:`\boldsymbol{G} \ne \boldsymbol{0}` and consider
  :math:`\boldsymbol{G} = \boldsymbol{0}` (i.e. :math:`\boldsymbol{q} = \boldsymbol{0}`)
  in general.


One can see that the orientation of the spin vectors does not depend on the index of the
unit cell, therefore, this case is named as "ferromagnetic". Note, that the orientation
of the spins within each unit cell is arbitrary. It means that the spin alignment can
be quite rich and the word "ferromagnetic" only refers to the inter-cell order.


============
Total energy
============

Considering :math:`\delta_{\boldsymbol{q}, \, \boldsymbol{G}} = 1` and
:math:`\delta_{\boldsymbol{2q}, \, \boldsymbol{G}} = 1` we get an expression for the
total energy:

.. math::
  E^{FM}
  &=
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \Biggl[
    \cos\theta_i\, \cos\theta_j\, (J_{\boldsymbol{d}ij}^I + S^{nn}_{\boldsymbol{d}ij})
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \sin\theta_j\,
    \operatorname{Re}\left(
      J_{\boldsymbol{d}ij}^{++} e^{-i(\Delta\phi_j - \Delta\phi_i)}
      +
      J_{\boldsymbol{d}ij}^{+-} e^{i(\Delta\phi_j + \Delta\phi_i)}
    \right)
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \cos\theta_i\, \sin\theta_j\,
    \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+} e^{-i\Delta\phi_j}\right)
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \cos\theta_j\,
    \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\Delta\phi_i}\right)
  \Biggr]
  \\&+
  \mu_B\,
  \sum_i\, g_i\, S_i\,
  \Bigl[\,
    h^n\, \cos\theta_i\, +\,
    \sin\theta_i\,
    \left(h^u\, \cos\Delta\phi_i+h^v\, \sin\Delta\phi_i\, \right)
  \Bigr]

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

.. math::
  \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+} e^{-i\Delta\phi_j}\right)
  &=
  (J_{ij}^{nu}\,\cos\Delta\phi_j+J_{ij}^{nv}\,\sin\Delta\phi_j)
  \\
  \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\Delta\phi_i}\right)
  &=
  (J_{ij}^{un}\,\cos\Delta\phi_i+J_{ij}^{vn}\,\sin\Delta\phi_i)

========
Examples
========

# TODO

The different FM configurations can be obtained as follows:

* Spins aligned along the :math:`+\boldsymbol{\hat{z}}` axis.
  Then :math:`\theta_i=0` and :math:`\Delta\phi_i` is undefined (we set it to
  :math:`0`).
* Spins aligned along the :math:`-\boldsymbol{\hat{z}}` axis.
  Then :math:`\theta_i=\pi` and :math:`\Delta\phi_i` is undefined (we set it to
  :math:`0`).
* Spins lying in the XY-plane. Then :math:`\theta_i=\pi/2` and
  :math:`\Delta\phi_i` is arbitrary.

=====================
Minimization strategy
=====================

In case of the ferromagnetic energy the choice of the :math:`(\, u\, v\, n\, )`
reference frame is arbitrary, since the phase shift between the unit cells is zero, then
we can choose the :math:`\boldsymbol{\hat{n}}` axis to match the
:math:`\boldsymbol{\hat{z}}` axis.

Then, the ground state energy is found via numerical minimization with respect to
the :math:`2I` parameters: :math:`\theta_i`, :math:`\Delta\phi_i`, where :math:`i = 1, ..., I`
and :math:`I` is a number of atoms in the unit cell. The expression to minimize is:

.. math::
  E^{FM}
  &=
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\, S_j\,
  \Biggl[
    \cos\theta_i\, \cos\theta_j\,
    J_{\boldsymbol{d}ij}^{zz}
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \sin\theta_j\,
    \Bigl(
      J^{xx}_{\boldsymbol{d}ij}\, \cos\Delta\phi_i\, \cos\Delta\phi_j
      +
      J^{xy}_{\boldsymbol{d}ij}\, \cos\Delta\phi_i\, \sin\Delta\phi_j
      +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[\sin\theta_i\, \sin\theta_j\,(}+
      J^{yx}_{\boldsymbol{d}ij}\, \sin\Delta\phi_i\, \cos\Delta\phi_j
      +
      J^{yy}_{\boldsymbol{d}ij}\, \sin\Delta\phi_i\, \sin\Delta\phi_j
    \Bigr)
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \cos\theta_i\, \sin\theta_j\,
    (J_{ij}^{zx}\,\cos\Delta\phi_j+J_{ij}^{zy}\,\sin\Delta\phi_j)
    +\\&\phantom{=\frac{1}{2}\,\sum_{i,j,\boldsymbol{d}_{ij}}S_i\, S_j\,\Biggl[}+
    \sin\theta_i\, \cos\theta_j\,
    (J_{ij}^{xz}\,\cos\Delta\phi_i+J_{ij}^{yz}\,\sin\Delta\phi_i)
  \Biggr]
  \\&+
  \mu_B\,
  \sum_i\, g_i\, S_i\,
  \Bigl[\,
    h^z\, \cos\theta_i\, +\,
    \sin\theta_i\,
    \left(h^x\, \cos\Delta\phi_i+h^u\, \sin\Delta\phi_i\, \right)
  \Bigr]


in a compact form it is an initial Hamiltonian, written in the :math:`(\, x\, y\, z\, )`
reference frame:

.. math::
  E^{FM}
  =
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d}_{ij}}
  \boldsymbol{S}_i^T \cdot \boldsymbol{J}_{\boldsymbol{d}ij} \cdot \boldsymbol{S}_j
  +
  \mu_B\,
  \sum_i\, g_i\,
  \boldsymbol{h}^T \cdot \boldsymbol{S}_i
