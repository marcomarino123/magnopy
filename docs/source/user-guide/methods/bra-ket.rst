.. _user-guide_methods_bra-ket:

**********************************************
Notes on Dirac's bra-ket notation for vectors
**********************************************

Let :math:`\cal{E}` be a three-dimensional vector space, whose vectors are denoted
by :math:`\ket{\,a\,}`. Let  :math:`(\,u\,v\,n\,)=\{\ket{u},\,\ket{v},\,\ket{n}\}`
be a basis spanning the vector space.
Let :math:`\cal{E}^*` be the dual space. Dual vectors are denoted by
:math:`\bra{a}`, and the dual basis by :math:`(\,u\,v\,n\,)=\{\bra{u},\,\bra{v},\,\bra{n}\}`.

We define the row and column vectors

.. math::
  \ket{\,u\,v\,n\,}&=\begin{pmatrix} \ket{u} & \ket{v} &\ket{n}\end{pmatrix}\\
  \bra{\,u\,v\,n\,}&=\begin{pmatrix} \bra{u}\\ \bra{v}\\ \bra{n} \end{pmatrix}

The basis completeness relationship is

.. math::
  \boldsymbol{I} = \ket{\,u\,v\,n\,}\,\bra{\,u\,v\,n\,}=
             \ket{u}\,\bra{u}+\ket{v}\,\bra{v}+\ket{n}\,\bra{n}

where :math:`\boldsymbol{I}` represents the identity operator acting on :math:`\cal{E}`.
Then a vector  :math:`\ket{a}` can be expressed in the above basis as

.. math::
  \ket{a}
  =&
  \ket{\,u\,v\,n\,}\,\braket{\,u\,v\,n\,|\,a}=
  \ket{u}\,\braket{u|a}+\ket{v}\,\braket{v|a}+\ket{n}\,\braket{n|a}
  \\&
  =\ket{u}\,a^u+\ket{v}\,a^v+\ket{n}\,a^n\,=\, ^n\boldsymbol{a}\,\ket{\,u\,v\,n\,}

where the vector components have been arranged as the column vector

.. math::
  ^n\boldsymbol{a}=\begin{pmatrix}a^u\\a^v\\a^n\end{pmatrix}

This way, :math:`^n\boldsymbol{a}` is nothing but a placeholder for the above
vector components, and the left :math:`^n` super-script indicates unequivocally that
the vector components are referred to the :math:`\ket{\,u\,v\,n\,}` basis.

Similarly, a linear operator :math:`\boldsymbol{O}` is expressed in the :math:`\ket{\,u\,v\,n\,}` basis
as

.. math::
  \boldsymbol{O} =\ket{\,u\,v\,n\,}\bra{\,u\,v\,n\,}\,\boldsymbol{O}\,\ket{\,u\,v\,n\,}\bra{\,u\,v\,n\,}=
  \ket{\,u\,v\,n\,}\,^n\boldsymbol{O}\,\bra{\,u\,v\,n\,}

where the operator components have been arranged in the matrix

.. math::
  ^n\boldsymbol{O}=\begin{pmatrix}
         O^{uu}&O^{uv}&O^{un}\\O^{vu}&O^{vv}&O^{vn}\\O^{nu}&O^{nv}&O^{nn}
       \end{pmatrix}

In other words, a matrix :math:`^n\boldsymbol{O}` is a placeholder for the matrix elements
of the operator :math:`\boldsymbol{O}` in the the basis :math:`\ket{\,u\,v\,n\,}`.

A comprehensive introduction to Dirac's bra-ket notation in the context of quantum mechanics can be found in the book
:math:`Quantum\, Mechanics`, by Cohen-Tannouidji, Diu and Laloe, chapter 2.
