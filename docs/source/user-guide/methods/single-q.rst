.. _user-guide_methods_single-q:

**********************
Single-q conical state
**********************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/rotations.inc

================================
Description of the conical state
================================
The conical state is defined by the cone axis, that is collinear to the unit
vector :math:`\ket{n}`, and by the spiral wave-vector
:math:`\boldsymbol{q}`. Magnopy constructs the single-q conical state in three stages.

1.  It starts by populating all the atomic sites with spin vectors collinear to
    :math:`\ket{n}`

    .. math::
      S_i\, \ket{n}

2.  These vectors are subsequently rotated by the rotation matrices

    .. math::
      \boldsymbol{R}_i = e^{i\,\theta_i\,\ket{r(\phi_i)}\,\times}

    that have been introduced
    :ref:`previously <user-guide_methods_spin-rotations>`, where the rotation
    azimuth angles are
    :math:`\phi_i(\boldsymbol{q}) = \boldsymbol{q}\cdot\boldsymbol{r_i} + \Delta\phi_i`.
    These rotations populate each unit cell in the lattice by a collection of
    non-collinear atomic spins

    .. math::
      \ket{\tilde{S}_i^0}=S_i\, \boldsymbol{R}_i\, \ket{n}=S_i\, \ket{f_i}

    Since the rotations do not depend on the cell index :math:`m`, all unit
    cells spin arrangements are replica of each other at this stage.

3.  Finally, all spins are rotated by the cell-dependent rotation operator

    .. math::
      \boldsymbol{R}_m = e^{i \,\phi_m\,\ket{n}\,\times}

    where the azimuth angle is :math:`\phi_m(\boldsymbol{q}) = \boldsymbol{q}\cdot\boldsymbol{r_m}`
    now. The explicit expression for the rotation matrix in the :math:`(u\, v\, n)` reference frame is

    .. math::
      ^n\boldsymbol{R}_m&=
            \begin{pmatrix}
                  \cos\phi_m  & -\sin\phi_m & 0 \\
                  \sin\phi_m  & \cos\phi_m  & 0 \\
                  0           & 0           & 1 \\
            \end{pmatrix}

    The lattice is populated now by the ground-state spin vectors

    .. math::
      \ket{S_{mi}^0} =\boldsymbol{R}_m\, \ket{\tilde{S}_i^0}
       = S_i\,\boldsymbol{R}_m\,\boldsymbol{R}_i\,\ket{n}

    whose coordinates in the :math:`(u\, v\, n)` reference frame are

    .. math::
      ^n\boldsymbol{S}_{mi}^0
      \,=\,
      S_i
      \begin{pmatrix}
        \sin\theta_i\, \cos\phi_{mi} \\
        \sin\theta_i\, \sin\phi_{mi} \\
        \cos\theta_i
      \end{pmatrix}

    where the full azimuth angles are

    .. math::
      \phi_{mi}(\boldsymbol{q})
      =
      \phi_m(\boldsymbol{q}) + \phi_i(\boldsymbol{q})
      =
      \boldsymbol{q}\cdot\boldsymbol{r_m} + \boldsymbol{q}\cdot\boldsymbol{r_i} + \Delta\phi_i
      =
      \boldsymbol{q}\cdot\boldsymbol{r_{mi}} + \Delta\phi_i

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

=======================================================
Spin coordinates in the :math:`(\,n^+\,n^-\,n\,)` basis
=======================================================

.. math::
  ^{sn}\boldsymbol{S_{mi}}=\braket{\,n^+\,n^-\,n\,|\,S_{mi}\,}=
  \boldsymbol{T}^\dagger\,^{n}\boldsymbol{S_{mi}}
  =S_i\,\begin{pmatrix}
    \frac{1}{\sqrt{2}}\,\sin \theta_i\,e^{- i (\boldsymbol{q} \cdot \boldsymbol{r_m} + \phi_i)}\\
    \frac{1}{\sqrt{2}}\,\sin \theta_i\,e^{ i (\boldsymbol{q} \cdot \boldsymbol{r_m} + \phi_i)}\\
    \cos \theta_i
  \end{pmatrix}

whose Fourier transform is

