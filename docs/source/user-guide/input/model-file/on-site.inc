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
  :lines: 44-55
  :language: text

.. dropdown:: Description

  * line 1: Section separator (10 or more ``=`` symbols)
  * line 2: One or two entries:

    - ``On-site`` keyword. Only the first letter is actually checked.
    - (optional) ``<Units>``. One of the predefined keywords.
      Defines the units of the on-site anisotropy parameters. Allowed values are

      - meV -  :math:`10^{-3}` electron-Volt (default)
      - eV -  electron-Volt
      - J - Joule
      - K - Kelvin
      - Ry - Rydberg units of energy

      Note: Only the first letter is actually checked.

  * line 3: Subsection separator (10 or more ``-`` symbols)
  * line 4-5: On-site anisotropy parameter for atom ``A1``, exactly two lines.

    - line 4: ``A1`` - atom's label. Have to be consistent with
      :ref:`user-guide_input_model-file_atoms` section.
    - line 5: ``Axx Ayy Azz Axy Axz Ayz`` - unique values of the anisotropy matrix.
      Six numbers, separated by spaces. They translates into the matrix form as:

      .. math::
        \boldsymbol{A}
        =
        \begin{pmatrix}
          A^{xx} & A^{xy} & A^{xz} \\
          A^{xy} & A^{yy} & A^{yz} \\
          A^{xz} & A^{yz} & A^{zz} \\
        \end{pmatrix}

  * line 6: Subsection separator (10 or more ``-`` symbols)
  * line 7: Specification of the anisotropy for other atom
  * line 8: Section separator (10 or more ``=`` symbols)

.. dropdown:: Examples

  Below we provide several ways to write the same on-site anisotropy.

  ::

    ==========
    On-site
    ----------
    A1
    1 0 0 0 0 0
    ----------
    ==========

  ::

    ==========
    On-site meV
    ----------
    A1
    1 0 0 0 0 0
    ----------
    ==========

  ::

    ==========
    On-site eV
    ----------
    A1
    0.001 0 0 0 0 0
    ----------
    ==========

  ::

    ==========
    On-site K
    ----------
    A1
    11.60451812 0 0 0 0 0
    ----------
    ==========

  ::

    ==========
    On-site Ry
    ----------
    A1
    7.349864435130999e-05 0 0 0 0 0
    ----------
    ==========

  ::

    ==========
    On-site J
    ----------
    A1
    1.6021766341182764e-22 0 0 0 0 0
    ----------
    ==========


.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :linenos:
  :lines: 1,2,45-55
  :language: text

.. dropdown:: Description

  All names of Datasets and Groups are lowercase.

  One Datasets is required:

  * "units" - one of the following: "meV", "eV", "Joule", "Kelvin", "Ry"

  One group is required:

  * "parameters"

    At least one group is required. Every group describe one parameter.
    Inside every group two Datasets are required:

    - "atom" - a string.
    - "matrix" - :math:`3\times3` matrix of numbers.
