.. _user-guide_methods_spin-roations:

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
  :file: ../../../images/spin-rotations-1.html

Any direction of the spin vector can be achieved from the direction of the
vector :math:`\hat{v}` by two consecutive rotations:

.. math::
  \vec{S} = R(\phi)R(\theta)\vec{S}^0
  = e^{\phi\hat{n}\times}e^{\theta\hat{v}\times}\vec{S}^0

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
    R = R(\phi)R(\theta) =
    \begin{pmatrix}
      \cos\phi\cdot\cos\theta & -\sin\phi & \cos\phi\cdot\sin\theta \\
      \sin\phi\cdot\cos\theta & \cos\phi  & \sin\phi\cdot\sin\theta \\
      -\sin\theta             & 0         & \cos\theta              \\
    \end{pmatrix}

Alternatively we can define one rotation, as it was done for the reference
frame change in :ref:`user-guide_methods_cs-choice`:

.. math::

    R^{\prime}(\theta, \phi) =
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

.. raw:: html
  :file: ../../../images/spin-rotations-2.html
