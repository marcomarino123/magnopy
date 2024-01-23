.. _user-guide_methods_energy-minimization:

*********************************************
Minimization of the classical exchange energy
*********************************************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.txt
  * .. include:: ../page-notations/matrix.txt
  * .. include:: ../page-notations/bra-ket.txt
  * .. include:: ../page-notations/parentheses.txt
  * .. include:: ../page-notations/kronecker-delta.txt

Let us recall the expression for the exchange energy:

.. include:: ../repeated-formulas/classic-exchange-energy.txt

In order to minimize this equation and find ground state we split all possible cases into
three distinct ones:

* :math:`\boldsymbol{q} = \boldsymbol{G}` - ferromagnetic alignment.
* :math:`\boldsymbol{q} = \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - antiferromagnetic cone.
* :math:`\boldsymbol{q} \ne \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - spiral state.

For each case the general equation is simplified and minimized. Then the true
ground state is defined by the comparison of the three obtained minimums.

Before we proceed to the detailed discussion about each of the three cases
let us recall the equation for the spin vector in the :math:`uvn`
reference frame:

.. include:: ../repeated-formulas/spin-uvn.txt

Ferromagnetic alignment
=======================

If :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 1`,
then :math:`\boldsymbol{q}\boldsymbol{d}_{ab} = 2\pi n` for any :math:`\boldsymbol{d}_{ab}`
and :math:`\boldsymbol{q}\boldsymbol{r}_m = 2\pi n` for any :math:`\boldsymbol{r}_m`,
thus, the spin vector is simplified to

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
    :math:`\boldsymbol{q} = (2\pi,0,0)^T`:

    - :math:`\boldsymbol{r}_1 = (0,0,0)`,
      :math:`\theta_1 = 150^{\circ}`,
      :math:`\phi_1 = 180^{\circ}`
    - :math:`\boldsymbol{r}_2 = (\frac{1}{2},\frac{1}{2},0)`,
      :math:`\theta_2 = 30^{\circ}`,
      :math:`\phi_2 = 0^{\circ}`

  .. raw:: html
    :file: ../../../../images/minimization-ferro.html

  .. note::
    Alignment of two spins inside the unit cell is antiferromagnetic, due to the
    choice of the :math:`\theta_a`, :math:`\phi_a`. But the alignment of the spins with
    the same unit-cell index is ferromagnetic with respect to the change of the unit cell.

We note, tha if :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 1`,
then :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1` as well,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{a, b, \boldsymbol{d}_{ab}}
  S_aS_b
  \Biggl\{
    J_{ab}^{nn}(\boldsymbol{d}_{ab})\cos\theta_a\cos\theta_b
    +\\&+
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{ab}^{uu}(\boldsymbol{d}_{ab})+J_{ab}^{vv}(\boldsymbol{d}_{ab})}{2}\cos(\phi_b-\phi_a)
      +
      \dfrac{J_{ab}^{uv}(\boldsymbol{d}_{ab})-J_{ab}^{vu}(\boldsymbol{d}_{ab})}{2}\sin(\phi_b-\phi_a)
    \Bigr]
    +\\&+
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{ab}^{uu}(\boldsymbol{d}_{ab})-J_{ab}^{vv}(\boldsymbol{d}_{ab})}{2}\cos(\phi_a+\phi_b)
        +
      \dfrac{J_{ab}^{uv}(\boldsymbol{d}_{ab})+J_{ab}^{vu}(\boldsymbol{d}_{ab})}{2}\sin(\phi_a+\phi_b)
    \Bigr]
    +\\&+
    \sin\theta_a\cos\theta_b
    \Bigl[
      J_{ab}^{un}(\boldsymbol{d}_{ab})\cos\phi_a
      +
      J_{ab}^{vn}(\boldsymbol{d}_{ab})\sin\phi_a
    \Bigr]
    +\\&+
    \cos\theta_a\sin\theta_b
    \Bigl[
      J_{ab}^{nu}(\boldsymbol{d}_{ab})\cos\phi_b
      +
      J_{ab}^{nv}(\boldsymbol{d}_{ab})\sin\phi_b
    \Bigr]
  \Biggr\}


Antiferromagnetic cone
======================

If :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1`,
then :math:`\boldsymbol{q}\boldsymbol{d}_{ab} = \pi n` for any :math:`\boldsymbol{d}_{ab}`
and :math:`\boldsymbol{q}\boldsymbol{r}_m = \pi n` for any :math:`\boldsymbol{r}_m`,
thus, the spin vector is simplified to

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
In this section we discuss the case with :math:`n=2k+1`.

.. dropdown:: Example

  * Two spins in the unit cell,
    :math:`\boldsymbol{q} = (\pi,0,0)^T`:

    - :math:`\boldsymbol{r}_1 = (0,0,0)`,
      :math:`\theta_1 = 150^{\circ}`,
      :math:`\phi_1 = 180^{\circ}`
    - :math:`\boldsymbol{r}_2 = (\frac{1}{2},\frac{1}{2},0)`,
      :math:`\theta_2 = 30^{\circ}`,
      :math:`\phi_2 = 0^{\circ}`

  .. raw:: html
    :file: ../../../../images/minimization-antiferro.html

  .. note::
    Alignment of two spins inside the unit cell is antiferromagnetic, due to the
    choice of the :math:`\theta_a`, :math:`\phi_a`. The alignment of the in-plane
    (:math:`\hat{u}\hat{v}`) spin's component with the same unit-cell index is antiferromagnetic
    with respect to the change of the unit cell.

If :math:`n = 2k+1`, than :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 0`,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{a, b, \boldsymbol{d}_{ab}}
  S_aS_b
  \Biggl\{
    J_{ab}^{nn}(\boldsymbol{d}_{ab})\cos\theta_a\cos\theta_b
    -\\&-
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{ab}^{uu}(\boldsymbol{d}_{ab})+J_{ab}^{vv}(\boldsymbol{d}_{ab})}{2}\cos(\phi_b-\phi_a)
      +
      \dfrac{J_{ab}^{uv}(\boldsymbol{d}_{ab})-J_{ab}^{vu}(\boldsymbol{d}_{ab})}{2}\sin(\phi_b-\phi_a)
    \Bigr]
    -\\&-
    \sin\theta_a\sin\theta_b
    \Bigl[
      \dfrac{J_{ab}^{uu}(\boldsymbol{d}_{ab})-J_{ab}^{vv}(\boldsymbol{d}_{ab})}{2}\cos(\phi_a+\phi_b)
        +
      \dfrac{J_{ab}^{uv}(\boldsymbol{d}_{ab})+J_{ab}^{vu}(\boldsymbol{d}_{ab})}{2}\sin(\phi_a+\phi_b)
    \Bigr]
  \Biggr\}



.. include:: spiral-case.txt
