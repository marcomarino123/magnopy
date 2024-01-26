.. _user-guide_methods_xyz-to-uvn:

*******************************************************
Vector and matrix changes from the xyz to the uvn bases
*******************************************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/bra-ket.txt


The :math:`(x\,y\,z)` to :math:`(u\,v\,n)` basis change modifies the spin vector components
and the exchange tensor matrix elements. These changes are governed by the rotation
matrix :math:`\boldsymbol{R_r}` that has been introduced and written explicitly in
the  :ref:`previous section <eq:uvn-choice-rot-matrix>`.

-----------------
Basis coordinates
-----------------

The :math:`(u\,v\,n)` basis coordinates can be better calculated by using
Dirac's notation:

.. math::
  \ket{\,u\,v\,n\,} = \boldsymbol{R_r}\, \ket{\,x\,y\,z\,}

.. math::
  \braket{\,x\,y\,z\,|\,u\,v\,n\,}=\bra{\,x\,y\,z\,}\, \boldsymbol{R_r}\, \ket{\,x\,y\,z\,}

---------------
Spin components
---------------
The components of a spin vector :math:`\ket{S}` are more easily calculated using Dirac's
notation

.. math::
  \braket{\,u\,v\,n\, \,|\, S\,} = \braket{\,x\,y\,z\, |\,\boldsymbol{R_r}\,|\, S\,}
  =
  \braket{\,x\,y\,z \,|\,\boldsymbol{R_r}^\dagger\,| \,x\,y\,z\,}
  \braket{\,x\,y\,z\, | \,S\,}

The components are therefore

.. math::
  \begin{pmatrix}
    S^u \\
    S^v \\
    S^n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    R^{xx} & R^{xy} & R^{xz} \\
    R^{yx} & R^{yy} & R^{yz} \\
    R^{zx} & R^{zy} & R^{zz} \\
  \end{pmatrix}
  \begin{pmatrix}
    S^x \\
    S^y \\
    S^z \\
  \end{pmatrix}

-------------------------------
Exchange tensor matrix elements
-------------------------------

.. math::

  \braket{\,u\,v\,n \,| \,\boldsymbol{J}\,|\,u\,v\,n\,}
  =&
  \braket{\,u\,v\,n \,|\, x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\, \boldsymbol{J}\,| \,x\,y\,z\,}\,
  \braket{\,x\,y\,z \,|\, u\,v\,n\,} \\
  =&
  \braket{\,x\,y\,z\, |\, \boldsymbol{R_r}^{\dagger}\,|\,x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\, \boldsymbol{J}\,|\,x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\,\boldsymbol{R_r}\,|\,x\,y\,z\,}

So the matrix elements are

.. math::
  \begin{pmatrix}
    J_{ij}^{uu} & J_{ij}^{uv} & J_{ij}^{un} \\
    J_{ij}^{vu} & J_{ij}^{vv} & J_{ij}^{vn} \\
    J_{ij}^{nu} & J_{ij}^{nv} & J_{ij}^{nn} \\
  \end{pmatrix}
  = \boldsymbol{R_r}^{\dagger}\,
  \begin{pmatrix}
    J_{ij}^{xx} & J_{ij}^{xy} & J_{ij}^{xz} \\
    J_{ij}^{yx} & J_{ij}^{yy} & J_{ij}^{yz} \\
    J_{ij}^{zx} & J_{ij}^{zy} & J_{ij}^{zz} \\
  \end{pmatrix} \,\boldsymbol{R_r}
