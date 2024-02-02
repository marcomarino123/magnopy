and fulfills the hermiticity property

  .. math::
    ((\boldsymbol{R_m^s})^{\dagger}
    \boldsymbol{J_{ij}^s}(\boldsymbol{d_{ij}})
    \boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    =
    (\boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    (\boldsymbol{J_{ij}^s})^{\dagger}(\boldsymbol{d_{ij}})
    \boldsymbol{R_m^s}
    =
    (\boldsymbol{R_{m+d_{ij}}^s})^{\dagger}
    \boldsymbol{J_{ji}^s}(\boldsymbol{d_{ji}})
    \boldsymbol{R_m^s}

  Before we proceed with derivation let us demonstrate hermicity of the Hamiltonian.
  The easiest way to do so is to write two entries of the same bond for arbitrary bond
  and show that their sum is unchanged under the application of the hermitian conjugate.

  We write the part of the Hamiltonian for the bond between atoms
  :math:`1` and :math:`2`,
  with first atom being located in the unit cell :math:`0` and the second in
  the unit cell :math:`0+d`. Then two entries of the bond are:

  * :math:`1 \Rightarrow 2` (:math:`{\cal H}_{12}`)

    - :math:`a = 1`
    - :math:`b = 2`
    - :math:`\boldsymbol{d_{ij}} = \boldsymbol{d}`
    - :math:`m = 0`
  * :math:`2 \Rightarrow 1` (:math:`{\cal H}_{21}`)

    - :math:`a = 2`
    - :math:`b = 1`
    - :math:`\boldsymbol{d_{ij}} = -\boldsymbol{d}`
    - :math:`m = 0+d`

  Then

  .. include:: hermicity-two-bond-part.txt

  and

  .. include:: hermicity-two-bond-part-hc.txt

  By comparison of two formulas above we see that
  :math:`{\cal H}_{12}={\cal H}_{21}^{\dagger}`, therefore:

  .. math::
    ({\cal H}_{12} + {\cal H}_{21})^{\dagger}
    =
    {\cal H}_{12}^{\dagger} + {\cal H}_{21}^{\dagger}
    =
    {\cal H}_{21} + {\cal H}_{12}
    =
    {\cal H}_{12} + {\cal H}_{21}
