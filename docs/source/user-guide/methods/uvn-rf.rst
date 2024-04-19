.. _user-guide_methods_uvn:

*********************
(uvn) reference frame
*********************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/cross-product.inc
  * .. include:: page-notations/rotations.inc
  * .. include:: page-notations/exchange-tensor.inc

Magnopy assumes that the ground state spin arrangement follows a spiral conical
configuration, where the cone axis is defined by the unit vector :math:`\boldsymbol{n}`.
Eventually, the program rotates every atomic spin to make it collinear to
:math:`\boldsymbol{n}` and quantize the spin vectors along :math:`\boldsymbol{n}`.

However, the exchange :math:`\boldsymbol{J}` and on-site anisotropy
:math:`\boldsymbol{A}` tensors are usually provided in a different global reference
frame, say :math:`(x\, y\, z)`, where neither of these three unit vectors is collinear to
:math:`\boldsymbol{n}`. A rotation is therefore performed on :math:`\boldsymbol{J}` and
:math:`\boldsymbol{A}` from :math:`(x\, y\, z)` to a new reference frame
:math:`(u\, v\, n)`. There is a freedom in the choice of the unit vectors
:math:`\boldsymbol{\hat{u}}` and :math:`\boldsymbol{\hat{v}}` due to the rotational
symmetry of the system about the :math:`\boldsymbol{\hat{n}}` cone axis.

Let :math:`\boldsymbol{\hat{r}}` be a vector perpendicular to both
:math:`\boldsymbol{\hat{z}}` and :math:`\boldsymbol{\hat{n}}`. Then
:math:`\boldsymbol{\hat{z}}` is brought to :math:`\boldsymbol{\hat{n}}` by performing
a rotation :math:`\boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)` of angle
:math:`\alpha` about :math:`\boldsymbol{\hat{r}}`. We choose  the :math:`(u\, v\, n)`
reference frame by performing this same rotation
:math:`\boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)` over all the three unit vectors
of the :math:`(x\, y\, z)` reference frame.

.. raw:: html
  :file: ../../../images/uvn-rf-main-case.html

.. rst-class:: plotly-figure-caption

  **Figure 1** (interactive): Construction of the :math:`(u\, v\, n)` reference frame.

.. dropdown:: Explicit formulas

  The unit vector

  .. math::
      \boldsymbol{\hat{r}}(\beta)
      =
      \dfrac{
        \boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}
      }{
        \vert\boldsymbol{\hat{z}}\times\boldsymbol{\hat{n}}\vert
      }
      =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta  \\
        0
      \end{pmatrix}

  is defined by the angle :math:`\beta` in the figure below

  .. raw:: html
    :file: ../../../images/uvn-rf-n-angles.html

  The rotation matrix is

  .. math::
    :name: eq:uvn-rf-rot-matrix

    \boldsymbol{R}_{\boldsymbol{r}(\beta)}(\alpha)
    &=
    \boldsymbol{R_r}(\alpha,\beta)
    \\&=
    \begin{pmatrix}
      1 - \dfrac{(n^x)^2}{1+n^z} & -\dfrac{n^xn^y}{1+n^z}   & n^x  \\
      -\dfrac{n^xn^y}{1+n^z}   & 1 - \dfrac{(n^y)^2}{1+n^z} & n^y  \\
      -n^x                     & -n^y                       & n^z  \\
    \end{pmatrix}
    \\&=
    \begin{pmatrix}
      \cos\alpha + \sin^2\beta\, \, (1-\cos\alpha) &
      -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
      \cos\beta\, \sin\alpha                       \\
      -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
      \cos\alpha + \cos^2\beta\, \, (1-\cos\alpha) &
      \sin\beta\, \sin\alpha                       \\
      -\cos\beta\, \sin\alpha &
      -\sin\beta\, \sin\alpha &
      \cos\alpha              \\
    \end{pmatrix}

  The unit vectors of the rotated reference frame are written in the :math:`(x\, y\, z)`
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
        -\dfrac{n^xn^y}{1+n^z}     \\
        -n^x                       \\
      \end{pmatrix}
      =
      \begin{pmatrix}
        \cos\alpha + \sin^2\beta\, \, (1-\cos\alpha) \\
        -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)      \\
        -\cos\beta\sin\alpha                   \\
      \end{pmatrix}
      \\
      \boldsymbol{\hat{v}}
      &=
      \boldsymbol{R_r}(\alpha,\beta)
      \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
      =
      \begin{pmatrix}
        -\dfrac{n^xn^y}{1+n^z}     \\
        1 - \dfrac{(n^y)^2}{1+n^z} \\
        -n^y                       \\
      \end{pmatrix}
      =
      \begin{pmatrix}
        -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)      \\
        \cos\alpha + \cos^2\beta\, \, (1-\cos\alpha) \\
        -\sin\beta\, \sin\alpha                   \\
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
        \cos\beta\, \sin\alpha \\
        \sin\beta\, \sin\alpha \\
        \cos\alpha          \\
      \end{pmatrix}
    \end{aligned}

  Notice also that these vectors can be written in Dirac's notation as

  .. math::
    \begin{aligned}
      \boldsymbol{\hat{u}} &= \braket{\, x\, y\, z\, |\, u\, }
      =
      \braket{\, x\, y\, z\, |\, \boldsymbol{R_r}(\alpha,\beta)\, |\, x\, }
      \\
      \boldsymbol{\hat{v}} &= \braket{\, x\, y\, z\, |\, v\, }
      =
      \braket{\, x\, y\, z\, |\, \boldsymbol{R_r}(\alpha,\beta)\, |\, y\, }
      \\
      \boldsymbol{\hat{n}} &= \braket{\, x\, y\, z\, |\, n\, }
      =
      \braket{\, x\, y\, z\, |\, \boldsymbol{R_r}(\alpha,\beta)\, |\, z\, }
    \end{aligned}

