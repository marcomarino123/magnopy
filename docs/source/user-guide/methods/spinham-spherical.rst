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

.. math::
  H = \dfrac{1}{2} \sum_{m, \vec{d}, a, b} \vec{S}_{ma}^T J_{ab}(d_{ab})\vec{S}_{m+d,b}


.. dropdown:: Bra-ket notation

  .. math::
    H = \dfrac{1}{2} \sum_{m, \vec{d}, a, b}
    \langle S_{ma}\vert uvn\rangle
    \langle uvn \vert J_{ab}(d_{ab})\vert uvn \rangle
    \langle uvn \vert S_{m+d,b} \rangle

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

.. math::
  \langle uvn\vert T\vert uvn \rangle
  = \dfrac{1}{\sqrt{2}}
  \begin{pmatrix}
    1 &  1 & 0        \\
    i & -i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}

And write the exchange matrix in the spherical reference frame:

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

  Now we define isotropic, symmetric and antisymmetric parts of the exchange matrix:

  .. math::
    \begin{pmatrix}
        J_{uu} & J_{uv} & J_{un} \\
        J_{vu} & J_{vv} & J_{vn} \\
        J_{nu} & J_{nv} & J_{nn} \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      J_{iso} & 0 & 0 \\
      0 & J_{iso} & 0 \\
      0 & 0 & J_{iso} \\
    \end{pmatrix}
    +
    \begin{pmatrix}
      S_{uu} & S_{uv} & S_{un} \\
      S_{uv} & S_{vv} & S_{vn} \\
      S_{un} & S_{vn} & S_{nn} \\
    \end{pmatrix}
    +
    \begin{pmatrix}
      0 & D_n & -D_v \\
      -D_n & 0 & D_u \\
      D_v & -D_u & 0 \\
    \end{pmatrix}

  where :math:`J_{iso} = \dfrac{1}{3}(J_{uu} + J_{vv} + J_{nn})` and
  :math:`S_{uu} + S_{vv} + S_{nn} = 0`.

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

.. math::
  \begin{pmatrix}
    J_{iso} + \dfrac{S_{uu} + S_{vv}}{2} + iD_n                       &
    \dfrac{S_{uu} - S_{vv}}{2} - iS_{uv}                              &
    \dfrac{S_{un} - iS_{vn}}{\sqrt{2}} - \dfrac{D_v + iD_u}{\sqrt{2}} \\
    \dfrac{S_{uu} - S_{vv}}{2} + iS_{uv}                              &
    J_{iso} + \dfrac{S_{uu} + S_{vv}}{2} - iD_n                       &
    \dfrac{S_{un} + iS_{vn}}{\sqrt{2}} - \dfrac{D_v - iD_u}{\sqrt{2}} \\
    \dfrac{S_{un} + iS_{vn}}{\sqrt{2}} + \dfrac{D_v - iD_u}{\sqrt{2}} &
    \dfrac{S_{un} - iS_{vn}}{\sqrt{2}} + \dfrac{D_v + iD_u}{\sqrt{2}} &
    J_{iso} + S_{nn}                                                  \\
  \end{pmatrix}

Further defining

.. math::
  \begin{matrix}
    D^{\pm} = \dfrac{D_v \pm iD_u}{\sqrt{2}} \\
    \text{and}                              \\
    S^{\pm} = \dfrac{S_{un} \pm iS_{vn}}{\sqrt{2}} \\
  \end{matrix}

One can write the exchange matrix in the spherical reference frame as:

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

Hamiltonian
===========

Now let us write the Hamiltonian in the spherical reference frame:

.. math::
  H = \dfrac{1}{2} \sum_{m, \vec{d}, a, b}
  (\vec{S}_{ma}^{ferro})^TR^{\dagger}(\theta_a,\phi_a)R^{\dagger}(\theta_m)
  J_{ab}(d_{ab})
  R(\theta_{m+d})R(\theta_b,\phi_b)\vec{S}_{m+d,b}^{ferro}

.. dropdown:: Relevant tensors in spherical reference frame

  See :ref:`user-guide_methods_spherical-rf` for details.

  .. math::
    R(\theta_a,\phi_a) =
    \begin{pmatrix}
      \dfrac{1+\cos\theta_a}{2}                  &
      \dfrac{(\cos\theta_a-1)e^{-2i\phi_a}}{2}     &
      \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}}  \\
      \dfrac{(\cos\theta_a - 1)e^{2i\phi_a}}{2}    &
      \dfrac{1 + \cos\theta_a}{2}                &
      \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}}    \\
      \dfrac{-\sin\theta_a e^{i\phi_a} }{\sqrt{2}} &
      \dfrac{-\sin\theta_a e^{-i\phi_a}}{\sqrt{2}} &
      \cos\theta_a                               \\
    \end{pmatrix}

  .. math::
    R(\theta_m) =
    \begin{pmatrix}
      e^{-i\theta_m} & 0              & 0 \\
      0              & e^{i\theta_m}  & 0 \\
      0              & 0              & 1 \\
    \end{pmatrix}=
    \begin{pmatrix}
      e^{-i\vec{Q}\cdot\vec{r}_m} & 0                          & 0 \\
      0                           & e^{i\vec{Q}\cdot\vec{r}_m} & 0 \\
      0                           & 0                          & 1 \\
    \end{pmatrix}

  .. math::
    \vec{S}_{ma}^{ferro} =
    \begin{pmatrix}
      0 & 0 & 0 \\
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
      J_{11} & J_{12} & J_{13} \\
      J_{21} & J_{22} & J_{23} \\
      J_{31} & J_{32} & J_{33} \\
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
      J_{11} & J_{12} & J_{13} \\
      J_{21} & J_{22} & J_{23} \\
      J_{31} & J_{32} & J_{33} \\
    \end{pmatrix}
    \begin{pmatrix}
      e^{-i\vec{Q}\cdot\vec{d}} & 0                        & 0 \\
      0                         & e^{i\vec{Q}\cdot\vec{d}} & 0 \\
      0                         & 0                        & 1 \\
    \end{pmatrix}


