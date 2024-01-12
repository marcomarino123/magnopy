.. _user-guide_methods_spin-rotations:

**************
Spin rotations
**************


.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/unit-vector.txt
  * .. include:: page-notations/spin-unit-vector-operator.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/cross-product.txt
  * .. include:: page-notations/in-uvn.txt

Given a spin vector :math:`\vec{S}_a = S_a\cdot\hat{S}_a`, we define its direction
with two angles: :math:`\theta_a` and :math:`\phi_a`.

.. math::
  \vec{S}_a
  =
  S_a\cdot
  \begin{pmatrix}
    \sin\theta_a\cos\phi_a \\
    \sin\theta_a\sin\phi_a \\
    \cos\theta_a           \\
  \end{pmatrix}


.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

Any direction of the spin vector can be produced from the direction of the
vector :math:`\vec{n}` by a rotation around the vector :math:`\vec{r}` by
the angle :math:`\theta_a`, similarly to how it was done for the reference
frame change in :ref:`user-guide_methods_uvn-choice`:

.. math::
  \vec{r}
  =
  \dfrac{\hat{n} \times \vec{S}_a}{\vert\hat{n} \times \vec{S}_a\vert}
  =
  \begin{pmatrix}
    -\sin\phi_a \\
    \cos\phi_a  \\
    0           \\
  \end{pmatrix}

.. include:: repeated-formulas/spin-rotation-matrix-uvn.txt


Then the spin vector in the :math:`\vert uvn\rangle` reference frame can be written as:

.. math::
  \vec{S}_a
  =
  \boldsymbol{R}(\theta_a, \phi_a)\vec{S}_a^{ferro}
  =
  S_a\cdot \boldsymbol{R}(\theta_a, \phi_a)\hat{S}_a^{ferro}
  =
  S_a\cdot \boldsymbol{R}(\theta_a, \phi_a)\hat{n}

.. dropdown:: Bra-ket notation

  .. math::
    \langle uvn \vert S_a\rangle
    =
    \langle uvn \vert R(\theta_a, \phi_a) \vert S_a^{ferro} \rangle
    =
    \langle uvn \vert R(\theta_a, \phi_a) \vert uvn \rangle
    \langle uvn \vert S_a^{ferro} \rangle
    =
    S_a
    \cdot
    \langle uvn \vert R(\theta_a, \phi_a) \vert uvn \rangle
    \langle uvn \vert n \rangle


.. dropdown:: Alternative rotation

  Alternatively one can define two consecutive rotations:

  .. math::
    \vec{S}_a
    =
    \boldsymbol{R}(\phi_a) \boldsymbol{R}(\theta_a) \vec{S}_a^{ferro}
    =
    e^{\phi_a\hat{n}\times} e^{\theta_a\hat{v}\times} \vec{S}_a^{ferro}

  With the rotation matrices defined as:

  .. math::
    \begin{matrix}
      \boldsymbol{R}(\theta_a)
      =
      \begin{pmatrix}
        \cos\theta_a  & 0 & \sin\theta_a \\
        0           & 1 & 0              \\
        -\sin\theta_a & 0 & \cos\theta_a \\
      \end{pmatrix};
      &
      \boldsymbol{R}(\phi_a)
      =
      \begin{pmatrix}
        \cos\phi_a & -\sin\phi_a & 0 \\
        \sin\phi_a & \cos\phi_a  & 0 \\
        0        & 0         & 1     \\
      \end{pmatrix}
    \end{matrix}

  .. math::
      \boldsymbol{R^{\prime}}(\theta_a,\phi_a)
      =
      \boldsymbol{R}(\phi_a) \boldsymbol{R}(\theta_a) =
      \begin{pmatrix}
        \cos\phi_a\cdot\cos\theta_a & -\sin\phi_a & \cos\phi_a\cdot\sin\theta_a \\
        \sin\phi_a\cdot\cos\theta_a & \cos\phi_a  & \sin\phi_a\cdot\sin\theta_a \\
        -\sin\theta_a               & 0           & \cos\theta_a                \\
      \end{pmatrix}

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. note::
    We will NOT use the alternative rotation in the following pages.
