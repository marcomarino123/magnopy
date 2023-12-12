.. _user-guide_methods_energy-classic:

****************
Classical energy
****************

.. dropdown:: Notation used in this page

    * We work in the :math:`\vert u^+ u^- n \rangle` reference frame, if not specified otherwise.
    * Parentheses () and square brackets [] are equivalent.

Let us recall the Hamiltonian:

.. include:: repeated-formulas/hamiltonian-main-from-ferro-any.txt


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
  \vec{H}^T
  R(\theta_m)
  \right]
  R(\theta_a,\phi_a)
  \vec{S}_{a}^{ferro}

We focus our attention on the expressions in the square brackets:

Exchange matrices
=================

For this subsection we drop the :math:`ab` indices and recall
:ref:`exchange matrix in a spherical reference frame <user-guide_methods_spinham-spherical>`
and
:ref:`rotation matrix in a spherical reference frame <user-guide_methods_spherical-rf>`:
from previous sections:

.. include:: repeated-formulas/exchange-matrix-spherical.txt

.. include:: repeated-formulas/spiral-rotation-matrix-spherical.txt

Next we write the expression under the sum explicitly:

.. dropdown:: Details

  .. math::
    \begin{pmatrix}
      e^{i\vec{Q}\vec{r}_m} & 0              & 0 \\
      0             & e^{-i\vec{Q}\vec{r}_m} & 0 \\
      0             & 0              & 1 \\
    \end{pmatrix}
    \begin{pmatrix}
      J_{++} & J_{+-} & J_{+n} \\
      J_{-+} & J_{--} & J_{-n} \\
      J_{n+} & J_{n-} & J_{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      e^{-i\vec{Q}(\vec{r}_m+\vec{d})} &
      0 &
      0 \\
      0 &
      e^{i\vec{Q}(\vec{r}_m+\vec{d})} &
      0 \\
      0 &
      0 &
      1 \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      J_{++}e^{i\vec{Q}\vec{r}_m}  &
      J_{+-}e^{i\vec{Q}\vec{r}_m}  &
      J_{+n}e^{i\vec{Q}\vec{r}_m}  \\
      J_{-+}e^{-i\vec{Q}\vec{r}_m} &
      J_{--}e^{-i\vec{Q}\vec{r}_m} &
      J_{-n}e^{-i\vec{Q}\vec{r}_m} \\
      J_{n+}                       &
      J_{n-}                       &
      J_{nn}                       \\
    \end{pmatrix}
    \begin{pmatrix}
      e^{-i\vec{Q}(\vec{r}_m+\vec{d})} &
      0 &
      0 \\
      0 &
      e^{i\vec{Q}(\vec{r}_m+\vec{d})} &
      0 \\
      0 &
      0 &
      1 \\
    \end{pmatrix}
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
  and
  :math:`\sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = \sum_{r_m}e^{\pm i\vec{Q}(\vec{r}_m+\vec{d})}`


  .. dropdown:: Details

    Due to the periodicity of the crystal lattice, the sum over :math:`r_m` will not
    change if we shift all the vectors :math:`r_m` by any lattice vector
    :math:`\vec{r}_0 = \sum_{i}\vec{a}_in_i`

    .. math::
      \sum_{\vec{r}_m} e^{\pm i\vec{Q}\vec{r}_m}
      =
      \sum_{\vec{r}_m} e^{\pm i\vec{Q}(\vec{r}_m + \vec{r}_0)}
      =
      e^{\pm i\vec{Q}\vec{r}_0} \sum_{\vec{r}_m} e^{\pm i\vec{Q}\vec{r}_m}

    Which leads to the conclusions that either the sum is zero, or
    :math:`\pm\vec{Q}\vec{r}_0 = 2\pi n` for any :math:`\vec{r}_0`.
    Whose two facts give us the value for the sum:

    .. math::
      \sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M

    And the restriction on the :math:`\vec{Q}` vector:

    .. math::
      \sum_{i=1}^{3}Q_{a_i}a_in_i = 2\pi n,  \forall n_1, n_2, n_3 \in \mathbb{Z}

    where we projected the :math:`\vec{Q}` vector on the three lattice vectors
    :math:`\vec{a}_1`, :math:`\vec{a}_2`, :math:`\vec{a}_3`; :math:`n \in \mathbb{Z}`
    This restriction leads to the definition of the allowed :math:`\vec{Q}` vectors:

    .. math::
      Q_{a_i} = \dfrac{2\pi}{a_i}n_i,  i = 1, 2, 3

    where :math:`n_i \in \mathbb{Z}`.

    Which means that the :math:`\vec{Q}` vector is a reciprocal lattice vector,
    which we denote as :math:`\vec{G} = \sum_{i}\vec{b}_in_i`. For the spiral state this
    means that the ordering of the spins is ferromagnetic between the unit cells. We
    denote this condition on the :math:`\vec{Q}` vector as :math:`\delta_{\vec{Q},\vec{G}}`
    and write the sum in a form:

    .. math::
      \sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\vec{G}}

    In the case of the second sum the logic is the same, but at the end the condition on the
    :math:`\vec{Q}` vector is different:

    .. math::
      Q_{a_i} = \dfrac{\pi}{a_i}n_i,  i = 1, 2, 3

    Which means that the :math:`\vec{Q}` vector is a reciprocal lattice vector divided by 2:
    :math:`\vec{Q} = \dfrac{\vec{G}}{2} = \sum_{i}\dfrac{\vec{b}_i}{2}n_i`.
    For the spiral state it can be interpreted as the possible ferromagnetic order of
    spins or antiferromagnetic order of :math:`\hat{u}\hat{v}` component of spin between
    unit cells. We denote this condition on the :math:`\vec{Q}` vector as
    :math:`\delta_{\vec{Q},\frac{\vec{G}}{2}}` and write the sum in a form:

    .. math::
      \sum_{r_m}e^{\pm i\vec{Q}\vec{r}_m} = M\delta_{\vec{Q},\frac{\vec{G}}{2}}



