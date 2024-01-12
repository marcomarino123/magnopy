.. _user-guide_methods_hp-bosons:

*************************
Holstein-Primakoff bosons
*************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/parentheses.txt
  * .. include:: page-notations/operators.txt
  * .. include:: page-notations/spin-unit-vector-operator.txt
  * .. include:: page-notations/bra-ket.txt



In order to describe the excitations we will use Holstein-Primakoff (HP) bosons [1]_
for the ferromagnetic state in the :math:`uvn` reference frame.

Before we proceed to the transformation we need to mention the transition from the
spin-vectors to the spin-operators. We choose the direction of vector :math:`\hat{n}`
of the :math:`uvn` basis as a quantization axis and substitute the vector
components of the spin with the corresponding spin operators:

.. math::

  \begin{pmatrix}
    \vec{S}_u \\
    \vec{S}_v \\
    \vec{S}_n \\
  \end{pmatrix}
  \Rightarrow
  \begin{pmatrix}
    \hat{s}_u \\
    \hat{s}_v \\
    \hat{s}_n \\
  \end{pmatrix}

Next, we write the HP transformation:

.. include:: repeated-formulas/hp-general-uvn.txt

In the following treatment we work with the terms with at most 4
creation/annihilation operators, therefore, we expand the square root up to the first
power of the :math:`1/S`, because already the :math:`1/S^2` gives the five-operator term:

.. include:: repeated-formulas/hp-expanded-uvn.txt

Now we write the vector of spin operators in the
:ref:`spherical reference frame <user-guide_methods_spherical-rf>`:

.. dropdown:: Details

  First we recall the transformation matrix:

  .. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

  .. math::
    &\langle u^+u^-n \vert s \rangle
    =
    \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert s \rangle
    =
    \boldsymbol{T}^{\dagger}
    \langle uvn \vert s \rangle
    \\&=
    \dfrac{1}{\sqrt{2}}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 & i  & 0        \\
      0 & 0  & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      \hat{s}_u \\
      \hat{s}_v \\
      \hat{s}_n \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      \dfrac{\hat{s}_u - i\hat{s}_v}{\sqrt{2}} \\
      \dfrac{\hat{s}_u + i\hat{s}_v}{\sqrt{2}} \\
      \hat{s}_n                                \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      \dfrac{\hat{s}^-}{\sqrt{2}} \\
      \dfrac{\hat{s}^+}{\sqrt{2}} \\
      \hat{s}_n                   \\
    \end{pmatrix}

.. math::
  &\langle u^+u^-n \vert s \rangle
  =
  \begin{pmatrix}
    \dfrac{\hat{s}^-}{\sqrt{2}} \\
    \dfrac{\hat{s}^+}{\sqrt{2}} \\
    \hat{s}_n                   \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \sqrt{S}
    \cdot
    \left[
      \hat{a}^{\dagger}
      -
      \dfrac{\hat{a}^{\dagger}\hat{a}^{\dagger}\hat{a}}{4S}
    \right] \\
    \sqrt{S}
    \cdot \left[
      \hat{a}
      -
      \dfrac{\hat{a}^{\dagger}\hat{a}\hat{a}}{4S}
    \right] \\
    S - \hat{a}^{\dagger}\hat{a} \\
  \end{pmatrix}












References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
