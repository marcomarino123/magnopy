.. _user-guide_input_model-spiral-vector:

Spiral vector
=============

.txt file
---------

This section is optional and contains the information about the
spiral vector, that describe the spiral ground state of the spin Hamiltonian.

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 19-22
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     Two blocks, separated by spaces, the order is fixed:

        * ``spiral-vector`` keyword

          * Required.
          * Full word is checked, case-insensitive.

        * ``units``

          * Optional.
          * Only first letter is actually checked, case-insensitive.
          * Recognized values:

            * ``relative`` (default)
              The :math:`\boldsymbol{q}` vector is given in the relative
              coordinates with respect to the reciprocal unit cell.
            * ``absolute``
              The :math:`\boldsymbol{q}` vector is given in the absolute
              coordinates in Angstrom\ :math:`^{-1}` or Bohr\ :math:`^{-1}`,
              depending on the units of the lattice vectors from the
              :ref:`user-guide_input_model-file_cell` section.
              :math:`\boldsymbol{q} = (q^1,\,q^2,\,q^3)^T`

  3     Three numbers, separated by spaces, required. Components of the spiral vector.
  4     Section separator (10 or more ``=`` symbols)
  ====  ========================================================================

.. dropdown:: Examples

  Below we list several ways to provide the same spiral vector.
  The reciprocal lattice is assumed to be :math:`\boldsymbol{b_1} = (1,0,0)^T`,
  :math:`\boldsymbol{b_2} = (0,2,0)^T`, :math:`\boldsymbol{b_3} = (0,0,3)^T`

  .. code-block:: text

    =============
    Spiral-vector
    0.5 0.3 0
    =============

  .. code-block:: text

    ======================
    Spiral-vector Relative
    0.5 0.3 0
    ======================

  .. code-block:: text

    ======================
    Spiral-vector Absolute
    0.5 0.6 0
    ======================

.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,30,52
  :language: text

.. dropdown:: Description

  All names of datasets and groups are lowercase.

  Dataset's name: "spiral-vector".

  It is a dataset with three numbers.

  * Attributes

    * "units" - either "Relative" or "Absolute". Case-insensitive. Full word is
      checked.
