.. _user-guide_methods_cs-choice:

************************
Coordinate system choice
************************

.. dropdown:: Notation used on this page

  * :math:`\vec{v}` - is a vector.
  * :math:`\hat{v}` - is a unit vector, corresponding to the
    vector :math:`\vec{v}`.
  * :math:`(...)_{e_1e_2e_3}` - denotes the coordinate representation
    with respect to the :math:`\hat{e}_1\hat{e}_2\hat{e}_3` reference frame.
  * :math:`\times` - means cross product for vectors.
  * "reference frame" = "coordinate system" = "basis"

The exchange and on-site anisotropy matrices are usually given in
some global reference frame :math:`\hat{x}\hat{y}\hat{z}`.
However, majority of the derivation happens in the
:math:`\hat{u}\hat{v}\hat{n}` reference frame, which is defined by the cone
axis :math:`\hat{v}`. The unit vectors :math:`\hat{u}` and
:math:`v` can be defined in a several ways due to the rotational freedom
around :math:`\hat{v}` axis.

Here we explain which reference frame we choose given one unit vector
:math:`\hat{n}`. The idea behind the choice is to rotate the :math:`\hat{z}`
axis of the global reference frame to the direction of the given unit vector:

.. math::

  \hat{n} =
  \begin{pmatrix}
    n_x \\
    n_y \\
    n_z \\
  \end{pmatrix}_{xyz} =
  \begin{pmatrix}
    \cos\beta\sin\alpha \\
    \sin\beta\sin\alpha \\
    \cos\alpha          \\
  \end{pmatrix}_{xyz}

.. raw:: html
  :file: ../../../images/cs-choice-n-angles.html

.. note::
  * The given unit vector is called :math:`\hat{n}`, because in the
    context of magnopy we will use the cone axis as a given vector.
  * We rotate the :math:`\hat{z}` (not :math:`\hat{x}` or :math:`\hat{y}`)
    to match :math:`\hat{n}`, because in the context of magnopy we
    choose the cone axis to be the quantization axis.
  * When :math:`\hat{n} = \pm\hat{z}` the angle :math:`\beta` is not well defined,
    therefore, these two cases are treated separately below.

* If :math:`\hat{n} \ne \pm \hat{z}`, than
  :math:`\hat{x}\hat{y}\hat{z}` is rotated by the angle
  :math:`\alpha` around the axis :math:`\hat{r}`

  .. math::

    \begin{aligned}
      \hat{r}(\alpha,\beta) &= \hat{z}\times\hat{n} =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta \\
        0
      \end{pmatrix}_{xyz}
    \end{aligned}

  .. math::

    R = R(\alpha,\beta) =
    \begin{pmatrix}
      \cos\alpha + \sin^2\beta(1-\cos\alpha) &
      -\sin\beta\cos\beta(1-\cos\alpha) &
      \cos\beta\sin\alpha  \\
      -\sin\beta\cos\beta(1-\cos\alpha) &
      \cos\alpha + \cos^2\beta(1-\cos\alpha) &
      \sin\beta\sin\alpha  \\
      -\cos\beta\sin\alpha &
      -\sin\beta\sin\alpha &
      \cos\alpha \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      1 - \dfrac{n_x^2}{1+n_z} & -\dfrac{n_xn_y}{1+n_z}   & n_x  \\
      -\dfrac{n_xn_y}{1+n_z}   & 1 - \dfrac{n_y^2}{1+n_z} & n_y  \\
      -n_x                     & -n_y                     & n_z  \\
    \end{pmatrix}

  .. math::

    \begin{aligned}
      \hat{u}_{xyz} &= R \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
      =
      \begin{pmatrix}
        \cos\alpha + \sin^2\beta(1-\cos\alpha) \\
        -\sin\beta\cos\beta(1-\cos\alpha) \\
        -\cos\beta\sin\alpha \\
      \end{pmatrix}_{xyz}
      =
      \begin{pmatrix}
        1 - \dfrac{n_x^2}{1+n_z} \\
        -\dfrac{n_xn_y}{1+n_z} \\
        -n_x
      \end{pmatrix}_{xyz} \\
      \hat{v}_{xyz} &= R \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
      =
      \begin{pmatrix}
        -\sin\beta\cos\beta(1-\cos\alpha) \\
        \cos\alpha + \cos^2\beta(1-\cos\alpha) \\
        -\sin\beta\sin\alpha
      \end{pmatrix}_{xyz}
      =
      \begin{pmatrix}
        -\dfrac{n_xn_y}{1+n_z} \\
        1 - \dfrac{n_y^2}{1+n_z} \\
        -n_y
      \end{pmatrix}_{xyz} \\
      \hat{n}_{xyz} &= R \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
      =
      \begin{pmatrix}
        \cos\beta\sin\alpha \\
        \sin\beta\sin\alpha \\
        \cos\alpha
      \end{pmatrix}_{xyz}
      =
      \begin{pmatrix}
        n_x \\
        n_y \\
        n_z
      \end{pmatrix}_{xyz}
    \end{aligned}


.. raw:: html
  :file: ../../../images/cs-choice-case-3.html

* If :math:`\hat{n} = \hat{z}`

  .. math::
    \begin{matrix}
      \begin{aligned}
        \hat{u} &= \hat{x} \\
        \hat{v} &= \hat{y} \\
        \hat{n} &= \hat{z} \\
      \end{aligned} & \text{ and } &
      R =
      \begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1 \\
      \end{pmatrix}
      = R(\alpha = 0, \beta = \pi/2)
    \end{matrix}

.. raw:: html
  :file: ../../../images/cs-choice-case-1.html

* If :math:`\hat{n} = -\hat{z}`

  .. math::
    \begin{matrix}
      \begin{aligned}
        \hat{u} &= -\hat{y} \\
        \hat{v} &= -\hat{x} \\
        \hat{n} &= -\hat{z} \\
      \end{aligned} & \text{ and } &
      R =
      \begin{pmatrix}
        0  & -1 & 0  \\
        -1 & 0  & 0  \\
        0  & 0  & -1 \\
      \end{pmatrix}
      = R(\alpha = \pi, \beta = \pi/4)
    \end{matrix}

.. raw:: html
  :file: ../../../images/cs-choice-case-2.html


The spin vectors and exchange matrices under the change of the reference frame:

.. math::
  \vec{S}^a =
  R\begin{pmatrix} S_x^a \\ S_y^a \\ S_z^a \end{pmatrix}_{xyz}
  = \begin{pmatrix} S_u^a \\ S_v^a \\ S_n^a \end{pmatrix}_{uvn}

.. math::

  J_{a,b}(\vec{d})
  = R
  \begin{pmatrix}
      J_{xx} & J_{xy} & J_{xz} \\
      J_{yx} & J_{yy} & J_{yz} \\
      J_{zx} & J_{zy} & J_{zz}
  \end{pmatrix}_{xyz} R^{-1}
  = \begin{pmatrix}
      J_{uu} & J_{uv} & J_{un} \\
      J_{vu} & J_{vv} & J_{vn} \\
      J_{nu} & J_{nv} & J_{nn}
  \end{pmatrix}_{uvn}

.. important::
  In the following pages the reference frame :math:`\hat{u}\hat{v}\hat{n}`
  is often used, where :math:`\hat{n}` is a cone axis.
