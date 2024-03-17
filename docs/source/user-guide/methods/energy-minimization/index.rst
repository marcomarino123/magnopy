.. _user-guide_methods_energy-minimization:

*******************
Energy minimization
*******************

.. dropdown:: Notation used on this page

  * .. include:: ../page-notations/vector.inc
  * .. include:: ../page-notations/matrix.inc
  * .. include:: ../page-notations/bra-ket.inc
  * .. include:: ../page-notations/parentheses.inc
  * .. include:: ../page-notations/kronecker-delta.inc
  * .. include:: ../page-notations/uvn-or-spherical.inc

Let us recall the expression for the classical energy:

.. math::
  \epsilon_{classical}=&\epsilon_0\,
  +\mu_B\,
  \sum_i\,g_i\,  S_i\,\,h^n\,\cos\theta_i\\
  &+\,
  \delta_{\boldsymbol{q},\boldsymbol{G}}\,
  \left(\epsilon_1\,+\mu_B\,\sum_i\,g_i\,S_i\,\sin\theta_i\,
  (h^u\,\cos\phi_i+h^v\,\sin\phi_i),\right)\\
  &+\,
  \delta_{\boldsymbol{2\,q},\boldsymbol{G}}\,\epsilon_2

where the zeroth-, first- and second-order harmonic exchange contributions are

.. math::
  \epsilon_0=&
   \frac{1}{2}\,\sum_{i, j, \boldsymbol{d_{ij}}}
    S_i\,S_j\,\left(
      \,\cos\theta_i\,\cos\theta_j\,J_{ij}^{nn}+
      \sin\theta_i\,\sin\theta_j\,J_{ij}^{uv,0}\right)\\\\
  \epsilon_1=&
   \frac{1}{2}\,\sum_{i, j, \boldsymbol{d_{ij}}}
    S_i\,S_j\,\left(
      \cos\theta_i\,\cos\theta_j\,J_{ij}^{uvn,1}+
      \sin\theta_i\,\sin\theta_j\,J_{ij}^{uvn,2}\right)\\\\
  \epsilon_2=&
   \frac{1}{2}\,\sum_{i, j, \boldsymbol{d_{ij}}}
    S_i\,S_j\,
      \sin\theta_i\,\sin\theta_j\,J_{ij}^{uv,2}

and

.. math::
  J_{ij}^{uv,0}=&
       \frac{J_{ij}^{uu}+J_{ij}^{vv}}{2}\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)+
         D_{ij}^{n}\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)\\\\
  J_{ij}^{uv,2}=&
       \frac{J_{ij}^{uu}-J_{ij}^{vv}}{2}\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j+\phi_i)+
      S_{ij}^{uv}\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j+\phi_i)\\\\
  J_{ij}^{uvn,1}=&J_{ij}^{nu}\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)+
                  J_{ij}^{nv}\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j)\\\\
  J_{ij}^{uvn,2}=&J_{ij}^{un}\,\cos(\phi_i)+J_{ij}^{vn}\,\sin(\phi_i)

The above expression for the exchange energy demonstrate that for ferromagnetic spin alignments
where :math:`\boldsymbol{q}=0`, all harmonic contribute to it.
In contrast, for anti-ferromagnetic spin alignments, where
:math:`\boldsymbol{q}=\boldsymbol{G}/2`, only :math:`\epsilon_0` and
:math:`\epsilon_2` contribute to the exchange energy. Furthermore, for an
arbitrary spiral vector :math:`\boldsymbol{q}\=0,\,\boldsymbol{G}/2`,
:math:`\epsilon_{exchange} =\epsilon_0`.


In order to minimize this equation and find ground state we split all possible cases into
three distinct ones:

* :math:`\boldsymbol{q} = \boldsymbol{G}` - ferromagnetic alignment.
* :math:`\boldsymbol{q} = \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - antiferromagnetic cone.
* :math:`\boldsymbol{q} \ne \dfrac{\boldsymbol{G}}{2} \ne \boldsymbol{G}` - spiral state.

For each case the general equation is simplified and minimized. Then the true
ground state is defined by the comparison of the three obtained minimums.

Before we proceed to the detailed discussion about each of the three cases
let us recall the equation for the spin vector in the :math:`uvn`
reference frame:

.. include:: ../repeated-formulas/spin-uvn.inc

.. include:: ferromagnetic-case.inc

.. include:: afm-cone-case.inc

.. include:: spiral-case.inc

Minimization strategy
=====================

* We note, that for ferromagnetic case and antiferromagnetic cone case the choice of
  :math:`(uvn)` is arbitrary, therefore for those two cases we choose :math:`(uvn) = (xyz)`,
  which means that we do not need to minimize against :math:`\alpha` and :math:`\beta` angles.
* For the spiral case the minimization with respect to the angles :math:`\alpha` and :math:`\beta`
  (for any given set of other parameters) can be formulated as:

  .. math::
    \min_{||\boldsymbol{n}|| = 1}
    \left(
      \boldsymbol{n}^T
      \boldsymbol{C}
      \boldsymbol{n}
      +
      \boldsymbol{b}^T
      \boldsymbol{n}
    \right)

  Where matrix :math:`\boldsymbol{C}` and vector :math:`\boldsymbol{b}` are defined as

  .. math::
    \boldsymbol{C}
    =
    \dfrac{1}{2}
    \sum_{i, j, \boldsymbol{d_{ij}}}
    \boldsymbol{J_{ij}^S}(\boldsymbol{d_{ij}})
    S_iS_j
    \Biggl[
      \cos\theta_i\cos\theta_j
      -
      \sin\theta_i\sin\theta_j
      \cos(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
    \Biggr]

  .. math::
    \boldsymbol{b}
    =
    \dfrac{1}{2}
    \sum_{i, j, \boldsymbol{d_{ij}}}
    \boldsymbol{D_{ij}}(\boldsymbol{d_{ij}})
    S_iS_j
    \sin\theta_i\sin\theta_j
    \sin(\boldsymbol{q}\boldsymbol{d_{ij}}+\phi_j-\phi_i)