.. math::
  ^{n,s}\boldsymbol{S}_{ki}
  =
  S_i
  \begin{pmatrix}
    \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}} \\
    \dfrac{\sin\theta_i}{\sqrt{2}}\, e^{ i\phi_i}\, \delta_{\boldsymbol{k},  \boldsymbol{q}} \\
    \cos\theta\, \delta_{\boldsymbol{k}, \boldsymbol{0}}                                     \\
  \end{pmatrix}

This structure factor can be written in the :math:`(u\, v\, n)` reference frame as follows:

.. math::
  ^n\boldsymbol{S}_{ki}
  =
  S_i
  \begin{pmatrix}
      \dfrac{\sin\theta_i}{2}\,
      \left(
        e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}}
        +
        e^{i\phi_i}\, \delta_{\boldsymbol{k}, \boldsymbol{q}}
      \right)
    \\
      \dfrac{i\sin\theta_i}{2}\,
      \left(
        e^{-i\phi_i}\, \delta_{\boldsymbol{k}, -\boldsymbol{q}}
        -
        e^{i\phi_i}\, \delta_{\boldsymbol{k}, \boldsymbol{q}}
      \right)
    \\
      \cos\theta \, \delta_{\boldsymbol{k}, \boldsymbol{0}}
  \end{pmatrix}

===============================================================
Rotation matrix elements in the :math:`(\,n^+\,n^-\,n\,)` basis
===============================================================

.. math::
  ^{sn}\boldsymbol{R_i}
    &=
       \,\boldsymbol{T}^\dagger\,^n\boldsymbol{R_i}\,\boldsymbol{T}\\
    &=
      \dfrac{1}{2}
      \begin{pmatrix}
          1 + \cos\theta_i                        &
          (\cos\theta_i - 1)\, e^{-2i\phi_i}      &
          \sqrt{2}\, \sin\theta_i\, e^{-i\phi_i}  \\
          (\cos\theta_i - 1)\, e^{2i\phi_i}       &
          1 + \cos\theta_i                        &
          \sqrt{2}\, \sin\theta_i\, e^{i\phi_i}   \\
          -\sqrt{2}\, \sin\theta_i\, e^{i\phi_i}  &
          -\sqrt{2}\, \sin\theta_i\, e^{-i\phi_i} &
          2\cos\theta_i
      \end{pmatrix}

.. math::
  ^{sn}\boldsymbol{R_m}=\,\boldsymbol{T}^\dagger\,^n\boldsymbol{R_m}\,\boldsymbol{T}=
            \begin{pmatrix}
                  e^{-i\,\phi_m}  & 0              & 0 \\
                  0               & e^{i\,\phi_m}  & 0 \\
                  0               & 0.             & 1 \\
            \end{pmatrix}

Examples
========

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 90^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-1.html

.. rst-class:: plotly-figure-caption

  **Figure 1** (interactive)

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-2.html

.. rst-class:: plotly-figure-caption

  **Figure 2** (interactive)

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,0,1)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 60^{\circ}`,
    :math:`\phi_1 = 45^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-3.html

.. rst-class:: plotly-figure-caption

  **Figure 3** (interactive)

* One spin in the unit cell, :math:`\boldsymbol{q} = (0,1,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-4.html

.. rst-class:: plotly-figure-caption

  **Figure 4** (interactive)

* Two spins in the unit cell, :math:`\boldsymbol{q} = (0,1,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 30^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\boldsymbol{r}_2 = (\frac{1}{2},\frac{1}{2},\frac{1}{2})`,
    :math:`\theta_2 = 20^{\circ}`,
    :math:`\phi_2 = 45^{\circ}`


.. raw:: html
  :file: ../../../images/single-q-5.html

.. rst-class:: plotly-figure-caption

  **Figure 5** (interactive)

* Two spins in the unit cell, :math:`\boldsymbol{q} = (1,0,0)^T`:

  - :math:`\boldsymbol{r}_1 = (0,0,0)`,
    :math:`\theta_1 = 150^{\circ}`,
    :math:`\phi_1 = 0^{\circ}`
  - :math:`\boldsymbol{r}_2 = (0,\frac{1}{2},0)`,
    :math:`\theta_2 = 30^{\circ}`,
    :math:`\phi_2 =180^{\circ}`

.. raw:: html
  :file: ../../../images/single-q-6.html

.. rst-class:: plotly-figure-caption

  **Figure 6** (interactive)
