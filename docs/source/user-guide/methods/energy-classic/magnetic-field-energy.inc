
Next we turn our attention to the Zeeman term, where we assume henceforth that the
:ref:`magnetic field <user-guide_methods_spherical-rf_change_magnetic-field>`

.. math::
  \boldsymbol{h}^s
  =
  (\frac{1}{\sqrt{2}}\, h^+, \frac{1}{\sqrt{2}}\, h^-, h^n)^{\dagger}

is uniform. The Zeeman Hamiltonian can be written as follows:

.. math::
  H_{Z}
  =
  \mu_B\sum_ig_i\, \sum_{m}\,
  (\boldsymbol{h}^s)^{\dagger}\, \boldsymbol{R}_m^s\, \boldsymbol{S}_{i}^s

The sum over lattice sites is performed by taking into account that only the
:math:`\boldsymbol{R}_m^s` depend on :math:`m`:

.. math::
  \sum_{m}\, \boldsymbol{R_m^s}
  =
  M
  \begin{pmatrix}
    \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0                           & 0 \\
    0                           & \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0 \\
    0                           & 0                                       & 1 \\
  \end{pmatrix}

Then the Zeeman contribution to the energy **per unit cell** is:

.. math::
  E^Z
  =
  \mu_B\, \sum_i\, g_i\, S_i\,
  \left[
    h^n\, \cos\theta_i
    +
    \delta_{\boldsymbol{q}, \boldsymbol{G}}\, \sin\theta_i\,
    \left( h^u\, \cos\phi_i + h^v\, \sin\phi_i\, \right)
  \right]
