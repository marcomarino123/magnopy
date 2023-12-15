.. _user-guide_methods_single-q:

**********************
Single-Q conical state
**********************

.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
  * :math:`\vec{v}` - is a vector.
  * Parenthesis () and braquets [] are equivalent.

Single-:math:`Q` conical state can be described by two vectors:

* Cone axis :math:`\hat{n}`.
  It defines the global rotational axis of the spiral.
  Note, that we orient the reference frame as described in
  :ref:`user-guide_methods_uvn-choice`, therefore, the cone axis :math:`\hat{n}`
  is one of the reference frame axes.
* Spiral vector :math:`\vec{Q}`. It defines the phase as:
  :math:`\theta_m = \vec{Q}\cdot\vec{r_m}`.


Spiral rotation matrix
======================

We describe the position of each spin :math:`S_{ma}` in the crystal with
the two vectors :math:`\vec{r}_m` and :math:`\vec{r}_a`, where

.. math::
  \vec{r}_m = i\cdot\vec{a} + j\cdot\vec{b} + k\cdot\vec{c}

Gives the coordinate of the unit cell, to which the spin :math:`\vec{S}_{ma}`
belongs. And vector :math:`\vec{r}_a` describe the spin's position
inside unit cell and does not depend on the index :math:`m`. Therefore, the
spin :math:`\vec{S}_{ma}` is located at the position

.. math::
  \vec{r}_{ma} = \vec{r}_m + \vec{r}_a

We assume that the spins inside the unit cell can be oriented independently.
The direction of each one is given by two angles :math:`\theta_a` and
:math:`\phi_a` as described :ref:`here <user-guide_methods_spin-rotations>`.
The spiral rotation is assumed to be applied based on the coordinate of the
unit cell :math:`\vec{r}_m` only:

.. include:: repeated-formulas/spiral-rotation-matrix-uvn.txt


Full spin rotation matrix
=========================

In the following sections we will need to produce the spin spiral ground
state from the ferromagnetically ordered state, where each spin
:math:`\vec{S}_{ma}^{ferro}` is oriented along the direction of the
cone axis :math:`\hat{n}`. In order to do that we combine rotations inside
each unit cell as described in the :ref:`user-guide_methods_spin-rotations`
section and in this section:

.. include:: repeated-formulas/spin-from-ferro-any.txt

where we recall

.. include:: repeated-formulas/spin-rotation-matrix-uvn.txt

Matrix :math:`R_{ma}` has the form:

.. math::
  R_{ma} =
  \begin{pmatrix}
  ... & ... & \sin\theta_a\cos(\vec{Q}\cdot\vec{r}_m + \phi_a)\\
  ... & ... & \sin\theta_a\sin(\vec{Q}\cdot\vec{r}_m + \phi_a) \\
  -\cos\phi_a\sin\theta_a & -\sin\phi_a\sin\theta_a & \cos\theta_a \\
  \end{pmatrix}

And the spin :math:`\vec{S}_{ma}` is

.. include:: repeated-formulas/spin-uvn.txt

