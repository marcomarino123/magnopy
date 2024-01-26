****************
What is Magnopy?
****************

Magnopy is a python code that computes and plots the ground-state
energy and spin-wave spectrum of a generic bilinear Heisenberg
Hamiltonian describing the magnetic interactions of a periodic
lattice of localized spins :math:`{\bf S}_{m i}` of magnitude :math:`S_i`

.. math::
  {\cal H} = \frac{1}{2}\,\sum_{m,d,i,j} \,{\bf S}_{m i}^T\, {\bf J}_{i j}\,
  {\bf S}_{m+d j} \,+\, \sum_{m,i}\,{\bf S}_{m i}^T \,{\bf A}_i\,
  {\bf S}_{m i} + \mu_B\, {\bf h}^T\,\sum_{m,i} \,g_i \,{\bf S}_{m i}

where the sum runs over the bonds among all possible spin pairs up to a
distance :math:`d`, and the :math:`m`/:math:`i`-indexes
label the :math:`m` unit cell / the :math:`i` atom inside the unit cell.
The super-index :math:`T` of a vector means that the vector is transposed.
The exchange tensors

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

More specifically, Magnopy searchs among single-:math:`q` conical
ground-state spin configurations, where  the cone axis is defined
by the unit vector :math:`{\bf n}`, the cone angle :math:`\theta`
and the pitch wave-vector :math:`{\bf q}=q\,{\bf n}`, that are taken
as variational parameters.

Magnopy
then computes their classical plus quantum corrrections energies
as a function of the variational parameters
and  selects the cone configuration delivering the lowest energy.
It subsequently determines and plots the
magnon spectrum including all higher harmonic contributions.

Magnopy is based on the Holstein-Primakoff decomposition of spins into
bosonic fields, where it has implemented the so-called Linear Spin Wave
theory, where the Hamiltonian is bilinear is boson fields and is
correct to :math:`1/S`-order in the spin magnitude :math:`S`.

Magnopy will be extended in the near future to include higher-order
terms in the :math:`1/S` expansion, that are enncapsulated in cubic
and bi-quadratic bosonic pieces of the Hamiltonian.

.. note::
  The output of the magnopy is colored, however we respect |NO_COLOR|_.
