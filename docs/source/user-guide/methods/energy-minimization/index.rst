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

If :math:`\delta_{\vec{Q},\vec{G}} = 1`,
then :math:`\vec{Q}\vec{d} = 2\pi` for any :math:`\vec{d}`
and the spin vector is simplified to

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

We note, tha if :math:`\delta_{\vec{Q},\vec{G}} = 1`,
then :math:`\delta_{\vec{Q},\frac{\vec{G}}{2}} = 1`,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{a, b, \vec{d}}
  S_aS_b
  \Biggl\{
    J_{nn}\cos\theta_a\cos\theta_b
    \\
    &+
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{uu}+J_{vv}}{2}\cos(\phi_b-\phi_a)
      +
      \dfrac{J_{uv}-J_{vu}}{2}\sin(\phi_b-\phi_a)
    \Bigr]
    \\
    &+
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{uu}-J_{vv}}{2}\cos(\phi_a+\phi_b)
        +
      \dfrac{J_{uv}+J_{vu}}{2}\sin(\phi_a+\phi_b)
    \Bigr]
    \\
    &+
    \sin\theta_a\cos\theta_b
    \Bigl[
      J_{un}\cos\phi_a
      +
      J_{vn}\sin\phi_a
    \Bigr]
    \\
    &+
    \cos\theta_a\sin\theta_b
    \Bigl[
      J_{nu}\cos\phi_b
      +
      J_{nv}\sin\phi_b
    \Bigr]
  \Biggr\}


Antiferromagnetic cone
======================

If :math:`\delta_{\vec{Q},\frac{\vec{G}}{2}} = 1`,
then :math:`\vec{Q}\vec{d} = \pm\pi` for any :math:`\vec{d}`
and the spin vector is simplified to

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

where :math:`n \in \mathbb{Z}`. The case with :math:`n=2k` falls into the previous section.
In this section we discuss the case :math:`n=2k+1`.

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

In this case :math:`\delta_{\vec{Q},\vec{G}} = 0`,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{a, b, \vec{d}}
  S_aS_b
  \Biggl\{
    J_{nn}\cos\theta_a\cos\theta_b
    \\
    &-
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{uu}+J_{vv}}{2}\cos(\phi_b-\phi_a)
      +
      \dfrac{J_{uv}-J_{vu}}{2}\sin(\phi_b-\phi_a)
    \Bigr]
    \\
    &-
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{uu}-J_{vv}}{2}\cos(\phi_a+\phi_b)
        +
      \dfrac{J_{uv}+J_{vu}}{2}\sin(\phi_a+\phi_b)
    \Bigr]
  \Biggr\}



.. include:: spiral-case.txt