.. math::
    \begin{pmatrix}
      J_{11}e^{-i\vec{Q}\vec{d}} &
      J_{12}e^{i\vec{Q}(2\vec{r}_m+\vec{d})} &
      J_{13}e^{i\vec{Q}\vec{R}_m} \\
      J_{21}e^{-i\vec{Q}(2\vec{r}_m+\vec{d})} &
      J_{22}e^{i\vec{Q}\vec{d}} &
      J_{23}e^{-i\vec{Q}\vec{R}_m} \\
      J_{31}e^{-i\vec{Q}(\vec{R}_m+\vec{d})} &
      J_{32}e^{i\vec{Q}(\vec{R}_m+\vec{d})} &
      J_{33} \\
    \end{pmatrix}
    \stackrel{?}{=}
    \begin{pmatrix}
      J_{11}e^{-i\vec{Q}\vec{d}} & J_{12}e^{i\vec{Q}\vec{d}} & J_{13} \\
      J_{21}e^{-i\vec{Q}\vec{d}} & J_{22}e^{i\vec{Q}\vec{d}} & J_{23} \\
      J_{31}e^{-i\vec{Q}\vec{d}} & J_{32}e^{i\vec{Q}\vec{d}} & J_{33} \\
    \end{pmatrix}

As one can see two types of conditions may result from this equation:

* Conditions on the exchange matrix elements.
  In that case the Spiral vector is unrestricted.
* Conditions on the spiral vector.
  In that case exchange elements imply some restriction on the spiral vector :math:`\vec{Q}`.

First, let us list the combined conditions, which result in the truth of the relation:

.. dropdown:: Details

  * There are no restrictions on the diagonal elements.

  * Condition for :math:`J_{12}` and :math:`J_{21}`: are the same:

    .. math::
      \begin{matrix}
        J_{12} = \dfrac{S_{uu} - S_{vv}}{2} - iS_{uv}
        = (\dfrac{S_{uu} - S_{vv}}{2} + iS_{uv})^* = J_{21}^*\\
        \Downarrow \\
        J_{12}e^{2i\vec{Q}\vec{r}_m} = J_{12}
        \Leftrightarrow
        (J_{12}e^{2i\vec{Q}\vec{r}_m})^* = J_{12}^*
        \Leftrightarrow
        J_{21}e^{-2i\vec{Q}\vec{r}_m} = J_{21}
      \end{matrix}

  * Conditions on :math:`J_{31}` and :math:`J_{32}` are the same:

    .. math::
      J_{31} = S^+ + D^- = (S^- + D^+)^* = J_{32}^*

  * Conditions on J_{13} and J_{23} are the same:

    .. math::
      J_{13} = S^- - D^+ = (S^+ - D^-)^* = J_{23}^*


#.  :math:`J_{12}e^{2i\vec{Q}\vec{r}_m} = J_{12}`

    * Conditions on exchange matrices:
      :math:`S_{uv} = 0` and :math:`S_{uu} = S_{vv}`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = \pi n`

#.  :math:`J_{13}e^{i\vec{Q}\vec{r}_m}  = J_{13}`

    * Conditions on exchange matrices:
      :math:`S_{un} = D_v` and :math:`S_{vn} = -D_u`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

#.  :math:`J_{31}e^{-i\vec{Q}\vec{r}_m} = J_{31}`

    * Conditions on exchange matrices:
      :math:`S_{un} = -D_v` and :math:`S_{vn} = D_u`
    * Condition on the :math:`\vec{Q}`:
      :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

Which results in three unique possible cases:

* :math:`\vec{Q}\cdot\vec{r}_m = 2\pi n`

  "Even" commensurate spirals.
* :math:`\vec{Q}\cdot\vec{r}_m = \pi n = \pi (2k+1)` and
  :math:`S_{un} = D_v = S_{vn} = D_u = 0`

  "Odd" commensurate spiral.
* :math:`S_{uv} = 0` and :math:`S_{uu} = S_{vv}` and
  :math:`S_{un} = D_v = S_{vn} = D_u = 0`

  Incommensurate spiral.
