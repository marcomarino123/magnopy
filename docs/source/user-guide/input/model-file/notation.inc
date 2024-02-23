.. _user-guide_input_model-file_notation:

Notation
========

.txt file
---------

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 11-17
  :language: text

.. dropdown:: Description

  * line 1: Section separator (10 or more ``=`` symbols)
  * line 2: ``Notation`` keyword. Only the first letter is actually checked.
  * line 3-6: Four notation properties. The order can be arbitrary, but all four have to
    be present (if your hamiltonian does not have on-site anisotropy, then just put 1).
    Each line has two entries, separated by spaces:

    - line 3: ``Double-counting`` keyword and boolean ``value``. True if both pairs
      :math:`(m,i;m^{\prime},j)` and :math:`(m^{\prime},j;m,i)` are included in the
      Hamiltonian. False otherwise.
    - line 4: ``Spin-normalized`` keyword and boolean ``value``. True if spin vectors
      are unit vectors (i.e. if spin value is effectively absorbed in the
      exchange/on-site anisotropy parameters). False otherwise.
    - line 5: ``Exchange-factor`` keyword and ``number``. Numerical factor, that is
      written before the sum over spin pair. Usually it is either :math:`1`, :math:`-1`,
      :math:`0.5` or :math:`-0.5`.
    - line 6: ``On-site-factor`` keyword and ``number``. Numerical factor, that is written
      before the sum over spins. Usually it is either :math:`1` or :math:`-1`.

    Note: Only the first letter is actually checked.

    Allowed values for boolean values are (case-insensitive, full word is checked):

    - False: ``false``, ``f``, ``0``, ``no``, ``n``
    - True: ``true``, ``t``, ``1``, ``yes``, ``y``


    For the detailed discussion about various notations of spin Hamiltonian go
    :ref:`here <user-guide_hamiltonian-notation>`.

.. dropdown:: Examples

  For the Hamiltonian from the user guide of magnopy

  .. include:: ../../methods/repeated-formulas/hamiltonian-on-site-separate-any-classic.inc

  The notation section can be written as

  ::

    ==========
    Notation
    Double counting = true
    Spin normalized = false
    Exchange factor = 0.5
    On-site factor  = 1
    ==========

  Below we list several notations and abstract isotropic exchange parameter and abstract
  on-site parameter (say Axx) for each notation. Every example describe the same
  Hamiltonian, i.e. the energy of the abstract system is the same.
  We assume spin value at both ends of the bond to be equal to 1.5.

  ::

    ==========
    # iso = 1
    # on-site = 1
    Notation
    Double counting = true
    Spin normalized = true
    Exchange factor = 1
    On-site factor  = 1
    ==========

  ::

    ==========
    # iso = 2
    # on-site = 1
    Notation
    Double counting = false
    Spin normalized = true
    Exchange factor = 1
    On-site factor  = 1
    ==========

  ::

    ==========
    # iso = 8/9
    # on-site = 2/3
    Notation
    Double counting = false
    Spin normalized = false
    Exchange factor = 1
    On-site factor  = 1
    ==========

  ::

    ==========
    # iso = -8/9
    # on-site = 2/3
    Notation
    Double counting = false
    Spin normalized = false
    Exchange factor = -1
    On-site factor  = 1
    ==========

  ::

    ==========
    # iso = -8/9
    # on-site = -2/6
    Notation
    Double counting = false
    Spin normalized = false
    Exchange factor = -1
    On-site factor  = -2
    ==========

  ::

    ==========
    # iso = -2
    # on-site = -1/2
    Notation
    Double counting = false
    Spin normalized = true
    Exchange factor = -1
    On-site factor  = -2
    ==========


.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,22-26,55
  :language: text

.. dropdown:: Description

  All names of Datasets and Groups are lowercase.

  Four Datasets are required:

  * "double counting" - either 0 or 1.
  * "spin-normalized" - either 0 or 1.
  * "exchange-factor" - one number.
  * "on-site-factor" - one number.
