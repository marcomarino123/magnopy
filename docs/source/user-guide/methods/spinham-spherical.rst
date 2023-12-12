.. _user-guide_methods_spinham-spherical:

********************************************
Hamiltonian in a "spherical" reference frame
********************************************

.. dropdown:: Notation used on this page

  * The reference frame is :math:`\hat{u}\hat{v}\hat{n}` for the whole page.
    Unless specified otherwise.
  * Bra-ket notation for vectors. With one exception:

    - :math:`\vec{v_1}\cdot\vec{v}_2 = \langle v_1\vert v_2\rangle`
  * Parentheses () and brackets [] are equivalent.
  * :math:`S_a` - is length of the spin vector :math:`\vert S_{ma}\rangle`

.. note::
  In this page we discuss only the exchange (with on-site anisotropy) part of the Hamiltonian.

The reference frame of the given Hamiltonian is changed from
:math:`\hat{x}\hat{y}\hat{z}` to :math:`\hat{u}\hat{v}\hat{n}` as
described in :ref:`user-guide_methods_rf-change`.
We start this section from a Hamiltonian written in a :math:`\hat{u}\hat{v}\hat{n}`
reference frame:

.. include:: repeated-formulas/hamiltonian-main-any.txt


Exchange matrices
=================

The transformation of spin vectors to the spherical reference frame was discussed
in the :ref:`previous section <user-guide_methods_spherical-rf>`.
In this section we focus our attention on the transformation of the exchange
matrices. The exchange matrices are transformed as follows:

.. math::
  \begin{multline}
    \langle u^+u^-n \vert J_{ab}(d_{ab})\vert u^+u^-n \rangle
    = \langle u^+u^-n \vert uvn \rangle
    \langle uvn \vert J_{ab}(d_{ab})\vert uvn \rangle
    \langle uvn\vert u^+u^-n \rangle\\
    = \langle uvn \vert T^{\dagger} \vert uvn \rangle
    \langle uvn \vert J_{ab}(d_{ab})\vert uvn \rangle
    \langle uvn\vert T\vert uvn \rangle
  \end{multline}

Now we recall the definition of the transformation matrix
(:ref:`see here <user-guide_methods_spherical-rf>`):

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

And separate exchange matrix into isotropic, symmetric anisotropic and antisymmetric parts:

.. include:: repeated-formulas/exchange-matrix-decomposition-uvn.txt

Which leads to the exchange matrix in a spherical reference frame:

.. dropdown:: Details

  .. math::
    \begin{multline}
      \langle u^+u^-n \vert J_{ab}(d_{ab})\vert u^+u^-n \rangle =
      \dfrac{1}{2}
      \begin{pmatrix}
        1 & -i & 0        \\
        1 &  i & 0        \\
        0 &  0 & \sqrt{2} \\
      \end{pmatrix}
      \begin{pmatrix}
        J_{uu} & J_{uv} & J_{un} \\
        J_{vu} & J_{vv} & J_{vn} \\
        J_{nu} & J_{nv} & J_{nn} \\
      \end{pmatrix}
      \begin{pmatrix}
        1 &  1 & 0        \\
        i & -i & 0        \\
        0 &  0 & \sqrt{2} \\
      \end{pmatrix}
      \\ =
      \dfrac{1}{2}
      \begin{pmatrix}
        J_{uu} - i J_{vu} & J_{uv} - i J_{vv} & J_{un} - i J_{vn} \\
        J_{uu} + i J_{vu} & J_{uv} + i J_{vv} & J_{un} + i J_{vn} \\
        \sqrt{2}J_{nu}    & \sqrt{2}J_{nv}    & \sqrt{2}J_{nn}    \\
      \end{pmatrix}
      \begin{pmatrix}
        1 &  1 & 0        \\
        i & -i & 0        \\
        0 &  0 & \sqrt{2} \\
      \end{pmatrix}
      \\ =
      \dfrac{1}{2}
      \begin{pmatrix}
        (J_{uu} + J_{vv}) + i(J_{uv} - J_{vu}) &
        (J_{uu} - J_{vv}) - i(J_{uv} + J_{vu}) &
        \sqrt{2}(J_{un} - iJ_{vn})             \\
        (J_{uu} - J_{vv}) + i(J_{uv} + J_{vu}) &
        (J_{uu} + J_{vv}) - i(J_{uv} - J_{vu}) &
        \sqrt{2}(J_{un} + iJ_{vn})             \\
        \sqrt{2}(J_{nu} + iJ_{nv})             &
        \sqrt{2}(J_{nu} - iJ_{nv})             &
        2J_{nn}                                \\
      \end{pmatrix}
    \end{multline}

  Which gives us:

  .. math::
    \langle u^+u^-n \vert J_{ab}(d_{ab})\vert u^+u^-n \rangle =
    \dfrac{1}{2}
    \begin{pmatrix}
      2J_{iso} + S_{uu} + S_{vv} + 2iD_n      &
      S_{uu} - S_{vv} - 2iS_{uv}              &
      \sqrt{2}(S_{un} - iS_{vn} - D_v - iD_u) \\
      S_{uu} - S_{vv} + 2iS_{uv}              &
      2J_{iso} + S_{uu} + S_{vv} - 2iD_n      &
      \sqrt{2}(S_{un} + iS_{vn} - D_v + iD_u) \\
      \sqrt{2}(S_{un} + iS_{vn} + D_v - iD_u) &
      \sqrt{2}(S_{un} - iS_{vn} + D_v + iD_u) &
      2J_{iso} + 2S_{nn}                      \\
    \end{pmatrix}

