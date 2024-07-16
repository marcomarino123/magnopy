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

We assume that the ground state of the spin system follows an spiral conical
spin arrangement, where the cone axis lies along the direction defined by
the unit vector :math:`\boldsymbol{\hat{n}}`. We define the :math:`(u\, v\, n)`
reference frame as discussed in the previous section.

Convenience dictates that spins should be quantized along a global quantization
axis, that we choose here to be :math:`\boldsymbol{\hat{n}}`. Therefore, a key
technical tool in magnopy is the ability to rotate any atomic spin vector
:math:`\boldsymbol{S_{i}}=S_i\, \boldsymbol{\hat{f}_{i}}` into the direction
defined by :math:`\hat{\boldsymbol{n}}`, thus delivering the rotated "Ferromagnetic"
spin vector :math:`\boldsymbol{S^F_{i}}=S_i\, \boldsymbol{\hat{n}}`. We assume
henceforth that the spin vector coordinates in the :math:`(u\, v\, n)`
reference frame are

.. math::
  ^n\boldsymbol{\hat{f}_{i}}
  =
  \begin{pmatrix}
    \sin\theta_{i}\, \cos\phi_{i} \\
    \sin\theta_{i}\, \sin\phi_{i} \\
    \cos\theta_{i}              \\
  \end{pmatrix}



.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

.. rst-class:: plotly-figure-caption

  **Figure 1** (interactive): Vectors and angles used in the spin rotations.

The unit vector that defines the rotation axis is defined by
:math:`\boldsymbol{\hat{r}}(\phi_i)=\dfrac{\boldsymbol{\hat{n}}
\times \boldsymbol{S}_i}{|\, \boldsymbol{\hat{n}} \times \boldsymbol{S}_i\, |}`.

so that the rotation matrix is
:math:`\boldsymbol{R_i}=e^, {-i\,\theta_i\,\boldsymbol{\hat{r}_i}\,\times}`
with matrix elements in the :math:`(u\, v\, n)` reference frame

.. math::
  ^n\boldsymbol{\hat{r}_i}=\braket{\,u\,v\,n\,|\,r_i}=
  \begin{pmatrix}
    -\sin\phi_i \\
    \cos\phi_i  \\
    0           \\
  \end{pmatrix}

and

.. include:: repeated-formulas/spin-rotation-matrix-uvn.inc

All in all, we arrive at

.. include:: repeated-formulas/spin-from-ferro-any.inc

Furthermore, a new "local" or "rotated "reference frame
:math:`(p_i\, t_i\, f_i)` can
be obtained by applying the rotation :math:`\boldsymbol{R}_i` to the
:math:`(u\, v\, n)` reference frame. The coordinates of the new basis vectors
are

.. math::
  ^n\boldsymbol{\hat{p}}_i
  \,=\,
  ^n\boldsymbol{R}_i\,^n\boldsymbol{\hat{u}}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\theta_i + \sin^2\phi_i\, \, (1-\cos\theta_i) \\
    -\sin\phi_i\, \cos\phi_i\, \, (1-\cos\theta_i)    \\
    -\cos\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  ^n\boldsymbol{\hat{t}}_i
  \,=\,
  ^n\boldsymbol{R}_i\, ^n\boldsymbol{\hat{v}}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    -\sin\phi_i\, \cos\phi_i\,(1-\cos\theta_i)      \\
    \cos\theta_i + \cos^2\phi_i\, (1-\cos\theta_i)  \\
    \sin\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  ^n\boldsymbol{\hat{f}}_i
  \,=\,
  ^n\boldsymbol{R}_i\, ^n\boldsymbol{\hat{n}}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\phi_i\, \sin\theta_i \\
    \sin\phi_i\, \sin\theta_i \\
    \cos\theta_i
  \end{pmatrix}

We use the basis vectors :math:`\boldsymbol{\hat{p}_i}`,
:math:`\boldsymbol{\hat{t}_i}` and :math:`\boldsymbol{\hat{f}_i}` to describe the
direction of each individual spin in the unit cell. All in all, magnopy defines
a single global reference frame :math:`(u\, v\, n)`. Local reference frames
:math:`(p_i\, t_i\, f_i)` are rotated towards :math:`(u\, v\, n)`.

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
