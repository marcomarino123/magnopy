.. _user-guide_methods_spin-rotations:

**************
Spin rotations
**************


.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/unit-vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/cross-product.txt
  * .. include:: page-notations/in-uvn.txt

Given a spin vector :math:`\boldsymbol{S_i} = S_i\cdot\boldsymbol{\hat{S}_i}`, we define its direction
with two angles: :math:`\theta_i` and :math:`\phi_i`.

.. math::
  \boldsymbol{S_i}
  =
  S_i\cdot
  \begin{pmatrix}
    \sin\theta_i\cos\phi_i \\
    \sin\theta_i\sin\phi_i \\
    \cos\theta_i           \\
  \end{pmatrix}


.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

Any direction of the spin vector can be produced from the direction of the
vector :math:`\boldsymbol{n}` by a rotation around the vector :math:`\boldsymbol{\hat{r}}` by
the angle :math:`\theta_i`, similarly to how it was done for the reference
frame change in :ref:`user-guide_methods_uvn-choice`:

.. math::
  \boldsymbol{\hat{r}}
  =
  \dfrac{\boldsymbol{\hat{n}} \times \boldsymbol{S_i}}{\vert\boldsymbol{\hat{n}} \times \boldsymbol{S_i}\vert}
  =
  \begin{pmatrix}
    -\sin\phi_i \\
    \cos\phi_i  \\
    0           \\
  \end{pmatrix}

.. include:: repeated-formulas/spin-rotation-matrix-uvn.txt


Then the spin vector in the :math:`\vert uvn\rangle` reference frame can be written as:

.. math::
  \boldsymbol{S_i}
  =
  \boldsymbol{R}(\theta_i, \phi_i)\boldsymbol{S_i^{ferro}}
  =
  S_i\cdot \boldsymbol{R}(\theta_i, \phi_i)\boldsymbol{\hat{S}_i^{ferro}}
  =
  S_i\cdot \boldsymbol{R}(\theta_i, \phi_i)\boldsymbol{\hat{n}}

.. dropdown:: Bra-ket notation

  .. math::
    \langle uvn \vert S_i\rangle
    =
    \langle uvn \vert R(\theta_i, \phi_i) \vert S_i^{ferro} \rangle
    =
    \langle uvn \vert R(\theta_i, \phi_i) \vert uvn \rangle
    \langle uvn \vert S_i^{ferro} \rangle
    =
    S_i
    \cdot
    \langle uvn \vert R(\theta_i, \phi_i) \vert uvn \rangle
    \langle uvn \vert n \rangle


.. dropdown:: Alternative rotation

  Alternatively one can define two consecutive rotations:

  .. math::
    \boldsymbol{S_i}
    =
    \boldsymbol{R}(\phi_i) \boldsymbol{R}(\theta_i) \boldsymbol{S_i^{ferro}}
    =
    e^{\phi_i\boldsymbol{\hat{n}}\times} e^{\theta_i\boldsymbol{\hat{v}}\times} \boldsymbol{S_i^{ferro}}

  With the rotation matrices defined as:

  .. math::
    \begin{matrix}
      \boldsymbol{R}(\theta_i)
      =
      \begin{pmatrix}
        \cos\theta_i  & 0 & \sin\theta_i \\
        0           & 1 & 0              \\
        -\sin\theta_i & 0 & \cos\theta_i \\
      \end{pmatrix};
      &
      \boldsymbol{R}(\phi_i)
      =
      \begin{pmatrix}
        \cos\phi_i & -\sin\phi_i & 0 \\
        \sin\phi_i & \cos\phi_i  & 0 \\
        0        & 0         & 1     \\
      \end{pmatrix}
    \end{matrix}

  .. math::
      \boldsymbol{R^{\prime}}(\theta_i,\phi_i)
      =
      \boldsymbol{R}(\phi_i) \boldsymbol{R}(\theta_i) =
      \begin{pmatrix}
        \cos\phi_i\cdot\cos\theta_i & -\sin\phi_i & \cos\phi_i\cdot\sin\theta_i \\
        \sin\phi_i\cdot\cos\theta_i & \cos\phi_i  & \sin\phi_i\cdot\sin\theta_i \\
        -\sin\theta_i               & 0           & \cos\theta_i                \\
      \end{pmatrix}

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. note::
    We will NOT use the alternative rotation in the following pages.
