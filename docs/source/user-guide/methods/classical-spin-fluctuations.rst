.. _user-guide_methods_classical-spin-fluctuations:

***************************
Classical spin fluctuations
***************************

The previous pages have been devoted to the introduction of the formalism and
determination of the classical ground state of the Hamiltonian. Now we will turn our
attention to the small collective transverse spin fluctuations. This section introduce
classical spin fluctuations. These will be quantized later on, using the
Holstein-Primakoff decomposition of spins into bosonic fields.

We write fluctuations for the collinear arrangement of spins in the
:math:`(\, u\, v\, n\,)` basis :math:`\boldsymbol{S^F}_i=S_i\,\boldsymbol{\hat{n}}`.
Later perturbed spin vectors will be rotated to the actual spiral state
by two consecutive rotations as we discussed
:ref:`earlier <user-guide_methods_single-q>`.

If small fluctuations at each site arise over the ground state, the spin vector
becomes :math:`m`-dependent again
:math:`\boldsymbol{S^F}_i\longrightarrow \boldsymbol{\tilde{S}^F}_{mi}` (even before the
rotations). We denote by tilde the perturbed spin vector.

.. math::
  \boldsymbol{\tilde{S}^F}_{mi}
  =
  \boldsymbol{S^F}_i
  +
  \delta S_{mi}^u\, \boldsymbol{\hat{u}}
  +
  \delta S_{mi}^v\, \boldsymbol{\hat{v}}
  -
  \delta S_{mi}^n\, \boldsymbol{\hat{n}}
  =
  \begin{pmatrix}
    \delta S_{mi}^u \\
    \delta S_{mi}^v \\
    S_i - \delta S_{mi}^n
  \end{pmatrix}

where the minus sign in front of the :math:`\boldsymbol{\hat{n}}`-axis fluctuation
is written to illustrate the proper normalization of the spin vector. Since we consider
fluctuations that rotate the spin vector, but conserve its length, the
:math:`\delta S_{mi}^n` component depends on the :math:`\delta S_{mi}^u` and
:math:`\delta S_{mi}^v` components as

.. math::
  \delta S_{mi}^n
  =
  S_i - \sqrt{S_i^2 - (\delta S_{mi}^u)^2 - (\delta S_{mi}^v)^2}

.. dropdown:: Details

  The condition on the conservation of the spin length is

  .. math::
    |\boldsymbol{\tilde{S}^F}_{mi}| = S_i

  which leads to the quadratic equation on :math:`\delta S_{mi}^n`:

  .. math::
    (\delta S_{mi}^n)^2
    -
    2S_i\, \delta S_{mi}^n
    +
    (\delta S_{mi}^u)^2 + (\delta S_{mi}^v)^2
    =
    0


The vector components in the spherical basis are then

.. math::
  \boldsymbol{\tilde{S}^{F,s}}_{mi}
  =
  \boldsymbol{S^{F,s}}_i
  +
  \frac{\delta S_{mi}^-}{\sqrt{2}}\, \boldsymbol{\hat{u}^+}
  +
  \frac{\delta S_{mi}^+}{\sqrt{2}}\, \boldsymbol{\hat{u}^-}
  -
  \delta S_{mi}^n\,\boldsymbol{\hat{n}}
  =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\, \delta  S_{mi}^- \\
    \frac{1}{\sqrt{2}}\, \delta S_{mi}^+ \\
    S_{i}-\delta S_{mi}^n
  \end{pmatrix}

where :math:`\delta S_{mi}^{\pm} = \delta S_{mu}^u \pm i\delta S_{mi}^v`.
Application of the intra-cell rotation :math:`\boldsymbol{R}_i^s` leads to
a spin vector that looks as follows

.. math::
  \boldsymbol{R}_i^s\, \boldsymbol{\tilde{S}^{F,s}}_{mi}
  =
  \frac{\delta S_{mi}^-}{\sqrt{2}}\, \boldsymbol{\hat{p}}_{i}^s
  +
  \frac{\delta S_{mi}^+}{\sqrt{2}}\, \boldsymbol{\hat{t}}_{i}^s
  +
  (S_i - \delta S_{mi}^n)\, \boldsymbol{\hat{f}}_{i}^s
