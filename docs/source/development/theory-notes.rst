.. _development_theory-notes:

************
Theory notes
************

In this page we write some formulas that did not make it neither to the publication
about magnopy nor to the user guide, but should be listed somewhere for the convenience
of the developers.


Classical energy
================

.. math::
    E^{(0)}
    =&
    \,C_1
    \sum_{\substack{\alpha \\ k}}
    J_1^k(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        S_{\alpha}
    +\\&+
    C_{2,1}
    \sum_{\substack{\alpha, \\ k,l}}
    J_{2,1}^{kl}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        (S_{\alpha})^2
    +\\&+
    C_{2,2}
    \sum_{\substack{\nu, \\ \alpha, \beta, \\ k,l}}
    J_{2,2}^{kl}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\beta}
        S_{\alpha}
        S_{\beta}
    +\\&+
    C_{3, 1}
    \sum_{\substack{\alpha, \\ k,l,i}}
    J^{kli}_{3, 1}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        (S_{\alpha})^3
    +\\&+
    C_{3, 2}
    \sum_{\substack{\alpha,\beta,\nu, \\ k,l,i}}
    J^{kli}_{3, 2}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        (S_{\alpha})^2
        S_{\beta}
    +\\&+
    C_{3, 3}
    \sum_{\substack{\alpha,\beta,\gamma, \\ \nu,\lambda, \\ k,l,i}}
    J^{kli}_{3, 3}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        z^k_{\alpha}
        z^l_{\beta}
        z^i_{\gamma}
        S_{\alpha}
        S_{\beta}
        S_{\gamma}
    +\\&+
    C_{4, 1}
    \sum_{\substack{\alpha, \\ k,l,i,j}}
    J_{4, 1}^{klij}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        z^j_{\alpha}
        (S_{\alpha})^4
    +\\&+
    C_{4, 2, 1}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        z^j_{\beta}
        (S_{\alpha})^3
        S_{\beta}
    +\\&+
    C_{4, 2, 2}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        z^j_{\beta}
        (S_{\alpha})^2
        (S_{\beta})^2
    +\\&+
    C_{4, 3}
    \sum_{\substack{\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
    J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        z^j_{\gamma}
        (S_{\alpha})^2
        S_{\beta}
        S_{\gamma}
    +\\&+
    C_{4, 4}
    \sum_{\substack{\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
    J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
        z^k_{\alpha}
        z^l_{\beta}
        z^i_{\gamma}
        z^j_{\varepsilon}
        S_{\alpha}
        S_{\beta}
        S_{\gamma}
        S_{\varepsilon}


Correction to classical energy from LSWT
========================================

.. math::
    E^{(2)}
    =&
    \,\dfrac{1}{2}C_1
    \sum_{\substack{\alpha \\ k}}
    J_1^k(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
    +\\&+
    C_{2,1}
    \sum_{\substack{\alpha, \\ k,l}}
    J_{2,1}^{kl}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        S_{\alpha}
    +\\&+
    C_{2,2}
    \sum_{\substack{\nu, \\ \alpha, \beta, \\ k,l}}
    J_{2,2}^{kl}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\beta}
        S_{\beta}
    +\\&+
    \dfrac{3}{2}C_{3, 1}
    \sum_{\substack{\alpha, \\ k,l,i}}
    J^{kli}_{3, 1}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        (S_{\alpha})^2
    +\\&+
    \dfrac{3}{2}C_{3, 2}
    \sum_{\substack{\alpha,\beta,\nu, \\ k,l,i}}
    J^{kli}_{3, 2}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        S_{\alpha}
        S_{\beta}
    +\\&+
    \dfrac{3}{2}C_{3, 3}
    \sum_{\substack{\alpha,\beta,\gamma, \\ \nu,\lambda, \\ k,l,i}}
    J^{kli}_{3, 3}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        z^k_{\alpha}
        z^l_{\beta}
        z^i_{\gamma}
        S_{\beta}
        S_{\gamma}
    +\\&+
    2C_{4, 1}
    \sum_{\substack{\alpha, \\ k,l,i,j}}
    J_{4, 1}^{klij}(\boldsymbol{r}_{\alpha})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        z^j_{\alpha}
        (S_{\alpha})^3
    +\\&+
    2C_{4, 2, 1}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\alpha}
        z^j_{\beta}
        (S_{\alpha})^2
        S_{\beta}
    +\\&+
    2C_{4, 2, 2}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        z^j_{\beta}
        S_{\alpha}
        (S_{\beta})^2
    +\\&+
    2C_{4, 3}
    \sum_{\substack{\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
    J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        z^k_{\alpha}
        z^l_{\alpha}
        z^i_{\beta}
        z^j_{\gamma}
        S_{\alpha}
        S_{\beta}
        S_{\gamma}
    +\\&+
    2C_{4, 4}
    \sum_{\substack{\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
    J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
        z^k_{\alpha}
        z^l_{\beta}
        z^i_{\gamma}
        z^j_{\varepsilon}
        S_{\beta}
        S_{\gamma}
        S_{\varepsilon}
