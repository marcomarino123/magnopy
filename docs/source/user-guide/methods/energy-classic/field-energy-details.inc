.. math::
  &M\mu_B
  \sum_i
  g_i  S_i
  \sum_{m}
  \left(
    \dfrac{h^+}{\sqrt{2}},
    \dfrac{h^-}{\sqrt{2}},
    h^n
  \right)
  \begin{pmatrix}
    \delta_{\boldsymbol{q},\boldsymbol{G}} & 0                           & 0 \\
    0                           & \delta_{\boldsymbol{q},\boldsymbol{G}} & 0 \\
    0                           & 0                          & 1             \\
  \end{pmatrix}
  \begin{pmatrix}
    \dfrac{\sin\theta_i e^{-i\phi_i}}{\sqrt{2}} \\
    \dfrac{\sin\theta_i e^{i\phi_i}}{\sqrt{2}}  \\
    \cos\theta_i                                \\
  \end{pmatrix}
  =\\&=
  M
  \mu_B
  \sum_i
  g_i  S_i
  \left[
  \dfrac{\sin\theta_i}{2}
  \delta_{\boldsymbol{q},\boldsymbol{G}}
  \left(
    h^+e^{-i\phi_i}
    +
    h^-e^{i\phi_i}
  \right)
  +
  h^n\cos\theta_i
  \right]
  =\\&=
  M
  \mu_B
  \sum_i
  g_i  S_i
  \left[
  \dfrac{\sin\theta_i}{2}
  \delta_{\boldsymbol{q},\boldsymbol{G}}
  \left(
    (h^u + ih^v)e^{-i\phi_i}
    +
    (h^u - ih^v)e^{i\phi_i}
  \right)
  +
  h^n\cos\theta_i
  \right]
  =\\&=
  M
  \mu_B
  \sum_i
  g_i  S_i
  \left[
  \sin\theta_i
  \delta_{\boldsymbol{q},\boldsymbol{G}}
  \left(
    h^u
    \dfrac{
    e^{i\phi_i}
    +
    e^{-i\phi_i}
    }{2}
    +
    ih^v
    \dfrac{
    e^{-i\phi_i}
    - e^{i\phi_i}
    }{2}
  \right)
  +
  h^n\cos\theta_i
  \right]