However, the unit vector :math:`\boldsymbol{\hat{r}}` is ill-defined, and so is
:math:`\boldsymbol{R_r}(\alpha,\beta)`, whenever  :math:`\boldsymbol{\hat{n}}` and
:math:`\pm\boldsymbol{\hat{z}}` are collinear. We then choose
:math:`\boldsymbol{\hat{r}}=-\boldsymbol{\hat{x}}` and rotate
:math:`\boldsymbol{\hat{z}}` by either 0 or :math:`\pi` degrees for the parallel or
antiparallel cases, respectively, as shown in the figure below.

.. raw:: html
  :file: ../../../images/uvn-rf-special-cases.html

.. rst-class:: plotly-figure-caption

  **Figure 2** (interactive): Two special cases.

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
Vector and matrix elements in the :math:`(u\, v\, n)` reference frame
=======================================================================

The :math:`(x\, y\, z)` to :math:`(u\, v\, n)` basis change modifies the spin vector
components and the exchange tensor matrix elements. These changes are governed by the
rotation matrix :math:`\boldsymbol{R_r}(\alpha,\beta)` that has been introduced and
written explicitly in the :ref:`previous section <eq:uvn-rf-rot-matrix>`.

=================
Basis coordinates
=================

The rotation matrix by itself contains the coordinates of the :math:`(u\, v\, n)` basis
vectors written in the :math:`(x\, y\, z)` basis.

.. math::
  \boldsymbol{R_r}(\alpha,\beta)
  =&
  \braket{\, x\, y\, z\, |\, u\, v\, n\, }
  =
  \left(\, \boldsymbol{u}\, \boldsymbol{v}\, \boldsymbol{n}\, \right)
  \\=&
  \begin{pmatrix}
    \cos\alpha + \sin^2\beta\, \, (1-\cos\alpha) &
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
    \cos\beta\, \sin\alpha                       \\
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
    \cos\alpha + \cos^2\beta\, \, (1-\cos\alpha) &
    \sin\beta\, \sin\alpha                       \\
    -\cos\beta\, \sin\alpha &
    -\sin\beta\, \sin\alpha &
    \cos\alpha              \\
  \end{pmatrix}

===============
Spin components
===============
The components of a spin vector :math:`\ket{S}` are calculated
using Dirac's notation

.. math::
  \braket{\, u\, v\, n\, |\, S\, }
  =
  \braket{\, u\, v\, n\, |\, x\, y\, z\, }
  \braket{\, x\, y\, z\, |\, S\, }
  =
  \braket{
    \, x\, y\, z\, |\, \boldsymbol{\cal R_r}^\dagger(\alpha,\beta)\, |\, x\, y\, z\,
  }
  \braket{\, x\, y\, z\, |\, S\, }

The spin components in the :math:`(u\, v\, n)` basis are therefore

.. math::
  \begin{pmatrix}
    S^u \\
    S^v \\
    S^n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\alpha + \sin^2\beta\, \, (1-\cos\alpha) &
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
    -\cos\beta\, \sin\alpha                      \\
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)   &
    \cos\alpha + \cos^2\beta\, \, (1-\cos\alpha) &
    -\sin\beta\, \sin\alpha                      \\
    \cos\beta\, \sin\alpha &
    \sin\beta\, \sin\alpha &
    \cos\alpha             \\
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

Similarly, the exchange tensor matrix elements in the :math:`(u\, v\, n)` basis
are computed using Dirac's notation as follows

