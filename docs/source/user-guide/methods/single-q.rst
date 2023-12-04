.. _user-guide_methods_single-q:

**********************
Single-Q conical state
**********************

.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
  * :math:`\vec{v}` - is a vector.

Single-:math:`Q` conical state can be described by two vectors:

* Cone axis :math:`\hat{n}`.
  It defines the global rotational axis of the spiral.
  Note, that we orient the reference frame as described in
  :ref:`user-guide_methods_rf-choice`, therefore, the cone axis :math:`\hat{n}`
  is one of the reference frame axes.
* Spiral vector :math:`\vec{Q}`. It defines the phase as:
  :math:`\theta_m = \vec{Q}\cdot\vec{R_m}`.

Several examples of the conical structures are shown in the pictures below.

.. raw:: html
  :file: ../../../images/single-q-1.html

.. raw:: html
  :file: ../../../images/single-q-2.html

.. raw:: html
  :file: ../../../images/single-q-3.html

.. raw:: html
  :file: ../../../images/single-q-4.html

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

.. math::
  R(\theta_m) = R(\vec{Q}\cdot\vec{r}_m) =
  \begin{pmatrix}
  \cos(\vec{Q}\cdot\vec{r}_m) & -\sin(\vec{Q}\cdot\vec{r}_m) & 0 \\
  \sin(\vec{Q}\cdot\vec{r}_m) & \cos(\vec{Q}\cdot\vec{r}_m)  & 0 \\
  0                           & 0                            & 1 \\
  \end{pmatrix}


Full spin rotation matrix
=========================

In the following sections we will need to produce the spin spiral ground
state from the ferromagnetically ordered state, where each spin
:math:`\vec{S}_{ma}^{ferro}` is oriented along the direction of the
cone axis :math:`\hat{n}`. In order to do that we combine rotations inside
each unit cell as described in the :ref:`user-guide_methods_spin-rotations`
section and in this section:

.. math::
  \vec{S}_{ma} = R(\theta_m)R(\theta_a,\phi_a)\vec{S}_{ma}^{ferro}
  = R_{ma}\vec{S}_{ma}^{ferro}

where we recall

.. math::

    R(\theta_a, \phi_a) =
    \begin{pmatrix}
      \cos\theta_a + \sin^2\phi_a(1-\cos\theta_a) &
      -\sin\phi_a\cos\phi_a(1-\cos\theta_a) &
      \cos\phi_a\sin\theta_a  \\
      -\sin\phi_a\cos\phi_a(1-\cos\theta_a) &
      \cos\theta_a + \cos^2\phi_a(1-\cos\theta_a) &
      \sin\phi_a\sin\theta_a  \\
      -\cos\phi_a\sin\theta_a &
      -\sin\phi_a\sin\theta_a &
      \cos\theta_a \\
    \end{pmatrix}

Matrix :math:`R_{ma}` has the form:

.. math::
  R_{ma} =
  \begin{pmatrix}
  ... & ... & \sin\theta_a(\cos(\vec{Q}\cdot\vec{r}_m)\cos\phi_a - \sin(\vec{Q}\cdot\vec{r}_m)\sin\phi_a)\\
  ... & ... & \sin\theta_a(\sin(\vec{Q}\cdot\vec{r}_m)\cos\phi_a + \cos(\vec{Q}\cdot\vec{r}_m)\sin\phi_a) \\
  -\cos\phi_a\sin\theta_a & -\sin\phi_a\sin\theta_a & \cos\theta_a \\
  \end{pmatrix}

And the spin :math:`\vec{S}_{ma}` is

.. math::
  \vec{S}_{ma} =
  \begin{pmatrix}
    \sin\theta_a(\cos(\vec{Q}\cdot\vec{r}_m)\cos\phi_a - \sin(\vec{Q}\cdot\vec{r}_m)\sin\phi_a)\\
    \sin\theta_a(\sin(\vec{Q}\cdot\vec{r}_m)\cos\phi_a + \cos(\vec{Q}\cdot\vec{r}_m)\sin\phi_a) \\
    \cos\theta_a \\
  \end{pmatrix}
