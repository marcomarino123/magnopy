.. _user-guide_methods_spin-rotations:

**************
Spin rotations
**************


.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/unit-vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/cross-product.inc
  * .. include:: page-notations/uvn-or-spherical.inc
  * .. include:: page-notations/rotations.inc

At this moment we start to work in the :math:`(u\, v\, n)` reference frame. We are
left with the set of spin vectors, that are oriented in a way, that resembles the spiral
conical state of the Hamiltonian. However, as will be clear from the later derivations,
it is convenient to work with the ferromagnetic alignment of the spins. Therefore, a key
technical tool in magnopy is the ability to rotate any atomic spin vector

.. math::
  \boldsymbol{S_i}
  =
  S_i\, \boldsymbol{\hat{f}}_i
  =
  S_i
  \begin{pmatrix}
    \sin\theta_i\, \cos\phi_i \\
    \sin\theta_i\, \sin\phi_i \\
    \cos\theta_i              \\
  \end{pmatrix}

into the direction defined by the unit vector :math:`\hat{\boldsymbol{n}}`, thus
delivering the rotated "Ferromagnetic" spin vector
:math:`\boldsymbol{S^F}_i=S_i\, \boldsymbol{\hat{n}}`.

.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

The unit vector that defines the rotation axis is

.. math::
  \boldsymbol{\hat{r}}(\phi_i)
  =
  \dfrac{
    \boldsymbol{\hat{n}} \times \boldsymbol{S}_i
  }{
    |\, \boldsymbol{\hat{n}} \times \boldsymbol{S}_i\, |
  }
  =
  \begin{pmatrix}
    -\sin\phi_i \\
    \cos\phi_i  \\
    0           \\
  \end{pmatrix}

so that the rotation matrix is

.. include:: repeated-formulas/spin-rotation-matrix-uvn.inc

All in all,

.. include:: repeated-formulas/spin-from-ferro-any.inc

Furthermore, :math:`\boldsymbol{R}_i` can be applied to the :math:`(u\, v\, n)`
reference frame which result into the new basis defined by the unit vectors

.. math::
  \boldsymbol{\hat{p}}_i
  =
  \boldsymbol{R}_i\,\boldsymbol{\hat{u}}
  =
  \boldsymbol{R}_i\, \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\theta_i + \sin^2\phi_i\, \, (1-\cos\theta_i) \\
    -\sin\phi_i\, \cos\phi_i\, \, (1-\cos\theta_i)    \\
    -\cos\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  \boldsymbol{\hat{t}}_i
  =
  \boldsymbol{R}_i\, \boldsymbol{\hat{v}}
  =
  \boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    -\sin\phi_i\, \cos\phi_i\,(1-\cos\theta_i)      \\
    \cos\theta_i + \cos^2\phi_i\, (1-\cos\theta_i)  \\
    \sin\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  \boldsymbol{\hat{f}}_i
  =
  \boldsymbol{R}_i\, \boldsymbol{\hat{n}}
  =
  \boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\phi_i\, \sin\theta_i \\
    \sin\phi_i\, \sin\theta_i \\
    \cos\theta_i
  \end{pmatrix}

One could call this :math:`(p_i\, t_i\, f_i)` reference frame the "local reference
frame" or "rotated reference frame". We use the vectors :math:`\boldsymbol{\hat{p}_i}`,
:math:`\boldsymbol{\hat{t}_i}` and :math:`\boldsymbol{\hat{f}_i}` to describe the
direction of each individual spin in the unit cell, however, we will not refer to the
concept of the "local" reference frame in the following. In magnopy we define one global
reference frame :math:`(u\, v\, n)` that corresponds to the global spiral conical state
of the Hamiltonian. The introduction of the :math:`(p_i\, t_i\, f_i)` reference frame is
only a technical tool and we avoid it in order to reduce the amount of the reference
frames that are used in the formalism.


The rotation matrix can therefore be written as
:math:`\boldsymbol{R}_i=(\boldsymbol{\hat{p}_i}\, \boldsymbol{\hat{t}_i}\, \boldsymbol{\hat{f}_i})`.

.. dropdown:: Bra-ket notation

  .. math::
    \braket{\, u\, v\, n\, |\, p_i\, t_i\, f_i\, }
    =
    \braket{\, u\, v\, n\, |\, \boldsymbol{\cal R}_i\, |\, u\, v\, n\, }

.. dropdown:: Alternative rotation

  Alternatively one can rotate :math:`\boldsymbol{\hat{n}}` first about the
  :math:`\boldsymbol{\hat{v}}` axis by an angle :math:`\theta_i` and afterwards about
  :math:`\boldsymbol{\hat{n}}` by an angle :math:`\phi_i` as shown in the figure

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. math::
    \boldsymbol{S}_i
    =
    \boldsymbol{R_n}(\phi_i)\, \boldsymbol{R_v}(\theta_i)\, \boldsymbol{S^F}_i
    =
    e^{\phi_i\, \boldsymbol{\hat{n}}\, \times}\,
    e^{\theta_i\, \boldsymbol{\hat{v}}\, \times}\,
    \boldsymbol{S^F}_i

  where the rotation matrices are

  .. math::
    \begin{matrix}
      \boldsymbol{R_v}(\theta_i)
      =
      \begin{pmatrix}
        \cos\theta_i  & 0 & \sin\theta_i \\
        0             & 1 & 0            \\
        -\sin\theta_i & 0 & \cos\theta_i \\
      \end{pmatrix};
      &
      \boldsymbol{R_n}(\phi_i)
      =
      \begin{pmatrix}
        \cos\phi_i & -\sin\phi_i & 0 \\
        \sin\phi_i & \cos\phi_i  & 0 \\
        0          & 0           & 1 \\
      \end{pmatrix}
    \end{matrix}

  .. note::
    This alternative rotation is NOT used in Magnopy.
