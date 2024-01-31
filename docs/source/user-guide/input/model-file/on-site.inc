On-site anisotropy parameters
=============================

Parameters of the on-site anisotropy part of the Hamiltonian:

.. math::
  \boldsymbol{S_i}
  \boldsymbol{A_{ii}}
  \boldsymbol{S_i}

.. code-block:: text
    :linenos:

    ==========
    On-site <Units>
    ----------
    A1
    Axx Ayy Azz Axy Axz Ayz
    ----------
    ...
    ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: One or two entries:

  - ``On-site`` keyword. Indicate the interpretation of the section.
    Only the first letter is actually checked.
  - (optional) ``<Units>``. One of the predefined units for the Hamiltonian parameters.
    Allowed keyword values are

    - meV -  :math:`10^{-3}` electron-Volt (default)
    - eV -  electron-Volt
    - J - Joule
    - K - Kelvin
    - Ry - Rydberg units of energy

    Note: Only the first letter is actually checked.

* line 3: Subsection separator (10 or more ``-`` symbols)
* line 4-5: On-site anisotropy parameter for atom ``A1``, exactly two lines.

  - line 4: Atom's label ``A1``. Have to be consistent with
    :ref:`user-guide_input_model-file_atoms` section.
  - line 5: Unique values of the anisotropy matrix. Six numbers, separated by spaces:
    ``Axx Ayy Azz Axy Axz Ayz``. It translates into the matrix form as:

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
