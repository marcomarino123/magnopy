The comment below is based on the book [1]_.

Due to the periodicity of the crystal lattice, the sum over all lattice vectors
:math:`\boldsymbol{r}_m` will not change if we shift all the vectors
:math:`\boldsymbol{r}_m` by any lattice vector
:math:`\boldsymbol{r}_0 = \sum_{i}\boldsymbol{a}_in_i`

.. math::
  \sum_m e^{\pm i\boldsymbol{q}\boldsymbol{r}_m}
  =
  \sum_m e^{\pm i\boldsymbol{q}(\boldsymbol{r}_m + \boldsymbol{r}_0)}
  =
  e^{\pm i\boldsymbol{q}\boldsymbol{r}_0} \sum_m e^{\pm i\boldsymbol{q}\boldsymbol{r}_m}

This equation leads to the conclusions that either the sum is zero, or
:math:`\pm\boldsymbol{q}\,\boldsymbol{r}_0 = 2\pi n` for any :math:`\boldsymbol{r}_0`.
Since the sum should not be zero and :math:`\boldsymbol{r_0}` is an arbitrary lattice
vector, then :math:`\pm\boldsymbol{q}\,\boldsymbol{r}_m = 2\pi n` for any :math:`r_m`
and the value of the sum is

.. math::
  \sum_me^{\pm i\boldsymbol{q}\boldsymbol{r}_m} = M

where :math:`M` is the number of lattice vectors.

Since :math:`\pm\boldsymbol{q}\,\boldsymbol{r}_m = 2\pi n` for **any**
:math:`\boldsymbol{R}_m`, then allowed values of the :math:`\boldsymbol{q}` vector are

.. math::
  \sum_{i=1}^{3}q_{a_i}a_in_i = 2\pi n,  \forall n_1, n_2, n_3 \in \mathbb{Z}

where we projected the :math:`\boldsymbol{q}` vector on the three lattice vectors
:math:`\boldsymbol{a_1}`, :math:`\boldsymbol{a_2}`, :math:`\boldsymbol{a_3}`;
:math:`n \in \mathbb{Z}`. One can rewrite the condition above in a form:

.. math::
  q_{a_i} = \dfrac{2\pi}{a_i}n_i,  i = 1, 2, 3

where :math:`n_i \in \mathbb{Z}`. It is evident that the :math:`\boldsymbol{q}` shall
be a reciprocal lattice vector, which we denote as
:math:`\boldsymbol{G} = \sum_{i}\boldsymbol{b}_in_i`. Finally, one can write the sum in
a form

.. math::
  \sum_{r_m}e^{\pm i\boldsymbol{q}\boldsymbol{r}_m}
  =
  M\delta_{\boldsymbol{q},\boldsymbol{G}}

In the case of the sum with :math:`2\boldsymbol{q}\boldsymbol{r}_m` under the exponent
the argument is the same, but the final condition differs by the factor :math:`1/2`:

.. math::
  q_{a_i} = \dfrac{\pi}{a_i}n_i,  i = 1, 2, 3

In the second case spiral vector is expressed through the reciprocal lattice vectors as:

.. math::
  \boldsymbol{q} = \dfrac{\boldsymbol{G}}{2} = \sum_{i}\dfrac{\boldsymbol{b}_i}{2}n_i

And the sum is written as

.. math::
  \sum_{r_m}e^{\pm 2i\boldsymbol{q}\boldsymbol{r}_m}
  =
  M\delta_{\boldsymbol{q},\frac{\boldsymbol{G}}{2}}
  =
  M\delta_{2\boldsymbol{q},\boldsymbol{G}}


.. [1] Ashcroft, Neil W., and N. David Mermin.
       Solid state physics. Cengage Learning, 2022.
