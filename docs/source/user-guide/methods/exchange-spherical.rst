.. _user-guide_methods_spinham-spherical:

*****************************************************
Exchange tensor in the spherical reference frame
*****************************************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/bra-ket.txt
  * .. include:: page-notations/in-uvn.txt
  * .. include:: page-notations/parentheses.txt

The exchange tensor :math:`\boldsymbol{J_{ij}}`
in the :math:`(\,u\,v\,n\,)` reference frame , that was discussed
:ref:`here <user-guide_methods_xyz-to-uvn>`, can be split into
isotropic, symmetric and anti-symmetric (DM) matrices as follows

.. include:: repeated-formulas/exchange-matrix-decomposition-uvn.txt

This page discusses how this exchange tensor looks in the spherical
:math:`(\,u^+ \,u^-\,n\,)` reference frame introduced
:ref:`here <user-guide_methods_spherical-rf>`, and which is defined by the
transformation matrix

.. math::
  \boldsymbol{T} =\braket{\,u\,v\,n\,|\, \boldsymbol{T} \,|\, u\,v\,n\,}
  =
  \dfrac{1}{\sqrt{2}}\,
  \begin{pmatrix}
    1 &  1 & 0        \\
    i & -i & 0        \\
    0 &  0 & \sqrt{2} \\
  \end{pmatrix}

Little algebra shows that the exchange matrix in the spherical reference frame is

.. math:: \boldsymbol{J^s_{ij}} =&
  \begin{pmatrix}
    J_{ij}^{++} & J_{ij}^{+-} & J_{ij}^{+n} \\
    J_{ij}^{-+} & J_{ij}^{--} & J_{ij}^{-n} \\
    J_{ij}^{n+} & J_{ij}^{n-} & J_{ij}^{nn} \\
  \end{pmatrix}\,=\,
  \boldsymbol{T}^\dagger\,\boldsymbol{J^s_{ij}}\,\boldsymbol{T}\,=
  \\=&
  \begin{pmatrix}
    J^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} + iD_{ij}^n                       &
    \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} - iS_{ij}^{uv}                              &
    \dfrac{S_{ij}^{un} - iS_{ij}^{vn}}{\sqrt{2}} - \dfrac{D_{ij}^v + iD_{ij}^u}{\sqrt{2}} \\
    \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} + iS_{ij}^{uv}                              &
    J^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} - iD_{ij}^n                       &
    \dfrac{S_{ij}^{un} + iS_{ij}^{vn}}{\sqrt{2}} - \dfrac{D_{ij}^v - iD_{ij}^u}{\sqrt{2}} \\
    \dfrac{S_{ij}^{un} + iS_{ij}^{vn}}{\sqrt{2}} + \dfrac{D_{ij}^v - iD_{ij}^u}{\sqrt{2}} &
    \dfrac{S_{ij}^{un} - iS_{ij}^{vn}}{\sqrt{2}} + \dfrac{D_{ij}^v + iD_{ij}^u}{\sqrt{2}} &
    J^{iso} + S_{ij}^{nn}                                                  \\
  \end{pmatrix}


.. dropdown:: Details

  .. math::
    \braket{ \,u^+\,u^-\,n\, |\, J_{ij} \,|\, u^+\,u^-\,n\,}
    =&
    \braket{\,u^+\,u^-\,n \,|\,u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, J_{ij}\,|\, u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, u^+\,u^-\,n\,}
    =\\=&
    \braket{\,u\,v\,n\,|\, T^{\dagger}\,|\, u\,v\,n\,}\,
    \braket{\,u\,v\,n\,|\, J_{ij}\,|\,u\,v\,n\,} \,
    \braket{\,u\,v\,n\,|\, T\,|\, u\,v\,n\,}

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
      J_{ij}^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} + iD_{ij}^n &
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} - iS_{ij}^{uv}        &
      S_{ij}^- - D_{ij}^+                                   \\
      \dfrac{S_{ij}^{uu} - S_{ij}^{vv}}{2} + iS_{ij}^{uv}        &
      J_{ij}^{iso} + \dfrac{S_{ij}^{uu} + S_{ij}^{vv}}{2} - iD_{ij}^n &
      S_{ij}^+ - D_{ij}^-                                   \\
      S_{ij}^+ + D_{ij}^-                                   &
      S_{ij}^- + D_{ij}^+                                   &
      J_{ij}^{iso} + S_{ij}^{nn}                            \\
    \end{pmatrix}
