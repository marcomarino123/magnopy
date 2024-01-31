Spiral state
============

Examples of the spirals can be found :ref:`here<user-guide_methods_single-q_examples>`.

In that case both :math:`\delta_{\boldsymbol{q},\boldsymbol{G}} = 0`
and :math:`\delta_{\frac{\boldsymbol{q}}{2},\boldsymbol{G}} = 0`,
therefore, the expression for the exchange energy is simplified to

.. math::
  &\dfrac{E}{M}
  =
  \dfrac{1}{2}
  \sum_{i, j, \boldsymbol{d_{ij}}}
  S_iS_j
  \Biggl\{
    J_{ij}^{nn}(\boldsymbol{d_{ij}})\cos\theta_i\cos\theta_j
    +\\&+
    \sin\theta_i\sin\theta_j
    \Bigl[
      \dfrac{J_{ij}^{uu}(\boldsymbol{d_{ij}})+J_{ij}^{vv}(\boldsymbol{d_{ij}})}{2}\cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
      +\\&+
      \dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})-J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}\sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
    \Bigr]
  \Biggr\}
  +\\&+
  \mu_B
  h^n
  \sum_i
  g_i  S_i
  \sin\theta_i\cos\theta_i


For the minimization we will need explicit expressions with :math:`\alpha` and :math:`\beta`
angles, which define the direction of the global rotation axis :math:`\boldsymbol{\hat{n}}`
in :math:`(xyz)` reference frame. Therefore we need to express

* :math:`J_{ij}^{nn}(\boldsymbol{d_{ij}})
  =
  J_{ij}^{iso}(\boldsymbol{d_{ij}}) + S_{ij}^{nn}(\boldsymbol{d_{ij}})`
* :math:`J_{ij}^{uu}(\boldsymbol{d_{ij}})+J_{ij}^{vv}(\boldsymbol{d_{ij}})
  =
  J_{ij}^{iso}(\boldsymbol{d_{ij}}) - S_{ij}^{nn}(\boldsymbol{d_{ij}})`
* :math:`\dfrac{J_{ij}^{uv}(\boldsymbol{d_{ij}})-J_{ij}^{vu}(\boldsymbol{d_{ij}})}{2}
  =
  D_{ij}^n(\boldsymbol{d_{ij}})`

Isotropic part of the matrix is indifferent to the rotations. Antisymmetric part of the matrix
can be separated from symmetric one, therefore :math:`D^n` is merely a projection of the
DMI vector onto the direction of the vector :math:`\boldsymbol{\hat{n}}`:

.. math::
  D^n
  =
  \boldsymbol{D}^T
  \boldsymbol{\hat{n}}
  =
  D^x \cos\beta\sin\alpha
  +
  D^y \sin\beta\sin\alpha
  +
  D^z \cos\alpha

Finally, symmetric anisotropy in :math:`(uvn)` basis, being traceless, is defined
solely by the symmetric anisotropic part of the matrix in :math:`(xyz)` basis.

.. math::
  &S^{nn}
  =
  \boldsymbol{\hat{n}}^T
  \begin{pmatrix}
    S^{xx} & S^{xy} & S^{xz} \\
    S^{xy} & S^{yy} & S^{yz} \\
    S^{xz} & S^{yz} & S^{zz} \\
  \end{pmatrix}
  \boldsymbol{\hat{n}}
  =\\&=
  S^{xx}(\cos^2\beta\sin^2\alpha-\cos^2\alpha)
  +
  S^{yy}(\sin^2\beta\sin^2\alpha-\cos^2\alpha)
  +\\&+
  2S^{xy}\sin^2\alpha\sin\beta\cos\beta
  +
  2S^{xz}\sin\alpha\cos\alpha\cos\beta
  +
  S^{yz}\sin\alpha\cos\alpha\sin\beta
