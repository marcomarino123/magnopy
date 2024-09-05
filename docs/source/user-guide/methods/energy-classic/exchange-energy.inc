We have shown in the previous :ref:`section <user-guide_methods_spinham>` that the
exchange part of the Hamiltonian can be written as follows

.. math::
    H_{exc}\, =\,
   \dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,
   ^{sf}\boldsymbol{\tilde{S}_{mi}}\,^{sf}\boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}\,
   ^{sf}\boldsymbol{\tilde{S}_{m+d_{ij},j}}
   =\dfrac{1}{2} \sum_{m, \boldsymbol{d}_{ij}, i, j}\,S_i\,S_j\,\tilde{J}_{d_{ij}}^{f,00}

where

.. math::
  \tilde{J}_{d_{ij}}^{f,00}
          =\sum_{l=0,\pm 1,\pm 2}\,^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,l}\,\,\,
              e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

Here, the m-summation affects only the phases
:math:`e^{i\,l\,\boldsymbol{q}\cdot\boldsymbol{r_m}}` yielding Kronecker deltas, so that the exchange
contribution to the energy becomes

.. math::
  E^{0,cl}_{exc}=
  \dfrac{M}{2}
  \sum_{\boldsymbol{d}_{ij}, i, j}\,S_i\,S_j\,
    \left(^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,0}
    +
    \delta_{\boldsymbol{q}, \, \boldsymbol{G}}\,
    \left[^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,1}+^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,-1}\right]
    +
    \delta_{\boldsymbol{2q}, \, \boldsymbol{G}}\,
    \left[^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,2}+^{sf}\tilde{J}_{\boldsymbol{d}ij}^{00,-2}\right]
  \right)


.. dropdown:: Details

  .. math::
    \boldsymbol{\tilde{J}}^s_{\boldsymbol{d}ij}
    =
    \sum_{l=0,\pm 1,\pm 2}\,
    \boldsymbol{\tilde{J}}_{\boldsymbol{d}ij}^l\,
    \cdot
    \sum_m
    e^{i\,l\,\boldsymbol{q} \cdot \boldsymbol{r}_m}

  Therefore, one needs to compute the values of the sums of exponential

  .. math::
    \sum_m
    e^{i\, l\, \boldsymbol{q} \cdot \boldsymbol{r}_m}

  .. include:: details-on-fourier-identities.inc

The exchange energy per unit cell can therefore be split as follows

.. math::
  \frac{E_{exc}^{0,cl}}{M}
  =
  E^{(0)}
  +
  \delta_{\boldsymbol{q}, \, \boldsymbol{G}}\, E^{(1)}
  +
  \delta_{\boldsymbol{2q}, \, \boldsymbol{G}}\, E^{(2)}

where the zeroth-, first- and second-order harmonic exchange contributions are

.. math::
  E^{(0)}
  =\, &
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left[
    \cos\theta_i\, \cos\theta_j\,
    (J_{\boldsymbol{d}ij}^I+S_{\boldsymbol{d}ij}^{nn})
    +
    \sin\theta_i\, \sin\theta_j\,
    \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{++}
    e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)}\right)
  \right]
  \\\\
  E^{(1)}
  =\, &
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left[
    \cos\theta_i\, \sin\theta_j\,
    \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+}
    e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}\right)
    +
    \sin\theta_i\, \cos\theta_j\,
    \sqrt{2}\operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\phi_i}\right)
  \right]
  \\\\
  E^{(2)}
  =\, &
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\, \sin\theta_i\, \sin\theta_j\,
  \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+-}
  e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)}\right)

and

.. math::
  \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{++}
  e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)}\right)
  =\, &
  (J^I_{\boldsymbol{d}ij} - \frac{1}{2}S_{\boldsymbol{d}ij}^{nn})\,
  \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  +
  D_{\boldsymbol{d}ij}^{n}\,
  \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \\\\
  \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+}
  e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}\right)
  =\, &
  (S_{\boldsymbol{d}ij}^{un} + D_{\boldsymbol{d}ij}^v)\,
  \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  +
  (S_{\boldsymbol{d}ij}^{vn} - D_{\boldsymbol{d}ij}^u)\,
  \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  \\\\
  \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\phi_i}\right)
  =\, &
  (S_{\boldsymbol{d}ij}^{un} - D_{\boldsymbol{d}ij}^v)\,
  \cos(\phi_i) + (S_{\boldsymbol{d}ij}^{vn} + D_{\boldsymbol{d}ij}^u)\, \sin(\phi_i)
  \\\\
  \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+-}
  e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)}\right)
  =\, &
  \frac{S_{\boldsymbol{d}ij}^{uu} - S_{\boldsymbol{d}ij}^{vv}}{2}\,
  \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)
  +
  S_{\boldsymbol{d}ij}^{uv}\,
  \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)

