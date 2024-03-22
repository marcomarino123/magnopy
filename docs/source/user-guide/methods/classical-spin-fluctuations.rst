.. _user-guide_methods_classical-spin-fluctuations:

***************************
Classical spin fluctuations
***************************

The last section has been devoted to determine the minimum-energy spin
configuration, where all spins are collinear in the local reference
frame :math:`\boldsymbol{S^F}_i=S_i\,\boldsymbol{\hat{n}}`.

We analyze spin waves from now on, that are small collective transverse
spin fluctuations. This section describes classical spin fluctuations.
These will be quantized later on, using the Holstein-Primakoff decomposition
of spins into bosonic fields.

If small fluctuations at each site arise over the minimum energy state, the spin vector
becomes :math:`m`-dependent:

.. math::
  &\boldsymbol{S^F}_i\longrightarrow \boldsymbol{\tilde{S}^F}_{mi}\\\\
  &\boldsymbol{\tilde{S}^F}_{mi} =\boldsymbol{S^F}_i +
  \delta S_{mi}^u\,\boldsymbol{\hat{u}}+\delta S_{mi}^v\,\boldsymbol{\hat{v}}-\delta S_{mi}^n\,\boldsymbol{\hat{n}}
  =\begin{pmatrix}\delta S_{mi}^u\\\delta S_{mi}^v\\S_i-\delta S_{mi}^n
    \end{pmatrix}

where the minus sign in front of the :math:`\boldsymbol{\hat{n}}`-axis fluctuation ensure the
proper normalization of the spin vector. The vector components in the
spherical basis are then

.. math::
  \boldsymbol{\tilde{S}^{F,s}}_{mi} =\boldsymbol{S^{F,s}}_i+
  \frac{\delta S_{mi}^-}{\sqrt{2}}\,\boldsymbol{\hat{u}^+}+
  \frac{\delta S_{mi}^+}{\sqrt{2}}\,\boldsymbol{\hat{u}^-}
  -\delta S_{mi}^n\,\boldsymbol{\hat{n}}
  =\begin{pmatrix}\frac{1}{\sqrt{2}}\,\delta  S_{mi}^-\\\frac{1}{\sqrt{2}}\,\delta S_{mi}^+\\S_{i}-\delta S_{mi}^n
    \end{pmatrix}

where :math:`S_{mi}^{\pm}=S_{mu}^u\pm S_{mi}^v`.
Application of the intra-cell rotation :math:`\boldsymbol{R}_i^s` leads to
a spin vector that looks as follows

.. math::
  \boldsymbol{R}_i^s\,\boldsymbol{\tilde{S}^{F,s}}_{mi}=\frac{1}{\sqrt{2}}\,\delta S_{mi}^-\,\boldsymbol{\hat{p}}_{i}^s+
  \frac{1}{\sqrt{2}}\,\delta S_{mi}^+\,\boldsymbol{\hat{t}}_{i}^s
  +(S_i-\delta S_{mi}^n)\,\boldsymbol{\hat{f}}_{i}^s
