.. _user-guide_methods_uvn:

*************************
( u v n ) reference frame
*************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/rotations.inc
  * .. include:: page-notations/exchange-tensor.inc

Magnopy assumes that the ground-state spin arrangement follows a spiral conical
configuration, where the cone axis is defined by the unit vector :math:`\ket{n}`.
Eventually, the program rotates every atomic spin to make it collinear to
:math:`\ket{n}` and quantizes the spin vectors along :math:`\ket{n}`.

However, the exchange :math:`\boldsymbol{J}` and on-site anisotropy
:math:`\boldsymbol{A}` tensor operators are initially provided in the
cartesian reference :math:`(x\, y\, z)`, where none of the unit vectors may be
collinear to :math:`\ket{n}`.
A basis change that corresponds to a rotation from :math:`(x\, y\, z)` to a new
reference frame :math:`(u\, v\, n)` is therefore performed on :math:`\boldsymbol{J}`
and :math:`\boldsymbol{A}`.

This is done as follows. Let :math:`\ket{r}` be a vector perpendicular to both
:math:`\ket{z}` and :math:`\ket{n}`. Then :math:`\ket{z}` is brought to
:math:`\ket{n}` by performing a rotation of angle :math:`\alpha` about :math:`\ket{r}`,
that is denoted by :math:`\boldsymbol{R}_{\ket{r}}(\alpha)`. The :math:`(u\, v\, n)`
reference frame is defined by performing the same rotation over all the three unit vectors
:math:`(x\, y\, z)`.

.. raw:: html
  :file: ../../../images/uvn-rf-main-case.html

.. rst-class:: plotly-figure-caption

  **Figure 1** (interactive): Construction of the :math:`(u\, v\, n)` reference frame.

--------------------------------------
Rotation operator and basis definition
--------------------------------------

The unit vector

.. math::
    ^z\boldsymbol{\hat{r}}(\beta)
    =
    \dfrac{\boldsymbol{\hat{z}}\,\times\,^z\boldsymbol{\hat{n}}
      }{
      \vert\boldsymbol{\hat{z}}\,\times\,^z\boldsymbol{\hat{n}}\vert
      }
    =
    \begin{pmatrix}-\sin\beta \\\cos\beta  \\0\end{pmatrix}

is defined by the angle :math:`\beta` in the figure below

.. raw:: html
  :file: ../../../images/uvn-rf-n-angles.html

The rotation operator is

.. math::
  \boldsymbol{R_\ket{r}}(\alpha,\beta)=e^{-i\,\alpha\,\ket{r(\beta)}\,\times}

The basis :math:`(\,u\,v\,n\,)` is defined by

.. math::
  \ket{u}&=\boldsymbol{R_\ket{r}}\,\ket{x}\\
  \ket{v}&=\boldsymbol{R_\ket{r}}\,\ket{y}\\
  \ket{n}&=\boldsymbol{R_\ket{r}}\,\ket{z}

Therefore the rotation operator can also be expressed as

.. math::
  \boldsymbol{R_\ket{r}}(\alpha,\beta)=\ket{\,u\,v\,n}\,\bra{\,x\,y\,z\,}

-------------------------------------
Rotation matrix and basis coordinates
-------------------------------------

The rotation operator matrix elements in the :math:`(xyz)` basis are therefore

.. math::
  ^z\boldsymbol{R_r}(\alpha,\beta)&=
  \braket{\,x\,y\,z\,|\,u\,v\,n\,}=
  \braket{\,x\,y\,z\,|\,\boldsymbol{R_\ket{r}}(\alpha,\beta)\,|\,x\,y\,z\,}
  \\\\&=
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

The vector components in the :math:`(x\, y\, z)` basis are
nothing but the columns of the above matrix

.. math::
  ^z\boldsymbol{\hat{u}}
  &=\braket{\,x\,y\,z\,|\,u\,}\,=\,
  ^z\boldsymbol{R_r}\,
  \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\alpha + \sin^2\beta\, \, (1-\cos\alpha) \\
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)      \\
    -\cos\beta\sin\alpha                   \\
  \end{pmatrix}
  \\
  ^z\boldsymbol{\hat{v}}
  &=\braket{\,x\,y\,z\,|\,v\,}
  \,=\,
  ^z\boldsymbol{R_r}\,
  \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    -\sin\beta\, \cos\beta\, \, (1-\cos\alpha)      \\
    \cos\alpha + \cos^2\beta\, \, (1-\cos\alpha) \\
    -\sin\beta\, \sin\alpha                   \\
  \end{pmatrix}
  \\
  ^z\boldsymbol{\hat{n}}
  &=\braket{\,x\,y\,z\,|\,v\,}\,=\,
  ^z\boldsymbol{R_r}\,
  \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\beta\, \sin\alpha \\
    \sin\beta\, \sin\alpha \\
    \cos\alpha          \\
  \end{pmatrix}

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

=====================================================================
Vector and matrix elements in the :math:`(u\, v\, n)` reference frame
=====================================================================

The :math:`(x\, y\, z)` to :math:`(u\, v\, n)` basis change modifies the spin vector
components and the exchange tensor matrix elements. These changes are governed by the
rotation matrix :math:`\boldsymbol{R_r}(\alpha,\beta)` that has been introduced and
written explicitly above.

---------------
Spin components
---------------

