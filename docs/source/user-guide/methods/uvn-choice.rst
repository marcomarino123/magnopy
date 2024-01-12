.. _user-guide_methods_uvn-choice:

*********************************
Choice of the uvn reference frame
*********************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/unit-vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/cross-product.txt
  * On this page all vectors and matrices are written in the
    :math:`xyz` reference frame.


The exchange and on-site anisotropy matrices are usually given in some global
reference frame :math:`xyz`. However, majority of the derivation happens in the
:math:`uvn` reference frame, which is defined by the cone axis :math:`\hat{n}`.
The unit vectors :math:`\hat{u}` and :math:`\hat{v}` can be defined in a several
ways due to the rotational freedom around :math:`\hat{n}` axis.

Here we explain which reference frame we choose given one unit vector :math:`\hat{n}`.
The idea behind the choice is to rotate the :math:`\hat{z}` axis of the global reference
frame to the direction of the given unit vector:

.. math::

  \hat{n} =
  \begin{pmatrix}
    n_x \\
    n_y \\
    n_z \\
  \end{pmatrix} =
  \begin{pmatrix}
    \cos\beta\sin\alpha \\
    \sin\beta\sin\alpha \\
    \cos\alpha          \\
  \end{pmatrix}

.. raw:: html
  :file: ../../../images/uvn-choice-n-angles.html

.. note::
  * The given unit vector is called :math:`\hat{n}`, because in the
    context of magnopy we will use the cone axis as a given vector.
  * We rotate the :math:`\hat{z}` (not :math:`\hat{x}` nor :math:`\hat{y}`)
    to match :math:`\hat{n}`, because in the context of magnopy we
    choose the cone axis to be the quantization axis.
  * When :math:`\hat{n} = \pm\hat{z}` the angle :math:`\beta` is not well defined,
    therefore, these two cases are treated separately.

* If :math:`\hat{n} \ne \pm \hat{z}`, then
  :math:`xyz` is rotated by the angle
  :math:`\alpha` around the axis :math:`\hat{r}`

  .. dropdown:: Formulas

    .. math::

      \hat{r}(\alpha,\beta)
      =
      \dfrac{\hat{z}\times\hat{n}}{\vert\hat{z}\times\hat{n}\vert}
      =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta \\
        0
      \end{pmatrix}

    .. math::
      :name: eq:uvn-choice-rot-matrix

      &\boldsymbol{R_{rf}}
      =
      \boldsymbol{R_{rf}}(\alpha,\beta)
      =
      \begin{pmatrix}
        1 - \dfrac{n_x^2}{1+n_z} & -\dfrac{n_xn_y}{1+n_z}   & n_x  \\
        -\dfrac{n_xn_y}{1+n_z}   & 1 - \dfrac{n_y^2}{1+n_z} & n_y  \\
        -n_x                     & -n_y                     & n_z  \\
      \end{pmatrix}
      \\&=
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
      \end{pmatrix}

    .. math::

      \begin{aligned}
        \hat{u}
        &=
        \boldsymbol{R_{rf}} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
        =
        \begin{pmatrix}
          1 - \dfrac{n_x^2}{1+n_z} \\
          -\dfrac{n_xn_y}{1+n_z}   \\
          -n_x                     \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          \cos\alpha + \sin^2\beta(1-\cos\alpha) \\
          -\sin\beta\cos\beta(1-\cos\alpha)      \\
          -\cos\beta\sin\alpha                   \\
        \end{pmatrix}
        \\
        \hat{v}
        &=
        \boldsymbol{R_{rf}} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
        =
        \begin{pmatrix}
          -\dfrac{n_xn_y}{1+n_z}   \\
          1 - \dfrac{n_y^2}{1+n_z} \\
          -n_y                     \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          -\sin\beta\cos\beta(1-\cos\alpha)      \\
          \cos\alpha + \cos^2\beta(1-\cos\alpha) \\
          -\sin\beta\sin\alpha                   \\
        \end{pmatrix}
        \\
        \hat{n}
        &=
        \boldsymbol{R_{rf}} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
        =
        \begin{pmatrix}
          n_x \\
          n_y \\
          n_z \\
        \end{pmatrix}
        =
        \begin{pmatrix}
          \cos\beta\sin\alpha \\
          \sin\beta\sin\alpha \\
          \cos\alpha          \\
        \end{pmatrix}
      \end{aligned}

.. raw:: html
  :file: ../../../images/uvn-choice-main-case.html

* If :math:`\hat{n} = \pm\hat{z}`

  .. dropdown:: Formulas

    .. math::
      \boldsymbol{R_{rf}}
      =
      \begin{pmatrix}
        1 & 0     & 0     \\
        0 & \pm 1 & 0     \\
        0 & 0     & \pm 1 \\
      \end{pmatrix}
      =
      \boldsymbol{R_{rf}}(\alpha = \dfrac{\pi \mp \pi}{2}, \beta = \pi/2)
    .. math::
      \begin{aligned}
        \hat{u} &= \hat{x}    \\
        \hat{v} &= \pm\hat{y} \\
        \hat{n} &= \pm\hat{z} \\
      \end{aligned}

.. raw:: html
  :file: ../../../images/uvn-choice-special-cases.html
