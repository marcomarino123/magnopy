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
  :file: ../../../images/uvn-choice-main-case.html

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
    :file: ../../../images/uvn-choice-n-angles.html

  The rotation matrix is

  .. math::
    :name: eq:uvn-choice-rot-matrix

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

However, the unit vector :math:`\boldsymbol{\hat{r}}` is ill-defined, and so is
:math:`\boldsymbol{R_r}`, whenever  :math:`\boldsymbol{\hat{n}}` and
:math:`\pm\boldsymbol{\hat{z}}` are collinear. We then choose
:math:`\boldsymbol{\hat{r}}=-\boldsymbol{\hat{x}}` and rotate
:math:`\boldsymbol{\hat{z}}` by either 0 or :math:`\pi` degrees
for the parallel or antiparallel cases, respectively, as shown in the figure below.

.. raw:: html
  :file: ../../../images/uvn-choice-special-cases.html

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
