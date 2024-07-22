.. _user-guide_methods_exchange-tensor:

***************
Exchange tensor
***************

.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/exchange-tensor.inc

======================================================================
Exchange tensor :math:`^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}`
======================================================================

The exchange tensor introduced in the previous section can be decomposed as follows:

.. math::
  ^{sf}\boldsymbol{\tilde{J}_{\boldsymbol{d}ij}}=&
    \braket{\,f_i^+\,f_i^-\,f_i\,|\,\tilde{J}_{\boldsymbol{d}ij}\,|\,f_i^+\,f_i^-\,f_i\,}
    \\\\
     =&\braket{\,f_i^+\,f_i^-\,f_i\,|\,n^+\,n^-\,n\,}\,
       \braket{\,n^+\,n^-\,n\,|\boldsymbol{R_m}^\dagger\,|\,n^+\,n^-\,n\,}\,
        \braket{\,n^+\,n^-\,n\,|\,u\,v\,n\,}\,\times
        \\\,&\times\,
        \braket{\,u\,v\,n\,|\,\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,|\,u\,v\,n\,}\,\times
        \\\,&\times\,
        \braket{\,u\,v\,n\,|\,n^+\,n^-\,n\,}\,
        \braket{\,n^+\,n^-\,n\,|\,\boldsymbol{R_{m+d_{ij}}}\,|\,n^+\,n^-\,n\,}\,
        \braket{\,n^+\,n^-\,n\,|\,f_j^+\,f_j^-\,f_j\,}
        \\\\
        =&\,^{sn}\boldsymbol{R_i}^\dagger\,^{sn}\boldsymbol{R_m}^\dagger\,\boldsymbol{T}^\dagger\,
          ^n\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,
          \boldsymbol{T}\,^{sn}\boldsymbol{R_{m+d_{ij}}}\,^{sn}\boldsymbol{R_j}

This section is devoted to computing :math:`^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}`
in small steps, starting from the pristine exchange matrix

.. math::
  ^n\boldsymbol{J}_{\boldsymbol{d}_{ij}}=
      \begin{pmatrix}
        J_{\boldsymbol{d}ij}^{uu} & J_{\boldsymbol{d}ij}^{uv} & J_{\boldsymbol{d}ij}^{un} \\
        J_{\boldsymbol{d}ij}^{vu} & J_{\boldsymbol{d}ij}^{vv} & J_{\boldsymbol{d}ij}^{vn} \\
        J_{\boldsymbol{d}ij}^{nu} & J_{\boldsymbol{d}ij}^{nv} & J_{\boldsymbol{d}ij}^{nn} \\
      \end{pmatrix}