we get an expression for the sum:

.. dropdown:: Details

  .. math::
    \begin{multline}
      \sum_m
      R^{\dagger}(\theta_m)
      J_{ab}(d_{ab})
      R(\theta_{m+d})
      \\
      =
      \begin{pmatrix}
        J_{++}\sum_m e^{-i\vec{Q}\vec{d}}              &
        J_{+-}\sum_m e^{i\vec{Q}(2\vec{r}_m+\vec{d})}  &
        J_{+n}\sum_m e^{i\vec{Q}\vec{r}_m}             \\
        J_{-+}\sum_m e^{-i\vec{Q}(2\vec{r}_m+\vec{d})} &
        J_{--}\sum_m e^{i\vec{Q}\vec{d}}               &
        J_{-n}\sum_m e^{-i\vec{Q}\vec{r}_m}            \\
        J_{n+}\sum_m e^{-i\vec{Q}(\vec{r}_m+\vec{d})}  &
        J_{n-}\sum_m e^{i\vec{Q}(\vec{r}_m+\vec{d})}   &
        J_{nn}\sum_m 1                                 \\
      \end{pmatrix}
      \\
      =
      \begin{pmatrix}
        J_{++}e^{-i\vec{Q}\vec{d}}\sum_m 1   &
        J_{+-}\sum_m e^{i\vec{Q}2\vec{r}_m}  &
        J_{+n}\sum_m e^{i\vec{Q}\vec{r}_m}   \\
        J_{-+}\sum_m e^{-i\vec{Q}2\vec{r}_m} &
        J_{--}e^{i\vec{Q}\vec{d}}\sum_m 1    &
        J_{-n}\sum_m e^{-i\vec{Q}\vec{r}_m}  \\
        J_{n+}\sum_m e^{-i\vec{Q}\vec{r}_m}  &
        J_{n-}\sum_m e^{i\vec{Q}\vec{r}_m}   &
        M\cdot J_{nn}                        \\
      \end{pmatrix}
      \\
      =
      \begin{pmatrix}
        Me^{-i\vec{Q}\vec{d}} J_{++}                         &
        M\delta_{\vec{Q},\frac{\vec{G}}{2}} J_{+-} &
        M\delta_{\vec{Q},\vec{G}}\cdot J_{+n}                \\
        M\delta_{\vec{Q},\frac{\vec{G}}{2}} J_{-+} &
        Me^{i\vec{Q}\vec{d}} J_{--}                          &
        M\delta_{\vec{Q},\vec{G}}\cdot J_{-n}                \\
        M\delta_{\vec{Q},\vec{G}}\cdot J_{n+}                &
        M\delta_{\vec{Q},\vec{G}}\cdot J_{n-}                &
        M\cdot J_{nn}                                        \\
      \end{pmatrix}
    \end{multline}

