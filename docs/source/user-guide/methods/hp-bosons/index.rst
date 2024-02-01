.. _user-guide_methods_hp-bosons:

*************************
Holstein-Primakoff bosons
*************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/operators.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc

Decomposition of spin operators into Holstein-Primakoff bosons
==============================================================
Magnopy considers spins in the local rotated spherical :math:`(\,u^+\,u^-\,n\,)`
reference frame where all those spins are collinear
(see :ref:`spherical reference frame <user-guide_methods_spherical-rf>`).
It then chooses :math:`\boldsymbol{\hat{n}}` as the quantization axis direction
and decomposes the quantum spin operator components in the spherical basis
in terms of Holstein-Primakoff (HP) bosons [1]_

.. include:: ../repeated-formulas/hp-general-spherical.inc

.. note::
  Note that the definition above departs slightly from convention, because
  :math:`{\cal S}^\pm` are divided by :math:`\sqrt{2}`. The rationale behind this
  departure lies in the connection to the spherical basis, where :math:`\hat{S}^\pm/\sqrt{2}`
  are unit vectors.

Expansion of the square roots above leads to an infinite series in :math:`1/S`,
that translates into the Heisenberg Hamiltonian. This :math:`1/S` expansion of the
Hamiltonian in truncated at :math:`1/S^2` order, where terms up to four-boson
products are kept. This can be easily shown to be equivalent to
truncating the square roots above at :math:`1/S` order

.. include:: ../repeated-formulas/hp-expanded-uvn.inc

==========================================================
Quantum Hamiltonian in the :math:`(\,u^+\,u^-\,n\,)` basis
==========================================================
Let us recall the quantum Hamiltonian in the spherical basis:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-spherical-quantum.inc

The exchange term in the Hamiltonian is split into three pieces as follows

.. math::
  {\cal H}^{exchange}
  =&
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  \left[
    (\boldsymbol{S_{mi}^s})^{\dagger}\,
    (\boldsymbol{R_i^s})^{\dagger}\,
  \right]\,
  \left[
    (\boldsymbol{R_m^s})^{\dagger}\,
    \boldsymbol{J_{ij}^s}(\boldsymbol{d_{ij}})\,
    \boldsymbol{R_{m+d_{ij}}^s}
  \right]\,
  \left[
    \boldsymbol{R_j^s}\,
    \boldsymbol{S_{m+d_{ij},j}^s}
  \right]
  \\=&
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  (\boldsymbol{\tilde{S}_{mi}^s})^{\dagger}\,
  \boldsymbol{\tilde{J}_{mdij}^s}\,
  \boldsymbol{\tilde{S}_{m+d_{ij},j}^s}

where the rotated exchange tensor is

.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-spherical.inc

The expressions in the first and third square brackets are

.. include:: square-brackets-rewrite-left.inc

.. include:: square-brackets-rewrite-right.inc

The vectors :math:`\boldsymbol{p_i^s},\,\boldsymbol{t_i^s}` and :math:`\boldsymbol{f_i^s}`
result from splitting the intra-cell rotation matrix as follows

.. math::
    \begin{matrix}
      \boldsymbol{R_i^s}
      =\left(\boldsymbol{p_i^s}\,\boldsymbol{t_i^s}\,\boldsymbol{f_i^s}\right);
      &
      (\boldsymbol{R_i^s})^\dagger=
      \begin{pmatrix}
        (\boldsymbol{p_i^s})^{\dagger} \\
        (\boldsymbol{t_i^s})^{\dagger} \\
        (\boldsymbol{f_i^s})^{\dagger} \\
      \end{pmatrix}
    \end{matrix}

.. dropdown:: Details

  The rotation matrix in the spherical reference frame is

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.inc

  so that the above three vectors are

  .. include:: ../repeated-formulas/ptf-definition.inc

=====================
Hamiltonian splitting
=====================
The exchange part of the Hamiltonian can be decomposed into different pieces
according to their order in a :math:`1/S` expansion by assuming that
:math:`S_i = S_j = S`. The different pieces also correspond to terms having
zero, two, three and four bosons fields. Terms containing more than four boson
terms are cut, that could be justified as dropping terms further than :math:`1/S^2`
in the conventional :math:`1/S` expansion.

.. math::
  {\cal H}^{exchange}=E^{Cl}+{\cal H}^{LSWT}
                      +{\cal H}^{Cubic}+{\cal H}^{Biquadratic}

* The :ref:`classical energy piece is <user-guide_methods_energy-classic>`

.. math::
  {\cal H}^{Cl}=\dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  S_i\,S_j\,(\boldsymbol{f_i^s})^\dagger\,\boldsymbol{\tilde{J}_{mdij}^s}\,
  \boldsymbol{f_j^s}

* The :ref:`Linear Spin Wave Theory (LSWT) piece <user-guide_methods_lswt>` is

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.inc

* The piece containing :ref:`cubic terms <user-guide_methods_hp-cubic-terms>` is

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-cubic-part.inc

* And the piece containing
  :ref:`biquadratic terms <user-guide_methods_hp-quartic-terms>` is

.. include:: ../repeated-formulas/hamiltonian-hp-expansion-biquadratic-part.inc


.. important::
  We keep the magnitude of each atomic spin :math:`S_i,\,S_j` in the above expressions.
  Note that if the unit cell spins have different spin magnitudes, then
  the :math:`1/S` expansion becomes anbiguous. For example, the magnitude of
  a cubic term
  could be similar to some terms at LSWT order, so one should judiciously
  evaluate which terms should be kept for a particular system of interest.

.. dropdown:: Omitted terms

  .. include:: omitted-terms.inc

==========
References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