.. include:: repeated-formulas/exchange-matrix-spherical.txt

Let us note a few symmetries of the exchange matrix in a spherical reference frame:

.. include:: repeated-formulas/exchange-matrix-symmetries-spherical.txt

.. dropdown:: Alternative way to write the matrix

  If we define:

  .. math::
    \begin{matrix}
      D^{\pm} = \dfrac{D_v \pm iD_u}{\sqrt{2}} \\
      \text{and}                              \\
      S^{\pm} = \dfrac{S_{un} \pm iS_{vn}}{\sqrt{2}} \\
    \end{matrix}

  Then we can write the exchange matrix in the spherical reference frame as:

  .. math::
    \begin{pmatrix}
      J_{iso} + \dfrac{S_{uu} + S_{vv}}{2} + iD_n &
      \dfrac{S_{uu} - S_{vv}}{2} - iS_{uv}        &
      S^- - D^+                                   \\
      \dfrac{S_{uu} - S_{vv}}{2} + iS_{uv}        &
      J_{iso} + \dfrac{S_{uu} + S_{vv}}{2} - iD_n &
      S^+ - D^-                                   \\
      S^+ + D^-                                   &
      S^- + D^+                                   &
      J_{iso} + S_{nn}                            \\
    \end{pmatrix}

Rotation symmetry check
=======================

Now let us write the Hamiltonian in the spherical reference frame:

.. include:: repeated-formulas/hamiltonian-main-from-ferro-any.txt

.. dropdown:: Relevant tensors in spherical reference frame

  See :ref:`user-guide_methods_spherical-rf` for details.

  .. include:: repeated-formulas/spin-rotation-matrix-spherical.txt

  .. include:: repeated-formulas/spiral-rotation-matrix-spherical.txt

  .. math::
    \vec{S}_{ma}^{ferro} =
    \begin{pmatrix}
      0   \\
      0   \\
      S_a \\
    \end{pmatrix}


The following part: :math:`R^{\dagger}(\theta_m)J_{ab}(d_{ab}) R(\theta_{m+d})`
is of utmost importance. Later we will see that if the following relation holds, Than
the solution for the cone ground state can be easily obtained:

.. math::

  R^{\dagger}(\theta_m)J_{ab}(d_{ab}) R(\theta_{m+d}) \stackrel{?}{=}
  J_{ab}(d_{ab}) R(\theta_{d})

Let us write this equation explicitly in the spherical reference frame:

