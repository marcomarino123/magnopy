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


=====================
Minimization strategy
=====================
We have argued in the :ref:`previous section <../energy-classic_index>` that
it is more efficient to analyze separately the ferromagnetic (FM),
antiferromagnetic (AF)
and the spiral states (SP). This is specially clear when it comes to minimizing the energy
with respect to the different cone-state parameters: the angles
:math:`\alpha,\,\beta` defining the :math:`(\,u\,v\,n\,)` reference frame, the spiral
vector :math:`\boldsymbol{q}`, and the intra-cell polar and azimut angles
:math:`\theta_i,\,\phi_i` of all the atomic spins dwelling the unit cell.

However, :math:`\boldsymbol{q}` need not be determined for the FM and AF states.
Furthermore, the intracell angles :math:`\theta_i` and :math:`\phi_i` can be suitably chosen
for any FM or AF spin arrangement so that :math:`\alpha` and :math:`\beta` can be set to
zero. Altogether, the number of variational parameters that need to be minimized for those
to cases is reduced to only :math:`\theta_i` and :math:`\phi_i`.

--------
FM state
--------
The energy of the ferromagnetic state is

.. math::
  E^{C,FM}(\theta_i,\phi_i)=&
  \frac{1}{2}\,\sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\,S_j\,\left(
  \cos\theta_i\,\cos\theta_j\,J_{ij}^{zz}
  +\sin\theta_i\,\sin\theta_j\,J_{ij}^{F-AF}
  +\cos\theta_i\,\sin\theta_j\,J_{ij}^{F,1}
  +\sin\theta_i\,\cos\theta_j\,J_{ij}^{F,2}
  \right)\\
  &+\mu_B\,
  \sum_i\,g_i\,  S_i\,\left(\,\cos\theta_i\,h^n\,+\,
  \sin\theta_i\,
  \left(h^u\,\cos\phi_i+h^v\,\sin\phi_i\,\right)
  \right)

with

.. math::
  J_{ij}^{F-AF}=&
   (J_{ij}^{xx}\,\cos\phi_i\,\cos\phi_j+
  J_{ij}^{yy}\,\sin\phi_i\,\sin\phi_j+
  J_{ij}^{xy}\,\cos\phi_i\,\sin\phi_j+
  J_{ij}^{yx}\,\sin\phi_i\,\cos\phi_j)\\
  J_{ij}^{F,1}=&
  (J_{ij}^{zx}\,\cos\phi_j+J_{ij}^{zy}\,\sin\phi_j)\\
  J_{ij}^{F,2}=&(J_{ij}^{xz}\,\cos\phi_i+J_{ij}^{yz}\,\sin\phi_i)

The different FM configurations can be obtained as follows:

* Spins aligned along the :math:`\pm\boldsymbol{\hat{z}}` axis.
  Then :math:`\theta_i=\Delta\theta_i` and :math:`\phi_i=\Delta\phi_i`.
* Spins lying in the XY-plane. Then :math:`\theta_i=\pi/2+\Delta\theta_i` and
  :math:`\phi_i=\phi_0+\Delta\phi_i`.
* Spins lying along any other plane. Then :math:`\theta_i=\theta_0+\Delta\theta_i`,
  :math:`\phi_i=\phi_0+\Delta\phi_i`.

--------
AF state
--------
The AF state energy is

.. math::
  E^{C,AF}(\theta_i,\phi_i)=
  \frac{1}{2}\,\sum_{i, j, \boldsymbol{d}_{ij}}
  S_i\,S_j\,\left(
  \cos\theta_i\,\cos\theta_j\,J_{ij}^{zz}
  +(-1)^{mod(n_{ij},2)}\,\sin\theta_i\,\sin\theta_j\,
  J_{ij}^{F-AF}\right)
  +\mu_B\,\sum_i\,g_i\, S_i\,\cos\theta_i\,h^n

where :math:`\boldsymbol{q}\,\boldsymbol{d}_{ij} = \pi ,n_{ij}` and
:math:`\cos(\boldsymbol{q}\,\boldsymbol{d}_{ij})=(-1)^{mod(n_{ij},2)}`.

The different AF configurations can be obtained just as the FM ones:

* Spins aligned along the :math:`\pm\boldsymbol{\hat{z}}` axis.
  Then :math:`\theta_i=\Delta\theta_i` and :math:`\phi_i=\Delta\phi_i`.
* Spins lying in the XY-plane. Then :math:`\theta_i=\pi/2+\Delta\theta_i` and
  :math:`\phi_i=\phi_0+\Delta\phi_i`.
* Spins lying along any other plane. Then :math:`\theta_i=\theta_0+\Delta\theta_i`,
  :math:`\phi_i=\phi_0+\Delta\phi_i`.

--------
SP state
--------
The energy for the spiral state is

.. math::
   E^{C,SP}=
   \frac{1}{2}\,\sum_{i, j, \boldsymbol{d}_{ij}}
    S_i\,S_j\,\left(
      \,\cos\theta_i\,\cos\theta_j\,J_{ij}^{nn}+
      \sin\theta_i\,\sin\theta_j\,J_{ij}^{SP}\right)+
      \mu_B\,\sum_i\,g_i\,  S_i\,\cos\theta_i\,h^n

