Ferromagnetic alignment
=======================

If :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 1`,
then :math:`\boldsymbol{q}\boldsymbol{d_{ij}} = 2\pi n` for any :math:`\boldsymbol{d_{ij}}`
and :math:`\boldsymbol{q}\boldsymbol{r_m} = 2\pi n` for any :math:`\boldsymbol{r_m}`,
due to the fact that :math:`\boldsymbol{r_m}` is a lattice vector and
:math:`\boldsymbol{d_{ij}}` is a difference between two lattice vector, thus being the lattice vector by itself.
Therefore, the spin vector is simplified to

.. math::
  \boldsymbol{S_{mi}}
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
  &\dfrac{E}{M}
  =
  \dfrac{1}{2}
  \sum_{i, j, \boldsymbol{d_{ij}}}
  S_iS_j
  \Biggl\{
    J_{ij}^{nn}(\boldsymbol{d_{ij}})\cos\theta_i\cos\theta_j
    +\\&+
    \sin\theta_i\sin\theta_j
    \Bigl[
      J_{ij}^{uu}(\boldsymbol{d_{ij}})\cos\phi_i\cos\phi_j
      +
      J_{ij}^{vv}(\boldsymbol{d_{ij}})\sin\phi_i\sin\phi_j
      +\\&+
      J_{ij}^{uv}(\boldsymbol{d_{ij}})\cos\phi_i\sin\phi_j
      +
      J_{ij}^{vu}(\boldsymbol{d_{ij}})\sin\phi_i\cos\phi_j
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
  +\\&+
  \mu_B
  \sum_i
  g_i  S_i
  \left[
  \sin\theta_i
  \left(
    h^u\cos(\phi_i)
    +
    h^v\sin(\phi_i)
  \right)
  +
  h^n\cos\theta_i
  \right]
