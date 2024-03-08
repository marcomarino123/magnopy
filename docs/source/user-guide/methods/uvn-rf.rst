.. _user-guide_methods_uvn:

*********************
(uvn) reference frame
*********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/cross-product.inc

Magnopy assumes that the ground state spin arrangement follows a conical configuration,
where the cone axis is defined by the unit vector :math:`\boldsymbol{n}`. The program
rotates every atomic spin to make it collinear to :math:`\boldsymbol{n}`.
Magnopy subsequently quantizes the spin vectors along :math:`\boldsymbol{n}`.

However, the exchange :math:`\boldsymbol{J}` and on-site anisotropy
:math:`\boldsymbol{A}` tensors are usually
provided in a different global reference frame, say
:math:`(x\,y\,z)`,
where neither of these three unit vectors is collinear to :math:`\boldsymbol{n}`.
A rotation is therefore performed on :math:`J` and :math:`A` from :math:`(x\,y\,z)` to
a new reference frame :math:`(u\,v\,n)`, where there is freedom to choose the unit
vectors :math:`\boldsymbol{\hat{u}}` and :math:`\boldsymbol{\hat{v}}` due to
the rotational symmetry of the system about the :math:`\boldsymbol{\hat{n}}` cone axis.

Let :math:`\boldsymbol{\hat{r}}` be a vector perpendicular to both
:math:`\boldsymbol{\hat{z}}` and :math:`\boldsymbol{\hat{n}}`. Then
:math:`\boldsymbol{\hat{z}}` is brought to :math:`\boldsymbol{\hat{n}}` by performing
a rotation :math:`\boldsymbol{R_r}` of magnitude :math:`\alpha` about
:math:`\boldsymbol{\hat{r}}`. We choose  the :math:`(u\,v\,n)` reference frame by performing
this same rotation :math:`\boldsymbol{R_{r}}` over all the three unit vectors of
the :math:`(x\,y\,z)` reference frame.

.. raw:: html
  :file: ../../../images/uvn-rf-main-case.html

.. dropdown:: Explicit formulas

  The unit vector

  .. math::

      \boldsymbol{\hat{r}}(\alpha,\beta)
      =
      \dfrac{\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}}{\vert\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}\vert}
      =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta \\
        0
      \end{pmatrix}

  is actually defined by the two angles :math:`\alpha` and :math:`\beta`
  in the figure

  .. raw:: html
    :file: ../../../images/uvn-rf-n-angles.html

  The rotation matrix is

  .. math::
    :name: eq:uvn-rf-rot-matrix

      \boldsymbol{R_r}
      &=
      \begin{pmatrix}
        1 - \dfrac{(n^x)^2}{1+n^z} & -\dfrac{n^xn^y}{1+n^z}   & n^x  \\
        -\dfrac{n^xn^y}{1+n^z}   & 1 - \dfrac{(n^y)^2}{1+n^z} & n^y  \\
        -n^x                     & -n^y                     & n^z  \\
      \end{pmatrix} &\\
      &=
      \begin{pmatrix}
        \cos\alpha + \sin^2\beta(1-\cos\alpha) &
        -\sin\beta\cos\beta(1-\cos\alpha)      &
        \cos\beta\sin\alpha                    \\
        -\sin\beta\cos\beta(1-\cos\alpha)      &
        \cos\alpha + \cos^2\beta(1-\cos\alpha) &
        \sin\beta\sin\alpha                    \\
        -\cos\beta\sin\alpha                   &
        -\sin\beta\sin\alpha                   &
        \cos\alpha \\
      \end{pmatrix}&

  The unit vectors of the rotated reference frame are

  .. math::

      \begin{aligned}
        \boldsymbol{\hat{u}}
        &=
        \boldsymbol{R_r} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
        =
        \begin{pmatrix}
          1 - \dfrac{(n^x)^2}{1+n^z} \\
          -\dfrac{n^xn^y}{1+n^z}   \\
          -n^x                     \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          \cos\alpha + \sin^2\beta(1-\cos\alpha) \\
          -\sin\beta\cos\beta(1-\cos\alpha)      \\
          -\cos\beta\sin\alpha                   \\
        \end{pmatrix}
        \\
        \boldsymbol{\hat{v}}
        &=
        \boldsymbol{R_r} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
        =
        \begin{pmatrix}
          -\dfrac{n^xn^y}{1+n^z}   \\
          1 - \dfrac{(n^y)^2}{1+n^z} \\
          -n^y                     \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          -\sin\beta\cos\beta(1-\cos\alpha)      \\
          \cos\alpha + \cos^2\beta(1-\cos\alpha) \\
          -\sin\beta\sin\alpha                   \\
        \end{pmatrix}
        \\
        \boldsymbol{\hat{n}}
        &=
        \boldsymbol{R_r} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
        =
        \begin{pmatrix}
          n^x \\
          n^y \\
          n^z \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          \cos\beta\sin\alpha \\
          \sin\beta\sin\alpha \\
          \cos\alpha          \\
        \end{pmatrix}
      \end{aligned}

  Notice also that these vectors can be written in Dirac's notation as

  .. math::
    \begin{aligned}
        \boldsymbol{\hat{u}} &= \braket{x\,y\,z\,|u}\\
        \boldsymbol{\hat{v}} &= \braket{x\,y\,z\,|v}\\
        \boldsymbol{\hat{n}} &= \braket{x\,y\,z\,|n}

