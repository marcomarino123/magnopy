.. _development_theory-notes:

************
Theory notes
************

In this page we write some formulas that did not make it neither to the publication
about magnopy nor to the user guide, but should be listed somewhere for the convenience
of the developers.

Coefficients for expanded form
==============================

.. math::

    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{n_1, m_1, \dots, n_4, m_4}
    =
    &C_1
    \mathcal{J}_{\alpha}^{n_1m_1}
    \delta_{n_2,0}
    \delta_{m_2,0}
    \delta_{n_3,0}
    \delta_{m_3,0}
    \delta_{n_4,0}
    \delta_{m_4,0}
    \delta_{\nu,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\beta}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_2
    \mathcal{J}_{\nu,\alpha\beta}^{n_1m_1n_2m_2}
    \delta_{n_3,0}
    \delta_{m_3,0}
    \delta_{n_4,0}
    \delta_{m_4,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_4
    \mathcal{J}_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{n_1, m_1, \dots, n_4, m_4}

.. math::

    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{n_1, m_1, \dots, n_4, m_4}
    =&
    \,C_1
    \sum_{\substack{\alpha \\ k}}
    J_1^k(\boldsymbol{r}_{\alpha})
    v^{k, n_1m_1}_{\alpha}
    \delta_{n_2,0}
    \delta_{m_2,0}
    \delta_{n_3,0}
    \delta_{m_3,0}
    \delta_{n_4,0}
    \delta_{m_4,0}
    \delta_{\nu,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\beta}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{2,1}
    \sum_{\substack{\alpha, \\ k,l}}
    J_{2,1}^{kl}(\boldsymbol{r}_{\alpha})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\alpha}
    \delta_{n_3,0}
    \delta_{m_3,0}
    \delta_{n_4,0}
    \delta_{m_4,0}
    \delta_{\nu,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\beta}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{2,2}
    \sum_{\substack{\nu, \\ \alpha, \beta, \\ k,l}}
    J_{2,2}^{kl}(\boldsymbol{r}_{\nu,\alpha\beta})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\beta}
    \delta_{n_3,0}
    \delta_{m_3,0}
    \delta_{n_4,0}
    \delta_{m_4,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{4, 1}
    \sum_{\substack{\alpha, \\ k,l,i,j}}
    J_{4, 1}^{klij}(\boldsymbol{r}_{\alpha})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\alpha}
    v^{i, n_3m_3}_{\alpha}
    v^{j, n_4m_4}_{\alpha}
    \delta_{\nu,0}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\beta}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{4, 2, 1}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\alpha}
    v^{i, n_3m_3}_{\alpha}
    v^{j, n_4m_4}_{\beta}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{4, 2, 2}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\alpha}
    v^{i, n_3m_3}_{\beta}
    v^{j, n_4m_4}_{\beta}
    \delta_{\lambda,0}
    \delta_{\rho,0}
    \delta_{\alpha,\gamma}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{4, 3}
    \sum_{\substack{\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
    J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\alpha}
    v^{i, n_3m_3}_{\beta}
    v^{j, n_4m_4}_{\gamma}
    \delta_{\rho,0}
    \delta_{\alpha,\varepsilon}
    +\\&+
    C_{4, 4}
    \sum_{\substack{\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
    J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
    v^{k, n_1m_1}_{\alpha}
    v^{l, n_2m_2}_{\beta}
    v^{i, n_3m_3}_{\gamma}
    v^{j, n_4m_4}_{\varepsilon}




Classical energy
================

.. math::
    E_0
    =&
    \sum_{\substack{\nu,\lambda,\rho \\ \alpha,\beta,\gamma,\varepsilon}}
    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{0,0,0,0,0,0,0,0}
    =\\=&
    \,C_1
    \sum_{\substack{\alpha \\ k}}
    J_1^k(\boldsymbol{r}_{\alpha})
    v^{k, 00}_{\alpha}
    +
    C_{2,1}
    \sum_{\substack{\alpha, \\ k,l}}
    J_{2,1}^{kl}(\boldsymbol{r}_{\alpha})
    v^{k, 00}_{\alpha}
    v^{l, 00}_{\alpha}
    +
    C_{2,2}
    \sum_{\substack{\nu, \\ \alpha, \beta, \\ k,l}}
    J_{2,2}^{kl}(\boldsymbol{r}_{\nu,\alpha\beta})
    v^{k, 00}_{\alpha}
    v^{l, 00}_{\beta}
    +\\&+
    C_{4, 1}
    \sum_{\substack{\alpha, \\ k,l,i,j}}
    J_{4, 1}^{klij}(\boldsymbol{r}_{\alpha})
        v^{k, 00}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\alpha}
        v^{j, 00}_{\alpha}
    +\\&+
    C_{4, 2, 1}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        v^{k, 00}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\alpha}
        v^{j, 00}_{\beta}
    +\\&+
    C_{4, 2, 2}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        v^{k, 00}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\beta}
        v^{j, 00}_{\beta}
    +\\&+
    C_{4, 3}
    \sum_{\substack{\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
    J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        v^{k, 00}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\beta}
        v^{j, 00}_{\gamma}
    +\\&+
    C_{4, 4}
    \sum_{\substack{\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
    J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
        v^{k, 00}_{\alpha}
        v^{l, 00}_{\beta}
        v^{i, 00}_{\gamma}
        v^{j, 00}_{\varepsilon}


Correction to classical energy from LSWT
========================================

.. math::
    E_0^{(2)}
    =&
    -\dfrac{1}{2}
    \sum_{\substack{\alpha,\nu,\beta \\ \lambda,\gamma,\rho,\varepsilon}}
    \Bigl(
    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{2,1,0,0,0,0,0,0}
    +
    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{0,0,2,1,0,0,0,0}
    +
    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{0,0,0,0,2,1,0,0}
    +
    C_{\nu\lambda\rho,\alpha\beta\gamma\varepsilon}^{0,0,0,0,0,0,2,1}
    \Bigr)
    =\\=&
    \,-\dfrac{C_1}{2}
    \sum_{\substack{\alpha \\ k}}
    J_1^k(\boldsymbol{r}_{\alpha})
    v^{k, 21}_{\alpha}
    -
    C_{2,1}
    \sum_{\substack{\alpha, \\ k,l}}
    J_{2,1}^{kl}(\boldsymbol{r}_{\alpha})
    v^{k, 21}_{\alpha}
    v^{l, 00}_{\alpha}
    -
    C_{2,2}
    \sum_{\substack{\nu, \\ \alpha, \beta, \\ k,l}}
    J_{2,2}^{kl}(\boldsymbol{r}_{\nu,\alpha\beta})
    v^{k, 21}_{\alpha}
    v^{l, 21}_{\beta}
    -\\&-
    2C_{4, 1}
    \sum_{\substack{\alpha, \\ k,l,i,j}}
    J_{4, 1}^{klij}(\boldsymbol{r}_{\alpha})
        v^{k, 21}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\alpha}
        v^{j, 00}_{\alpha}
    -\\&-
    2C_{4, 2, 1}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 1}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        v^{k, 21}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\alpha}
        v^{j, 00}_{\beta}
    -\\&-
    2C_{4, 2, 2}
    \sum_{\substack{\nu, \\ \alpha,\beta, \\ k,l,i,j}}
    J_{4, 2, 2}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta})
        v^{k, 21}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\beta}
        v^{j, 00}_{\beta}
    -\\&-
    2C_{4, 3}
    \sum_{\substack{\nu,\lambda, \\ \alpha,\beta,\gamma, \\ k,l,i,j}}
    J_{4, 3}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma})
        v^{k, 21}_{\alpha}
        v^{l, 00}_{\alpha}
        v^{i, 00}_{\beta}
        v^{j, 00}_{\gamma}
    -\\&-
    2C_{4, 4}
    \sum_{\substack{\nu,\lambda,\rho, \\ \alpha,\beta,\gamma,\varepsilon, \\ k,l,i,j}}
    J_{4, 4}^{klij}(\boldsymbol{r}_{\nu,\alpha\beta}, \boldsymbol{r}_{\lambda,\alpha\gamma}, \boldsymbol{r}_{\rho,\alpha\varepsilon})
        v^{k, 21}_{\alpha}
        v^{l, 00}_{\beta}
        v^{i, 00}_{\gamma}
        v^{j, 00}_{\varepsilon}

# TODO Check four-spins terms
