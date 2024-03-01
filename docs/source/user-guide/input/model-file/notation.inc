.. _user-guide_input_model-file_notation:

Notation
========

.txt file
---------

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 12-18
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     ``notation`` keyword

        * Required.
        * Full word is checked, case-insensitive.

  3     Two blocks, separated by spaces, the order is fixed:

        * ``double-counting`` keyword

          * Required.
          * Only first letter is checked, case-insensitive.

          True if both pairs :math:`(m,i;m^{\prime},j)` and
          :math:`(m^{\prime},j;m,i)` are included in the Hamiltonian.

        * ``value``

          * Required.
          * Recognized values:

            * For ``True``: ``true``, ``t``, ``1``, ``yes``, ``y``
            * For ``False``: ``false``, ``f``, ``0``, ``no``, ``n``

  4     Two blocks, separated by spaces, the order is fixed:

        * ``spin-normalized`` keyword

          * Required.
          * Only first letter is checked, case-insensitive.

          True if spin vectors
          are unit vectors (i.e. if spin value is effectively absorbed in the
          exchange/on-site anisotropy parameters).

        * ``value``

          * Required.
          * Recognized values:

            * For ``True``: ``true``, ``t``, ``1``, ``yes``, ``y``
            * For ``False``: ``false``, ``f``, ``0``, ``no``, ``n``

  5     Two blocks, separated by spaces, the order is fixed:

        * ``exchange-factor`` keyword

          * Required.
          * Only first letter is checked, case-insensitive.

          Numerical factor, that is written before the sum over spin pair.
          Usually it is either :math:`1`, :math:`-1`, :math:`0.5`
          or :math:`-0.5`.

        * ``value``

          * Required.
          * One number.

  6     Two blocks, separated by spaces, the order is fixed:

        * ``on-site-factor`` keyword

          * Required.
          * Only first letter is checked, case-insensitive.

          Numerical factor, that is written before the sum over spins.
          Usually it is either :math:`1` or :math:`-1`.

        * ``value``

          * Required.
          * One number.

  7     Section separator (10 or more ``=`` symbols)
  ====  ========================================================================


  For the detailed discussion about various notations of spin Hamiltonian go
  :ref:`here <user-guide_hamiltonian-notation>`.

.. dropdown:: Examples

  For the Hamiltonian from the user guide of magnopy

  .. include:: ../../methods/repeated-formulas/hamiltonian-on-site-separate-any-classic.inc

  The notation section can be written as

  .. code-block:: text

    ======================
    Notation
    Double-counting  true
    Spin-normalized  false
    Exchange-factor  0.5
    On-site-factor   1
    ======================

  Below we list several notations and abstract isotropic exchange parameter and abstract
  on-site parameter (say Axx) for each notation. Every example describe the same
  Hamiltonian, i.e. the energy of the abstract system is the same.
  We assume spin value at both ends of the bond to be equal to 1.5.

  .. code-block:: text

    =====================
    # iso = 1
    # on-site = 1
    Notation
    Double-counting  true
    Spin-normalized  true
    Exchange-factor  1
    On-site-factor   1
    =====================

  .. code-block:: text

    ======================
    # iso = 2
    # on-site = 1
    Notation
    Double-counting  false
    Spin-normalized  true
    Exchange-factor  1
    On-site-factor   1
    ======================

  .. code-block:: text

    ======================
    # iso = 8/9
    # on-site = 2/3
    Notation
    Double-counting  false
    Spin-normalized  false
    Exchange-factor  1
    On-site-factor   1
    ======================

  .. code-block:: text

    ======================
    # iso = -8/9
    # on-site = 2/3
    Notation
    Double-counting  false
    Spin-normalized  false
    Exchange-factor  -1
    On-site-factor   1
    ======================

  .. code-block:: text

    ======================
    # iso = -8/9
    # on-site = -2/6
    Notation
    Double-counting  false
    Spin-normalized  false
    Exchange-factor  -1
    On-site-factor   -2
    ======================

  .. code-block:: text

    ======================
    # iso = -2
    # on-site = -1/2
    Notation
    Double-counting  false
    Spin-normalized  true
    Exchange-factor  -1
    On-site-factor   -2
    ======================


.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,25-29,54
  :language: text

.. dropdown:: Description

  All names of datasets and groups are lowercase.

  * Datasets

    * "double counting" - either 0 or 1.
    * "spin-normalized" - either 0 or 1.
    * "exchange-factor" - one number.
    * "on-site-factor" - one number.
