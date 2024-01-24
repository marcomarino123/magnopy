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
  * .. include:: page-notations/in-xyz.txt


The exchange and on-site anisotropy matrices are usually given in some global
reference frame :math:`xyz`. However, majority of the derivation happens in the
:math:`uvn` reference frame, which is defined by the cone axis :math:`\boldsymbol{\hat{n}}`.
The unit vectors :math:`\boldsymbol{\hat{u}}` and :math:`\boldsymbol{\hat{v}}` can be defined in a several
ways due to the rotational freedom around :math:`\boldsymbol{\hat{n}}` axis.

Here we explain which reference frame we choose given one unit vector :math:`\boldsymbol{\hat{n}}`.
The idea behind the choice is to rotate the :math:`\boldsymbol{\hat{z}}` axis of the global reference
frame to the direction of the given unit vector:

.. math::

  \boldsymbol{\hat{n}} =
  \begin{pmatrix}
    n^x \\
    n^y \\
    n^z \\
  \end{pmatrix} =
  \begin{pmatrix}
    \cos\beta\sin\alpha \\
    \sin\beta\sin\alpha \\
    \cos\alpha          \\
  \end{pmatrix}

.. raw:: html
  :file: ../../../images/uvn-choice-n-angles.html

.. note::
  * The given unit vector is called :math:`\boldsymbol{\hat{n}}`, because in the
    context of magnopy we will use the cone axis as a given vector.
  * We rotate the :math:`\boldsymbol{\hat{z}}` (not :math:`\boldsymbol{\hat{x}}` nor :math:`\boldsymbol{\hat{y}}`)
    to match :math:`\boldsymbol{\hat{n}}`, because in the context of magnopy we
    choose the cone axis to be the quantization axis.
  * When :math:`\boldsymbol{\hat{n}} = \pm\boldsymbol{\hat{z}}` the angle :math:`\beta` is not well defined,
    therefore, these two cases are treated separately.

* If :math:`\boldsymbol{\hat{n}} \ne \pm \boldsymbol{\hat{z}}`, then
  :math:`xyz` is rotated by the angle
  :math:`\alpha` around the axis :math:`\boldsymbol{\hat{r}}`

  .. dropdown:: Formulas

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

    .. math::
      :name: eq:uvn-choice-rot-matrix

      &\boldsymbol{R_{rf}}
      =
      \boldsymbol{R_{rf}}(\alpha,\beta)
      =
      \begin{pmatrix}
        1 - \dfrac{(n^x)^2}{1+n^z} & -\dfrac{n^xn^y}{1+n^z}   & n^x  \\
        -\dfrac{n^xn^y}{1+n^z}   & 1 - \dfrac{(n^y)^2}{1+n^z} & n^y  \\
        -n^x                     & -n^y                     & n^z  \\
      \end{pmatrix}
      =\\&=
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
        \boldsymbol{\hat{u}}
        &=
        \boldsymbol{R_{rf}} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
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
        \boldsymbol{R_{rf}} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
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
        \boldsymbol{R_{rf}} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
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

.. raw:: html
  :file: ../../../images/uvn-choice-main-case.html

* If :math:`\boldsymbol{\hat{n}} = \pm\boldsymbol{\hat{z}}`

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
        \boldsymbol{\hat{u}} &= \boldsymbol{\hat{x}}    \\
        \boldsymbol{\hat{v}} &= \pm\boldsymbol{\hat{y}} \\
        \boldsymbol{\hat{n}} &= \pm\boldsymbol{\hat{z}} \\
      \end{aligned}

.. raw:: html
  :file: ../../../images/uvn-choice-special-cases.html
