.. math::
    \begin{pmatrix}
        J_{ij}^{uu} & J_{ij}^{uv} & J_{ij}^{un} \\
        J_{ij}^{vu} & J_{ij}^{vv} & J_{ij}^{vn} \\
        J_{ij}^{nu} & J_{ij}^{nv} & J_{ij}^{nn} \\
    \end{pmatrix}
    =
    \begin{pmatrix}
      J^{iso} & 0 & 0 \\
      0 & J^{iso} & 0 \\
      0 & 0 & J^{iso} \\
    \end{pmatrix}
    +
    \begin{pmatrix}
      S_{ij}^{uu} & S_{ij}^{uv} & S_{ij}^{un} \\
      S_{ij}^{uv} & S_{ij}^{vv} & S_{ij}^{vn} \\
      S_{ij}^{un} & S_{ij}^{vn} & S_{ij}^{nn} \\
    \end{pmatrix}
    +
    \begin{pmatrix}
      0 & D_{ij}^n & -D_{ij}^v \\
      -D_{ij}^n & 0 & D_{ij}^u \\
      D_{ij}^v & -D_{ij}^u & 0 \\
    \end{pmatrix}

where
:math:`J^{iso} = \dfrac{1}{3}(J_{ij}^{uu} + J_{ij}^{vv} + J_{ij}^{nn})`
and
:math:`S_{ij}^{uu} + S_{ij}^{vv} + S_{ij}^{nn} = 0`.
