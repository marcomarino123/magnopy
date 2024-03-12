.. _user-guide_methods_spin-rotations:

**************
Spin rotations
**************


.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/cross-product.inc
  * .. include:: page-notations/uvn-or-spherical.inc

A key technical tool is the ability to rotate any atomic spin vector
:math:`\boldsymbol{S_i} = S_i\,\boldsymbol{\hat{S}_i}` into
the direction defined by the unit vector :math:`\hat{\boldsymbol{n}}`,
that determines the cone axis of the conical state. This rotated
spin vector will be denoted :math:`\boldsymbol{S_i^F}=S_i\,\boldsymbol{\hat{n}}`
henceforth.

.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

The figure above  shows that :math:`\boldsymbol{S_i^F}` is determined by the
angles :math:`\theta_i` and :math:`\phi_i`,
so that

.. math::
  \boldsymbol{S_i}
  =\,S_i\,
  \begin{pmatrix}
    \sin\theta_i\cos\phi_i \\
    \sin\theta_i\sin\phi_i \\
    \cos\theta_i           \\
  \end{pmatrix}

Then :math:`\boldsymbol{S_i}` can be obtained by rotating :math:`\boldsymbol{S_i^F}`
about the perpendicular unit vector

.. math::
  \boldsymbol{\hat{r}}(\phi_i)
  =
  \dfrac{\boldsymbol{\hat{n}} \times \boldsymbol{S_i}}{|\,\boldsymbol{\hat{n}} \times \boldsymbol{S_i}\,|}
  =
  \begin{pmatrix} -\sin\phi_i \\ \cos\phi_i  \\ 0  \\ \end{pmatrix}

by the angle :math:`\theta_i`. In other words,

.. math::
  \boldsymbol{S_i} = \boldsymbol{R_i}\,\boldsymbol{S_i^F} =
  \boldsymbol{R_{r(\phi_i)}}(\theta_i)\,\boldsymbol{S_i^F} =
  \boldsymbol{R_r}(\theta_i,\phi_i)\,\boldsymbol{S_i^F}

where the rotation matrix is

.. include:: repeated-formulas/spin-rotation-matrix-uvn.inc


.. dropdown:: Bra-ket notation

  .. math::
    \braket{\,u\, v\,n\,|\,S_i\,}
    =
    S_i\,\braket{\,u\, v\,n\, |\, \boldsymbol{\cal R}_i\,|\, n }
    =
    S_i\,\braket{\,u\, v\,n\, |\, \boldsymbol{\cal R}_i\,|\,u\, v\,n\,} \,
    \braket{\,u\, v\,n\,|\,  n}

.. dropdown:: Alternative rotation

  Alternatively one can rotate :math:`\boldsymbol{\hat{n}}` first about the
  :math:`\boldsymbol{\hat{v}}` axis by an angle :math:`\bar{\theta}_i`
  and afterwards about :math:`\boldsymbol{\hat{n}}` by an angle
  :math:`\bar{\phi}_i` as shown in the figure

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. math::
    \boldsymbol{S_i}
    =
    \boldsymbol{R}_n(\bar{\phi}_i) \,\boldsymbol{R}_v(\bar{\theta}_i) \,\boldsymbol{S_i^F}
    =
    e^{\bar{\phi}_i\,\boldsymbol{\hat{n}}\,\times}\, e^{\bar{\theta}_i\,\boldsymbol{\hat{v}}\,\times}
    \, \boldsymbol{S_i^F}

  where the rotation matrices are

  .. math::
    \begin{matrix}
      \boldsymbol{R}_v(\bar{\theta}_i)
      =
      \begin{pmatrix}
        \cos\bar{\theta}_i  & 0 & \sin\bar{\theta}_i \\
        0           & 1 & 0              \\
        -\sin\bar{\theta}_i & 0 & \cos\bar{\theta}_i \\
      \end{pmatrix};
      &
      \boldsymbol{R}_n(\bar{\phi}_i)
      =
      \begin{pmatrix}
        \cos\bar{\phi}_i & -\sin\bar{\phi}_i & 0 \\
        \sin\bar{\phi}_i & \cos\bar{\phi}_i  & 0 \\
        0        & 0         & 1     \\
      \end{pmatrix}
    \end{matrix}

  .. note::
    This alternative rotation is NOT used in Magnopy.
