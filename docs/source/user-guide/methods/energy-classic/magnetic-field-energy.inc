
Next we turn our attention to the Zeeman term, where we assume henceforth that the
:ref:`magnetic field <user-guide_methods_spherical-rf_change_magnetic-field>`

.. include:: ../repeated-formulas/magnetic-field-spherical.inc

is uniform. The Zeeman Hamiltonian can be written as follows:

.. math::
  H_{Z}
  =
  \mu_B\sum_i g_i\,
  ^{n,s}\boldsymbol{h}^{\dagger}\, ^{n,s}\boldsymbol{R}_0\, ^{ns}\boldsymbol{S}_{i}

Here the rotation matrix

.. math::
  ^{n,s}\boldsymbol{R}_0=\sum_{m}\, ^{n,s}\boldsymbol{R_m}
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
