Similarly, the Zeeman term of the Hamiltonian can be written as follows

.. math::
    H_Z\, =\,
   \mu_B \sum_{m,i}\, g_i\,S_i\,^{sn}\boldsymbol{h}^\dagger\, ^{sn}\boldsymbol{R_m}\,^{sn}\boldsymbol{S_i}

Here, the :math:`m`-summation can be factored out by defining

.. math::
  ^{sn}\boldsymbol{R_0}=\sum_m\,^{sn}\boldsymbol{R_m}
  M
  \begin{pmatrix}
    \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0                           & 0 \\
    0                           & \delta_{\boldsymbol{q}, \boldsymbol{G}} & 0 \\
    0                           & 0                                       & 1 \\
  \end{pmatrix}

so that

.. math::
    H_Z\, =\,
   \mu_B \,^{sn}\boldsymbol{h}^\dagger\, ^{sn}\boldsymbol{R_0}\,
   \sum_{i}\, g_i\,^{sn}\boldsymbol{S_i}

Inserting the spin vector

.. math::
  ^{sn}\boldsymbol{S_i}=
    S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{-i \,\phi_i}\\
           \frac{1}{\sqrt{2}}\,\sin \theta_i\, e^{i \,\phi_i}\\
           \cos \theta_i
           \end{pmatrix}

The Zeeman contribution to the energy per unit cell is found to be

.. math::
  \frac{E_z^0}{M}
  =
  \mu_B\, \sum_i\, g_i\, S_i\,
  \left[
    h^n\, \cos\theta_i
    +
    \delta_{\boldsymbol{q}, \boldsymbol{G}}\, \sin\theta_i\,
    \left( h^u\, \cos\phi_i + h^v\, \sin\phi_i\, \right)
  \right]
