.. _user-guide_methods_spin-fluctuations:

*****************
Spin fluctuations
*****************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/rotations.inc


-----------------------------------------------
Ground-state spin and and fluctuations about it
-----------------------------------------------

The minimum-energy spin vectors are

.. math::
  \ket{S_i^0} = S_i\,\ket{f_i}

with coordinates

.. math::
  ^f\boldsymbol{S_i^0}=\begin{pmatrix}0\\0\\S_i\end{pmatrix}

Spin fluctuations are described by replacing :math:`\ket{S_i^0}` with

.. math::
  \ket{S_i}=\ket{S_i^0}+\ket{\delta S_i}

whose components are

.. math::
  ^f\boldsymbol{S_i}=
  \begin{pmatrix}0\\0\\S_i\end{pmatrix}+
  \begin{pmatrix}\delta S_i^p\\ \delta S_i^t\\-\delta S_i^n\end{pmatrix}

where the minus sign in the last row accounts for the fact the spin vectors do not change their norm.

Spin fluctuations are fully inhomogeneous. This implies that the ground-state spin
vectors :math:`\ket{\tilde{S}_i^0}` must be replaced by the cell- and site-dependent
spin vectors

.. math::
  \ket{\tilde{S}_{mi}} = \ket{\,f_i^+\,f_i^-\,f_i\,}\braket{\,f_i^+\,f_i^-\,f_i\,|\,\tilde{S}_{mi}}
                       = \ket{\,f_i^+\,f_i^-\,f_i\,}\,^{sf}\boldsymbol{\tilde{S}_{mi}}

with coordinates

.. math::
  \boldsymbol{\tilde{S}_{mi}}=
    S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\delta S^{pt,-}_i\\
           \frac{1}{\sqrt{2}}\,\delta S^{pt,+}_i\\
           S_i-\delta S_i^n
           \end{pmatrix}

Then the full spin vectors are

.. math::
     \ket{S_{mi}} =\boldsymbol{R}_m\, \ket{\tilde{S}_i}

.. note::

  Magnopy absorbs the intra-cell spiral contribution inside the azimuth angle
  :math:`\phi_i(\boldsymbol{q}) = \boldsymbol{q}\cdot\boldsymbol{r_i} + \Delta\, \phi_i`.

  In the following we always use the notation :math:`\phi_i` for total intra-cell azimuth
  angle, :math:`\phi_{mi}` for the total azimuth angle and :math:`\phi_{m}` for the
  inter-cell part of the azimuth angle with the understanding that all three angles
  depends on the spiral vector :math:`\boldsymbol{q}`. The q-independent part of the
  azimuth angle :math:`\Delta\, \phi_i` will be used explicitly if needed.


  In the :ref:`Magnopy input file <user-guide_input_model-file>` in the
  :ref:`"Atoms" section <user-guide_input_model-file_atoms>` the direction of the atom's
  spin correspond **only** to the :math:`\Delta\, \phi_i` part of the total azimuth angle
  :math:`\phi_i`. The spiral-dependent part :math:`\boldsymbol{q}\cdot\boldsymbol{r_i}`
  of the azimuth angle :math:`\phi_i` is computed by Magnopy based on the provided
  :ref:`Cone axis <user-guide_input_model-file_cone-axis>` and
  :ref:`Spiral vector <user-guide_input_model-file_spiral-vector>`.
