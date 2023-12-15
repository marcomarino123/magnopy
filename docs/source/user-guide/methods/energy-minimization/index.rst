.. _user-guide_methods_energy-minimization:

*********************************************
Minimization of the classical exchange energy
*********************************************

Let us recall the expression for the exchange energy:

.. include:: ../repeated-formulas/classic-exchange-energy.txt

In order to minimize this equation and find ground state we split all possible cases into
three distinct ones:

* :math:`\vec{Q} = \vec{G}` - ferromagnetic alignment.
* :math:`\vec{Q} = \dfrac{\vec{G}}{2} \ne \vec{G}` - antiferromagnetic cone.
* :math:`\vec{Q} \ne \dfrac{\vec{G}}{2} \ne \vec{G}` - spiral state.

For each case the general equation is simplified and minimized. Then the true
ground state is defined by the comparison of the three obtained minimums.

Before we proceed to the detailed discussion about each of the three cases
let us recall the equation for the spin vector in the :math:`\hat{u}\hat{v}\hat{n}`
reference frame:

.. include:: ../repeated-formulas/spin-uvn.txt

Ferromagnetic alignment
=======================

.. dropdown:: Example

  * Two spins in the unit cell,
    :math:`\vec{Q} = (2\pi,0,0)^T`:

    - :math:`\vec{r}_1 = (0,0,0)`,
      :math:`\theta_1 = 150^{\circ}`,
      :math:`\phi_1 = 180^{\circ}`
    - :math:`\vec{r}_2 = (\frac{1}{2},\frac{1}{2},0)`,
      :math:`\theta_2 = 30^{\circ}`,
      :math:`\phi_2 = 0^{\circ}`

  .. raw:: html
    :file: ../../../../images/minimization-ferro.html

  .. note::
    Alignment of two spins inside the unit cell is antiferromagnetic, due to the
    choice of the :math:`\theta_a`, :math:`\phi_a`. But the alignment of the spins with
    the same unit-cell index is ferromagnetic with respect to the change of the unit cell.

The spin vector is simplified to

.. math::
  \langle uvn\vert S_{ma}\rangle
  = S_a\cdot
  \begin{pmatrix}
    \sin\theta_a\cos(2\pi n+\phi_a) \\
    \sin\theta_a\sin(2\pi n+\phi_a) \\
    \cos\theta_a                    \\
  \end{pmatrix}
  = S_a\cdot
  \begin{pmatrix}
    \sin\theta_a\cos(\phi_a) \\
    \sin\theta_a\sin(\phi_a) \\
    \cos\theta_a             \\
  \end{pmatrix}

where :math:`n \in \mathbb{Z}`.

This equation describes a ferromagnetic alignment of the spins between the unit cell.
Note that the alignment of the spins inside the unit cell can be arbitrary due
to the choice of :math:`\theta_a`, :math:`\phi_a`.

Antiferromagnetic cone
======================

.. dropdown:: Example

  * Two spins in the unit cell,
    :math:`\vec{Q} = (\pi,0,0)^T`:

    - :math:`\vec{r}_1 = (0,0,0)`,
      :math:`\theta_1 = 150^{\circ}`,
      :math:`\phi_1 = 180^{\circ}`
    - :math:`\vec{r}_2 = (\frac{1}{2},\frac{1}{2},0)`,
      :math:`\theta_2 = 30^{\circ}`,
      :math:`\phi_2 = 0^{\circ}`

  .. raw:: html
    :file: ../../../../images/minimization-antiferro.html

  .. note::
    Alignment of two spins inside the unit cell is antiferromagnetic, due to the
    choice of the :math:`\theta_a`, :math:`\phi_a`. The alignment of the in-plane
    (:math:`\hat{u}\hat{v}`) spin's component with the same unit-cell index is antiferromagnetic
    with respect to the change of the unit cell.

The spin vector is simplified to

.. math::
  \langle uvn\vert S_{ma}\rangle
  = S_a\cdot
  \begin{pmatrix}
    \sin\theta_a\cos(\pi n+\phi_a) \\
    \sin\theta_a\sin(\pi n+\phi_a) \\
    \cos\theta_a                    \\
  \end{pmatrix}
  =
  S_a\cdot
  \left\{
  \begin{matrix}
    \begin{pmatrix}
      \sin\theta_a\cos(\phi_a) \\
      \sin\theta_a\sin(\phi_a) \\
      \cos\theta_a             \\
    \end{pmatrix}
    \text{ if }n=2k
    \\
    \begin{pmatrix}
      -\sin\theta_a\cos(\phi_a) \\
      -\sin\theta_a\sin(\phi_a) \\
      \cos\theta_a              \\
    \end{pmatrix}
    \text{ if }n=2k+1
  \end{matrix}
  \right.

where :math:`n \in \mathbb{Z}`.

The alignment of the spins inside the unit cell can be arbitrary due
to the choice of :math:`\theta_a`, :math:`\phi_a` as in the ferromagnetic case.

Spiral state
============
