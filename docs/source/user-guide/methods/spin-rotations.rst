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

A key technical tool in magnopy is the ability to rotate any atomic spin vector

.. math::
  \boldsymbol{S_i} = S_i\,\boldsymbol{\hat{f}}_i
  =\,S_i\,
  \begin{pmatrix}
    \sin\theta_i\cos\phi_i \\
    \sin\theta_i\sin\phi_i \\
    \cos\theta_i           \\
  \end{pmatrix}

into the direction defined by the unit vector :math:`\hat{\boldsymbol{n}}`,
thus delivering the rotated spin vector :math:`\boldsymbol{S^F}_i=S_i\,\boldsymbol{\hat{n}}`.

.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

The unit vector that defines the rotation axis is

.. math::
  \boldsymbol{\hat{r}}(\phi_i)
  =
  \dfrac{\boldsymbol{\hat{n}} \times \boldsymbol{S}_i}{|\,\boldsymbol{\hat{n}} \times \boldsymbol{S}_i\,|}
  =
  \begin{pmatrix} -\sin\phi_i \\ \cos\phi_i  \\ 0  \\ \end{pmatrix}

so that the rotation matrix is

.. math::
  \boldsymbol{R}_i=
  e^{\boldsymbol{\hat{r}}(\phi_i)\,\theta_i\,\times}
    =
  \begin{pmatrix}
    \cos\theta_i+\sin^2\phi_i\,(1-cos\theta_i)  & -\sin\phi_i\,\cos\theta_i\,(1-\cos\theta_i) & \cos\phi_i\,\sin\theta_i \\
    -\sin\phi_i\,\cos\theta_i\,(1-\cos\theta_i) & \cos\theta_i+\sin^2\phi_i\,(1-cos\theta_i)  & \sin\phi_i\,\cos\theta_i \\
    -\cos\phi_i\,\sin\theta_i                   & \sin\phi_i\,\cos\theta_i                    & \cos\theta_i \\
  \end{pmatrix}

All in all,

.. math::
  \boldsymbol{S}_i = \boldsymbol{R}_i\,\boldsymbol{S^F}_i

Furthermore, :math:`\boldsymbol{R}_i` rotates the :math:`(\,u\,v\,n\,)` reference frame
into a new basis spanned by the unit vectors

.. math::
  \boldsymbol{\hat{p}}_i=\boldsymbol{R}_i\,\boldsymbol{\hat{u}}=
  \begin{pmatrix}
    \cos\theta_i+\sin^2\phi_i\,(1-cos\theta_i)  \\
    -\sin\phi_i\,\cos\theta_i\,(1-\cos\theta_i)  \\
    -\cos\phi_i\,\sin\theta_i
  \end{pmatrix}

.. math::
  \boldsymbol{\hat{t}}_i=\boldsymbol{R}_i\,\boldsymbol{\hat{v}}=
 \begin{pmatrix}
   -\sin\phi_i\,\cos\theta_i\,(1-\cos\theta_i)  \\
    \cos\theta_i+\sin^2\phi_i\,(1-cos\theta_i)   \\
    \sin\phi_i\,\cos\theta_i
  \end{pmatrix}

.. math::
  \boldsymbol{\hat{f}}_i=\boldsymbol{R}_i\,\boldsymbol{\hat{n}}=
    \begin{pmatrix}
    \cos\phi_i\,\sin\theta_i \\
    \sin\phi_i\,\cos\theta_i \\
    \cos\theta_i
  \end{pmatrix}

The rotation matrix can therefore be written as
:math:`\boldsymbol{R}_i=(\boldsymbol{\hat{p}_i}\,\boldsymbol{\hat{t}_i}\,\boldsymbol{\hat{f}_i})`.

.. dropdown:: Bra-ket notation

  .. math::
    \braket{\,u\, v\,n\,|\,p_i\,t_i\,f_i}
    =
    \braket{\,u\, v\,n\, |\, \boldsymbol{\cal R}_i\,|\,u\,v\, n }

.. dropdown:: Alternative rotation

  Alternatively one can rotate :math:`\boldsymbol{\hat{n}}` first about the
  :math:`\boldsymbol{\hat{v}}` axis by an angle :math:`\theta_i`
  and afterwards about :math:`\boldsymbol{\hat{n}}` by an angle
  :math:`\phi_i` as shown in the figure

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. math::
    \boldsymbol{S}_i
    =
    \boldsymbol{R_n}(\phi_i) \,\boldsymbol{R_v}(\theta_i) \,\boldsymbol{S^F}_i
    =
    e^{\phi_i\,\boldsymbol{\hat{n}}\,\times}\, e^{\theta_i\,\boldsymbol{\hat{v}}\,\times}
    \, \boldsymbol{S^F}_i

  where the rotation matrices are

  .. math::
    \begin{matrix}
      \boldsymbol{R_v}(\theta_i)
      =
      \begin{pmatrix}
        \cos\theta_i  & 0 & \sin\theta_i \\
        0           & 1 & 0              \\
        -\sin\theta_i & 0 & \cos\theta_i \\
      \end{pmatrix};
      &
      \boldsymbol{R_n}(\phi_i)
      =
      \begin{pmatrix}
        \cos\phi_i & -\sin\phi_i & 0 \\
        \sin\phi_i & \cos\phi_i  & 0 \\
        0        & 0         & 1     \\
      \end{pmatrix}
    \end{matrix}

  .. note::
    This alternative rotation is NOT used in Magnopy.
