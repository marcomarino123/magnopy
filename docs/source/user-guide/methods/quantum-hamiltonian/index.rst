.. _user-guide_methods_quantum-hamiltonian:

*******************
Quantum Hamiltonian
*******************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/operators.txt
  * .. include:: ../page-notations/bra-ket.txt

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

.. include:: square-brackets-rewrite-left.txt

.. include:: square-brackets-rewrite-right.txt

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

  .. include:: ptf-definition.txt
