.. _user-guide_methods_hp-bosons:

*************************
Holstein-Primakoff bosons
*************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/operators.txt
  * .. include:: ../page-notations/bra-ket.txt



In order to describe the excitations we will use Holstein-Primakoff (HP) bosons [1]_
for the ferromagnetic state in the :math:`uvn` reference frame.

Before we proceed to the transformation we need to mention the transition from the
spin-vectors to the spin-operators. We choose the direction of vector :math:`\boldsymbol{\hat{n}}`
of the :math:`uvn` basis as a quantization axis and substitute the vector
components of the spin with the corresponding spin operators:

.. math::

  \begin{pmatrix}
    S^u \\
    S^v \\
    S^n \\
  \end{pmatrix}
  \Rightarrow
  \begin{pmatrix}
    s^u \\
    s^v \\
    s^n \\
  \end{pmatrix}

Next, we write the HP transformation for the *ferromagnetic* ground state:

.. include:: ../repeated-formulas/hp-general-uvn.txt

In the following treatment we work with the terms with at most 4
creation/annihilation operators, therefore, we expand the square root up to the first
power of the :math:`1/S`, because already the :math:`1/S^2` gives the five-operator term:

.. include:: ../repeated-formulas/hp-expanded-uvn.txt

Next we write the vector of spin operators in the
:ref:`spherical reference frame <user-guide_methods_spherical-rf>`:

.. dropdown:: Details

  .. include:: spin-in-spherical-details.txt

.. math::
  &\langle u^+u^-n \vert s \rangle
  =
  \begin{pmatrix}
    \dfrac{s^-}{\sqrt{2}} \\
    \dfrac{s^+}{\sqrt{2}} \\
    s^n                   \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \sqrt{S}
    \cdot
    \left[
      a^{\dagger}
      -
      \dfrac{a^{\dagger}a^{\dagger}a}{4S}
    \right] \\
    \sqrt{S}
    \cdot \left[
      a
      -
      \dfrac{a^{\dagger}aa}{4S}
    \right] \\
    S - a^{\dagger}a \\
  \end{pmatrix}

Now we move on to the Hamiltonian in the
:ref:`spherical reference frame <user-guide_methods_spherical-rf>`:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any.txt

.. note::
  Before this section the parameters :math:`\boldsymbol{n}`, :math:`\theta_i`, :math:`\phi_i`,
  :math:`\boldsymbol{q}` were unknown. Starting from this section we assume that the ground
  state is known and we want to compute the low energy excitations to it.

and cast classical spin vectors to vector spin operators:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any-operators.txt

From this moment we focus on the exchange part of the Hamiltonian and work in the
spherical basis. We split the Hamiltonian into three parts as following:

.. math::
  {\cal H}^{exchange}
  =
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  \left[
  (\boldsymbol{s_{mi}^{ferro}})^{\dagger}
  \boldsymbol{R}^{\dagger}(\theta_i,\phi_i)
  \right]
  \left[
  \boldsymbol{R}^{\dagger}(\theta_m)
  \boldsymbol{J_{ij}}(\boldsymbol{d_{ij}})
  \boldsymbol{R}(\theta_{m+d_{ij}})
  \right]
  \left[
  \boldsymbol{R}(\theta_j,\phi_j)
  \boldsymbol{s_{m+d_{ij},j}^{ferro}}
  \right]
  \\=
  \dfrac{1}{2}
  \sum_{m, \boldsymbol{d_{ij}}, i, j}
  \left[
  (\boldsymbol{s_{mi}^{ferro}})^{\dagger}
  \boldsymbol{R}^{\dagger}(\theta_i,\phi_i)
  \right]
  \boldsymbol{\tilde{J}_{mdij}}
  \left[
  \boldsymbol{R}(\theta_j,\phi_j)
  \boldsymbol{s_{m+d_{ij},j}^{ferro}}
  \right]

Defining auxiliary vectors :math:`\boldsymbol{p_i}`, :math:`\boldsymbol{t_i}`, :math:`\boldsymbol{f_i}`
we rewrite the Hamiltonian as:

.. dropdown:: Details

  First we recall the rotation matrix in a spherical reference frame:

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.txt

  And define the vectors:

  .. include:: ptf-definition.txt

  Then:

  .. math::
    \begin{matrix}
      R(\theta_i,\phi_i)
      =
      \left(
        \boldsymbol{p_i},
        \boldsymbol{t_i},
        \boldsymbol{f_i}
      \right);
      &
      R(\theta_i,\phi_i)^{\dagger}
      =
      \begin{pmatrix}
        \boldsymbol{p_i}^{\dagger} \\
        \boldsymbol{t_i}^{\dagger} \\
        \boldsymbol{f_i}^{\dagger} \\
      \end{pmatrix}
    \end{matrix}

  Next, we rewrite the expressions in the square brackets:

  .. include:: square-brackets-rewrite-left.txt

  .. include:: square-brackets-rewrite-right.txt


.. include:: ../repeated-formulas/hamiltonian-hp-expansion-full.txt

.. dropdown:: Omitted terms

  .. include:: omitted-terms.txt

In the previous formula the terms are grouped with respect to the power of
:math:`1/S` if one would assume :math:`S_i = S_j = S`. Now we will separate them and
discuss each one in details:

.. math::

  {\cal H}^{exchange} = {\cal H}^{Cl} + {\cal H}^{LSWT} + {\cal H}^{Qubic} + {\cal H}^{Quatric}

* :ref:`Classical energy <user-guide_methods_energy-classic>`

  .. math::
    {\cal H}^{Cl}
    =
    \dfrac{1}{2}
    \sum_{m, \boldsymbol{d_{ij}}, i, j}
    S_iS_j
    \boldsymbol{f_i}^\dagger
    \boldsymbol{\tilde{J}_{mdij}}
    \boldsymbol{f_j}

* :ref:`Linear Spin Wave Theory <user-guide_methods_lswt>`

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-lswt-part.txt

* :ref:`Qubic terms <user-guide_methods_hp-cubic-terms>`

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-qubic-part.txt

* :ref:`Quartic terms <user-guide_methods_hp-quartic-terms>`

  .. include:: ../repeated-formulas/hamiltonian-hp-expansion-quartic-part.txt

.. important::
  We keep the indices of the spin numbers :math:`S_i` and :math:`S_j` for the derivation.
  If all atoms in the unit cell has the same
  spin number: :math:`S_i = S_j = S`, then the terms of the Hamiltonian from above
  belongs to the effects of the descending order (:math:`1`, :math:`1/S`,
  :math:`1/S^{3/2}`, :math:`1/S^2`, ...). However, if atoms in the unit cell have
  different spin numbers, then, for example, the order of some the qubic terms can
  be the same as of some terms of the LSWT terms and one should be cautious with the terms
  of the Hamiltonian to consider for the particular system.

References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
