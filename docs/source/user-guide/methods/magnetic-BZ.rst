.. _user-guide_methods_magnetic-BZ:

***********************
Magnetic Brillouin Zone
***********************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/exchange-tensor.inc

This section is devoted to displaying all the matrix elements of the exchange tensor
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
      \tilde{J}_{d_{ij}}^{f,++}     & \tilde{J}_{d_{ij}}^{f,+-}     & \tilde{J}_{d_{ij}}^{f,+0}    \\
      (\tilde{J}_{d_{ij}}^{f,+-})^* & (\tilde{J}_{d_{ij}}^{f,++})^* & (\tilde{J}_{d_{ij}}^{f,+0})^* \\
      \tilde{J}_{d_{ij}}^{f,0+}     & (\tilde{J}_{d_{ij}}^{f,0+})^* & \tilde{J}_{d_{ij}}^{f,00}
      \end{pmatrix}

Here, the different matrix elements are

.. math::
  \tilde{J}_{d_{ij}}^{f,\alpha\,\beta}=
      \braket{\,f^\alpha\,|\,\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,|\,f^\beta\,}
      =(^{sn}\boldsymbol{\hat{f}_i^\alpha})^\dagger\,
      ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,^{sn}\boldsymbol{\hat{f}_i^\beta}
      =\sum_{\nu=0,\pm 1,\pm 2}\,\tilde{J}_{\boldsymbol{d}ij}^{f\nu,\alpha\beta}\,\,\,
      e^{i\,\nu\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

where

.. math::
  \tilde{J}_{\boldsymbol{d}ij}^{f\nu,\alpha\beta}\,=\,
      (^{sn}\boldsymbol{\hat{f}_i^\alpha})^\dagger\,^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^\nu\,
      \,^{sn}\boldsymbol{\hat{f}_i^\beta}

The hermiticity relations listed in the previous expression can be proven in different ways.
For example, if tedious, related matrix elements can be computed explicitly and compared.
We compute explicitly the matrix element :math:`\tilde{J}_{dij}^{f0,++}`:

.. math::
  \tilde{J}_{\boldsymbol{d}ij}^{f0,++}\,
      =&\,
      (^{sn}\boldsymbol{\hat{f}_i^+})^\dagger\,^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^0\,
      \,^{sn}\boldsymbol{\hat{f}_i^+}\\\,=&\,
      \begin{pmatrix}
      \frac{1}{2}\,(\cos \theta_i + 1)&
      \frac{1}{2}\,(\cos \theta_i - 1) \,e^{-2\,i\,\phi_i}&
      -\frac{1}{\sqrt{2}} \sin\theta_i\,e^{-i\,\phi_i}
      \end{pmatrix}\,\,
      \begin{pmatrix}
      J_{dij}^{n,++}\,e^{-i\boldsymbol{q}\cdot\boldsymbol{d}_{ij}} & 0 & 0 \\
      0 & (J_{dij}^{n,++})^*\,e^{i\boldsymbol{q}\cdot\boldsymbol{d}_{ij}} & 0 \\
      0 & 0 & J_{dij}^{n,00}
      \end{pmatrix}\,\,
      \begin{pmatrix}
      \frac{1}{2}\,(\cos \theta_j + 1)\\
      \frac{1}{2}\,(\cos \theta_j - 1) \,e^{2\,i\,\phi_j}\\
      -\frac{1}{\sqrt{2}} \sin\theta_j\,e^{i\,\phi_j}
      \end{pmatrix}\\
      \,=&\,\frac{1}{2}\,\sin\theta_i\sin\theta_j\,e^{i\,(\phi_j-\phi_i)}
      \,J_{dij}^{n,00}+
      \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j +1)\,
      e^{-i\,\boldsymbol{q}\cdot\boldsymbol{d}_{ij}}\,J_{dij}^{n,++}+
      \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j -1)\,
      e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,(\phi_j-\phi_i)}\,(J_{dij}^{n,++})^*

All other matrix elements can be computed in a similar way, and we list here the results

.. math::
  \tilde{J}_{\boldsymbol{d}ij}^{f1,++}\, =& \,
      -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i +1)\,\sin\theta_j\,
      e^{i\,\phi_j}\,J_{dij}^{n,+0}
      -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j -1)\,
      e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\phi_j-\phi_i)}\,(J_{dij}^{n,0+})^*\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f-1,++}\, =& \,
      -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i -1)\,\sin\theta_j\,
      e^{i\,(\phi_j-2\,\phi_i)}\,(J_{dij}^{n,+0})^*
      -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j +1)\,
      e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_i)}\,J_{dij}^{n,0+}\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f2,++}\, =& \,
      \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j -1)\,
      e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\phi_j)}\,J_{dij}^{n,+-}\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f-2,++}\, =& \,
      \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j +1)\,
      e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i)}\,(J_{dij}^{n,+-})^*

The matrix elements related to :math:`\tilde{J}_{d_{ij}}^{f,+-}` are