However, the unit vector :math:`\boldsymbol{\hat{r}}` is ill-defined, and so is
:math:`\boldsymbol{R_r}`, whenever  :math:`\boldsymbol{\hat{n}}` and
:math:`\pm\boldsymbol{\hat{z}}` are collinear. We then choose
:math:`\boldsymbol{\hat{r}}=-\boldsymbol{\hat{x}}` and rotate
:math:`\boldsymbol{\hat{z}}` by either 0 or :math:`\pi` degrees
for the parallel or antiparallel cases, respectively, as shown in the figure below.

.. raw:: html
  :file: ../../../images/uvn-rf-special-cases.html

.. dropdown:: Explicit formulas

  .. math::
      \boldsymbol{R_r}
      =
      \begin{pmatrix}
        1 & 0     & 0     \\
        0 & \pm 1 & 0     \\
        0 & 0     & \pm 1 \\
      \end{pmatrix}

  .. math::
      \begin{aligned}
        \boldsymbol{\hat{u}} &= \boldsymbol{\hat{x}}    \\
        \boldsymbol{\hat{v}} &= \pm\boldsymbol{\hat{y}} \\
        \boldsymbol{\hat{n}} &= \pm\boldsymbol{\hat{z}} \\
      \end{aligned}

***********************************************************************
Vector and matrix elements in the :math:`(\,u\,v\,n\,)` reference frame
***********************************************************************

The :math:`(x\,y\,z)` to :math:`(u\,v\,n)` basis change modifies the spin vector components
and the exchange tensor matrix elements. These changes are governed by the rotation
matrix :math:`\boldsymbol{R_r}` that has been introduced and written explicitly in
the  :ref:`previous section <eq:uvn-rf-rot-matrix>`.

=================
Basis coordinates
=================

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

===============
Spin components
===============
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

===============================
Exchange tensor matrix elements
===============================

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

.. important::
  In the next sections we will not use the :math:`(\,x\,y\,z\,)` reference frame anymore.
  Every matrix or vector (classical or vector operator) symbol will be written in the
  :math:`(\,u\,v\,n\,)` reference frame. If the bold superscript appears ":math:`\boldsymbol{^s}`"
  in the vector character (i.e :math:`\boldsymbol{S_{mi}^s}`) or matrix symbol
  (i.e. :math:`\boldsymbol{R_m^s}(q)`) it means that corresponding quantity is
  written in a spherical reference frame. Note, that in the coordinate representation
  the subscripts of the vector/matrix components indicate the reference frame.
