****************
What is Magnopy?
****************

Magnopy is a python code that computes and plots the ground-state
energy and spin-wave spectrum of a generic bilinear Heisenberg
Hamiltonian describing the magnetic interactions of a periodic
lattice of localized spins :math:`{\bf S}_{m i}` of magnitude :math:`S_i`

.. math::
  {\cal H}=
  \frac{1}{2}
  \sum_{\substack{m,i,j,\boldsymbol{d}_{ij}\\\boldsymbol{d}_{ii} \ne \boldsymbol{0}}}
  \boldsymbol{S}_{mi}^T
  \boldsymbol{J}_{\boldsymbol{d}_{ij}}
  \boldsymbol{S}_{m+d_{ij}j}
  +
  \sum_{m,i}
  \boldsymbol{S}_{mi}^T
  \boldsymbol{A}_i
  \boldsymbol{S}_{mi}
  +
  \mu_B \boldsymbol{h}^T
  \sum_{m,i}
  g_i \boldsymbol{S}_{mi}

where the sum runs over the bonds among all possible spin pairs up to a
distance :math:`d`, and the index :math:`m` runs over the unit cells of the lattice,
while index :math:`i` runs over the magnetic sites inside the unit cell.
The super-index :math:`T` of a vector means that the vector is transposed.
The exchange tensors written in arbitrary coordinate system :math:`(x,y,z)`

.. math::
  {\bf J}=\left(\begin{matrix} J^{xx} & J^{xy} & J^{xz}\\
                               J^{yx} & J^{yy} & J^{yz}\\
                               J^{zx} & J^{zy} & J^{zz}\\
                               \end{matrix}\right)

account for all the possible bilinear isotropic and anisotropic
exchange interactions. The intra-atomic anisotropy tensors

.. math::
  {\bf A}=\left(\begin{matrix} A^{xx} & A^{xy} & A^{xz}\\
                               A^{yx} & A^{yy} & A^{yz}\\
                               A^{zx} & A^{zy} & A^{zz}\\
                               \end{matrix}\right)

account for any possible form of bilinear intra-atomic anisotropy.
Each spin responds to the presence of a magnetic field :math:`{\bf h}`
via its scalar gyromagnetic factor :math:`g_i`.

Magnopy supports single-:math:`q` conical
ground-state spin configurations, where  the cone axis is defined
by the unit vector :math:`{\bf n}` and the pitch wave-vector :math:`{\bf q}`, that are
taken as variational parameters. As well as traditional ferromagnetic and
antiferromagnetic ground states.

Magnopy is based on the Holstein-Primakoff decomposition of spins into
bosonic fields, where it has implemented the so-called Linear Spin Wave
theory, where the Hamiltonian is bilinear is boson fields and is
correct to :math:`1/S`-order in the spin magnitude :math:`S`.

Magnopy will be extended in the near future to include higher-order
terms in the :math:`1/S` expansion, that are encapsulated in cubic
and bi-quadratic bosonic pieces of the Hamiltonian.
As well as to include the generalized four-spins terms in the spin Hamiltonian

.. note::
  The output of the magnopy is colored, however we respect |NO_COLOR|_.
