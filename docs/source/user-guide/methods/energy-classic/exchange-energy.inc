The exchange energy **per unit cell** (i.e. divided by :math:`M`) can be found by
inserting the previous expression for the exchange constant into the Hamiltonian,
that leads to:

.. math::
  E^{X}
  =
  E^{\text{zero}}
  +
  \delta_{\boldsymbol{q}, \, \boldsymbol{G}}\, E^{\text{first}}
  +
  \delta_{\boldsymbol{2q}, \, \boldsymbol{G}}\, E^{\text{second}}

where the zeroth-, first- and second-order harmonic exchange contributions are

.. math::
  E^{\text{zero}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left(
    \cos\theta_i\, \cos\theta_j\, (J_{dij}^I+S_{dij}^{nn})
    +
    \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{zero}}
  \right)
  \\\\
  E^{\text{first}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\,
  \left(
    \cos\theta_i\, \cos\theta_j\, J_{dij}^{\text{first},1}+
    \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{first},2}
  \right)
  \\\\
  E^{\text{second}}
  =&
  \frac{1}{2}\, \sum_{i, j, \boldsymbol{d_{ij}}}
  S_i\, S_j\, \sin\theta_i\, \sin\theta_j\, J_{dij}^{\text{second}}

and

.. math::
  J_{dij}^{\text{zero}}
  =&
  (J^I_{dij} - \frac{1}{2}S_{dij}^{nn})\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  +
  D_{dij}^{n}\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j - \phi_i)
  \\\\
  J_{dij}^{\text{first},1}
  =&
  (S_{dij}^{un} + D_{dij}^v)\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  +
  (S_{dij}^{vn} - D_{dij}^u)\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j)
  \\\\
  J_{dij}^{\text{first}, 2}
  =&
  (S_{dij}^{un} - D_{dij}^v)\, \cos(\phi_i) + (S_{dij}^{vn} + D_{dij}^u)\, \sin(\phi_i)
  \\\\
  J_{dij}^{\text{second}}
  =&
  \frac{S_{dij}^{uu} - S_{dij}^{vv}}{2}\, \cos(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)
  +
  S_{dij}^{uv}\, \sin(\boldsymbol{q} \cdot \boldsymbol{d}_{ij} + \phi_j + \phi_i)

where we used the decomposition of exchange matrix into isotropic, symmetric anisotropic
and asymmetric parts

.. math::
  \begin{pmatrix}
      J_{dij}^{uu} & J_{dij}^{uv} & J_{dij}^{un} \\
      J_{dij}^{vu} & J_{dij}^{vv} & J_{dij}^{vn} \\
      J_{dij}^{nu} & J_{dij}^{nv} & J_{dij}^{nn} \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    J_{dij}^I + S_{dij}^{uu}             &             S_{dij}^{uv} + D_{dij}^n &             S_{dij}^{un} - D_{dij}^v \\
                S_{dij}^{uv} - D_{dij}^n & J_{dij}^I + S_{dij}^{vv}             &             S_{dij}^{vn} + D_{dij}^u \\
                S_{dij}^{un} + D_{dij}^v &             S_{dij}^{vn} - D_{dij}^u & J_{dij}^I + S_{dij}^{nn}             \\
  \end{pmatrix}

with :math:`J_{dij}^I = \dfrac{1}{3}(J_{dij}^{uu} + J_{dij}^{vv} + J_{dij}^{nn})`
and :math:`S_{dij}^{uu} + S_{dij}^{vv} + S_{dij}^{nn} = 0`.
