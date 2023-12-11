.. _user-guide_methods_spin-rotations:

**************
Spin rotations
**************


.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
  * :math:`\vec{v}` - is a vector.
  * :math:`\hat{v}` - is a unit vector, corresponding to the
    vector :math:`\vec{v}`.
  * :math:`v` - is a modulus of the vector :math:`\vec{v}`.

Given a spin vector :math:`\vec{S} = S\cdot\hat{S}`, we define its direction
with two angles: :math:`\theta` and :math:`\phi`.

.. math::
  \vec{S} =
  \begin{pmatrix}
    \sin\theta\cos\phi \\
    \sin\theta\sin\phi \\
    \cos\theta
  \end{pmatrix}


.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

Any direction of the spin vector can be produced from the direction of the
vector :math:`\vec{n}` by a rotation around the vector :math:`r` with
the angle :math:`\theta`, similary to how it was done for the reference
frame change in :ref:`user-guide_methods_rf-choice`:

.. math::
  \vec{r} = \dfrac{\hat{n} \times \vec{S}}{\vert\hat{n} \times \vec{S}\vert}
  = \begin{pmatrix}
    -\sin\phi \\
    \cos\phi \\
    0
  \end{pmatrix}

.. math::

    R(\theta, \phi) =
    \begin{pmatrix}
      \cos\theta + \sin^2\phi(1-\cos\theta) &
      -\sin\phi\cos\phi(1-\cos\theta) &
      \cos\phi\sin\theta  \\
      -\sin\phi\cos\phi(1-\cos\theta) &
      \cos\theta + \cos^2\phi(1-\cos\theta) &
      \sin\phi\sin\theta  \\
      -\cos\phi\sin\theta &
      -\sin\phi\sin\theta &
      \cos\theta \\
    \end{pmatrix}


Than the spin vector in the :math:`\vert uvn\rangle` reference frame can be written as:

.. math::
  \vec{S} = R(\theta, \phi)\vec{S}^{ferro}
  = S\cdot R(\theta, \phi)\hat{S}^{ferro}
  = S\cdot R(\theta, \phi)\hat{n}

.. dropdown:: Bra-ket notation

  .. math::
    \langle uvn\vert S\rangle = \langle uvn\vert R(\theta, \phi) \vert S^{ferro}\rangle
    = \langle uvn\vert R(\theta, \phi)\vert uvn \rangle
    \langle uvn \vert S^{ferro}\rangle
    = S\cdot\langle uvn\vert R(\theta, \phi)\vert uvn \rangle
    \langle uvn \vert n\rangle


.. dropdown:: Alternative rotation

  Alternatively one can define two consecutive rotations:

  .. math::
    \vec{S} = R(\phi)R(\theta)\vec{S}^{ferro}
    = e^{\phi\hat{n}\times}e^{\theta\hat{v}\times}\vec{S}^{ferro}

  With the rotation matrices defined as:

  .. math::
    \begin{matrix}
      R(\theta) =
      \begin{pmatrix}
        \cos\theta  & 0 & \sin\theta \\
        0           & 1 & 0          \\
        -\sin\theta & 0 & \cos\theta \\
      \end{pmatrix};
      &
      R(\phi) =
      \begin{pmatrix}
        \cos\phi & -\sin\phi & 0 \\
        \sin\phi & \cos\phi  & 0 \\
        0        & 0         & 1 \\
      \end{pmatrix}
    \end{matrix}

  .. math::
      R^{\prime}(\theta,\phi) = R(\phi)R(\theta) =
      \begin{pmatrix}
        \cos\phi\cdot\cos\theta & -\sin\phi & \cos\phi\cdot\sin\theta \\
        \sin\phi\cdot\cos\theta & \cos\phi  & \sin\phi\cdot\sin\theta \\
        -\sin\theta             & 0         & \cos\theta              \\
      \end{pmatrix}

  .. raw:: html
    :file: ../../../images/spin-rotations-simple.html

  .. note::
    We will not use the latter rotation in the following pages.