.. math::
  \boldsymbol{J}^{uvn}_{\boldsymbol{d}ij}
  =
  \braket{\, u\, v\, n\, |\, \boldsymbol{J}_{\boldsymbol{d}ij}\, |\, u\, v\, n\, }
  =&
  \braket{\, u\, v\, n\, |\, x\, y\, z\, }\,
  \braket{\, x\, y\, z\, \vert\, \boldsymbol{J}_{\boldsymbol{d}ij}\, \vert\, x\, y\, z\, }\,
  \braket{\, x\, y\, z\, |\, u\, v\, n\, } \\
  =&
  \braket{
    \, x\, y\, z\, |\, \boldsymbol{\cal R_r}^{\dagger}(\alpha,\beta)\, |\, x\, y\, z\,
  }\,
  \boldsymbol{J}^{xyz}_{\boldsymbol{d}ij}
  \braket{\, x\, y\, z\, |\, \boldsymbol{\cal R_r}(\alpha,\beta)\, |\, x\, y\, z\, }

Explicitly

.. math::
  \boldsymbol{J}^{u v n}_{\boldsymbol{d}ij}=
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{uu} & J_{\boldsymbol{d}ij}^{uv} & J_{\boldsymbol{d}ij}^{un} \\
    J_{\boldsymbol{d}ij}^{vu} & J_{\boldsymbol{d}ij}^{vv} & J_{\boldsymbol{d}ij}^{vn} \\
    J_{\boldsymbol{d}ij}^{nu} & J_{\boldsymbol{d}ij}^{nv} & J_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}
  =
  \boldsymbol{R_r}^{\dagger}\, \boldsymbol{J}_{\boldsymbol{d}ij}^{x y z}\, \boldsymbol{R_r}
  =
  \boldsymbol{R_r}^{\dagger}\,
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{xx} & J_{\boldsymbol{d}ij}^{xy} & J_{\boldsymbol{d}ij}^{xz} \\
    J_{\boldsymbol{d}ij}^{yx} & J_{\boldsymbol{d}ij}^{yy} & J_{\boldsymbol{d}ij}^{yz} \\
    J_{\boldsymbol{d}ij}^{zx} & J_{\boldsymbol{d}ij}^{zy} & J_{\boldsymbol{d}ij}^{zz} \\
  \end{pmatrix}\,
  \boldsymbol{R_r}

:math:`\boldsymbol{J}^{uvn}_{\boldsymbol{d}ij}` can be split into isotropic, symmetric
and anti-symmetric (DM) matrices in the :math:`(u\, v\, n)` reference frame also

.. math::
  \boldsymbol{J}_{\boldsymbol{d}ij}^{uvn}
  =
  J_{\boldsymbol{d}ij}^{I}\, \boldsymbol{I}
  +
  \boldsymbol{J}^{\boldsymbol{S},u v n}_{\boldsymbol{d}ij}
  +
  \boldsymbol{J}^{\boldsymbol{A},u v n}_{\boldsymbol{d}ij}

where
:math:`J^{I}_{\boldsymbol{d}ij} = \dfrac{1}{3}(J_{\boldsymbol{d}ij}^{uu} + J_{\boldsymbol{d}ij}^{vv} + J_{\boldsymbol{d}ij}^{nn}) =\dfrac{1}{3}(J_{\boldsymbol{d}ij}^{xx} + J_{\boldsymbol{d}ij}^{yy} + J_{\boldsymbol{d}ij}^{zz})`
and

.. math::
  \boldsymbol{J}^{\boldsymbol{S},u v n}_{\boldsymbol{d}ij}
  =
  \begin{pmatrix}
    S_{\boldsymbol{d}ij}^{uu} & S_{\boldsymbol{d}ij}^{uv} & S_{\boldsymbol{d}ij}^{un} \\
    S_{\boldsymbol{d}ij}^{uv} & S_{\boldsymbol{d}ij}^{vv} & S_{\boldsymbol{d}ij}^{vn} \\
    S_{\boldsymbol{d}ij}^{un} & S_{\boldsymbol{d}ij}^{vn} & S_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}

.. math::
  \boldsymbol{J}^{\boldsymbol{A},u v n}_{\boldsymbol{d}ij}
  =
  \begin{pmatrix}
    0                       & D_{\boldsymbol{d}ij}^n  & -D_{\boldsymbol{d}ij}^v \\
    -D_{\boldsymbol{d}ij}^n & 0                       & D_{\boldsymbol{d}ij}^u  \\
    D_{\boldsymbol{d}ij}^v  & -D_{\boldsymbol{d}ij}^u & 0                       \\
  \end{pmatrix}

with
:math:`S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv} + S_{\boldsymbol{d}ij}^{nn} = 0`.

.. important::
  We will not use the :math:`(x\, y\, z)` reference frame anymore.
  Every matrix or vector (classical or vector operator) symbol will be written in the
  :math:`(u\, v\, n)` reference frame. We will therefore drop the :math:`uvn`
  super-index to simplify the notation.
