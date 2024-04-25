.. math::
  \boldsymbol{J_{\boldsymbol{d}ij}}^s
  &=
  \begin{pmatrix}
    J_{\boldsymbol{d}ij}^{++} & J_{\boldsymbol{d}ij}^{+-} & J_{\boldsymbol{d}ij}^{+n} \\
    J_{\boldsymbol{d}ij}^{-+} & J_{\boldsymbol{d}ij}^{--} & J_{\boldsymbol{d}ij}^{-n} \\
    J_{\boldsymbol{d}ij}^{n+} & J_{\boldsymbol{d}ij}^{n-} & J_{\boldsymbol{d}ij}^{nn} \\
  \end{pmatrix}

where

.. math::
  \begin{aligned}
    J_{\boldsymbol{d}ij}^{++} &= J^{I}_{\boldsymbol{d}ij} + \dfrac{S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv}}{2} + iD_{\boldsymbol{d}ij}^n, & J_{\boldsymbol{d}ij}^{+-} &= \dfrac{S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv}}{2} - iS_{\boldsymbol{d}ij}^{uv}, \\
    J_{\boldsymbol{d}ij}^{--} &= J^{I}_{\boldsymbol{d}ij} + \dfrac{S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv}}{2} - iD_{\boldsymbol{d}ij}^n, & J_{\boldsymbol{d}ij}^{-+} &= \dfrac{S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv}}{2} + iS_{\boldsymbol{d}ij}^{uv},
  \end{aligned}

.. math::
  \begin{aligned}
    J_{\boldsymbol{d}ij}^{+n} &= \dfrac{S_{\boldsymbol{d}ij}^{un} - D_{\boldsymbol{d}ij}^v}{\sqrt{2}} - i\dfrac{S_{\boldsymbol{d}ij}^{vn} + D_{\boldsymbol{d}ij}^u}{\sqrt{2}}, & J_{\boldsymbol{d}ij}^{n+} &= \dfrac{S_{\boldsymbol{d}ij}^{un} + D_{\boldsymbol{d}ij}^v}{\sqrt{2}} + i\dfrac{S_{\boldsymbol{d}ij}^{vn} - D_{\boldsymbol{d}ij}^u}{\sqrt{2}}, \\
    J_{\boldsymbol{d}ij}^{-n} &= \dfrac{S_{\boldsymbol{d}ij}^{un} - D_{\boldsymbol{d}ij}^v}{\sqrt{2}} + i\dfrac{S_{\boldsymbol{d}ij}^{vn} + D_{\boldsymbol{d}ij}^u}{\sqrt{2}}, & J_{\boldsymbol{d}ij}^{n-} &= \dfrac{S_{\boldsymbol{d}ij}^{un} + D_{\boldsymbol{d}ij}^v}{\sqrt{2}} - i\dfrac{S_{\boldsymbol{d}ij}^{vn} - D_{\boldsymbol{d}ij}^u}{\sqrt{2}},
  \end{aligned}

.. math::
  J_{\boldsymbol{d}ij}^{nn}
  =
  J^{I}_{\boldsymbol{d}ij} + S_{\boldsymbol{d}ij}^{nn}.
