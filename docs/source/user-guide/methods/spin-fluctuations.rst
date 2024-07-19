.. _user-guide_methods_spin-fluctuations:

*****************
Spin fluctuations
*****************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/rotations.inc

The minimum-energy spin vectors are

.. math::
  \ket{S_i^0} = S_i\,\ket{f_i}

with coordinates in the local :math:`(\,p_i\,t_i\,f_i\,)` basis

.. math::
  ^f\boldsymbol{S_i^0}=\begin{pmatrix}0\\0\\S_i\end{pmatrix}

Spin fluctuations are different at each lattice site. This implies that the ground-state spin
vectors :math:`\ket{S_i^0}` must be replaced by the cell-dependent
spin vectors

.. math::
  \ket{S_{mi}}=\ket{S_i^0}+\ket{\delta S_{mi}}

whose components in the local :math:`(\,p_i\,t_i\,f_i\,)` basis are

.. math::
  ^f\boldsymbol{S_{mi}}=
  \begin{pmatrix}\delta S_{mi}^p\\ \delta S_{mi}^t\\S_i-\delta S_{mi}^n\end{pmatrix}

where the minus sign in the last row accounts for the fact the spin vectors do
not change their norm.
The vector coordinates in the spherical basis :math:`(\,f_i^+\,f_i^-\,f_i\,)`

.. math::
  \boldsymbol{S_{mi}}=
    ^{sf}S_i\,\begin{pmatrix}
           \frac{1}{\sqrt{2}}\,\delta S^{pt,-}_{mi}\\
           \frac{1}{\sqrt{2}}\,\delta S^{pt,+}_{mi}\\
           S_i-\delta S_{mi}^n
           \end{pmatrix}

are convenient to describe circularly polarized spin waves and to quantize the
Hamiltonian.
