.. _user-guide_methods_bra-ket:

**********************************************
Notes on Dirac's bra-ket notation for vectors
**********************************************

Let be a three-dimensional vector space and a basis :math:`(\,u\,v\,n\,)`
that spans it.

Vectors :math:`\boldsymbol{A}` are denoted in Dirac's notation
by :math:`\ket{\,A\,}`. Similarly, the basis set
:math:`{\ket{u},\,\ket{v},\,\ket{n}}` can be shorthanded
as :math:`\ket{\,u\,v\,n\,}`.
Dual vectors :math:`\boldsymbol{A^*}` are denoted in Dirac's notation by
:math:`\bra{A}`, and the dual basis :math:`{\bra{u},\,\bra{v},\,\bra{n}}`
can be shorthanded as :math:`\bra{\,u\,v\,n\,}`.

The basis completeness relationship is

.. math::
  {\cal I} = \ket{\,u\,v\,n\,}\,\bra{\,u\,v\,n\,}=
             \ket{u}\,\bra{u}+\ket{v}\,\bra{v}+\ket{n}\,\bra{n}

where :math:`{\cal I}` represents the identity operator acting on the vector space.
Then a vector  :math:`\boldsymbol{A}` can be written in the above basis as

.. math::
  \ket{A}
  =&
  \ket{\,u\,v\,n\,}\,\braket{\,u\,v\,n\,|\,A}=
  \braket{u|A}\,\ket{u}+\braket{v|A}\,\ket{v}+\braket{n|A}\,\ket{n}
  \\&
  =A^u\,\ket{u}+A^v\,\ket{v}+A^n\,\ket{n}

The vector components can be arranged as a column vector

.. math::
  \begin{pmatrix}A^u\\A^v\\A^n\end{pmatrix}


A comprehensive introduction to Dirac's bra-ket notation in the context of quantum mechanics can be found in the book
:math:`Quantum\, Mechanics`, by Cohen-Tannouidji, Diu and Laloe, chapter 2.
