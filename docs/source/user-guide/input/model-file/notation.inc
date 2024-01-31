Notation
========

.. code-block:: text
  :linenos:

  ==========
  Notation
  Double counting = value #  true or false
  Spin normalized = value #  true or false
  Exchange factor = value #  1 or -1 or 0.5 or any number
  On-site factor  = value #  1 or -1 or any number
  ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: ``Notation`` keyword. Indicate the interpretation of the section.
  Only the first letter is actually checked.
* line 3-6: Four notation properties. The order can be arbitrary, but all four have to
  be present (If you hamiltonian does not have on-site anisotropy, then just put 1).

  - Double counting. True if both pairs :math:`(m,i;m^{\prime},j)` and :math:`(m^{\prime},j;m,i)`
    are included in the Hamiltonian. False otherwise.
  - Spin normalized. True if spin vectors are unit vectors
    (i.e. if spin value is effectively absorbed in the exchange/on-site anisotropy parameters).
    False otherwise.
  - Exchange factor. Numerical factor, that is written before the sum over spin pair.
    Usually it is either :math:`1`, :math:`-1`, :math:`0.5` or :math:`-0.5`.
  - On-site factor. Numerical factor, that is written before the sum over spins.
    Usually it is either :math:`1` or :math:`-1`.

  For the detailed discussion about various notations of spin Hamiltonian go
  :ref:`here <user-guide_hamiltonian-notation>`.

  .. dropdown:: Example

    For the Hamiltonian from the user guide of magnopy

    #TODO

    The notation section can be written as

    .. code-block:: text

      ==========
      Notation
      Double counting = true
      Spin normalized = false
      Exchange factor = 0.5
      On-site factor  = 1
      ==========
