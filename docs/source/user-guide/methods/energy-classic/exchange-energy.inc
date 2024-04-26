The exchange energy **per unit cell** (i.e. divided by :math:`M`) can be found by
inserting the previous expression for the exchange constant into the Hamiltonian,
that leads to:

.. math::
  E^{X}
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
    \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{n+}
    e^{-i(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)}\right)
    +
    \sin\theta_i\, \cos\theta_j\,
    \operatorname{Re}\left(J_{\boldsymbol{d}ij}^{+n} e^{i\phi_i}\right)
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
