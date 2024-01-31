.. _user-guide_methods_xyz-to-uvn:

***********************************************************************
Vector and matrix elements in the :math:`(\,u\,v\,n\,)` reference frame
***********************************************************************

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
Dirac's notation, where the rotation matrix elements are

.. math::
  \ket{\,u\,v\,n\,} = \boldsymbol{\cal R_r}\, \ket{\,x\,y\,z\,}

.. math::
  \boldsymbol{R_r}=&
  \braket{\,x\,y\,z\,|\,u\,v\,n\,}=
  \bra{\,x\,y\,z\,}\, \boldsymbol{\cal R_r}\, \ket{\,x\,y\,z\,}\\\\
   =&
      \begin{pmatrix}
        \cos\alpha + \sin^2\beta\,\,(1-\cos\alpha) &
        -\sin\beta\,\cos\beta\,\,(1-\cos\alpha)      &
        \cos\beta\,\sin\alpha                    \\
        -\sin\beta\,\cos\beta\,\,(1-\cos\alpha)      &
        \cos\alpha + \cos^2\beta\,\,(1-\cos\alpha) &
        \sin\beta\,\sin\alpha                    \\
        -\cos\beta\,\sin\alpha                   &
        -\sin\beta\,\sin\alpha                   &
        \cos\alpha \\
      \end{pmatrix}

---------------
Spin components
---------------
The components of a spin vector :math:`\ket{S}` are also more easily calculated
using Dirac's notation

.. math::
  \braket{\,u\,v\,n\, \,|\, S\,} = \braket{\,u\,v\,n\, \,|\,x\,y\,z\,}\,
  \braket{\,x\,y\,z\,|\, S\,}
  =
  \braket{\,x\,y\,z \,|\,\boldsymbol{\cal R_r}^\dagger\,| \,x\,y\,z\,}
  \braket{\,x\,y\,z\, | \,S\,}

The spin components in the :math:`(\,u\,v\,n\,)` basis are therefore

.. math::
  \begin{pmatrix}
    S^u \\
    S^v \\
    S^n \\
  \end{pmatrix}
  =
       \begin{pmatrix}
        \cos\alpha + \sin^2\beta\,\,(1-\cos\alpha) &
        -\sin\beta\,\cos\beta\,\,(1-\cos\alpha)      &
        -\,\cos\beta\,\sin\alpha                    \\
        -\,\sin\beta\,\cos\beta\,\,(1-\cos\alpha)      &
        \cos\alpha + \cos^2\beta\,\,(1-\cos\alpha) &
        -\,\sin\beta\,\sin\alpha                    \\
        \cos\beta\,\sin\alpha                   &
        \sin\beta\,\sin\alpha                   &
        \cos\alpha \\
      \end{pmatrix}
      \,
  \begin{pmatrix}
    S^x \\
    S^y \\
    S^z \\
  \end{pmatrix}

-------------------------------
Exchange tensor matrix elements
-------------------------------
Similarly, the exchange tensor matrix elements in the :math:`(\,u\,v\,n\,)` basis
can be computed using Dirac's notation as follows

.. math::
  \braket{\,u\,v\,n \,| \,\boldsymbol{J}\,|\,u\,v\,n\,}
  =&
  \braket{\,u\,v\,n \,|\, x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\, \boldsymbol{J}\,| \,x\,y\,z\,}\,
  \braket{\,x\,y\,z \,|\, u\,v\,n\,} \\
  =&
  \braket{\,x\,y\,z\, |\, \boldsymbol{\cal R_r}^{\dagger}\,|\,x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\, \boldsymbol{J}\,|\,x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\,\boldsymbol{\cal R_r}\,|\,x\,y\,z\,}

So those matrix elements are

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
