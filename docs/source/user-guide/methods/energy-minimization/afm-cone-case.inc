Antiferromagnetic cone
======================

If :math:`\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}} = 1`,
then :math:`\boldsymbol{q}\boldsymbol{d_{ij}} = \pi n` for any :math:`\boldsymbol{d_{ij}}`
and :math:`\boldsymbol{q}\boldsymbol{r_m} = \pi n` for any :math:`\boldsymbol{r_m}`,
thus, the spin vector is simplified to

.. math::
  \boldsymbol{S_{mi}}
  = S_i\cdot
  \begin{pmatrix}
    \sin\theta_i\cos(\pi n_{m}+\phi_i) \\
    \sin\theta_i\sin(\pi n_{m}+\phi_i) \\
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
    \text{ if }n_{m}=2k
    \\
    \begin{pmatrix}
      -\sin\theta_i\cos(\phi_i) \\
      -\sin\theta_i\sin(\phi_i) \\
      \cos\theta_i              \\
    \end{pmatrix}
    \text{ if }n_{m}=2k+1
  \end{matrix}
  \right.

We note, that for different :math:`\boldsymbol{d_{ij}}` the conditions above
might be either one or another, therefore, the equation for the  total energy can
not be simplified as nicely as in the case of ferromagnetic alignment.
However, within the first brillouin zone (and the :math:`\boldsymbol{q}` can be
restricted to it due to the periodicity of the underlying lattice) the following is true:
:math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 0`, which leads to the simpler
equation for the total energy:

.. math::
  \begin{aligned}
    &\dfrac{E}{M}
    =
    \dfrac{1}{2}
    \sum_{i, j, \boldsymbol{d_{ij}}}
    S_iS_j
    \Biggl\{
      J_{ij}^{nn}\cos\theta_i\cos\theta_j
      +\\&+
      \sin\theta_i\sin\theta_j
      \Bigl[
        J_{ij}^{uu}(\boldsymbol{d_{ij}})\cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j)\cos\phi_i
        +
        J_{ij}^{vv}(\boldsymbol{d_{ij}})\sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j)\sin\phi_i
        +\\&+
        J_{ij}^{uv}(\boldsymbol{d_{ij}})\sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j)\cos\phi_i
        +
        J_{ij}^{vu}(\boldsymbol{d_{ij}})\cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j)\sin\phi_i
      \Bigr]
    \Biggr\}
    +\\&+
    \mu_B
    \sum_i
    g_i  S_i
    h^n\cos\theta_i
  \end{aligned}
