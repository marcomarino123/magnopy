.. _user-guide_methods_hp-bosons:

*************************
Holstein-Primakoff bosons
*************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/operators.txt
  * .. include:: ../page-notations/bra-ket.txt

Decomposition of spin operators into Holstein-Primakoff bosons
--------------------------------------------------------------
Magnopy considers spins in the local rotated spherical :math:`(\,u^+\,u^-\,n\,)`
reference frame where all those spins are collinear
(see :ref:`spherical reference frame <user-guide_methods_spherical-rf>`).
It then chooses :math:`\boldsymbol{\hat{n}}` as the quantization axis direction
and decomposes the quantum spin operator components in the spherical basis
in terms of Holstein-Primakoff (HP) bosons [1]_

.. include:: ../repeated-formulas/hp-general-spherical.txt

.. note::
  Note that the definition above departs slightly from convention, because
  :math:`{\cal S}^\pm` are divided by 2. The rationale behind this departure lies in
  the connection to the spherical basis, where :math:`\hat{S}^\pm` are unit vectors.

Expansion of the square roots above leads to an infinite series in :math:`1/S`,
that translates into the Heisenberg Hamiltonian. This :math:`1/S` expansion of the
Hamiltonian in truncated at :math:`1/S^2` order, where terms up to four-boson
products are kept. This can be easily shown to be equivalent to
truncating the square roots above at :math:`1/S` order

.. include:: ../repeated-formulas/hp-expanded-uvn.txt

Quantum Hamiltonian in the :math:`(\,u^+\,u^-\,n\,)` basis
----------------------------------------------------------
The quantum Heisenberg Hamiltonian looks exactly the same as its classical
counterpart, where all the classical spin vectors are replaced by quantum
spin vectors

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any.txt

.. note::
  The cone-state parameters :math:`\boldsymbol{n}`, :math:`\theta_i`, :math:`\phi_i`
  and :math:`\boldsymbol{q}` must be determined previously as explained
  :ref:`here <user-guide_methods_energy-minimization>`.
  This section assumes that those parameters are known already.

The exchange term in the Hamiltonian is split into three pieces as follows

.. math::
  {\cal H}^{exchange}
  =&
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  \left[
  (\boldsymbol{S_{mi}^s})^{\dagger}\,\boldsymbol{R_i}^{\dagger}\,\right]\,
  \left[\boldsymbol{R_m}^{\dagger}\,\boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})\,
  \boldsymbol{R_{m+d_{ij}}}\right]\,
  \left[\boldsymbol{R_j}\,\boldsymbol{S_{m+d_{ij},j}^s}\right]
  \\=&
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  (\boldsymbol{\tilde{S}_{mi}^s})^{\dagger}\,
  \boldsymbol{\tilde{J}_{mdij}}\,
  \boldsymbol{\tilde{S}_{m+d_{ij},j}^s}

where the rotated exchange tensor is

.. include:: ../repeated-formulas/exchange-matrix-spiral-rotated-uvn.txt

The expressions in the first and third square brackets are

.. include:: ../quantum-hamiltonian/square-brackets-rewrite-left.txt

.. include:: ../quantum-hamiltonian/square-brackets-rewrite-right.txt

The vectors :math:`\boldsymbol{p},\,\boldsymbol{t}` and :math:`\boldsymbol{f}`
result from splitting the intra-cell rotation matrix as follows

.. math::
    \begin{matrix}
      \boldsymbol{R_i}
      =\left(\boldsymbol{p_i}\,\boldsymbol{t_i}\,\boldsymbol{f_i}\right);
      &
      \boldsymbol{R_i}^\dagger=
      \begin{pmatrix}
        \boldsymbol{p_i}^{\dagger} \\
        \boldsymbol{t_i}^{\dagger} \\
        \boldsymbol{f_i}^{\dagger} \\
      \end{pmatrix}
    \end{matrix}

.. dropdown:: Details

  The rotation matrix in the spherical reference frame is

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.txt

  so that the above three vectors are

  .. include:: ../repeated-formulas/ptf-definition.txt

Hamiltonian splitting
---------------------
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
  S_i\,S_j\,\boldsymbol{f_i}^\dagger\,\boldsymbol{\tilde{J}_{mdij}}\,
  \boldsymbol{f_j}

* The :ref:`Linear Spin Wave Theory piece <user-guide_methods_lswt>` is

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.txt

* The piece containing :ref:`cubic terms <user-guide_methods_hp-cubic-terms>` is

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-qubic-part.txt

* And the piece containing :ref:`Quartic terms <user-guide_methods_hp-quartic-terms>` is

.. include:: ../repeated-formulas/hamiltonian-hp-expansion-quartic-part.txt


.. important::
  We keep the magnitude of each atomic spin :math:`S_i` in the above expressions.
  Note that if the unit cell spins have different spin magnitudes, then
  the expansion becomes anbiguous. For example, the magnitude of a cubic term
  could be similar to some terms at LSWT order, so one should judiciously
  evaluate which terms should be kept for a particular system of interest.

.. dropdown:: Omitted terms

  .. include:: omitted-terms.txt

References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
