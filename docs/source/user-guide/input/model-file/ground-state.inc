.. _user-guide_input_model-file_ground-state:

Ground-state
============

.txt file
---------

This section is optional and contains the information about the ground state of the model.

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 17-21
  :language: text

.. dropdown:: Description

  * line 1: Section separator (10 or more ``=`` symbols)
  * line 2: Two entries,separated by spaces:

    - ``Ground-state`` keyword. Only the first letter is actually checked.
    - (optional) ``<Units>``. One of the predefined keywords.
      Defines the units of the spiral vector. Allowed values are

      - ``Relative`` (default). The :math:`\boldsymbol{q}` vector is given in the relative
        coordinates with respect to the reciprocal unit cell.
        :math:`\boldsymbol{q} = q^1\boldsymbol{b_1}+q^2\boldsymbol{b_2}+q^3\boldsymbol{b_3}`
      - ``Absolute`` (default). The :math:`\boldsymbol{q}` vector is given in the absolute
        coordinates in Angstrom\ :math:`^{-1}` or Bohr\ :math:`^{-1}`, depending on the
        units of the lattice vectors from the :ref:`user-guide_input_model-file_cell` section.
        :math:`\boldsymbol{q} = (q^1,\,q^2,\,q^3)^T`

      Note: Only the first letter is actually checked.
  * line 3: Three numbers, separated by spaces. Components of the spiral vector.
  * line 4: Two or three entries, separated by spaces.
    Direction of the cone axis :math:`\boldsymbol{\hat{n}}` (i.e. global rotation axis).
    Can be provided in two ways:

    - ``nx ny nz`` - direction of the cone axis. The modulus can be arbitrary,
      since the vector is converted to the unit one upon reading.

      .. math::
        \boldsymbol{n^{direction}} &= (n^x,\,n^y\,n^z)^T

        \boldsymbol{\hat{n}} &= \dfrac{\boldsymbol{n^{direction}}}{n^{direction}}
    - :math:`a\alpha` :math:`b\beta` - polar (:math:`a\alpha`) and azimuthal (:math:`b\beta`)
      angles of the cone axis. Two angles, that define the direction of the global rotation
      axis as described :ref:`here <user-guide_methods_uvn>`.
      The order can be arbitrary. Examples:

      - ``a90 b0``
      - ``b0 a90``

      :math:`\boldsymbol{\hat{n}} = (\cos\beta\sin\alpha,\,\sin\beta\sin\alpha,\,\cos\alpha)^T`
  * line 5: Section separator (10 or more ``=`` symbols)

.. dropdown:: Examples

  Below we list several ways to provide the same spiral vector and cone axis.
  The reciprocal lattice is assumed to be :math:`\boldsymbol{b_1} = (1,0,0)^T`,
  :math:`\boldsymbol{b_2} = (0,2,0)^T`, :math:`\boldsymbol{b_3} = (0,0,3)^T`

  ::

    ==========
    Ground-state
    0.5 0.3 0
    0 1 0
    ==========

  ::

    ==========
    Ground-state Relative
    0.5 0.3 0
    a90 b90
    ==========

  ::

    ==========
    Ground-state Absolute
    0.5 0.6 0
    b90 a90
    ==========

.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,27-30,55
  :language: text

.. dropdown:: Description

  All names of Datasets and Groups are lowercase.

  Three Datasets are required:

  * "units" - either "Relative" or "Absolute"
  * "spiral-vector" - three numbers.
  * "cone-axis" - three numbers.
