.. _user-guide_methods_spinham-spherical:

********************************************
Hamiltonian in a "spherical" reference frame
********************************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/in-uvn.txt
  * .. include:: page-notations/parentheses.txt

.. note::
  In this page we discuss only the exchange (with on-site anisotropy) part of the Hamiltonian.

The reference frame of the given Hamiltonian is changed from :math:`xyz` to :math:`uvn`
as described in :ref:`user-guide_methods_xyz-to-uvn`. We start this section from a
Hamiltonian written in a :math:`uvn` reference frame:

.. include:: repeated-formulas/hamiltonian-main-any.txt

Exchange matrices
=================

The transformation of spin vectors to the spherical reference frame was discussed
in the :ref:`previous section <user-guide_methods_spherical-rf>`.
In this section we focus our attention on the transformation of the exchange
matrices. The exchange matrices are transformed as follows:

.. math::
  &\langle u^+u^-n \vert J_{ab}(\vec{d}_{ab}) \vert u^+u^-n \rangle
  =
  \langle u^+u^-n \vert uvn \rangle
  \langle uvn \vert J_{ab}(\vec{d}_{ab}) \vert uvn \rangle
  \langle uvn \vert u^+u^-n \rangle
  =\\&=
  \langle uvn \vert T^{\dagger} \vert uvn \rangle
  \langle uvn \vert J_{ab}(\vec{d}_{ab}) \vert uvn \rangle
  \langle uvn \vert T\vert uvn \rangle

Now we recall the definition of the transformation matrix
(from :ref:`here <user-guide_methods_spherical-rf>`):

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

and separate exchange matrix into isotropic, symmetric anisotropic and antisymmetric parts:

.. include:: repeated-formulas/exchange-matrix-decomposition-uvn.txt

Which leads to the exchange matrix in a spherical reference frame:

.. dropdown:: Details

  .. math::
    &\langle u^+u^-n \vert J_{ab}(\vec{d}_{ab}) \vert u^+u^-n \rangle
    =
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
    =\\&=
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
    =\\&=
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

  Which gives:

  .. math::
    \langle u^+u^-n \vert J_{ab}(\vec{d}_{ab})\vert u^+u^-n \rangle
    =
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
      D^{\pm} = \dfrac{D_v \pm iD_u}{\sqrt{2}};      &
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