.. math::
  \sum_m
  R^{\dagger}(\theta_m)
  J_{ab}(d_{ab})
  R(\theta_{m+d})
  =
  M
  \begin{pmatrix}
    e^{-i\vec{Q}\vec{d}}J_{++}                          &
    \delta_{\vec{Q},\frac{\vec{G}}{2}} J_{+-} &
    \delta_{\vec{Q},\vec{G}}\cdot J_{+n}                \\
    \delta_{\vec{Q},\frac{\vec{G}}{2}} J_{-+} &
    e^{i\vec{Q}\vec{d}}J_{--}                           &
    \delta_{\vec{Q},\vec{G}}\cdot J_{-n}                \\
    \delta_{\vec{Q},\vec{G}}\cdot J_{n+}                &
    \delta_{\vec{Q},\vec{G}}\cdot J_{n-}                &
    J_{nn}                                              \\
  \end{pmatrix}

Which leads to the expression for the exchange part of total energy:

.. dropdown:: Details

  First, we recall the rotation matrix in the spherical reference frame:

  .. include:: repeated-formulas/spin-rotation-matrix-spherical.txt

  Then we compute:

  .. math::
    R(\theta_b,\phi_b)
    \vec{S}_b^{ferro}
    =
    S_b
    \begin{pmatrix}
      \dfrac{\sin\theta_b e^{-i\phi_b}}{\sqrt{2}}  \\
      \dfrac{\sin\theta_b e^{i\phi_b}}{\sqrt{2}}   \\
      \cos\theta_b                                 \\
    \end{pmatrix}

  and

  .. math::
    (\vec{S}_a^{ferro})^T
    R^{\dagger}(\theta_a,\phi_a)
    =
    (0,0,S_a)
    \begin{pmatrix}
      \dfrac{1+\cos\theta_a}{2}                     &
      \dfrac{(\cos\theta_a - 1)e^{-2i\phi_a}}{2}    &
      \dfrac{-\sin\theta_a e^{-i\phi_a} }{\sqrt{2}} \\
      \dfrac{(\cos\theta_a-1)e^{2i\phi_a}}{2}       &
      \dfrac{1 + \cos\theta_a}{2}                   &
      \dfrac{-\sin\theta_a e^{i\phi_a}}{\sqrt{2}}   \\
      \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}}    &
      \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}}   &
      \cos\theta_a                                  \\
    \end{pmatrix}
    =
    S_a
    \left(
    \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}},
    \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}},
    \cos\theta_a
    \right)

  Finally, we compute the exchange energy:

  .. math::
    \begin{multline}
      H
      =
      \dfrac{1}{2}
      \sum_{a, b, \vec{d}}
      (\vec{S}_a^{ferro})^T
      R^{\dagger}(\theta_a,\phi_a)
      \left[
      \sum_{m}
      R^{\dagger}(\theta_m)
      J_{ab}(d_{ab})
      R(\theta_{m+d})
      \right]
      R(\theta_b,\phi_b)
      \vec{S}_b^{ferro}
      \\
      =
      \dfrac{1}{2}
      \sum_{a, b, \vec{d}}
      MS_aS_b
      \left(
      \dfrac{\sin\theta_a e^{i\phi_a}}{\sqrt{2}},
      \dfrac{\sin\theta_a e^{-i\phi_a}}{\sqrt{2}},
      \cos\theta_a
      \right)
      \begin{pmatrix}
        e^{-i\vec{Q}\vec{d}}J_{++}                          &
        \delta_{\vec{Q},\frac{\vec{G}}{2}} J_{+-} &
        \delta_{\vec{Q},\vec{G}}\cdot J_{+n}                \\
        \delta_{\vec{Q},\frac{\vec{G}}{2}} J_{-+} &
        e^{i\vec{Q}\vec{d}}J_{--}                           &
        \delta_{\vec{Q},\vec{G}}\cdot J_{-n}                \\
        \delta_{\vec{Q},\vec{G}}\cdot J_{n+}                &
        \delta_{\vec{Q},\vec{G}}\cdot J_{n-}                &
        J_{nn}                                              \\
      \end{pmatrix}
      \begin{pmatrix}
        \dfrac{\sin\theta_b e^{-i\phi_b}}{\sqrt{2}}  \\
        \dfrac{\sin\theta_b e^{i\phi_b}}{\sqrt{2}}   \\
        \cos\theta_b                                 \\
      \end{pmatrix}
      \\
      =
      \dfrac{1}{2}
      \sum_{a, b, \vec{d}}
      MS_aS_b
      \left(
      \dfrac{
      J_{++}\sin\theta_a\sin\theta_b e^{i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      +
      J_{--}\sin\theta_a\sin\theta_b e^{-i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      }{2}
      +
      J_{nn}\cos\theta_a\cos\theta_b
      \right.
      \\
      +
      \delta_{\vec{Q},\frac{\vec{G}}{2}}
      \left[
      \dfrac{
      J_{+-}\sin\theta_a\sin\theta_b e^{i(\phi_a+\phi_b)}
      +
      J_{-+}\sin\theta_a\sin\theta_b e^{-i(\phi_a+\phi_b)}
      }{2}
      \right]
      \\
      +
      \delta_{\vec{Q},\vec{G}}
      \left[
      \dfrac{
      J_{+n}\sin\theta_a\cos\theta_b e^{i\phi_a}
      +
      J_{-n}\sin\theta_a\cos\theta_b e^{-i\phi_a}
      }{\sqrt{2}}
      \right.
      \\
      \left.
      +
      \dfrac{
      J_{n+}\cos\theta_a\sin\theta_b e^{-i\phi_b}
      +
      J_{n-}\cos\theta_a\sin\theta_b e^{i\phi_b}
      }{\sqrt{2}}
      \right]
      \left.
      \right)
    \end{multline}

  Now we simplify each term of the summ separately:

  .. math::
    \begin{multline}
      \dfrac{
        J_{++}\sin\theta_a\sin\theta_b e^{i(\phi_a-\phi_b-\vec{Q}\vec{d})}
        +
        J_{--}\sin\theta_a\sin\theta_b e^{-i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      }{2}
      \\
      =
      \dfrac{
        (A + iD_n)\sin\theta_a\sin\theta_b e^{i(\phi_a-\phi_b-\vec{Q}\vec{d})}
        +
        (A - iD_n)\sin\theta_a\sin\theta_b e^{-i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      }{2}
      \\
      =
      A\sin\theta_a\sin\theta_b
      \dfrac{
      e^{i(\phi_a-\phi_b)}+e^{-i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      }{2}
      -
      D_n\sin\theta_a\sin\theta_b
      \dfrac{
      e^{i(\phi_a-\phi_b)}-e^{-i(\phi_a-\phi_b-\vec{Q}\vec{d})}
      }{2i}
      \\
      =
      A\sin\theta_a\sin\theta_b\cos(\phi_a-\phi_b-\vec{Q}\vec{d})
      -
      D_n\sin\theta_a\sin\theta_b\sin(\phi_a-\phi_b-\vec{Q}\vec{d})
      \\
      =
      (J+\dfrac{S_{uu}+S_{vv}}{2})\sin\theta_a\sin\theta_b\cos(\phi_a-\phi_b-\vec{Q}\vec{d})
      -
      D_n\sin\theta_a\sin\theta_b\sin(\phi_a-\phi_b-\vec{Q}\vec{d})
      \\
      =
      \dfrac{J_{uu}+J_{vv}}{2}\sin\theta_a\sin\theta_b\cos(\phi_a-\phi_b-\vec{Q}\vec{d})
      -
      \dfrac{J_{uv}-J_{vu}}{2}\sin\theta_a\sin\theta_b\sin(\phi_a-\phi_b-\vec{Q}\vec{d})
      \\
      =
      \dfrac{J_{uu}+J_{vv}}{2}\sin\theta_a\sin\theta_b\cos(\vec{Q}\vec{d}+\phi_b-\phi_a)
      +
      \dfrac{J_{uv}-J_{vu}}{2}\sin\theta_a\sin\theta_b\sin(\vec{Q}\vec{d}+\phi_b-\phi_a)
    \end{multline}

  where :math:`A = J+\dfrac{S_{uu}+S_{vv}}{2}`

  .. math::
    \begin{multline}
      \dfrac{
      J_{+-}\sin\theta_a\sin\theta_b e^{i(\phi_a+\phi_b)}
      +
      J_{-+}\sin\theta_a\sin\theta_b e^{-i(\phi_a+\phi_b)}
      }{2}
      \\
      =
      \dfrac{
      (A-iS_{uv})\sin\theta_a\sin\theta_b e^{i(\phi_a+\phi_b)}
      +
      (A+iS_{uv})\sin\theta_a\sin\theta_b e^{-i(\phi_a+\phi_b)}
      }{2}
      \\
      =
      A\sin\theta_a\sin\theta_b
      \dfrac{
      e^{i(\phi_a+\phi_b)}+e^{-i(\phi_a+\phi_b)}
      }{2}
      +
      S_{uv}\sin\theta_a\sin\theta_b
      \dfrac{
      e^{i(\phi_a+\phi_b)}-e^{-i(\phi_a+\phi_b)}
      }{2i}
      \\
      =
      A\sin\theta_a\sin\theta_b\cos(\phi_a+\phi_b)
      +
      S_{uv}\sin\theta_a\sin\theta_b\sin(\phi_a+\phi_b)
      \\
      =
      \dfrac{S_{uu}-S_{vv}}{2}\sin\theta_a\sin\theta_b\cos(\phi_a+\phi_b)
      +
      S_{uv}\sin\theta_a\sin\theta_b\sin(\phi_a+\phi_b)
      \\
      =
      \dfrac{J_{uu}-J_{vv}}{2}\sin\theta_a\sin\theta_b\cos(\phi_a+\phi_b)
      +
      \dfrac{J_{uv}+J_{vu}}{2}\sin\theta_a\sin\theta_b\sin(\phi_a+\phi_b)
    \end{multline}


  where :math:`A = \dfrac{S_{uu}-S_{vv}}{2}`

  .. math::
    \begin{multline}
      \dfrac{
      J_{+n}\sin\theta_a\cos\theta_b e^{i\phi_a}
      +
      J_{-n}\sin\theta_a\cos\theta_b e^{-i\phi_a}
      }{\sqrt{2}}
      \\
      =
      \dfrac{
      (J_{un}-iJ_{vn})\sin\theta_a\cos\theta_b e^{i\phi_a}
      +
      (J_{un}+iJ_{vn})\sin\theta_a\cos\theta_b e^{-i\phi_a}
      }{2}
      \\
      =
      J_{un}\sin\theta_a\cos\theta_b
      \dfrac{
      e^{i\phi_a}
      +
      e^{-i\phi_a}
      }{2}
      +
      J_{vn}\sin\theta_a\cos\theta_b
      \dfrac{
      e^{i\phi_a}
      -
      e^{-i\phi_a}
      }{2i}
      \\
      =
      J_{un}\sin\theta_a\cos\theta_b\cos\phi_a
      +
      J_{vn}\sin\theta_a\cos\theta_b\sin\phi_a
      \\
      =
      (S_{un} - D_v)\sin\theta_a\cos\theta_b\cos\phi_a
      +
      (S_{vn} + D_u)\sin\theta_a\cos\theta_b\sin\phi_a
    \end{multline}

  where :math:`J_{un} = S_{un} - D_v` and :math:`J_{vn} = S_{vn} + D_u`

  .. math::
    \begin{multline}
      \dfrac{
      J_{n+}\cos\theta_a\sin\theta_b e^{-i\phi_b}
      +
      J_{n-}\cos\theta_a\sin\theta_b e^{i\phi_b}
      }{\sqrt{2}}
      \\
      =
      \dfrac{
      (J_{nu}+iJ_{nv})\cos\theta_a\sin\theta_b e^{-i\phi_b}
      +
      (J_{nu} - iJ_{nv})\cos\theta_a\sin\theta_b e^{i\phi_b}
      }{2}
      \\
      =
      J_{nu}\cos\theta_a\sin\theta_b
      \dfrac{
      e^{-i\phi_b}+e^{i\phi_b}
      }{2}
      +
      J_{nv}\cos\theta_a\sin\theta_b
      \dfrac{
      e^{i\phi_b}-e^{-i\phi_b}
      }{2i}
      \\
      =
      J_{nu}\cos\theta_a\sin\theta_b\cos\phi_b
      +
      J_{nv}\cos\theta_a\sin\theta_b\sin\phi_b
      \\
      =
      (S_{un} + D_v)\cos\theta_a\sin\theta_b\cos\phi_b
      +
      (S_{vn} - D_u)\cos\theta_a\sin\theta_b\sin\phi_b
    \end{multline}

  where :math:`J_{nu} = S_{un} + D_v` and :math:`J_{nv} = S_{vn} - D_u`

.. math::
  \begin{multline}
    \dfrac{1}{2}
    \sum_{a, b, \vec{d}}
    MS_aS_b
    \left(
    J_{nn}\cos\theta_a\cos\theta_b
    \right.
    \\+
    \sin\theta_a\sin\theta_b
    \left(
    \dfrac{J_{uu}+J_{vv}}{2}\cos(\vec{Q}\vec{d}+\phi_b-\phi_a)
    +
    \dfrac{J_{uv}-J_{vu}}{2}\sin(\vec{Q}\vec{d}+\phi_b-\phi_a)
    \right)
    \\
    +
    \delta_{\vec{Q},\frac{\vec{G}}{2}}
    \sin\theta_a\sin\theta_b
    \left(
    \dfrac{J_{uu}-J_{vv}}{2}\cos(\phi_a+\phi_b)
      +
    \dfrac{J_{uv}+J_{vu}}{2}\sin(\phi_a+\phi_b)
    \right)
    \\
    +
    \delta_{\vec{Q},\vec{G}}
    \left[
    \sin\theta_a\cos\theta_b
    (
    J_{un}\cos\phi_a
    +
    J_{vn}\sin\phi_a
    )
    +
    \cos\theta_a\sin\theta_b
    (
    J_{nu}\cos\phi_b
    +
    J_{nv}\sin\phi_b
    )
    \right]
    \left.
    \right)
    \end{multline}