.. dropdown:: All elements of the matrix  :math:`\text{ }R_{ma}`

  For simplicity of the notation we call the matrix :math:`R_{ma}`
  as :math:`R`:

  .. math::
    R_{ma} = R =
    \begin{pmatrix}
      R_{11} & R_{12} & R_{13} \\
      R_{21} & R_{22} & R_{23} \\
      R_{31} & R_{32} & R_{33} \\
    \end{pmatrix}

  .. math::
    &R_{11}
    =
    \cos(\vec{Q}\cdot\vec{r}_m)\left[\cos\theta_a + \sin^2\phi_a(1-\cos\theta_a)\right]-\sin(\vec{Q}\cdot\vec{r}_m)\left[-\sin\phi_a\cos\phi_a(1-\cos\theta_a)\right]
    \\&=
    (1-\cos\theta_a)\left[\cos(\vec{Q}\cdot\vec{r}_m)\sin^2\phi_a+\sin(\vec{Q}\cdot\vec{r}_m)\sin\phi_a\cos\phi_a\right]+\cos(\vec{Q}\cdot\vec{r}_m)\cos\theta_a
    \\&=
    (1-\cos\theta_a)\sin\phi_a\sin(\vec{Q}\cdot\vec{r}_m+\phi_a)+\cos(\vec{Q}\cdot\vec{r}_m)\cos\theta_a

  .. math::
    &R_{12}
    =
    \cos(\vec{Q}\cdot\vec{r}_m)\left[-\sin\phi_a\cos\phi_a(1-\cos\theta_a)\right]-\sin(\vec{Q}\cdot\vec{r}_m)\left[\cos\theta_a + \cos^2\phi_a(1-\cos\theta_a)\right]
    \\&=
    (1-\cos\theta_a)\left[-\cos(\vec{Q}\cdot\vec{r}_m)\sin\phi_a\cos\phi_a-\sin(\vec{Q}\cdot\vec{r}_m)\cos^2\phi_a\right]-\sin(\vec{Q}\cdot\vec{r}_m)\cos\theta_a
    \\&=
    -(1-\cos\theta_a)\cos\phi_a\sin(\vec{Q}\cdot\vec{r}_m+\phi_a)-\sin(\vec{Q}\cdot\vec{r}_m)\cos\theta_a

  .. math::
    R_{13}
    =
    \sin\theta_a(\cos(\vec{Q}\cdot\vec{r}_m)\cos\phi_a - \sin(\vec{Q}\cdot\vec{r}_m)\sin\phi_a)
    =
    \sin\theta_a\cos(\vec{Q}\cdot\vec{r}_m + \phi_a)

  .. math::
    &R_{21}
    =
    \sin(\vec{Q}\cdot\vec{r}_m)\left[\cos\theta_a + \sin^2\phi_a(1-\cos\theta_a)\right]+\cos(\vec{Q}\cdot\vec{r}_m)\left[-\sin\phi_a\cos\phi_a(1-\cos\theta_a)\right]
    \\&=
    (1-\cos\theta_a)\left[\sin(\vec{Q}\cdot\vec{r}_m)\sin^2\phi_a-\cos(\vec{Q}\cdot\vec{r}_m)\sin\phi_a\cos\phi_a\right]+\sin(\vec{Q}\cdot\vec{r}_m)\cos\theta_a
    \\&=
    -(1-\cos\theta_a)\sin\phi_a\cos(\vec{Q}\cdot\vec{r}_m+\phi_a)+\sin(\vec{Q}\cdot\vec{r}_m)\cos\theta_a

  .. math::
    &R_{22}
    =
    \sin(\vec{Q}\cdot\vec{r}_m)\left[-\sin\phi_a\cos\phi_a(1-\cos\theta_a)\right]+\cos(\vec{Q}\cdot\vec{r}_m)\left[\cos\theta_a + \cos^2\phi_a(1-\cos\theta_a)\right]
    \\&=
    (1-\cos\theta_a)\left[-\sin(\vec{Q}\cdot\vec{r}_m)\sin\phi_a\cos\phi_a+\cos(\vec{Q}\cdot\vec{r}_m)\cos^2\phi_a\right]+\cos(\vec{Q}\cdot\vec{r}_m)\cos\theta_a
    \\&=
    (1-\cos\theta_a)\cos\phi_a\cos(\vec{Q}\cdot\vec{r}_m+\phi_a)+\cos(\vec{Q}\cdot\vec{r}_m)\cos\theta_a

  .. math::
    R_{23}
    =
    \sin\theta_a(\sin(\vec{Q}\cdot\vec{r}_m)\cos\phi_a + \cos(\vec{Q}\cdot\vec{r}_m)\sin\phi_a)
    =
    \sin\theta_a\sin(\vec{Q}\cdot\vec{r}_m + \phi_a)

  .. math::
    R_{31} = -\cos\phi_a\sin\theta_a

  .. math::
    R_{32} = -\sin\phi_a\sin\theta_a

  .. math::
    R_{33} = \cos\theta_a


Examples
========

* One spin in the unit cell, :math:`\vec{Q} = (0,0,1)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 90^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-1.html

* One spin in the unit cell, :math:`\vec{Q} = (0,0,1)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-2.html

* One spin in the unit cell, :math:`\vec{Q} = (0,0,1)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 45^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-3.html

* One spin in the unit cell, :math:`\vec{Q} = (0,1,0)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-4.html

* Two spins in the unit cell, :math:`\vec{Q} = (0,1,0)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\vec{r}_2 = (\frac{1}{2},\frac{1}{2},\frac{1}{2})`,
    :math:`\theta_2 = 20^{\circ}`,
    :math:`\phi_2 = 45^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-5.html

* Two spins in the unit cell, :math:`\vec{Q} = (1,0,0)^T`:

  - :math:`\vec{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 150^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\vec{r}_2 = (0,\frac{1}{2},0)`,
    :math:`\theta_2 = 30^{\circ}`,
    :math:`\phi_2 =180^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-6.html
