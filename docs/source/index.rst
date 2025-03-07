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

In short magnopy computes bosonic Hamiltonian of the form

.. math::
    \mathcal{H}
    \approx
    \Bigl(
    E_0 + E_0^{(2)}
    \Bigr)
    +
    \sum_{\alpha}
    \sum_{\boldsymbol{k}\in 1^{st} BZ}
    \Delta_{\alpha}(\boldsymbol{k})
    +
    \sum_{\alpha}
    \sum_{\boldsymbol{k}\in 1^{st} BZ}
    \omega_{\alpha}(\boldsymbol{k})
    \Biggl(
    b^{\dagger}_{\alpha}(\boldsymbol{k})b_{\alpha}(\boldsymbol{k})
    +
    \dfrac{1}{2}
    \Biggr)
    +
    \dots

From the given spin Hamiltonian with the user-defined bosonic representation of spins.

* :math:`E_0` is a classical energy of the ground state.
* :math:`E_0^{(2)}` is a quantum correction to the ground state energy arising from the
  Linear Spin Wave Theory (LSWT).
* :math:`\omega_{\alpha}(\boldsymbol{k})` is magnon dispersion relation that is computed
  at the level of LSWT.
* ...
