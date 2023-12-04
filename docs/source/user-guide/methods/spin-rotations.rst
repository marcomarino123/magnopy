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
  \vec{S} =R(\phi)R(\theta)\vec{S}^0
  = e^{\phi\hat{n}\times}e^{\theta\hat{v}\times}\vec{S}^0
