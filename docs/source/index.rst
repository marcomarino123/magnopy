*******
Magnopy
*******

.. toctree::
    :maxdepth: 1
    :hidden:

    User Guide <user-guide/index>
    api/index
    support
    contribute/index
    cite

:Release: |version|
:Date: |release_date|

**Useful links**:
`Issue Tracker <https://github.com/magnopy/magnopy/issues>`_ |
:ref:`Cite us <cite>` |
:ref:`support`

In short, given :ref:`user-guide_theory-behind_spin-hamiltonian` in **any**
:ref:`notation <user-guide_theory-behind-notation>` magnopy computes bosonic Hamiltonian
of the form

.. include:: core-formulas/bosonic-hamiltonian.inc

where

* :math:`E_0` is a classical energy of the ground state.
* :math:`E_0^{(2)}` is a quantum correction to the ground state energy arising from the
  Linear Spin Wave Theory (LSWT).
* :math:`\omega_{\alpha}(\boldsymbol{k})` is magnon dispersion relation that is computed
  at the level of LSWT.
* ...
