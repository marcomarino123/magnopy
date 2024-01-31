.. _user-guide_methods_quantum-hamiltonian:

*********************************
From classical to quantum picture
*********************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/uvn-or-spherical.inc

.. include:: page-notations/operators.inc

The transition from classical to quantum picture is done by the substitution of the
spin vector components with the corresponding spin vector operator components:

.. math::
  \boldsymbol{S_{mi}}
  \rightarrow
  \boldsymbol{{\cal S}_{mi}}

The quantum Heisenberg Hamiltonian looks exactly the same as its classical
counterpart, where all the classical spin vectors are replaced by quantum
spin vectors

.. include:: repeated-formulas/hamiltonian-main-from-ferro-any-quantum.inc

.. note::
  The cone-state parameters :math:`\boldsymbol{n}`, :math:`\theta_i`, :math:`\phi_i`
  and :math:`\boldsymbol{q}` must be determined previously as explained
  :ref:`here <user-guide_methods_energy-minimization>`.
  Starting from this section we assumes that those parameters are known already.
