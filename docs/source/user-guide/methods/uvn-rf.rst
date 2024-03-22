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
  * .. include:: page-notations/rotations.inc

Magnopy assumes that the ground state spin arrangement follows a spiral conical
configuration, where the cone axis is defined by the unit vector :math:`\boldsymbol{n}`.
Eventually, the program rotates every atomic spin to make it collinear to
:math:`\boldsymbol{n}` and quantize the spin vectors along :math:`\boldsymbol{n}`.

However, the exchange :math:`\boldsymbol{J}` and on-site anisotropy :math:`\boldsymbol{A}`
tensors are usually provided in a different global reference frame, say :math:`(x\,y\,z)`,
where neither of these three unit vectors is collinear to :math:`\boldsymbol{n}`.
A rotation is therefore performed on :math:`\boldsymbol{J}` and :math:`\boldsymbol{A}`
from :math:`(x\,y\,z)` to a new reference frame :math:`(u\,v\,n)`. There is a
freedom in the choice of the unit vectors :math:`\boldsymbol{\hat{u}}` and
:math:`\boldsymbol{\hat{v}}` due to the rotational symmetry of the system about
the :math:`\boldsymbol{\hat{n}}` cone axis.

Let :math:`\boldsymbol{\hat{r}}` be a vector perpendicular to both
:math:`\boldsymbol{\hat{z}}` and :math:`\boldsymbol{\hat{n}}`. Then
:math:`\boldsymbol{\hat{z}}` is brought to :math:`\boldsymbol{\hat{n}}` by performing
a rotation :math:`\boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)` of angle :math:`\alpha` about
:math:`\boldsymbol{\hat{r}}`. We choose  the :math:`(u\,v\,n)` reference frame by performing
this same rotation :math:`\boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)` over all the three unit vectors of
the :math:`(x\,y\,z)` reference frame.

.. raw:: html
  :file: ../../../images/uvn-rf-main-case.html

.. dropdown:: Explicit formulas

  The unit vector

  .. math::
      \boldsymbol{\hat{r}}(\beta)
      =
      \dfrac{\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}}{\vert\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}\vert}
      =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta \\
        0
      \end{pmatrix}

  is defined by the angle :math:`\beta` in the figure below

  .. raw:: html
    :file: ../../../images/uvn-rf-n-angles.html

  The rotation matrix is

  .. math::
    :name: eq:uvn-rf-rot-matrix

    \boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)
    &=\boldsymbol{R_r}(\alpha,\beta)\\
    =&
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

  The unit vectors of the rotated reference frame are written in the :math:`(x\,y\,z)`
  basis as

  .. math::

      \begin{aligned}
        \boldsymbol{\hat{u}}
        &=
        \boldsymbol{R_r}(\alpha,\beta)
        \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
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
        \boldsymbol{R_r}(\alpha,\beta)
        \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
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
        \boldsymbol{R_r}(\alpha,\beta)
        \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
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
        \boldsymbol{\hat{u}} &= \braket{x\,y\,z\,|u}
        =
        \braket{x\,y\,z\,|\,\boldsymbol{R_r}(\alpha,\beta)\,|x}
        \\
        \boldsymbol{\hat{v}} &= \braket{x\,y\,z\,|v}
        =
        \braket{x\,y\,z\,|\,\boldsymbol{R_r}(\alpha,\beta)\,|y}
        \\
        \boldsymbol{\hat{n}} &= \braket{x\,y\,z\,|n}
        =
        \braket{x\,y\,z\,|\,\boldsymbol{R_r}(\alpha,\beta)\,|z}
    \end{aligned}

However, the unit vector :math:`\boldsymbol{\hat{r}}` is ill-defined, and so is
:math:`\boldsymbol{R_r}(\alpha,\beta)`, whenever  :math:`\boldsymbol{\hat{n}}` and
:math:`\pm\boldsymbol{\hat{z}}` are collinear. We then choose
:math:`\boldsymbol{\hat{r}}=-\boldsymbol{\hat{x}}` and rotate
:math:`\boldsymbol{\hat{z}}` by either 0 or :math:`\pi` degrees
for the parallel or antiparallel cases, respectively, as shown in the figure below.

.. raw:: html
  :file: ../../../images/uvn-rf-special-cases.html

.. dropdown:: Explicit formulas

  .. math::
      \boldsymbol{R_r}(\alpha,\beta)
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

=======================================================================
Vector and matrix elements in the :math:`(\,u\,v\,n\,)` reference frame
=======================================================================

