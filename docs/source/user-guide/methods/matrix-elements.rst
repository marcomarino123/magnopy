.. _user-guide_methods_matrix-elements:

*******************************
Exchange tensor matrix elements
*******************************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/exchange-tensor.inc

This section is devoted to display all the matrix elements of the exchange tensor
in the spherical local basis, that was introduced at the end of the previous
:ref:`section <user-guide_methods_exchange-tensor>` . The matrix is

.. math::
  ^{sf}\boldsymbol{\tilde{J}}^s_{\boldsymbol{d}_{ij}}=
     \begin{pmatrix}
     \tilde{J}_{d_{ij}}^{f,++} & \tilde{J}_{d_{ij}}^{f,+-} & \tilde{J}_{d_{ij}}^{f,+0} \\
     \tilde{J}_{d_{ij}}^{f,-+} & \tilde{J}_{d_{ij}}^{f,--} & \tilde{J}_{d_{ij}}^{f,-0} \\
     \tilde{J}_{d_{ij}}^{f,0+} & \tilde{J}_{d_{ij}}^{f,0-} & \tilde{J}_{d_{ij}}^{f,00}
     \end{pmatrix}
     =
     \begin{pmatrix}
     \tilde{J}_{d_{ij}}^{f,++}     & \tilde{J}_{d_{ij}}^{f,+-}     & \tilde{J}_{d_{ij}}^{f,+0}.    \\
     (\tilde{J}_{d_{ij}}^{f,+-})^* & (\tilde{J}_{d_{ij}}^{f,++})^* & (\tilde{J}_{d_{ij}}^{f,+0})^* \\
     \tilde{J}_{d_{ij}}^{f,0+}     & (\tilde{J}_{d_{ij}}^{f,0+})^* & \tilde{J}_{d_{ij}}^{f,00}
     \end{pmatrix}

Here, the different matrix elements are

.. math::
  \tilde{J}_{d_{ij}}^{f,\alpha\,\beta}=\braket{\,f^\alpha\,|\,\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,|\,f^\beta\,}
          =(^{sn}\boldsymbol{\hat{f}_i^\alpha})^\dagger\,
          ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,^{sn}\boldsymbol{\hat{f}_i^\beta}
          =\sum_{l=0,\pm 1,\pm 2}\,^{sf}\tilde{J}_{\boldsymbol{d}ij}^{\alpha\beta,l}\,\,\,
              e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

where

.. math::
  ^{sf}\tilde{J}_{\boldsymbol{d}ij}^{\alpha\beta,l}\,=\,
            (^{sn}\boldsymbol{\hat{f}_i^\alpha})^\dagger\,^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
            \,^{sn}\boldsymbol{\hat{f}_i^\beta}

The hermiticity relations listed in the previous expression can be proven in different ways.
For example, if tedious, related matrix elements can be computed explicitly and compared.

We compute explicitly the matrix element :math:`^{sf}\tilde{J}_{dij}^{00}`:

.. math::
  ^{sf}\tilde{J}_{\boldsymbol{d}ij}^{++,0}\,
          =&\,
            (^{sn}\boldsymbol{\hat{f}_i^0})^\dagger\,^{sn}\tilde{J}_{\boldsymbol{d}ij}^0\,
            \,^{sn}\boldsymbol{\hat{f}_i^0}\\=&
            \begin{pmatrix}
            \frac{1}{2}\,(\cos \theta_i + 1)&
            \frac{1}{2}\,(\cos \theta_i - 1) \,e^{-2\,i\,\phi_i}&
            -\frac{1}{\sqrt{2}} \sin\theta_i\,e^{-i\,\phi_i}
            \end{pmatrix}\,\,
            \begin{pmatrix}
            J_{dij}^{n,++}\,e^{i\boldsymbol{q}\cdot\boldsymbol{d}_{ij}} & 0 & 0 \\
            0 & J_{dij}^{n,++}\,e^{i\boldsymbol{q}\cdot\boldsymbol{d}_{ij}} & 0 \\
            0 & 0 & J_{dij}^{n,00}
            \end{pmatrix}\,\,
            \begin{pmatrix}
            \frac{1}{2}\,(\cos \theta_j + 1)&
            \frac{1}{2}\,(\cos \theta_j - 1) \,e^{-2\,i\,\phi_j}&
            -\frac{1}{\sqrt{2}} \sin\theta_j\,e^{-i\,\phi_j}
            \end{pmatrix}\\
            =&\frac{1}{2}\,\sin\theta_i\sin\theta_j\,e^{i\,(\phi_i+\phi_j)}\,J_{dij}^{n,00}+
            \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j +1)\,
            e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i)}\,J_{dij}^{n,++}+
            \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j -1)\,
            e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_j)}\,(J_{dij}^{n,++})^*

All other matrix elements can be computed in a similar way, and we list here the results

.. math::
  ^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{00,1}\, =& \,
            =&\frac{1}{2}\,\sin\theta_i\sin\theta_j\,e^{i\,(\phi_i+\phi_j)}\,J_{dij}^{n,00}+
            \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j +1)\,
            e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i)}\,J_{dij}^{n,++}+
            \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j -1)\,
            e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_j)}\,(J_{dij}^{n,++})^*\\\\
  ^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{00,1}\, =& \,
            -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i +1)\,\sin\theta_j\,
            e^{-i\,\phi_j}\,J_{dij}^{n,+0}
            -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j +1)\,
            e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}-\phi_i)}\,(J_{dij}^{n,0+})^*\\\\
  ^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{00,-1}\, =& \,
            -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i -1)\,\sin\theta_j\,
            e^{-i\,(2\,\phi_i+\phi_j)}\,(J_{dij}^{n,+0})^*
            -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j -1)\,
            e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_i+2\,\phi_j)}\,J_{dij}^{n,0+}\\\\
    ^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{00,2}\, =& \,
            \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j +1)\,
            e^{i\,\boldsymbol{q}\cdot\boldsymbol{d}_{ij}}\,J_{dij}^{n,+-}\\\\
    ^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{00,-2}\, =& \,
            \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j -1)\,
            e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i+2\,\phi_j)}\,(J_{dij}^{n,+-})^*

The matrix elements related to :math:`\tilde{J}_{d_{ij}}^{f,+-}` are

.. math::