that was introduced, calculated and discussed :ref:´here <user-guide_methods_uvn-rf>`.
These small steps consist of determining the intermediate exchange tensors

.. math::
  ^{sn}\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,=&
  \boldsymbol{T}^\dagger\,^n\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,\boldsymbol{T}\\\\
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,=&
         ^{sn}\boldsymbol{R_m}^\dagger\,^{sn}\boldsymbol{J}_{\boldsymbol{d}_{ij}}\,^{sn}\boldsymbol{R_{m+d_{ij}}}\\\\
  ^{sf}\boldsymbol{\tilde{J}_{\boldsymbol{d}ij}}\,=&
        \,^{sn}\boldsymbol{R_i}^\dagger\,^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,^{sn}\boldsymbol{R_j}

==============================================================
Exchange tensor :math:`^{sn}\boldsymbol{J_{\boldsymbol{d}ij}}`
==============================================================

Matrix multiplication leads to the following expression

.. math::
  ^{sn}\boldsymbol{J}^s_{\boldsymbol{d}_{ij}}=
     \begin{pmatrix}
     J_{d_{ij}}^{n,++} & J_{d_{ij}}^{n,+-} & J_{d_{ij}}^{n,+0} \\
     J_{d_{ij}}^{n,-+} & J_{d_{ij}}^{n,--} & J_{d_{ij}}^{n,-0} \\
     J_{d_{ij}}^{n,0+} & J_{d_{ij}}^{n,0-} & J_{d_{ij}}^{n,00} \\
     \end{pmatrix}

where

.. math::
  J_{d_{ij}}^{n,++}&=J_{d_{ij}}^{uv,+}\,+\,i\,D_{d_{ij}}^n\,+\,2\,\delta_{ij}\,\delta_{d_{ij},0}\,A_i^{uv,+}\\
  J_{d_{ij}}^{n,+-}&=J_{d_{ij}}^{uv,-}\,-\,i\,S_{d_{ij}}^n\,+\,2\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{uv,-}\,-\,i\,A_i^n)\\
  J_{d_{ij}}^{n,+0}&=\frac{1}{\sqrt{2}}\,(\,J_{d_{ij}}^{un}\,-\,i\,J_{d_{ij}}^{vn})\,+\,\sqrt{2}\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{un}\,-\,i\,A_i^{vn})\\
  J_{d_{ij}}^{n,-+}&=J_{d_{ij}}^{uv,-}\,+\,i\,S_{d_{ij}}^n\,+\,2\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{uv,-}\,+\,i\,A_i^n)\\
  J_{d_{ij}}^{n,--}&=J_{d_{ij}}^{uv,+}\,-\,i\,D_{d_{ij}}^n\,+\,2\,\delta_{ij}\,\delta_{d_{ij},0}\,A_i^{uv,+}\\
  J_{d_{ij}}^{n,-0}&=\frac{1}{\sqrt{2}}\,(\,J_{d_{ij}}^{un}\,+\,i\,J_{d_{ij}}^{vn})\,+\,\sqrt{2}\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{un}\,+\,i\,A_i^{vn})\\
  J_{d_{ij}}^{n,0+}&=\frac{1}{\sqrt{2}}\,(\,J_{d_{ij}}^{nu}\,+\,i\,J_{d_{ij}}^{nv})\,+\,\sqrt{2}\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{un}\,+\,i\,A_i^{vn})\\
  J_{d_{ij}}^{n,0-}&=\frac{1}{\sqrt{2}}\,(\,J_{d_{ij}}^{nu}\,-\,i\,J_{d_{ij}}^{nv})\,+\,\sqrt{2}\,\delta_{ij}\,\delta_{d_{ij},0}\,(A_i^{un}\,-\,i\,A_i^{vn})\\
  J_{d_{ij}}^{n,00}&=J_{d_{ij}}^{nn}\,+\,2\,\delta_{ij}\,\delta_{d_{ij},0}\,A_i^{nn}

with

.. math::
  J_{d_{ij}}^{uv,\pm}&=\frac{J_{d_{ij}}^{uu}\pm J_{d_{ij}}^{vv}}{2}\\
  D_{d_{ij}}^n       &=\frac{J_{d_{ij}}^{uv}- J_{d_{ij}}^{vu}}{2}\\
  S_{d_{ij}}^n       &=\frac{J_{d_{ij}}^{uv}+ J_{d_{ij}}^{vu}}{2}\\
  A_i^{uv,\pm}       &=\frac{A_i^{uu}\pm A_i^{vv}}{2}\\

======================================================================
Exchange tensor :math:`^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}`
======================================================================

This exchange tensor is better written as the sum of zero-, first- and second-harmonics, as
follows:

.. include:: repeated-formulas/exchange-matrix-rotated-split-spherical.inc

and where

.. math::
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^0
  =
  \begin{pmatrix}
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{n,++} & 0 & 0 \\
    0 & e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} (J_{\boldsymbol{d}ij}^{n,++})^*  & 0 \\
    0 & 0 & J_{\boldsymbol{d}ij}^{n,00}
  \end{pmatrix}

.. math::
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^1
  =
  \begin{pmatrix}
    0 & 0 & J_{\boldsymbol{d}ij}^{n,+0} \\
    0 & 0 & 0 \\
    0 & e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} (J_{\boldsymbol{d}ij}^{n,0+})^* & 0
  \end{pmatrix}

.. math::
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-1}
  =
  \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & (J_{\boldsymbol{d}ij}^{n,+0})^* \\
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}}\, J_{\boldsymbol{d}ij}^{n,0+} & 0 & 0
  \end{pmatrix}

.. math::
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^2
  =
  \begin{pmatrix}
    0  &  e^{i\boldsymbol{q}\boldsymbol{d}_{ij}} J_{\boldsymbol{d}ij}^{n,+-} & 0  \\
    0  &  0                                                                & 0  \\
    0  &  0                                                                & 0
  \end{pmatrix}

.. math::
  ^{sn}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^{-2}
  =
  \begin{pmatrix}
    0                                                                 &  0  &  0  \\
    e^{-i\boldsymbol{q}\boldsymbol{d}_{ij}} (J_{\boldsymbol{d}ij}^{n,+-})^* &  0  &  0  \\
    0                                                                 &  0  &  0
  \end{pmatrix}

======================================================================
Exchange tensor :math:`^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}`
======================================================================

The exchange tensor matrix elements are defined as follows

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

and the sub-indices :math:`\alpha,\,\beta` run over :math:`+,\,-,\,0`.

The explicit expressions for these matrix elements are provided in the
following :ref:`section <user-guide_methods_matrix-elements>`.
