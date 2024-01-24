.. math::
  &\dfrac{
    J_{ij}^{++}\sin\theta_i\sin\theta_j e^{i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
    +
    J_{ij}^{--}\sin\theta_i\sin\theta_j e^{-i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
  }{2}
  =\\&=
  \dfrac{
    (A + iD_{ij}^n)\sin\theta_i\sin\theta_j e^{i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
    +
    (A - iD_{ij}^n)\sin\theta_i\sin\theta_j e^{-i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
  }{2}
  =\\&=
  A\sin\theta_i\sin\theta_j
  \dfrac{
  e^{i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}+e^{-i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
  }{2}
  -
  D_{ij}^n\sin\theta_i\sin\theta_j
  \dfrac{
  e^{i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}-e^{-i(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})}
  }{2i}
  =\\&=
  A\sin\theta_i\sin\theta_j\cos(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  -
  D_{ij}^n\sin\theta_i\sin\theta_j\sin(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  =\\&=
  (J+\dfrac{S_{ij}^{uu}+S_{ij}^{vv}}{2})\sin\theta_i\sin\theta_j\cos(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  -
  D_{ij}^n\sin\theta_i\sin\theta_j\sin(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  =\\&=
  \dfrac{J_{ij}^{uu}+J_{ij}^{vv}}{2}\sin\theta_i\sin\theta_j\cos(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  -
  \dfrac{J_{ij}^{uv}-J_{ij}^{vu}}{2}\sin\theta_i\sin\theta_j\sin(\phi_i-\phi_j-\boldsymbol{q}\boldsymbol{d_{ij}})
  =\\&=
  \dfrac{J_{ij}^{uu}+J_{ij}^{vv}}{2}\sin\theta_i\sin\theta_j\cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
  +
  \dfrac{J_{ij}^{uv}-J_{ij}^{vu}}{2}\sin\theta_i\sin\theta_j\sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)

where :math:`A = J+\dfrac{S_{ij}^{uu}+S_{ij}^{vv}}{2}`
