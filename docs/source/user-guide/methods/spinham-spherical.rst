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
  &\langle u^+u^-n \vert J_{ij}(\boldsymbol{d_{ij}}) \vert u^+u^-n \rangle
  =
  \langle u^+u^-n \vert uvn \rangle
  \langle uvn \vert J_{ij}(\boldsymbol{d_{ij}}) \vert uvn \rangle
  \langle uvn \vert u^+u^-n \rangle
  =\\&=
  \langle uvn \vert T^{\dagger} \vert uvn \rangle
  \langle uvn \vert J_{ij}(\boldsymbol{d_{ij}}) \vert uvn \rangle
  \langle uvn \vert T\vert uvn \rangle

Now we recall the definition of the transformation matrix
(from :ref:`here <user-guide_methods_spherical-rf>`):

.. include:: repeated-formulas/transformation-matrix-uvn-to-spherical-uvn.txt

and separate exchange matrix into isotropic, symmetric anisotropic and antisymmetric parts:

.. include:: repeated-formulas/exchange-matrix-decomposition-uvn.txt

Which leads to the exchange matrix in a spherical reference frame:

.. dropdown:: Details

  .. math::
    &\langle u^+u^-n \vert J_{ij}(\boldsymbol{d_{ij}}) \vert u^+u^-n \rangle
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      1 & -i & 0        \\
      1 &  i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    \begin{pmatrix}
      J_{ij}^{uu} & J_{ij}^{uv} & J_{ij}^{un} \\
      J_{ij}^{vu} & J_{ij}^{vv} & J_{ij}^{vn} \\
      J_{ij}^{nu} & J_{ij}^{nv} & J_{ij}^{nn} \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      J_{ij}^{uu} - i J_{ij}^{vu} & J_{ij}^{uv} - i J_{ij}^{vv} & J_{ij}^{un} - i J_{ij}^{vn} \\
      J_{ij}^{uu} + i J_{ij}^{vu} & J_{ij}^{uv} + i J_{ij}^{vv} & J_{ij}^{un} + i J_{ij}^{vn} \\
      \sqrt{2}J_{ij}^{nu}    & \sqrt{2}J_{ij}^{nv}    & \sqrt{2}J_{ij}^{nn}    \\
    \end{pmatrix}
    \begin{pmatrix}
      1 &  1 & 0        \\
      i & -i & 0        \\
      0 &  0 & \sqrt{2} \\
    \end{pmatrix}
    =\\&=
    \dfrac{1}{2}
    \begin{pmatrix}
      (J_{ij}^{uu} + J_{ij}^{vv}) + i(J_{ij}^{uv} - J_{ij}^{vu}) &
      (J_{ij}^{uu} - J_{ij}^{vv}) - i(J_{ij}^{uv} + J_{ij}^{vu}) &
      \sqrt{2}(J_{ij}^{un} - iJ_{ij}^{vn})             \\
      (J_{ij}^{uu} - J_{ij}^{vv}) + i(J_{ij}^{uv} + J_{ij}^{vu}) &
      (J_{ij}^{uu} + J_{ij}^{vv}) - i(J_{ij}^{uv} - J_{ij}^{vu}) &
      \sqrt{2}(J_{ij}^{un} + iJ_{ij}^{vn})             \\
      \sqrt{2}(J_{ij}^{nu} + iJ_{ij}^{nv})             &
      \sqrt{2}(J_{ij}^{nu} - iJ_{ij}^{nv})             &
      2J_{ij}^{nn}                                \\
    \end{pmatrix}

  Which gives:

  .. math::
    \langle u^+u^-n \vert J_{ij}(\boldsymbol{d_{ij}})\vert u^+u^-n \rangle
    =
    \dfrac{1}{2}
    \begin{pmatrix}
      2J^{iso} + S_{ij}^{uu} + S_{ij}^{vv} + 2iD_{ij}^n      &
      S_{ij}^{uu} - S_{ij}^{vv} - 2iS_{ij}^{uv}              &
      \sqrt{2}(S_{ij}^{un} - iS_{ij}^{vn} - D_{ij}^v - iD_{ij}^u) \\
      S_{ij}^{uu} - S_{ij}^{vv} + 2iS_{ij}^{uv}              &
      2J^{iso} + S_{ij}^{uu} + S_{ij}^{vv} - 2iD_{ij}^n      &
      \sqrt{2}(S_{ij}^{un} + iS_{ij}^{vn} - D_{ij}^v + iD_{ij}^u) \\
      \sqrt{2}(S_{ij}^{un} + iS_{ij}^{vn} + D_{ij}^v - iD_{ij}^u) &
      \sqrt{2}(S_{ij}^{un} - iS_{ij}^{vn} + D_{ij}^v + iD_{ij}^u) &
      2J^{iso} + 2S_{ij}^{nn}                      \\
    \end{pmatrix}

.. include:: repeated-formulas/exchange-matrix-spherical.txt

Let us note a few symmetries of the exchange matrix in a spherical reference frame:

.. include:: repeated-formulas/exchange-matrix-symmetries-spherical.txt

.. dropdown:: Alternative way to write the matrix

  If we define:

  .. math::
    \begin{matrix}
      D^{\pm} = \dfrac{D_{ij}^v \pm iD_{ij}^u}{\sqrt{2}};      &
      S^{\pm} = \dfrac{S_{ij}^{un} \pm iS_{ij}^{vn}}{\sqrt{2}} \\
    \end{matrix}

  Then we can write the exchange matrix in the spherical reference frame as:

  .. math::
    \begin{pmatrix}
      J^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} + iD_{ij}^n &
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} - iS_{ij}^{uv}        &
      S^- - D^+                                   \\
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} + iS_{ij}^{uv}        &
      J^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} - iD_{ij}^n &
      S^+ - D^-                                   \\
      S^+ + D^-                                   &
      S^- + D^+                                   &
      J^{iso} + S_{ij}^{nn}                            \\
    \end{pmatrix}