The :math:`(x\,y\,z)` to :math:`(u\,v\,n)` basis change modifies the spin vector components
and the exchange tensor matrix elements. These changes are governed by the rotation
matrix :math:`\boldsymbol{R_r}(\alpha,\beta)` that has been introduced and written explicitly in
the  :ref:`previous section <eq:uvn-rf-rot-matrix>`.

=================
Basis coordinates
=================

The rotation matrix by itself contains the coordinates of the :math:`(u\,v\,n)` basis
vectors written in the :math:`(x\,y\,z)` basis.

.. math::
  \boldsymbol{R_r}(\alpha,\beta)=&
  \braket{\,x\,y\,z\,|\,u\,v\,n\,}=
  \left(\,\boldsymbol{u}\, \boldsymbol{v}\, \boldsymbol{n}\,\right)
  \\\\
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
      \end{pmatrix}\\

===============
Spin components
===============
The components of a spin vector :math:`\ket{S}` are calculated
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
  \boldsymbol{J}^{uvn}
  \braket{\,u\,v\,n \,| \,\boldsymbol{J}\,|\,u\,v\,n\,}
  =&
  \braket{\,u\,v\,n \,|\, x\,y\,z\,}\,
  \braket{\,x\,y\,z\, |\, \boldsymbol{J}\,| \,x\,y\,z\,}\,
  \braket{\,x\,y\,z \,|\, u\,v\,n\,} \\
  =&
  \braket{\,x\,y\,z\, |\, \boldsymbol{\cal R_r}^{\dagger}\,|\,x\,y\,z\,}\,
  \boldsymbol{J}^{xyz}\,
  \braket{\,x\,y\,z\, |\,\boldsymbol{\cal R_r}\,|\,x\,y\,z\,}

Explicitly

.. math::
  \boldsymbol{J}^{u v n}_{ij}=
  \begin{pmatrix}
    J_{ij}^{uu} & J_{ij}^{uv} & J_{ij}^{un} \\
    J_{ij}^{vu} & J_{ij}^{vv} & J_{ij}^{vn} \\
    J_{ij}^{nu} & J_{ij}^{nv} & J_{ij}^{nn} \\
  \end{pmatrix}
  =\boldsymbol{R_r}^{\dagger}\,\boldsymbol{J}_{ij}\,\boldsymbol{R_r}
  = \boldsymbol{R_r}^{\dagger}\,
  \begin{pmatrix}
    J_{ij}^{xx} & J_{ij}^{xy} & J_{ij}^{xz} \\
    J_{ij}^{yx} & J_{ij}^{yy} & J_{ij}^{yz} \\
    J_{ij}^{zx} & J_{ij}^{zy} & J_{ij}^{zz} \\
  \end{pmatrix} \,\boldsymbol{R_r}

:math:`\boldsymbol{J}^{u v n}_{ij}` can be split into isotropic, symmetric and anti-symmetric (DM) matrices
in the :math:`(\,u\,v\,n\,)` reference frame also

.. math::
  \boldsymbol{J}_{ij}^{u v n}=J_{ij}\,\boldsymbol{I}+
  \boldsymbol{J}^{u v n,S}_{ij}+\boldsymbol{J}^{u v n, A}_{ij}

where :math:`J^{I} = \dfrac{1}{3}(J_{ij}^{uu} + J_{ij}^{vv} + J_{ij}^{nn}) =\dfrac{1}{3}(J_{ij}^{xx} + J_{ij}^{yy} + J_{ij}^{zz})` and

.. math::
  \boldsymbol{J}^{u v n, S}_{ij}=
    \begin{pmatrix}
      S_{ij}^{uu} & S_{ij}^{uv} & S_{ij}^{un} \\
      S_{ij}^{uv} & S_{ij}^{vv} & S_{ij}^{vn} \\
      S_{ij}^{un} & S_{ij}^{vn} & S_{ij}^{nn} \\
    \end{pmatrix}

.. math::
  \boldsymbol{J}^{u v n, A}_{ij}=
      \begin{pmatrix}
      0 & D_{ij}^n & -D_{ij}^v \\
      -D_{ij}^n & 0 & D_{ij}^u \\
      D_{ij}^v & -D_{ij}^u & 0 \\
    \end{pmatrix}

with :math:`S_{ij}^{uu} + S_{ij}^{vv} + S_{ij}^{nn} = 0`.

.. important::
  We will not use the :math:`(\,x\,y\,z\,)` reference frame anymore.
  Every matrix or vector (classical or vector operator) symbol will be written in the
  :math:`(\,u\,v\,n\,)` reference frame. We will therefore drop the :math:`u v n` super-index
  to simplify the notation.