The components of the spin vector :math:`\ket{S_i}` in the :math:`(u\, v\, n)`
basis are

.. math::
  ^n\boldsymbol{S_i}&=\braket{\, u\, v\, n\, |\, S_i\, }
  =
  \braket{\, u\, v\, n\, |\, x\, y\, z\, }
  \braket{\, x\, y\, z\, |\, S\, }
  \,=\,
  ^z\boldsymbol{\cal R_r}^\dagger\, ^z\boldsymbol{S}\\

Explicitly

.. math::
  \begin{pmatrix}
    S_i^u \\
    S_i^v \\
    S_i^n \\
  \end{pmatrix}\,=\,
  ^z\boldsymbol{\cal R_r}^\dagger
  \,
  \begin{pmatrix}
    S^x \\
    S^y \\
    S^z \\
  \end{pmatrix}

-------------------------------
Exchange tensor matrix elements
-------------------------------

Similarly, the exchange tensor matrix elements in the :math:`(u\, v\, n)` basis
are computed using Dirac's notation as follows

.. math::
  ^n\boldsymbol{J}_{\boldsymbol{d}ij}
  &=
  \braket{\, u\, v\, n\, |\, \boldsymbol{J}_{\boldsymbol{d}ij}\, |\, u\, v\, n\, }
  =
  \braket{\, u\, v\, n\, |\, x\, y\, z\, }\,
  \braket{\, x\, y\, z\, \vert\, \boldsymbol{J}_{\boldsymbol{d}ij}\, \vert\, x\, y\, z\, }\,
  \braket{\, x\, y\, z\, |\, u\, v\, n\, } \\
  &=
  \, ^z\boldsymbol{\cal R_r}^{\dagger}(\alpha,\beta)\, \,
  ^z\boldsymbol{J}_{\boldsymbol{d}ij}
 \, ^z\boldsymbol{\cal R_r}(\alpha,\beta)

Explicitly

.. math::
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{uu} & J_{\boldsymbol{d}ij}^{uv} & J_{\boldsymbol{d}ij}^{un} \\
    J_{\boldsymbol{d}ij}^{vu} & J_{\boldsymbol{d}ij}^{vv} & J_{\boldsymbol{d}ij}^{vn} \\
    J_{\boldsymbol{d}ij}^{nu} & J_{\boldsymbol{d}ij}^{nv} & J_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}
  \,=\,
  ^z\boldsymbol{R_r}^{\dagger}\,
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{xx} & J_{\boldsymbol{d}ij}^{xy} & J_{\boldsymbol{d}ij}^{xz} \\
    J_{\boldsymbol{d}ij}^{yx} & J_{\boldsymbol{d}ij}^{yy} & J_{\boldsymbol{d}ij}^{yz} \\
    J_{\boldsymbol{d}ij}^{zx} & J_{\boldsymbol{d}ij}^{zy} & J_{\boldsymbol{d}ij}^{zz} \\
  \end{pmatrix}\,
  ^z\boldsymbol{R_r}

:math:`^n\boldsymbol{J}_{\boldsymbol{d}ij}` can be split into isotropic, symmetric
and anti-symmetric (DM) matrices in the :math:`(u\, v\, n)` reference frame

.. math::
  ^n\boldsymbol{J}_{\boldsymbol{d}ij}
  =
  J_{\boldsymbol{d}ij}^{I}\, \boldsymbol{I}
  \,+\,
  ^n\boldsymbol{J}^\boldsymbol{S}_{\boldsymbol{d}ij}
  \,+\,
  ^n\boldsymbol{J}^\boldsymbol{A}_{\boldsymbol{d}ij}

where

.. math::
  J^{I}_{\boldsymbol{d}ij} = \dfrac{1}{3}(J_{\boldsymbol{d}ij}^{uu} + J_{\boldsymbol{d}ij}^{vv} + J_{\boldsymbol{d}ij}^{nn}) =\dfrac{1}{3}(J_{\boldsymbol{d}ij}^{xx} + J_{\boldsymbol{d}ij}^{yy} + J_{\boldsymbol{d}ij}^{zz})

.. math::
  ^n\boldsymbol{J}^\boldsymbol{S}_{\boldsymbol{d}ij}
  =
  \begin{pmatrix}
    S_{\boldsymbol{d}ij}^{uu} & S_{\boldsymbol{d}ij}^{uv} & S_{\boldsymbol{d}ij}^{un} \\
    S_{\boldsymbol{d}ij}^{uv} & S_{\boldsymbol{d}ij}^{vv} & S_{\boldsymbol{d}ij}^{vn} \\
    S_{\boldsymbol{d}ij}^{un} & S_{\boldsymbol{d}ij}^{vn} & S_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}

.. math::
  ^n\boldsymbol{J}^\boldsymbol{A}_{\boldsymbol{d}ij}
  =
  \begin{pmatrix}
    0                       & D_{\boldsymbol{d}ij}^n  & -D_{\boldsymbol{d}ij}^v \\
    -D_{\boldsymbol{d}ij}^n & 0                       & D_{\boldsymbol{d}ij}^u  \\
    D_{\boldsymbol{d}ij}^v  & -D_{\boldsymbol{d}ij}^u & 0                       \\
  \end{pmatrix}

with
:math:`S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv} + S_{\boldsymbol{d}ij}^{nn} = 0`.
