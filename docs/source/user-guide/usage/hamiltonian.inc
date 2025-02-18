.. math::

    \mathcal{H} &= \mathcal{H}_{Z} + \mathcal{H}_{DD} + \mathcal{H}_{on-site} + \mathcal{H}_{exchange}
    \\
    \mathcal{H}_{Z}
    &=
    \mu_B
    \boldsymbol{h}
    \sum_{\mu, \alpha}
    g_{\alpha}
    \boldsymbol{S}_{\mu,\alpha}
    \\
    \mathcal{H}_{DD}
    &=
    \dfrac{1}{2}
    \dfrac{\mu_0\mu_B^2}{4\pi}
    \sum_{\mu,\alpha}
    \sum_{\nu, \beta}
    g_{\alpha}g_{\beta}
    \left[
        \dfrac{(\boldsymbol{S}_{\mu,\alpha} \cdot \boldsymbol{S}_{\mu+\nu,\beta})}{\vert \boldsymbol{r}_{\nu,\alpha\beta}\vert^3}
        -
        \dfrac{3(\boldsymbol{S}_{\mu,\alpha} \cdot \boldsymbol{r}_{\nu,\alpha\beta})
        (\boldsymbol{S}_{\mu+\nu,\beta} \cdot \boldsymbol{r}_{\nu,\alpha\beta})}{\vert \boldsymbol{r}_{\nu,\alpha\beta}\vert^5}
    \right]
    \\
    \mathcal{H}_{on-site}
    &=
    C_{2,1}
    \sum_{\mu,\alpha}
    \boldsymbol{S}_{\mu,\alpha}
    \boldsymbol{A}(\boldsymbol{r}_{\alpha})
    \boldsymbol{S}_{\mu,\alpha}
    \\
    \mathcal{H}_{exchange}
    &=
    C_{2,2}
    \sum_{\mu,\alpha}
    \sum_{\nu, \beta}
    \boldsymbol{S}_{\mu,\alpha}
    \boldsymbol{J}(\boldsymbol{r}_{\nu,\alpha\beta})
    \boldsymbol{S}_{\mu+\nu,\beta}
