Ground-state
============

This section is optional and contains the information about the ground state of the model.

.. code-block:: text
  :linenos:

  ==========
  Ground-state <Units>
  q1 q2 q3
  nx ny nz # or a<number> b<number>
  ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: Two entries, specifying the section type and the units for the spiral vector:

  - ``Ground-state`` keyword. Indicate the interpretation of the section.
    Only the first letter is actually checked.
  - (optional) ``<Units>``. Two types of the units are supported:

    - ``Relative`` (default). The :math:`\boldsymbol{q}` vector is given in the relative
      coordinates with respect to the reciprocal unit cell.
    - ``Absolute`` (default). The :math:`\boldsymbol{q}` vector is given in the absolute
      coordinates in Angstrom\ :math:`^{-1}` or Bohr\ :math:`^{-1}`, depending on the units of the
      lattice vectors from the :ref:`user-guide_input_model-file_cell` section.
* line 3: Three components of the spiral vector. Three numbers, separated by space.
* line 4: Direction of the global rotation axis. Can be provided in two ways:

  - Three numbers, separated by space: ``nx ny nz``. Only the direction is important.
    The modulus can be arbitrary, since the vector is converted to the unit one upon reading.
  - :math:`a\alpha` :math:`b\beta` - two strings, separated by space.
    Two angles, that define the direction of the global rotation axis as described
    :ref:`here <user-guide_methods_uvn-choice>`. The order can be arbitrary. Examples:

    - ``a90 b0``
    - ``b0 a90``
* line 5: Section separator (10 or more ``=`` symbols)
