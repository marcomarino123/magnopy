.. math::
  &\begin{pmatrix}
    e^{i\boldsymbol{q}\boldsymbol{r_m}} & 0                      & 0 \\
    0                     & e^{-i\boldsymbol{q}\boldsymbol{r_m}} & 0 \\
    0                     & 0                      & 1 \\
  \end{pmatrix}
  \begin{pmatrix}
    J_{ij}^{++} & J_{ij}^{+-} & J_{ij}^{+n} \\
    J_{ij}^{-+} & J_{ij}^{--} & J_{ij}^{-n} \\
    J_{ij}^{n+} & J_{ij}^{n-} & J_{ij}^{nn} \\
  \end{pmatrix}
  \begin{pmatrix}
    e^{-i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})} &
    0                                &
    0                                \\
    0                                &
    e^{i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})}  &
    0                                \\
    0                                &
    0                                &
    1                                \\
  \end{pmatrix}
  =\\&=
  \begin{pmatrix}
    J_{ij}^{++}e^{i\boldsymbol{q}\boldsymbol{r_m}}  &
    J_{ij}^{+-}e^{i\boldsymbol{q}\boldsymbol{r_m}}  &
    J_{ij}^{+n}e^{i\boldsymbol{q}\boldsymbol{r_m}}  \\
    J_{ij}^{-+}e^{-i\boldsymbol{q}\boldsymbol{r_m}} &
    J_{ij}^{--}e^{-i\boldsymbol{q}\boldsymbol{r_m}} &
    J_{ij}^{-n}e^{-i\boldsymbol{q}\boldsymbol{r_m}} \\
    J_{ij}^{n+}                       &
    J_{ij}^{n-}                       &
    J_{ij}^{nn}                       \\
  \end{pmatrix}
  \begin{pmatrix}
    e^{-i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})} &
    0                                &
    0                                \\
    0                                &
    e^{i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})}  &
    0                                \\
    0                                &
    0                                &
    1                                \\
  \end{pmatrix}
  =\\&=
  \begin{pmatrix}
    J_{ij}^{++}e^{-i\boldsymbol{q}\boldsymbol{d_{ij}}}              &
    J_{ij}^{+-}e^{i\boldsymbol{q}(2\boldsymbol{r_m}+\boldsymbol{d_{ij}})}  &
    J_{ij}^{+n}e^{i\boldsymbol{q}\boldsymbol{r_m}}             \\
    J_{ij}^{-+}e^{-i\boldsymbol{q}(2\boldsymbol{r_m}+\boldsymbol{d_{ij}})} &
    J_{ij}^{--}e^{i\boldsymbol{q}\boldsymbol{d_{ij}}}               &
    J_{ij}^{-n}e^{-i\boldsymbol{q}\boldsymbol{r_m}}            \\
    J_{ij}^{n+}e^{-i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})}  &
    J_{ij}^{n-}e^{i\boldsymbol{q}(\boldsymbol{r_m}+\boldsymbol{d_{ij}})}   &
    J_{ij}^{nn}                                  \\
  \end{pmatrix}
