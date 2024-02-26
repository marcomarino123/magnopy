.. _user-guide_input_model-cone-axis:

Cone axis
=========

.txt file
---------

This section is optional and contains the information about the
cone axis, that describe the spiral ground state of the spin Hamiltonian.

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 21-24
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     Two blocks, separated by spaces, the order is fixed:

        * ``cone-axis`` keyword

          * Required
          * Full word is checked.

        * ``units``

          * Optional
          * Only first letter is actually checked
          * Recognized values:

            * ``relative`` (default)
              The :math:`\boldsymbol{n}` vector is given in the relative
              coordinates with respect to the unit cell:

              .. math::

                \boldsymbol{n}
                =
                n_x\boldsymbol{a}
                +
                n_y\boldsymbol{b}
                +
                n_z\boldsymbol{c}

            * ``absolute``
              The :math:`\boldsymbol{n}` vector is given in the absolute
              coordinates.

  3     Two or three blocks, separated by spaces.

        Direction of the cone axis :math:`\boldsymbol{\hat{n}}` (i.e. global rotation axis).

        * Required
        * Recognized combinations:

          * ``nx ny nz`` - direction of the cone axis. The modulus can be arbitrary,
            since the vector is converted to the unit one upon reading. If units are relative, then the
            cone axis is computed as:

            .. math::
              \boldsymbol{n} = n_x\boldsymbol{a_1}+n_y\boldsymbol{a_2}+n_z\boldsymbol{a_3}

            Otherwise it is just

            .. math::
              \boldsymbol{n} = (n^x,\,n^y\,n^z)^T

          * ``alpha beta`` - polar (:math:`\alpha`) and
            azimuthal (:math:`\beta`) angles of the cone axis. Two angles, that
            define the direction of the global rotation axis as described
            :ref:`here <user-guide_methods_uvn>`. The order is fixed.

            .. math::
              \boldsymbol{\hat{n}}
              =
              (\cos\beta\sin\alpha,\,\sin\beta\sin\alpha,\,\cos\alpha)^T

  4     Section separator (10 or more ``=`` symbols)
  ====  ========================================================================

.. dropdown:: Examples

  Below we list several ways to provide the same spiral vector and cone axis.
  The lattice is assumed to be :math:`\boldsymbol{a} = (1,0,0)^T`,
  :math:`\boldsymbol{b} = (0,2,0)^T`, :math:`\boldsymbol{c} = (0,0,3)^T`

  .. code-block:: text

    ==========
    Cone-axis
    0 1 0
    ==========

  .. code-block:: text

    ==================
    Cone-axis Relative
    0 0.5 0
    ==================

  .. code-block:: text

    ==========
    Cone-axis
    90 90
    ==========

.hdf5 file
----------


.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,31,54
  :language: text

.. dropdown:: Description

  All names of datasets and groups are lowercase.

  It is a dataset with three numbers.

  * Attributes

    * "units" - either "Relative" or "Absolute"
