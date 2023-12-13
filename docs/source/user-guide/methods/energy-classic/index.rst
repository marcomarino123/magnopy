.. _user-guide_methods_energy-classic:

****************
Classical energy
****************

.. dropdown:: Notation used in this page

    * We work in the :math:`\vert u^+ u^- n \rangle` reference frame, if not specified otherwise.
    * Parentheses (), square brackets [] and figure parentheses {} are equivalent.

Let us recall the Hamiltonian:

.. include:: ../repeated-formulas/hamiltonian-main-from-ferro-any.txt


Let us separate the summation over cites in unit cell and over unit cells:

.. note::
    Ferromagnetic spin does not depend on the unit cell index:

    .. math::
        \vec{S}_{ma}^{ferro}
        =
        (0, 0, S_a )^T
        =
        \vec{S}_a^{ferro}

    We assume that magnetic field can vary over the space:

    .. math::
        \vec{H} = \vec{H}(\vec{r_{ma}}) = \vec{H}_{ma}

.. math::
  H
  =
  \dfrac{1}{2}
  \sum_{a, b}
  (\vec{S}_a^{ferro})^T
  R^{\dagger}(\theta_a,\phi_a)
  \sum_{\vec{d}}
  \left[
  \sum_{m}
  R^{\dagger}(\theta_m)
  J_{ab}(d_{ab})
  R(\theta_{m+d})
  \right]
  R(\theta_b,\phi_b)
  \vec{S}_b^{ferro}
  +
  \mu_B
  \sum_{a}
  g_a
  \left[
  \sum_{m}
  \vec{H}^T_{ma}
  R(\theta_m)
  \right]
  R(\theta_a,\phi_a)
  \vec{S}_{a}^{ferro}

We focus our attention on the expressions in the square brackets:

Exchange energy
===============

For this subsection we drop the :math:`ab` indices and recall
:ref:`exchange matrix in a spherical reference frame <user-guide_methods_spinham-spherical>`
and
:ref:`rotation matrix in a spherical reference frame <user-guide_methods_spherical-rf>`:
from previous sections:

.. include:: ../repeated-formulas/exchange-matrix-spherical.txt

.. include:: ../repeated-formulas/spiral-rotation-matrix-spherical.txt

Next we write the expression under the sum explicitly:

.. dropdown:: Details

  .. include:: exchange-matrix-spiral-rotated-details.txt

.. math::
  R^{\dagger}(\theta_m)
  J(d)
  R(\theta_{m+d})
  =
  \begin{pmatrix}
    J_{++}e^{-i\vec{Q}\vec{d}}              &
    J_{+-}e^{i\vec{Q}(2\vec{r}_m+\vec{d})}  &
    J_{+n}e^{i\vec{Q}\vec{r}_m}             \\
    J_{-+}e^{-i\vec{Q}(2\vec{r}_m+\vec{d})} &
    J_{--}e^{i\vec{Q}\vec{d}}               &
    J_{-n}e^{-i\vec{Q}\vec{r}_m}            \\
    J_{n+}e^{-i\vec{Q}(\vec{r}_m+\vec{d})}  &
    J_{n-}e^{i\vec{Q}(\vec{r}_m+\vec{d})}   &
    J_{nn}                                  \\
  \end{pmatrix}

Next we write back the sum over :math:`m`, and using the facts that:

* :math:`\vec{d} = \sum_{i}\vec{a}_in_i`
* :math:`J` does not depend on the index :math:`m`
* :math:`\sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\vec{G}}`
  and
  :math:`\sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\frac{\vec{G}}{2}}`

  .. dropdown:: Details

    .. include:: exchange-details-on-fourier-identities.txt


we get an expression for the sum:

.. dropdown:: Details

  .. include:: exchange-matrix-sum-over-m-details.txt

.. include:: ../repeated-formulas/exchange-matrix-rotated-and-summed-over-m.txt

Which leads to the expression for the exchange part of total energy:

.. dropdown:: Details

  First, we recall the rotation matrix in the spherical reference frame:

  .. include:: ../repeated-formulas/spin-rotation-matrix-spherical.txt

  Then we compute:

  .. include:: exchange-energy-left-part.txt

  and

  .. include:: exchange-energy-right-part.txt

  Finally, we compute the exchange energy:

  .. include:: exchange-energy-not-simplified.txt


  Now we simplify each term of the sum separately:

  .. include:: exchange-energy-simplify-ppmm.txt

  .. include:: exchange-energy-simplify-pmmp.txt

  .. include:: exchange-energy-simplify-pnmn.txt

  .. include:: exchange-energy-simplify-npnm.txt


.. math::
  \begin{multline}
    E_{exchange}
    =
    \dfrac{1}{2}
    \sum_{a, b, \vec{d}}
    MS_aS_b
    \left\{
      J_{nn}\cos\theta_a\cos\theta_b
    \right.
    \\
    +
    \sin\theta_a\sin\theta_b
    \left[
      \dfrac{J_{uu}+J_{vv}}{2}\cos(\vec{Q}\vec{d}+\phi_b-\phi_a)
      +
      \dfrac{J_{uv}-J_{vu}}{2}\sin(\vec{Q}\vec{d}+\phi_b-\phi_a)
    \right]
    \\
    +
    \delta_{\vec{Q},\frac{\vec{G}}{2}}
    \sin\theta_a\sin\theta_b
    \left[
      \dfrac{J_{uu}-J_{vv}}{2}\cos(\phi_a+\phi_b+\vec{Q}\vec{d})
        +
      \dfrac{J_{uv}+J_{vu}}{2}\sin(\phi_a+\phi_b+\vec{Q}\vec{d})
    \right]
    \\
    +
    \delta_{\vec{Q},\vec{G}}
    \left(
      \sin\theta_a\cos\theta_b
      \left[
        J_{un}\cos\phi_a
        +
        J_{vn}\sin\phi_a
      \right]
      \right.
      \\
      \left.
      \left.
      +
      \cos\theta_a\sin\theta_b
      \left[
        J_{nu}\cos(\phi_b+\vec{Q}\vec{d})
        +
        J_{nv}\sin(\phi_b+\vec{Q}\vec{d})
      \right]
    \right)
    \right\}
  \end{multline}