.. dropdown:: Details

  .. math::
    R^{\dagger}(\theta_m)J_{ab}(d_{ab}) R(\theta_{m+d})
    =
    \begin{pmatrix}
      e^{i\vec{Q}\cdot\vec{r}_m} & 0                          & 0 \\
      0                           & e^{-i\vec{Q}\cdot\vec{r}_m} & 0 \\
      0                           & 0                          & 1 \\
    \end{pmatrix}
    \begin{pmatrix}
      J_{++} & J_{+-} & J_{+n} \\
      J_{-+} & J_{--} & J_{-n} \\
      J_{n+} & J_{n-} & J_{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      e^{-i\vec{Q}\cdot(\vec{r}_m+\vec{d})} & 0                                    & 0 \\
      0                                     & e^{i\vec{Q}\cdot(\vec{r}_m+\vec{d})} & 0 \\
      0                                     & 0                                    & 1 \\
    \end{pmatrix}

  .. math::
    J_{ab}(d_{ab}) R(\theta_{d})
    =
    \begin{pmatrix}
      J_{++} & J_{+-} & J_{+n} \\
      J_{-+} & J_{--} & J_{-n} \\
      J_{n+} & J_{n-} & J_{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      e^{-i\vec{Q}\cdot\vec{d}} & 0                        & 0 \\
      0                         & e^{i\vec{Q}\cdot\vec{d}} & 0 \\
      0                         & 0                        & 1 \\
    \end{pmatrix}


.. math::
    \begin{pmatrix}
      J_{++}e^{-i\vec{Q}\vec{d}} &
      J_{+-}e^{i\vec{Q}(2\vec{r}_m+\vec{d})} &
      J_{+n}e^{i\vec{Q}\vec{R}_m} \\
      J_{-+}e^{-i\vec{Q}(2\vec{r}_m+\vec{d})} &
      J_{--}e^{i\vec{Q}\vec{d}} &
      J_{-n}e^{-i\vec{Q}\vec{R}_m} \\
      J_{n+}e^{-i\vec{Q}(\vec{R}_m+\vec{d})} &
      J_{n-}e^{i\vec{Q}(\vec{R}_m+\vec{d})} &
      J_{nn} \\
    \end{pmatrix}
    \stackrel{?}{=}
    \begin{pmatrix}
      J_{++}e^{-i\vec{Q}\vec{d}} & J_{+-}e^{i\vec{Q}\vec{d}} & J_{+n} \\
      J_{-+}e^{-i\vec{Q}\vec{d}} & J_{--}e^{i\vec{Q}\vec{d}} & J_{-n} \\
      J_{n+}e^{-i\vec{Q}\vec{d}} & J_{n-}e^{i\vec{Q}\vec{d}} & J_{nn} \\
    \end{pmatrix}

As one can see two types of conditions may result from this equation:

* Conditions on the exchange matrix elements.
  In that case the Spiral vector is unrestricted.
* Conditions on the spiral vector.
  In that case exchange elements imply some restriction on the spiral vector :math:`\vec{Q}`.

First, let us list the combined conditions, which result in the truth of the relation:

.. dropdown:: Details

  * There are no restrictions on the diagonal elements.

  * Condition for :math:`J_{+-}` and :math:`J_{-+}`: are the same:

    .. math::
      \begin{matrix}
        J_{+-} = \dfrac{S_{uu} - S_{vv}}{2} - iS_{uv}
        = (\dfrac{S_{uu} - S_{vv}}{2} + iS_{uv})^* = J_{-+}^*\\
        \Downarrow \\
        J_{+-}e^{2i\vec{Q}\vec{r}_m} = J_{+-}
        \Leftrightarrow
        (J_{+-}e^{2i\vec{Q}\vec{r}_m})^* = J_{+-}^*
        \Leftrightarrow
        J_{-+}e^{-2i\vec{Q}\vec{r}_m} = J_{-+}
      \end{matrix}

  * Conditions on :math:`J_{n+}` and :math:`J_{n-}` are the same:

    .. math::
      J_{n+} = S^+ + D^- = (S^- + D^+)^* = J_{n-}^*

  * Conditions on J_{+n} and J_{-n} are the same:

    .. math::
      J_{+n} = S^- - D^+ = (S^+ - D^-)^* = J_{-n}^*


#.  :math:`J_{+-}e^{2i\vec{Q}\vec{r}_m} = J_{+-}`

    * Conditions on exchange matrices:
      :math:`S_{uv} = 0` and :math:`S_{uu} = S_{vv}`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = \pi n`

#.  :math:`J_{+n}e^{i\vec{Q}\vec{r}_m}  = J_{+n}`

    * Conditions on exchange matrices:
      :math:`S_{un} = D_v` and :math:`S_{vn} = -D_u`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

#.  :math:`J_{n+}e^{-i\vec{Q}\vec{r}_m} = J_{n+}`

    * Conditions on exchange matrices:
      :math:`S_{un} = -D_v` and :math:`S_{vn} = D_u`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

Which results in three unique possible cases:

.. dropdown:: Details

  First let us recall how the spin vector is defined in a :math:`\hat{u}\hat{v}\hat{n}`
  reference frame:

  .. include:: repeated-formulas/spin-uvn.txt

  * What does :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n` mean?

    .. math::
      \langle uvn\vert S_{ma}\rangle =S_a\cdot
      \begin{pmatrix}
          \sin\theta_a\cos(\phi_a) \\
          \sin\theta_a\sin(\phi_a) \\
          \cos\theta_a                                     \\
      \end{pmatrix}

    One can see that it corresponds to the ferromagnetic alignment of spins between
    the unit cells.

  * What does :math:`\vec{Q}\cdot\vec{r}_m = \pi n` mean?

    .. math::
      \langle uvn\vert S_{ma}\rangle =S_a\cdot
      \begin{pmatrix}
          \pm\sin\theta_a\cos(\phi_a) \\
          \pm\sin\theta_a\sin(\phi_a) \\
          \cos\theta_a                                     \\
      \end{pmatrix}

    One can see that it corresponds to the "antiferromagnetic" alignment of spins between
    the unit cells: If :math:`\cos\theta_a = 0` then it is just antiferromagnetic,
    but if :math:`\cos\theta_a \neq 0` then it is antiferromagnetic only in
    :math:`\hat{u}\hat{v}` plane. We will call this case a "Antiferromagnetic cone".



* :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

  Ferromagnetic case
* :math:`\vec{Q}\cdot\vec{r}_m = \pi n = \pi (2k+1)` and
  :math:`S_{un} = D_v = S_{vn} = D_u = 0`

  Antiferromagnetic cone.
* :math:`S_{uv} = 0` and :math:`S_{uu} = S_{vv}` and
  :math:`S_{un} = D_v = S_{vn} = D_u = 0`

  Incommensurate spiral.
