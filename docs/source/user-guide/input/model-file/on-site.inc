.. _user-guide_input_model-file_on-site:

On-site anisotropy parameters
=============================

Parameters of the on-site anisotropy part of the Hamiltonian:

.. math::
  \boldsymbol{S_i}
  \boldsymbol{A_{ii}}
  \boldsymbol{S_i}

.. literalinclude:: full-txt.inc
  :linenos:
  :lines: 47-58
  :language: text

.. dropdown:: Description

  ====  ========================================================================
  Line  Content
  ====  ========================================================================
  1     Section separator (10 or more ``=`` symbols)
  2     One or two blocks, the order is fixed:

        * ``on-site`` keyword

          * Required.
          * Full word is checked, case-insensitive.

        * ``units``

          * Optional.
          * Only first letter is actually checked, case-insensitive.
          * Recognized values:

            * ``meV`` -  :math:`10^{-3}` electron-Volt (default)
            * ``eV`` -  electron-Volt
            * ``J`` - Joule
            * ``K`` - Kelvin
            * ``Ry`` - Rydberg units of energy

          Defines the units of the exchange parameters.

  3     Subsection separator (10 or more ``-`` symbols)
  4-5   On-site anisotropy parameter for atom ``atom-1``, exactly two lines.

        * ``atom-1``

          * Required.
          * Have to be consistent with :ref:`user-guide_input_model-file_atoms` section.
          * Case-sensitive.

          Atom's name.

        * ``Axx Ayy Azz Axy Axz Ayz``

          * Six numbers, separated by spaces.
          * The order is fixed.

          Unique values of the anisotropy matrix.
          They translates into the matrix form as:

          .. math::
            \boldsymbol{A}
            =
            \begin{pmatrix}
              A^{xx} & A^{xy} & A^{xz} \\
              A^{xy} & A^{yy} & A^{yz} \\
              A^{xz} & A^{yz} & A^{zz} \\
            \end{pmatrix}

  6     Subsection separator (10 or more ``-`` symbols)
  7     Specifications of bonds
  8     Subsection separator (10 or more ``-`` symbols)
  9-10  Specification of the anisotropy for the last atom
  11    Subsection separator (10 or more ``-`` symbols)
  12    Section separator (10 or more ``=`` symbols)
  ====  ========================================================================

.. dropdown:: Examples

  Below we provide several ways to write the same on-site anisotropy.

  .. code-block:: text

    ===========
    On-site
    -----------
    A1
    1 0 0 0 0 0
    -----------
    ===========

  .. code-block:: text

    ===========
    On-site meV
    -----------
    A1
    1 0 0 0 0 0
    -----------
    ===========

  .. code-block:: text

    ===============
    On-site eV
    ---------------
    A1
    0.001 0 0 0 0 0
    ---------------
    ===============

  .. code-block:: text

    =====================
    On-site K
    ---------------------
    A1
    11.60451812 0 0 0 0 0
    ---------------------
    =====================

  .. code-block:: text

    ===============================
    On-site Ry
    -------------------------------
    A1
    7.349864435130999e-05 0 0 0 0 0
    -------------------------------
    ===============================

  .. code-block:: text

    ================================
    On-site J
    --------------------------------
    A1
    1.6021766341182764e-22 0 0 0 0 0
    --------------------------------
    ================================


.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,44-52
  :language: text

.. dropdown:: Description

  All names of datasets and groups are lowercase.

  Group's name: "on-site".

  * Attributes

    * "units" - one of the following: "milli-electron-Volt", "electron-Volt", "Joule", "Kelvin", "Rydberg". Case-insensitive. Full word is
      checked.

  * Groups

    * <number from 1 to n>

      Every group describes one on-site parameter.
      There may be no groups.
      Inside each group two datasets are required:

      * "atom" - a string.
      * "matrix" - :math:`3\times3` matrix of numbers.