.. math::
  \tilde{J}_{\boldsymbol{d}ij}^{f0,+-}\,=&\,
      \frac{1}{2}\,\sin\theta_i\sin\theta_j\,e^{i\,(\phi_i+\phi_j)}\,J_{dij}^{n,00}+
      \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j +1)\,
      e^{i\,(-\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i)}\,J_{dij}^{n,++}+
      \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j -1)\,
      e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_j)}\,(J_{dij}^{n,++})^*\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f1,+-}\, =& \,
      -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i +1)\,\sin\theta_j\,
      e^{-i\,\phi_j}\,J_{dij}^{n,+0}
      -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j +1)\,
      e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}-\phi_i)}\,(J_{dij}^{n,0+})^*\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f-1,+-}\, =& \,
      -\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i -1)\,\sin\theta_j\,
      e^{-i\,(2\,\phi_i+\phi_j)}\,(J_{dij}^{n,+0})^*
      -\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j -1)\,
      e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_i+2\,\phi_j)}\,J_{dij}^{n,0+}\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f2,+-}\, =& \,
      \frac{1}{4}\,(\cos\theta_i +1)\,(\cos\theta_j +1)\,
      e^{i\,\boldsymbol{q}\cdot\boldsymbol{d}_{ij}}\,J_{dij}^{n,+-}\\\\
  \tilde{J}_{\boldsymbol{d}ij}^{f-2,+-}\, =& \,
      \frac{1}{4}\,(\cos\theta_i -1)\,(\cos\theta_j -1)\,
      e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_i+2\,\phi_j)}\,(J_{dij}^{n,+-})^*

Those related to :math:`\tilde{J}_{d_{ij}}^{f,00}` are

.. math::
    \tilde{J}_{\boldsymbol{d}ij}^{f0,00}\,=&\,
    \cos\theta_i\,\cos\theta_j\,\,J_{dij}^{n,00}+
    \sin\theta_i\,\sin\theta_j\,
    \left(\,Real(\,J_{dij}^{n,++})\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)+
    Imag(\,J_{dij}^{n,++})\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)\right)
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f1,00}\,=&\,
    \frac{1}{\sqrt{2}}\,\cos\theta_i\,\sin\theta_j\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)}\,(J_{dij}^{n,0+})^*+
    \frac{1}{\sqrt{2}}\,\sin\theta_i\,\cos\theta_j\,
    e^{i\,\phi_i}\,J_{dij}^{n,+0}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-1,00}\,=&\,(\tilde{J}_{\boldsymbol{d}ij}^{f-1,00})^*
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f2,00}\,=&\,
    \frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_i+\phi_j)}\,J_{dij}^{n,+-}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-2,00}\,=&\,(\tilde{J}_{\boldsymbol{d}ij}^{f2,00})^*

Those related to :math:`\tilde{J}_{d_{ij}}^{f,+0}` are

.. math::
    \tilde{J}_{\boldsymbol{d}ij}^{f0,+0}\,=&\,
    -\frac{1}{\sqrt{2}}\,\sin\theta_i\,\cos\theta_j\,e^{-i\,\phi_i}\,J_{dij}^{n,00}
    +\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i-1)\,\sin\theta_j\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-2\,\phi_i)}\,(J_{dij}^{n,++})^*
    +\frac{1}{2\,\sqrt{2}}\,(\cos\theta_i+1)\,\sin\theta_j\,
    e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)}\,J_{dij}^{n,++}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f1,+0}\,=&\,
    \frac{1}{2}\,(\cos\theta_i-1)\,\cos\theta_j\,e^{-2\,i\,\phi_i}\,(J_{dij}^{n,+0})^*
    -\frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
    e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j+\phi_i)}\,J_{dij}^{n,0+}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-1,+0}\,=&\,
    \frac{1}{2}\,(\cos\theta_i+1)\,\cos\theta_j\,J_{dij}^{n,+0}
    -\frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)}\,(J_{dij}^{n,0+})^*
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f2,+0}\,=&\,
    \frac{1}{2\,\sqrt{2}}\,(\cos\theta_i-1)\,\sin\theta_j\,
    e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j+2\,\phi_i)}\,(J_{dij}^{n,+-})^*
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-2,+0}\,=&\,
    \frac{1}{2\,\sqrt{2}}\,(\cos\theta_i+1)\,\sin\theta_j\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)}\,J_{dij}^{n,+-}

Finally, those related to :math:`\tilde{J}_{d_{ij}}^{f,0+}` are

.. math::
    \tilde{J}_{\boldsymbol{d}ij}^{f0,0+}\,=&\,
    -\frac{1}{\sqrt{2}}\,\cos\theta_i\,\sin\theta_j\,e^{i\,\phi_j}\,J_{dij}^{n,00}
    +\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j-1)\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_j-\phi_i)}\,(J_{dij}^{n,++})^*
    +\frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j+1)\,
    e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}-\phi_i)}\,J_{dij}^{n,++}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f1,0+}\,=&\,
    \frac{1}{2}\,\cos\theta_i\,(\cos\theta_j+1)\,
    e^{-i\,\boldsymbol{q}\cdot\boldsymbol{d}_{ij}}\,J_{dij}^{n,0+}
    -\frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
    e^{i\,(\phi_j-\phi_i)}\,(J_{dij}^{n,+0})^*
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-1,0+}\,=&\,
   \frac{1}{2}\,\cos\theta_i\,(\cos\theta_j-1)\,
   e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)}\,(J_{dij}^{n,0+})^*
    -\frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
    e^{i\,(\phi_j+\phi_i)}\,J_{dij}^{n,+0}
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f2,0+}\,=&\,
    \frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j+1)\,
    e^{-i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_i)}\,(J_{dij}^{n,+-})^*
    \\
    \tilde{J}_{\boldsymbol{d}ij}^{f-2,0+}\,=&\,
    \frac{1}{2\,\sqrt{2}}\,\sin\theta_i\,(\cos\theta_j+1)\,
    e^{i\,(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+2\,\phi_j+\phi_i)}\,J_{dij}^{n,+-}
