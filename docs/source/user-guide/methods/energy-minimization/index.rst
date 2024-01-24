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
then :math:`\boldsymbol{q}\boldsymbol{d_{ij}} = 2\pi n` for any :math:`\boldsymbol{d_{ij}}`
and :math:`\boldsymbol{q}\boldsymbol{r_m} = 2\pi n` for any :math:`\boldsymbol{r_m}`,
thus, the spin vector is simplified to

.. math::
  \langle uvn\vert S_{mi}\rangle
  = S_i\cdot
  \begin{pmatrix}
    \sin\theta_i\cos(2\pi n+\phi_i) \\
    \sin\theta_i\sin(2\pi n+\phi_i) \\
    \cos\theta_i                    \\
  \end{pmatrix}
  = S_i\cdot
  \begin{pmatrix}
    \sin\theta_i\cos(\phi_i) \\
    \sin\theta_i\sin(\phi_i) \\
    \cos\theta_i             \\
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
    choice of the :math:`\theta_i`, :math:`\phi_i`. But the alignment of the spins with
    the same unit-cell index is ferromagnetic with respect to the change of the unit cell.

We note, tha if :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 1`,
then :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1` as well,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{i, j, \boldsymbol{d_{ij}}}
  S_iS_j
  \Biggl\{
    J_{ij}^{nn}(\boldsymbol{d_{ij}})\cos\theta_i\cos\theta_j
    +\\&+
    \sin\theta_i\sin\theta_j
    \Bigl[
      \dfrac{J_{ij}^{uu}(\boldsymbol{d_{ij}})+J_{ij}^{vv}(\boldsymbol{d_{ij}})}{2}\cos(\phi_j-\phi_i)
      +
      \dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})-J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}\sin(\phi_j-\phi_i)
    \Bigr]
    +\\&+
    \sin\theta_i\sin\theta_j
    \Bigl[
      \dfrac{J_{ij}^{uu}(\boldsymbol{d_{ij}})-J_{ij}^{vv}(\boldsymbol{d_{ij}})}{2}\cos(\phi_i+\phi_j)
        +
      \dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})+J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}\sin(\phi_i+\phi_j)
    \Bigr]
    +\\&+
    \sin\theta_i\cos\theta_j
    \Bigl[
      J_{ij}^{un}(\boldsymbol{d_{ij}})\cos\phi_i
      +
      J_{ij}^{vn}(\boldsymbol{d_{ij}})\sin\phi_i
    \Bigr]
    +\\&+
    \cos\theta_i\sin\theta_j
    \Bigl[
      J_{ij}^{nu}(\boldsymbol{d_{ij}})\cos\phi_j
      +
      J_{ij}^{nv}(\boldsymbol{d_{ij}})\sin\phi_j
    \Bigr]
  \Biggr\}


Antiferromagnetic cone
======================

If :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1`,
then :math:`\boldsymbol{q}\boldsymbol{d_{ij}} = \pi n` for any :math:`\boldsymbol{d_{ij}}`
and :math:`\boldsymbol{q}\boldsymbol{r_m} = \pi n` for any :math:`\boldsymbol{r_m}`,
thus, the spin vector is simplified to

.. math::
  \langle uvn\vert S_{mi}\rangle
  = S_i\cdot
  \begin{pmatrix}
    \sin\theta_i\cos(\pi n+\phi_i) \\
    \sin\theta_i\sin(\pi n+\phi_i) \\
    \cos\theta_i                    \\
  \end{pmatrix}
  =
  S_i\cdot
  \left\{
  \begin{matrix}
    \begin{pmatrix}
      \sin\theta_i\cos(\phi_i) \\
      \sin\theta_i\sin(\phi_i) \\
      \cos\theta_i             \\
    \end{pmatrix}
    \text{ if }n=2k
    \\
    \begin{pmatrix}
      -\sin\theta_i\cos(\phi_i) \\
      -\sin\theta_i\sin(\phi_i) \\
      \cos\theta_i              \\
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
    choice of the :math:`\theta_i`, :math:`\phi_i`. The alignment of the in-plane
    (:math:`\boldsymbol{\hat{u}}\boldsymbol{\hat{v}}`) spin's component with the same unit-cell index is antiferromagnetic
    with respect to the change of the unit cell.

If :math:`n = 2k+1`, than :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 0`,
therefore, the expression for the energy is simplified to:

.. math::
  &\dfrac{E_{exchange}}{M}
  =
  \dfrac{1}{2}
  \sum_{i, j, \boldsymbol{d_{ij}}}
  S_iS_j
  \Biggl\{
    J_{ij}^{nn}(\boldsymbol{d_{ij}})\cos\theta_i\cos\theta_j
    -\\&-
    \sin\theta_i\sin\theta_j
    \Bigl[
      \dfrac{J_{ij}^{uu}(\boldsymbol{d_{ij}})+J_{ij}^{vv}(\boldsymbol{d_{ij}})}{2}\cos(\phi_j-\phi_i)
      +
      \dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})-J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}\sin(\phi_j-\phi_i)
    \Bigr]
    -\\&-
    \sin\theta_i\sin\theta_j
    \Bigl[
      \dfrac{J_{ij}^{uu}(\boldsymbol{d_{ij}})-J_{ij}^{vv}(\boldsymbol{d_{ij}})}{2}\cos(\phi_i+\phi_j)
        +
      \dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})+J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}\sin(\phi_i+\phi_j)
    \Bigr]
  \Biggr\}



.. include:: spiral-case.txt