with

.. math::
  J_{ij}^{SP}=
       J_{ij}^+\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)+
         D_{ij}^{n}\,\sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)

and :math:`J_{ij}^+=\frac{1}{2}\,(J_{ij}^{uu}+J_{ij}^{vv})`.
The above equation can be rewritten using the original :math:`(\,x\,y\,z\,)` reference frame
by introducing the isotropic component of the exchange tensor

.. math::
  J_{ij}^{I}=&\frac{J_{ij}^{uu}+J_{ij}^{vv}+J_{ij}^{nn}}{3}=
  \frac{J_{ij}^{xx}+J_{ij}^{yy}+J_{ij}^{zz}}{3}=
  \frac{2\,J_{ij}^++J_{ij}^{nn}}{3}\\
  J_{ij}^+  =&\frac{3}{2}\,J_{ij}^{I}-\frac{1}{2}\,J_{ij}^{nn}

and recalling that

.. math::
  J_{ij}^{nn}=& \boldsymbol{\hat{n}}^\dagger\,\boldsymbol{J}_{ij}^{xyz}\,\boldsymbol{\hat{n}}\\
             =&\,J_{ij}^{xx}\,\sin^2\alpha\,\cos^2\beta+J_{ij}^{yy}\,\sin^2\alpha\,\sin^2\beta
             +J_{ij}^{zz}\,\cos^2\alpha\\
             &+S_{ij}^{xy}\,\sin^2\alpha\,sin(\,\beta)+S_{ij}^{xz}\,\sin(2\,\alpha)\,\cos\beta+
             +S_{ij}^{yz}\,\sin(2\,\alpha)\,\cos\beta\\\\
  D_{ij}^n   =&(\boldsymbol{D}_{ij}^{xyz})^\dagger\cdot\boldsymbol{\hat{n}}
             =\boldsymbol{\hat{n}}^\dagger\cdot \boldsymbol{D}_{ij}^{xyz}
             = D_{ij}^x\,\sin\alpha\,\cos\beta+D_{ij}^y\,\sin\alpha\,\sin\beta+D_{ij}^z\,\cos\alpha
as follows

.. math::
  E^{C,SP}=E^{I}+
  \frac{1}{2}\,\boldsymbol{\hat{n}}^\dagger\,\boldsymbol{E_J}\,\boldsymbol{\hat{n}}
  +\frac{1}{2}\,\boldsymbol{\hat{n}}^\dagger\,\cdot\boldsymbol{E_D}
  +\frac{1}{2}\,\boldsymbol{E_D}^\dagger\cdot\boldsymbol{\hat{n}}

where the matrix

.. math::
  \boldsymbol{E_J}=\sum_{i, j, \boldsymbol{d}_{ij}}\,
  \boldsymbol{J}_{ij}^{xyz}(\boldsymbol{d}_{ij})\,
  \left(\cos\theta_i\,\cos\theta_j-\frac{1}{2}\,\sin\theta_i\,\sin\theta_j\,
  \cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)\right)

the vector

.. math::
  \boldsymbol{E_D}=\sum_{i, j, \boldsymbol{d}_{ij}}\,
  \boldsymbol{D}_{ij}^{xyz}(\boldsymbol{d}_{ij})\,\sin\theta_i\,\sin\theta_j\,
  \sin(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)

and

.. math::
  E^{I}=\frac{3}{4}\,\sum_{i, j, \boldsymbol{d}_{ij}}\,J_{ij}^I(\boldsymbol{d}_{ij})\,
  \sin\theta_i\,\sin\theta_j\,\cos(\boldsymbol{q}\cdot\boldsymbol{d}_{ij}+\phi_j-\phi_i)


The variational angles :math:`\alpha` and :math:`\beta` can be found be redefining

.. math::
  x=\frac{E^{C,SP}}{\boldsymbol{\hat{n}}^\dagger\cdot \boldsymbol{\hat{n}}}

Minimizing the above expression leads to

.. math::
  \boldsymbol{\hat{n}}=\frac{1}{2}\,(\boldsymbol{E_J}-x)^{-1}\,\boldsymbol{E_D}

Requesting now that :math:`\|\boldsymbol{\hat{n}}\|=1` yields a sixth-order polynomial equation for
:math:`x=E^{C,SP}`,

.. math::
  f(x)=a_6\,x^6+a_5\,x^5+a_4\,x^4+a_3\,x^3+a_2\,x^2+a_1\,x+a_0=0

whose real roots deliver local-energy minima. The minimum of those roots is just the global energy
minimum :math:`E_0^{C,SP}` that we are searching for. Cauchy's bound theorem then states
that those real roots lie in the range :math:`[-(x_c+1),\,x_c+1]`, where

.. math::
  x_c = \max(\,|\frac{a_0}{a_6}|,\,|\frac{a_1}{a_6}|,\,|\frac{a_2}{a_6}|,\,|\frac{a_3}{a_6}|,\,
             |\frac{a_4}{a_6}|,\,|\frac{a_5}{a_6}|\,)