where we used the decomposition of exchange matrix into isotropic, symmetric anisotropic
and asymmetric parts

.. dropdown:: Details

  The exchange matrix in a spherical reference frame written with the component of the
  exchange matrix in a :math:`(u, v, n)` reference frame and further decomposed into
  isotropic, symmetric anisotropic and asymmetric parts reads as

  .. include:: ../repeated-formulas/exchange-matrix-decomposed-spherical.inc

  with :math:`J_{\boldsymbol{d}ij}^I = \dfrac{1}{3}(J_{\boldsymbol{d}ij}^{uu} + J_{\boldsymbol{d}ij}^{vv} + J_{\boldsymbol{d}ij}^{nn})`
  and :math:`S_{\boldsymbol{d}ij}^{uu} + S_{\boldsymbol{d}ij}^{vv} + S_{\boldsymbol{d}ij}^{nn} = 0`.

  Before we proceed to the derivation let us recall a few useful symmetries of the exchange
  matrix in a spherical reference frame:

  .. math::
    J_{\boldsymbol{d}ij}^{++} = (J_{\boldsymbol{d}ij}^{--})^*
    \quad\quad
    J_{\boldsymbol{d}ij}^{+-} = (J_{\boldsymbol{d}ij}^{-+})^*
    \quad\quad
    J_{\boldsymbol{d}ij}^{n-} = (J_{\boldsymbol{d}ij}^{n+})^*
    \quad\quad
    J_{\boldsymbol{d}ij}^{-n} = (J_{\boldsymbol{d}ij}^{+n})^*

  .. note::
    In the following :math:`\operatorname{Re}(\cdot)` denotes the real part of a complex
    number and :math:`\operatorname{Im}(\cdot)` the imaginary part.


  .. math::
    E^{(0)}
    &=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \Biggl[
      \cos\theta_i\, \cos\theta_j\, J_{\boldsymbol{d}ij}^{nn}
      +
      \sin\theta_i\, \sin\theta_j\, \dfrac{1}{2}
      \Bigl(J_{\boldsymbol{d}ij}^{++}
      e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)}
      +\\&\phantom{=\,\frac{1}{2}\,\sum_{i,j,\boldsymbol{d_{ij}}}S_iS_j\Biggl[\cos\theta_i\,\cos\theta_j\,J_{\boldsymbol{d}ij}^{nn}+\sin\theta_i\,\sin\theta_j\,\dfrac{1}{2}\Bigl(}+
      J_{\boldsymbol{d}ij}^{--}
      e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)}\Bigr)
    \Biggr]
    =\\&=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \Biggl[
      \cos\theta_i\, \cos\theta_j\, J_{\boldsymbol{d}ij}^{nn}
      +
      \sin\theta_i\, \sin\theta_j\,
      \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{++}
      e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)}\right)
    \Biggr]
    \\\\
    E^{(1)}
    &=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \Biggl[
      \dfrac{\cos\theta_i\, \sin\theta_j}{\sqrt{2}}
      \left(J_{\boldsymbol{d}ij}^{n+} e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}
      +
      J_{\boldsymbol{d}ij}^{n-} e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}\right)
      +\\&\phantom{=\,\frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j\Biggl[}+
      \dfrac{\sin\theta_i\, \cos\theta_j}{\sqrt{2}}
      \Bigl(J_{\boldsymbol{d}ij}^{+n} e^{i\phi_i}
      +
      J_{\boldsymbol{d}ij}^{-n} e^{-i\phi_i}\Bigr)
    \Biggr]
    =\\&=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \Biggl[
      \cos\theta_i\, \sin\theta_j \sqrt{2}
      \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+}
      e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}\right)
      +\\&\phantom{=\,\frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j\Biggl[}+
      \sin\theta_i\, \cos\theta_j \sqrt{2}
      \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\phi_i}\right)
    \Biggr]
    \\\\
    E^{(2)}
    &=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \sin\theta_i\, \sin\theta_j
    \Bigl(
      J_{\boldsymbol{d}ij}^{+-}
      e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)}
      +
      J_{\boldsymbol{d}ij}^{-+}
      e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)}
    \Bigr)
    =\\&=\,
    \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}S_iS_j
    \sin\theta_i\, \sin\theta_j
    \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+-}
    e^{i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)}\right)
