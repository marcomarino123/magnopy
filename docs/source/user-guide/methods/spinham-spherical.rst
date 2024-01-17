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
      J_{ab}^{uu} & J_{ab}^{uv} & J_{ab}^{un} \\
      J_{ab}^{vu} & J_{ab}^{vv} & J_{ab}^{vn} \\
      J_{ab}^{nu} & J_{ab}^{nv} & J_{ab}^{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      J_{ab}^{uu} - i J_{ab}^{vu} & J_{ab}^{uv} - i J_{ab}^{vv} & J_{ab}^{un} - i J_{ab}^{vn} \\
      J_{ab}^{uu} + i J_{ab}^{vu} & J_{ab}^{uv} + i J_{ab}^{vv} & J_{ab}^{un} + i J_{ab}^{vn} \\
      \sqrt{2}J_{ab}^{nu}    & \sqrt{2}J_{ab}^{nv}    & \sqrt{2}J_{ab}^{nn}    \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      (J_{ab}^{uu} + J_{ab}^{vv}) + i(J_{ab}^{uv} - J_{ab}^{vu}) &
      (J_{ab}^{uu} - J_{ab}^{vv}) - i(J_{ab}^{uv} + J_{ab}^{vu}) &
      \sqrt{2}(J_{ab}^{un} - iJ_{ab}^{vn})             \\
      (J_{ab}^{uu} - J_{ab}^{vv}) + i(J_{ab}^{uv} + J_{ab}^{vu}) &
      (J_{ab}^{uu} + J_{ab}^{vv}) - i(J_{ab}^{uv} - J_{ab}^{vu}) &
      \sqrt{2}(J_{ab}^{un} + iJ_{ab}^{vn})             \\
      \sqrt{2}(J_{ab}^{nu} + iJ_{ab}^{nv})             &
      \sqrt{2}(J_{ab}^{nu} - iJ_{ab}^{nv})             &
      2J_{ab}^{nn}                                \\
    \end{pmatrix}

  Which gives:

  .. math::
    \langle u^+u^-n \vert J_{ab}(\vec{d}_{ab})\vert u^+u^-n \rangle
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      2J_{iso} + S_{ab}^{uu} + S_{ab}^{vv} + 2iD_{ab}^n      &
      S_{ab}^{uu} - S_{ab}^{vv} - 2iS_{ab}^{uv}              &
      \sqrt{2}(S_{ab}^{un} - iS_{ab}^{vn} - D_{ab}^v - iD_{ab}^u) \\
      S_{ab}^{uu} - S_{ab}^{vv} + 2iS_{ab}^{uv}              &
      2J_{iso} + S_{ab}^{uu} + S_{ab}^{vv} - 2iD_{ab}^n      &
      \sqrt{2}(S_{ab}^{un} + iS_{ab}^{vn} - D_{ab}^v + iD_{ab}^u) \\
      \sqrt{2}(S_{ab}^{un} + iS_{ab}^{vn} + D_{ab}^v - iD_{ab}^u) &
      \sqrt{2}(S_{ab}^{un} - iS_{ab}^{vn} + D_{ab}^v + iD_{ab}^u) &
      2J_{iso} + 2S_{ab}^{nn}                      \\
    \end{pmatrix}

.. include:: repeated-formulas/exchange-matrix-spherical.txt

Let us note a few symmetries of the exchange matrix in a spherical reference frame:

.. include:: repeated-formulas/exchange-matrix-symmetries-spherical.txt

.. dropdown:: Alternative way to write the matrix

  If we define:

  .. math::
    \begin{matrix}
      D^{\pm} = \dfrac{D_{ab}^v \pm iD_{ab}^u}{\sqrt{2}};      &
      S^{\pm} = \dfrac{S_{ab}^{un} \pm iS_{ab}^{vn}}{\sqrt{2}} \\
    \end{matrix}

  Then we can write the exchange matrix in the spherical reference frame as:

  .. math::
    \begin{pmatrix}
      J_{iso} + \dfrac{S_{ab}^{uu} + S_{ab}^{vv}}{2} + iD_{ab}^n &
      \dfrac{S_{ab}^{uu} - S_{ab}^{vv}}{2} - iS_{ab}^{uv}        &
      S^- - D^+                                   \\
      \dfrac{S_{ab}^{uu} - S_{ab}^{vv}}{2} + iS_{ab}^{uv}        &
      J_{iso} + \dfrac{S_{ab}^{uu} + S_{ab}^{vv}}{2} - iD_{ab}^n &
      S^+ - D^-                                   \\
      S^+ + D^-                                   &
      S^- + D^+                                   &
      J_{iso} + S_{ab}^{nn}                            \\
    \end{pmatrix}