Magnetic field energy
=====================

Next we turn our attention to the Zeeman term:

.. math::
  \mu_B
  \sum_{a}
  g_a
  \left[
  \sum_{m}
  \vec{H}^T_{ma}
  R(\theta_m)
  \right]
  R(\theta_a,\phi_a)
  \vec{S}_{a}^{ferro}

Let us compute part of the expression:

.. math::
  R(\theta_a,\phi_a)
  \vec{S}_a^{ferro}
  =
  S_a
  \begin{pmatrix}
    \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}} \\
    \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}}  \\
    \cos\theta_a                                \\
  \end{pmatrix}

Magnetic field in the spherical reference frame is written as:

.. dropdown:: Details

  Magnetic field in the :math:`\hat{u}\hat{v}\hat{n}` reference frame is written as:

  .. math::
    \langle uvn\vert H_{ma}\rangle = \left(H_{ma}^u, H_{ma}^v, H_{ma}^n\right)^T

  Let us recall the transformation matrix:

  .. include:: ../repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

  And compute the magnetic field in the spherical reference frame:

  .. math::
    \langle u^+u^-n\vert H_{ma}\rangle
    =
    \langle u^+u^-n\vert uvn\rangle
    \langle uvn\vert H_{ma}\rangle
    =
    \langle uvn\vert T^{\dagger}\vert uvn\rangle
    \langle uvn\vert H_{ma}\rangle

  Which leads to the expression:

.. math::
  \dfrac{1}{\sqrt{2}}
  \begin{pmatrix}
    1 & -i & 0        \\
    1 &  i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}
  \begin{pmatrix}
    H_{ma}^u \\
    H_{ma}^v \\
    H_{ma}^n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{H_{ma}^u - iH_{ma}^v}{\sqrt{2}} \\
    \dfrac{H_{ma}^u + iH_{ma}^v}{\sqrt{2}} \\
    H_{ma}^n     \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    \dfrac{H_{ma}^{-}}{\sqrt{2}}       \\
    \dfrac{H_{ma}^{+}}{\sqrt{2}}       \\
    H_{ma}^n \\
  \end{pmatrix}

Then the energy is:

.. dropdown:: Details

  .. include:: field-energy-details.txt

.. math::
  \mu_B
  \sum_{a}
  g_a  S_a
  \sum_{m}
  \left[
  \sin\theta_a
  \left(
    H_{ma}^u\cos(\vec{Q}\cdot\vec{r}_m+\phi_a)
    -
    H_{ma}^v\sin(\vec{Q}\cdot\vec{r}_m+\phi_a)
  \right)
  +
  H_{ma}^n\cos\theta_a
  \right]

Let us set each component of the magnetic field to be a harmonic function in the
:math:`\hat{u}\hat{v}\hat{n}` reference frame:

.. math::
  \begin{aligned}
    H_{ma}^u
    &=
    H^u\cos(\vec{Q^u}(\vec{r}_m+\vec{r}_a)+\varphi^u)
    =
    H^u\cos(\vec{Q}^u\vec{r}_m+\phi_a^u) \\
    H_{ma}^v
    &=
    H^v\cos(\vec{Q^v}(\vec{r}_m+\vec{r}_a)+\varphi^v)
    =
    H^v\cos(\vec{Q}^v\vec{r}_m+\phi_a^v) \\
    H_{ma}^n
    &=
    H^v\cos(\vec{Q^v}(\vec{r}_m+\vec{r}_a)+\varphi^v)
    =
    H^n\cos(\vec{Q}^n\vec{r}_m+\phi_a^n) \\
  \end{aligned}

Then we can write:

.. dropdown:: Details

  * :math:`\hat{u}` component

    .. include:: field-sum-u-component-details.txt

  * :math:`\hat{v}` component

    .. include:: field-sum-v-component-details.txt

  * :math:`\hat{n}` component

    .. include:: field-sum-n-component-details.txt

.. math::
  E_{Zeeman}
  =
  \mu_BM
  \sum_{a}
  g_a  S_a
  \left\{
    H^n
    \delta_{\vec{Q}^n, \vec{G}}
    \cos\phi^n_a\cos\theta_a
  \right.
  \\
  +
  \sin\theta_a
  \left(
    \dfrac{H^uM}{2}
    \left[
      \delta_{\vec{Q}_m^u + \vec{Q}_m, \vec{G}} \cos(\phi_a^u + \phi_a)
      +
      \delta_{\vec{Q}_m^u - \vec{Q}_m, \vec{G}} \cos(\phi_a^u - \phi_a)
    \right]
  \right.
  \\
  \left.
  \left.
    -
    \dfrac{H^vM}{2}
    \left[
      \delta_{\vec{Q}_m^v + \vec{Q}_m, \vec{G}} \sin(\phi_a^v + \phi_a)
      +
      \delta_{\vec{Q}_m^v - \vec{Q}_m, \vec{G}} \sin(\phi_a^v - \phi_a)
    \right]
  \right)
  \right\}

Total energy
============

Finally, we can write the total classical energy:

.. include:: ../repeated-formulas/classic-total-energy.txt
