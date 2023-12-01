.. _user-guide_methods_cs-choice:

************************
Coordinate system choice
************************

.. hint::

    * :math:`\vec{v}` - is a vector.
    * :math:`\hat{v}` - is a unit vector, corresponding to the
      vector :math:`\vec{v}`.
    * :math:`(...)_{e_1e_2e_3}` - denotes the coordinate representation
      expressed in the :math:`\hat{e}_1\hat{e}_2\hat{e}_3` coordinate system.
    * :math:`A_{{e_1e_2e_3}}` - denotes the vector/matrix, expressed in the
      :math:`\hat{e}_1\hat{e}_2\hat{e}_3` coordinate system.
    * :math:`\times` - means cross product for vectors.
    * Vectors are represented by columns: :math:`(,,)^T`

We are given a set of matrices in the global :math:`\hat{x}\hat{y}\hat{z}`
coordinate system.

.. math::

    J_{a,b}(\vec{d}) =
    \begin{pmatrix}
        J_{xx} & J_{xy} & J_{xz} \\
        J_{yx} & J_{yy} & J_{yz} \\
        J_{zx} & J_{zy} & J_{zz}
    \end{pmatrix}_{xyz}

where :math:`\vec{d}` is a vector between cite :math:`a` and :math:`b`.

We assume that ground state, corresponding to those matrices, can be describe by the
single-:math:`\vec{Q}` spin spiral with the global rotation axis
:math:`\vec{n}` and a set of spin directions in one unit cell

.. math::

    \vec{Q} = (Q_x, Q_y, Q_z)_{xyz}^T

.. math::

    \hat{n} = (n_x, n_y, \sqrt{1 - n_x^2 - n_y^2})_{xyz}
    = (n_x, n_y, n_z)_{xyz}^T

.. math::

    \vec{S}^a = (S_x^a, S_y^a, S_z^a)_{xyz}^T = S^a\hat{S}^a

where :math:`a = 1, ..., N` and :math:`N` is a number of spins in the
unit cell.

At first we change from :math:`\hat{x}\hat{y}\hat{z}` coordinate system
to the :math:`\hat{u}\hat{v}\hat{n}` coordinate system.
Where :math:`\hat{n}` is the global rotation axis and
:math:`\hat{u}`, :math:`\hat{v}` are chosen by the following rule:

* If :math:`\hat{n} = \hat{z}`

  .. math::

      \begin{aligned}
          \hat{u} &= \hat{x} \\
          \hat{v} &= \hat{y} \\
          \hat{n} &= \hat{z} \\
      \end{aligned}

* If :math:`\hat{n} = -\hat{z}`

  .. math::

      \begin{aligned}
          \hat{u} &= -\hat{y} \\
          \hat{v} &= -\hat{x} \\
          \hat{n} &= -\hat{z} \\
      \end{aligned}

* In other cases
  :math:`\hat{x}\hat{y}\hat{z}` is rotated by the angle
  :math:`\alpha` around the axis :math:`\hat{r}_n`

  .. math::

      \begin{aligned}
        \cos\alpha &= \hat{z}\cdot\hat{n} = v_z \\
        \sin\alpha &= \sqrt{1 - v_z^2} \\
        \hat{r}_n &= \hat{z}\times\hat{n} =
        \dfrac{1}{\sqrt{v_x^2+v_z^2}}(v_z, 0, -v_x)_{xyz}^T \\
      \end{aligned}

  .. math::

      R_{\alpha}^{\hat{r}_v} =
      \begin{pmatrix}
        1 - \dfrac{v_x^2}{1+v_y} & v_x & -\dfrac{v_xv_z}{1+v_y}   \\
        -v_x                     & v_y & -v_z                     \\
        -\dfrac{v_xv_z}{1+v_y}   & v_z & 1 - \dfrac{v_z^2}{1+v_y} \\
      \end{pmatrix}

  .. math::

      \begin{aligned}
        \hat{u}_{xyz} &= R_{\alpha}^{\hat{r}_v} (1,0,0)^T
        = (1 - \dfrac{v_x^2}{1+v_y}, -v_x, -\dfrac{v_xv_z}{1+v_y})^T\\
        \hat{v}_{xyz} &= R_{\alpha}^{\hat{r}_v} (0,1,0)^T
        = (v_x, v_y, v_z)^T\\
        \hat{n}_{xyz} &= R_{\alpha}^{\hat{r}_v} (0,0,1)^T
        = (-\dfrac{v_xv_z}{1+v_y}, -v_z, 1 - \dfrac{v_z^2}{1+v_y})^T\\
      \end{aligned}

.. image:: ../../../images/cs-choice.png
  :alt: Examples of coordinate system choices
  :target: ../../_images/cs-choice.png

The spin vectors and exchange matrices under the change of the coordinate system:

.. math::
    \vec{S}^a = R_{\alpha}^{\hat{r}_v}(S_x^a, S_y^a, S_z^a)_{xyz}^T
    = (S_u^a, S_v^a, S_n^a)_{uvn}^T

.. math::

    J_{a,b}(\vec{d})
    = R_{\alpha}^{\hat{r}_v}
    \begin{pmatrix}
        J_{xx} & J_{xy} & J_{xz} \\
        J_{yx} & J_{yy} & J_{yz} \\
        J_{zx} & J_{zy} & J_{zz}
    \end{pmatrix}_{xyz} (R_{\alpha}^{\hat{r}_v})^T
    = \begin{pmatrix}
        J_{uu} & J_{uv} & J_{un} \\
        J_{vu} & J_{vv} & J_{vn} \\
        J_{nu} & J_{nv} & J_{nn}
    \end{pmatrix}_{uvn}

.. note::
    The properties of the exchange matrix should be preserved by the coordinate
    system change.
