.. _user-guide_methods_bra-ket:

**********************************************
Notes on Dirac's bra-ket notation for vectors
**********************************************

Let :math:`\cal{E}` be a three-dimensional vector space, whose vectors are denoted
by :math:`\ket{\,A\,}`. Let  :math:`\ket{\,u\,v\,n\,}=\{\ket{u},\,\ket{v},\,\ket{n}\}`
be a basis spanning the vector space.
Let :math:`\cal{E}^*` be the dual space. Dual vectors are denoted by
:math:`\bra{A}`, and the dual basis by :math:`\bra{\,u\,v\,n\,}=\{\bra{u},\,\bra{v},\,\bra{n}\}`.
The basis completeness relationship is

.. math::
  {\cal I} = \ket{\,u\,v\,n\,}\,\bra{\,u\,v\,n\,}=
             \ket{u}\,\bra{u}+\ket{v}\,\bra{v}+\ket{n}\,\bra{n}

where :math:`{\cal I}` represents the identity operator acting on :math:`\cal{E}`.
Then a vector  :math:`\ket{A}` can be expressed in the above basis as

.. math::
  \ket{A}
  =&
  \ket{\,u\,v\,n\,}\,\braket{\,u\,v\,n\,|\,A}=
  \braket{u|A}\,\ket{u}+\braket{v|A}\,\ket{v}+\braket{n|A}\,\ket{n}
  \\&
  =A^u\,\ket{u}+A^v\,\ket{v}+A^n\,\ket{n}

The vector components can be arranged as the column vector

.. math::
  ^n\boldsymbol{A}=\begin{pmatrix}A^u\\A^v\\A^n\end{pmatrix}

where :math:`^n\boldsymbol{A}` is nothing but a placeholder for the above
vector components, and the left :math:`^n` super-script indicates that
the vector components are referred to the :math:`\ket{u\,v\,n}` basis.

Similarly, a linear operator :math:`O` is expressed in the :math:`\ket{\,u\,v\,n\,}` basis
as

.. math::
  O =\ket{\,u\,v\,n\,}\bra{\,u\,v\,n\,}\,O\,\ket{\,u\,v\,n\,}\bra{\,u\,v\,n\,}=
  \ket{\,u\,v\,n\,}\,^nO\,\bra{\,u\,v\,n\,}

where the operator components in the :math:`\ket{\,u\,v\,n\,}` basis have been
arranged in the matrix

.. math::
  ^nO=\begin{pmatrix}
         O^{uu}&O^{uv}&O^{un}\\O^{vu}&O^{vv}&O^{vn}\\O^{nu}&O^{nv}&O^{nn}
       \end{pmatrix}


A comprehensive introduction to Dirac's bra-ket notation in the context of quantum mechanics can be found in the book
:math:`Quantum\, Mechanics`, by Cohen-Tannouidji, Diu and Laloe, chapter 2.
