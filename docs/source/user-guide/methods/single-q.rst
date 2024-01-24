.. _user-guide_methods_single-q:

**********************
Single-q conical state
**********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/in-uvn.txt
  * .. include:: page-notations/parentheses.txt

Single-:math:`\boldsymbol{q}` conical state can be described by two vectors:

* Cone axis :math:`\boldsymbol{\hat{n}}`.
  It defines the global rotational axis of the spiral.
  Note, that we orient the reference frame as described in
  :ref:`user-guide_methods_uvn-choice`, therefore, the cone axis :math:`\boldsymbol{\hat{n}}`
  is one of the reference frame axes.
* Spiral vector :math:`\boldsymbol{q}`. It defines the phase as:
  :math:`\phi_m = \boldsymbol{q}\cdot\boldsymbol{r_m}`.


Spiral rotation matrix
======================

We describe the position of each spin :math:`\boldsymbol{S_{mi}}` in the crystal with
the two vectors :math:`\boldsymbol{r_m}` and :math:`\boldsymbol{r_i}`, where

.. math::
  \boldsymbol{r_m} = i\cdot\boldsymbol{a} + j\cdot\boldsymbol{b} + k\cdot\boldsymbol{c}

gives the coordinate of the unit cell, to which the spin :math:`\boldsymbol{S_{mi}}`
belongs. Vector :math:`\boldsymbol{r_i}` describes the spin's position
inside unit cell and does not depend on the index :math:`m`. Therefore, the
spin :math:`\boldsymbol{S_{mi}}` is located at the position

.. math::
  \boldsymbol{r_{mi}} = \boldsymbol{r_m} + \boldsymbol{r_i}

We assume that the spins inside the unit cell can be oriented independently.
The direction of each one is given by two angles :math:`\theta_i` and
:math:`\phi_i` as described :ref:`here <user-guide_methods_spin-rotations>`.
The spiral rotation is assumed to be applied based on the coordinate of the
unit cell :math:`\boldsymbol{r_m}` only:

.. include:: repeated-formulas/spiral-rotation-matrix-uvn.txt

In other words we absorb the in-cell spiral contribution :math:`\boldsymbol{q}\cdot\boldsymbol{r_i}`
into the angle :math:`\phi_i`


Full spin rotation matrix
=========================

In the following sections we produce the spin spiral ground
state from the ferromagnetically ordered state, where each spin
:math:`\boldsymbol{S_{mi}^{ferro}}` is oriented along the direction of the
cone axis :math:`\boldsymbol{\hat{n}}`. In order to do that we combine the rotation inside
each unit cell as described in the :ref:`user-guide_methods_spin-rotations`
section and the rotation between unit cells as described above:

.. include:: repeated-formulas/spin-from-ferro-any.txt

where we recall

.. include:: repeated-formulas/spin-rotation-matrix-uvn.txt

Matrix :math:`\boldsymbol{R_{mi}}` has the form:

.. math::
  \boldsymbol{R_{mi}}
  =
  \begin{pmatrix}
    ... & ... & \sin\theta_i\cos(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)     \\
    ... & ... & \sin\theta_i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)     \\
    -\cos\phi_i\sin\theta_i & -\sin\phi_i\sin\theta_i & \cos\theta_i \\
  \end{pmatrix}

And the spin :math:`\boldsymbol{S_{mi}}` is

.. include:: repeated-formulas/spin-uvn.txt

.. dropdown:: All elements of the matrix  :math:`\text{ }\boldsymbol{R_{mi}}`

  For simplicity of the notation we call the matrix :math:`\boldsymbol{R_{mi}}`
  as :math:`\boldsymbol{R}`:

  .. math::
    \boldsymbol{R_{mi}}
    =
    \boldsymbol{R}
    =
    \begin{pmatrix}
      R^{11} & R^{12} & R^{13} \\
      R^{21} & R^{22} & R^{23} \\
      R^{31} & R^{32} & R^{33} \\
    \end{pmatrix}

  .. math::
    &R^{11}
    =
    \cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[\cos\theta_i + \sin^2\phi_i(1-\cos\theta_i)\right]-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[-\sin\phi_i\cos\phi_i(1-\cos\theta_i)\right]
    =\\&=
    (1-\cos\theta_i)\left[\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin^2\phi_i+\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i\cos\phi_i\right]+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i
    =\\&=
    (1-\cos\theta_i)\sin\phi_i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i

  .. math::
    &R^{12}
    =
    \cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[-\sin\phi_i\cos\phi_i(1-\cos\theta_i)\right]-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[\cos\theta_i + \cos^2\phi_i(1-\cos\theta_i)\right]
    =\\&=
    (1-\cos\theta_i)\left[-\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i\cos\phi_i-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos^2\phi_i\right]-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i
    =\\&=
    -(1-\cos\theta_i)\cos\phi_i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i

  .. math::
    R^{13}
    =
    \sin\theta_i(\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\phi_i - \sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i)
    =
    \sin\theta_i\cos(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)

  .. math::
    &R^{21}
    =
    \sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[\cos\theta_i + \sin^2\phi_i(1-\cos\theta_i)\right]+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[-\sin\phi_i\cos\phi_i(1-\cos\theta_i)\right]
    =\\&=
    (1-\cos\theta_i)\left[\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin^2\phi_i-\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i\cos\phi_i\right]+\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i
    =\\&=
    -(1-\cos\theta_i)\sin\phi_i\cos(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)+\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i

  .. math::
    &R^{22}
    =
    \sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[-\sin\phi_i\cos\phi_i(1-\cos\theta_i)\right]+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\left[\cos\theta_i + \cos^2\phi_i(1-\cos\theta_i)\right]
    =\\&=
    (1-\cos\theta_i)\left[-\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i\cos\phi_i+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos^2\phi_i\right]+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i
    =\\&=
    (1-\cos\theta_i)\cos\phi_i\cos(\boldsymbol{q}\cdot\boldsymbol{r_m}+\phi_i)+\cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\theta_i

  .. math::
    R^{23}
    =
    \sin\theta_i(\sin(\boldsymbol{q}\cdot\boldsymbol{r_m})\cos\phi_i + \cos(\boldsymbol{q}\cdot\boldsymbol{r_m})\sin\phi_i)
    =
    \sin\theta_i\sin(\boldsymbol{q}\cdot\boldsymbol{r_m} + \phi_i)

  .. math::
    R^{31} = -\cos\phi_i\sin\theta_i

  .. math::
    R^{32} = -\sin\phi_i\sin\theta_i

  .. math::
    R^{33} = \cos\theta_i

.. _user-guide_methods_single-q_examples:

Examples
========

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 90^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-1.html

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-2.html

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 45^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-3.html

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,1,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-4.html

* Two spins in the unit cell, :math:`\boldsymbol{q} = (0,1,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\boldsymbol{r}_2 = (\frac{1}{2},\frac{1}{2},\frac{1}{2})`,
    :math:`\theta_2 = 20^{\circ}`,
    :math:`\phi_2 = 45^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-5.html

* Two spins in the unit cell, :math:`\boldsymbol{q} = (1,0,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 150^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\boldsymbol{r}_2 = (0,\frac{1}{2},0)`,
    :math:`\theta_2 = 30^{\circ}`,
    :math:`\phi_2 =180^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-6.html
