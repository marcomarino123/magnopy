.. _user-guide_methods_rf-choice:

*****************************
Choice of the reference frame
*****************************

.. dropdown:: Notation used on this page

  * :math:`\vec{v}` - is a vector.
  * :math:`\hat{v}` - is a unit vector, corresponding to the
    vector :math:`\vec{v}`.
  * :math:`\times` - means cross product for vectors.
  * "reference frame" = "coordinate system" = "basis"
  * On this page all vectors and matrices are written in the
    :math:`\hat{x}\hat{y}\hat{z}` reference frame.


The exchange and on-site anisotropy matrices are usually given in
some global reference frame :math:`\hat{x}\hat{y}\hat{z}`.
However, majority of the derivation happens in the
:math:`\hat{u}\hat{v}\hat{n}` reference frame, which is defined by the cone
axis :math:`\hat{v}`. The unit vectors :math:`\hat{u}` and
:math:`\hat{v}` can be defined in a several ways due to the rotational freedom
around :math:`\hat{n}` axis.

Here we explain which reference frame we choose given one unit vector
:math:`\hat{n}`. The idea behind the choice is to rotate the :math:`\hat{z}`
axis of the global reference frame to the direction of the given unit vector:

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
  :file: ../../../images/rf-choice-n-angles.html

.. note::
  * The given unit vector is called :math:`\hat{n}`, because in the
    context of magnopy we will use the cone axis as a given vector.
  * We rotate the :math:`\hat{z}` (not :math:`\hat{x}` or :math:`\hat{y}`)
    to match :math:`\hat{n}`, because in the context of magnopy we
    choose the cone axis to be the quantization axis.
  * When :math:`\hat{n} = \pm\hat{z}` the angle :math:`\beta` is not well defined,
    therefore, these two cases are treated separately below.

* If :math:`\hat{n} \ne \pm \hat{z}`, then
  :math:`\hat{x}\hat{y}\hat{z}` is rotated by the angle
  :math:`\alpha` around the axis :math:`\hat{r}`

  .. math::

    \begin{aligned}
      \hat{r}(\alpha,\beta) &= \dfrac{\hat{z}\times\hat{n}}
      {\vert\hat{z}\times\hat{n}\vert} =
      \begin{pmatrix}
        -\sin\beta \\
        \cos\beta \\
        0
      \end{pmatrix}
    \end{aligned}

  .. math::
    :name: eq:rf-choice-rot-matrix

    R_{rf} = R_{rf}(\alpha,\beta) =
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
      \hat{u} &= R_{rf} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
      =
      \begin{pmatrix}
        \cos\alpha + \sin^2\beta(1-\cos\alpha) \\
        -\sin\beta\cos\beta(1-\cos\alpha) \\
        -\cos\beta\sin\alpha \\
      \end{pmatrix}
      =
      \begin{pmatrix}
        1 - \dfrac{n_x^2}{1+n_z} \\
        -\dfrac{n_xn_y}{1+n_z} \\
        -n_x
      \end{pmatrix} \\
      \hat{v} &= R_{rf} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
      =
      \begin{pmatrix}
        -\sin\beta\cos\beta(1-\cos\alpha) \\
        \cos\alpha + \cos^2\beta(1-\cos\alpha) \\
        -\sin\beta\sin\alpha
      \end{pmatrix}
      =
      \begin{pmatrix}
        -\dfrac{n_xn_y}{1+n_z} \\
        1 - \dfrac{n_y^2}{1+n_z} \\
        -n_y
      \end{pmatrix} \\
      \hat{n} &= R_{rf} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
      =
      \begin{pmatrix}
        \cos\beta\sin\alpha \\
        \sin\beta\sin\alpha \\
        \cos\alpha
      \end{pmatrix}
      =
      \begin{pmatrix}
        n_x \\
        n_y \\
        n_z
      \end{pmatrix}
    \end{aligned}


.. raw:: html
  :file: ../../../images/rf-choice-main-case.html

* If :math:`\hat{n} = \pm\hat{z}`

  .. math::
    \begin{matrix}
      \begin{aligned}
        \hat{u} &= \hat{x} \\
        \hat{v} &= \pm\hat{y} \\
        \hat{n} &= \pm\hat{z} \\
      \end{aligned} & \text{ and } &
      R_{rf} =
      \begin{pmatrix}
        1 & 0     & 0 \\
        0 & \pm 1 & 0 \\
        0 & 0     & \pm 1 \\
      \end{pmatrix}
      = R_{rf}(\alpha = \dfrac{\pi \mp \pi}{2}, \beta = \pi/2)
    \end{matrix}

.. raw:: html
  :file: ../../../images/rf-choice-special-cases.html
