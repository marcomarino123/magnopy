

***********************************
Minimization of the energy function
***********************************

As per the formula FIXME of the paper FIXME. Minimization of the energy function can be
formulated as a problem of minimizing the function over the :math:`I` vectors of the
spin directions :math:`\boldsymbol{e}_{\alpha}, \alpha = 1, ..., I`

.. math::

	E = F(\boldsymbol{e}_{1}, ..., \boldsymbol{e}_{I})

Direction vectors are unitary vectors and should vary on the sphere. This fact
introduces complications in the minimization procedure as the optimization space is not
a vector space. This problem is elegantly solved via parametrization of those vectors
with the exponents of skew-symmetric matrices. Given an initial guess
:math:`\boldsymbol{e}_{\alpha, 0}`, any other cone axis and set of direction vectors
can be obtained by the following formulae:

.. math::

	\boldsymbol{e}_{\alpha} = e^{\boldsymbol{A}_{\alpha}} \boldsymbol{e}_{\alpha, 0}

where :math:`\boldsymbol{E}_{\alpha}` are skew-symmetric
matrices. The energy function can be rewritten as:

.. math::

	E
	=
	F(
		e^{\boldsymbol{A}_1} \boldsymbol{e}_{1, 0},
		...,
		e^{\boldsymbol{A}_I} \boldsymbol{e}_{I, 0}
	)

Skew-symmetric matrices are parametrized by three numbers as

.. math::

	\boldsymbol{A}_{\alpha}
	=
	\begin{pmatrix}
		0 & -a_{\alpha}^z & a_{\alpha}^y \\
		a_{\alpha}^z & 0 & -a_{\alpha}^x \\
		-a_{\alpha}^y & a_{\alpha}^x & 0
	\end{pmatrix}

Finally the energy can be written as a function of vector :math:`\boldsymbol{x}` from
the vector space :math:`\mathbb{R}^{3I}`:

.. math::

	E = F(\boldsymbol{x})
	\qquad
	\boldsymbol{x}
	=(
		a_{1}^x, a_{1}^y, a_{1}^z,
		...,
		a_{I}^x, a_{I}^y, a_{I}^z
	)

Then energy of the system is minimized with the BFGS algorithm [1]_.


Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm
=================================================

Formula for the inverse Hessian update:

.. math::

	H^{ij}_{k+1}
	=
	\sum_{u,v}(\delta_{i,u} - \rho_ks^i_ky^u_k)
	H^{uv}_k
	(\delta_{v,j} - \rho_ky^v_ks^j_k) + \rho_k s^i_ks^j_k,
	\qquad
	\rho_k = \dfrac{1}{\sum_i y^i_k s^i_k}

Given :ref:`user-guide_theory-behind_energy_minimization_initial-guess`
:math:`\boldsymbol{x}_0` and :ref:`user-guide_theory-behind_energy_minimization_initial-hessian`
:math:`\boldsymbol{H}_0`,


1.  :math:`k \gets 0`
#.  While convergence is not achieved:

    a)  :ref:`Compute the gradient <user-guide_theory-behind_energy_minimization_gradient>`
        of the function :math:`\boldsymbol{\nabla} F(\boldsymbol{x}_k)`;
    #)  Compute the search direction
        :math:`\boldsymbol{p}_k = -\boldsymbol{H}_k \boldsymbol{\nabla} F(\boldsymbol{x}_k)`;
    #)  Compute length of the step :math:`\alpha_k` via
        :ref:`user-guide_theory-behind_energy_minimization_line-search`;
    #)  Set :math:`\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k \boldsymbol{p}_k`
        and compute gradient :math:`\boldsymbol{\nabla} F(\boldsymbol{x}_{k+1})`;
    #)  Set :math:`\boldsymbol{s}_k = \boldsymbol{x}_{k+1} - \boldsymbol{x}_k` and
        :math:`\boldsymbol{y}_k = \boldsymbol{\nabla} F(\boldsymbol{x}_{k+1}) - \boldsymbol{\nabla} F(\boldsymbol{x}_k)`;
    #)  Update the hessian matrix :math:`\boldsymbol{H}_{k+1}` by the BFGS formula;
    #)  :math:`k \gets k + 1`.


.. note::
	In our implementation we update the direction vectors at the end of each iteration
	(i.e. at step 2.7). Therefore, the vector :math:`\boldsymbol{x}_k` if equal to
	:math:`( 0, 0, 0, 0, 0, 0, ..., 0, 0, 0)` at the beginning of each iteration.



.. _user-guide_theory-behind_energy_minimization_initial-guess:

Initial guess
=============

Initial guess is provided by the user  or randomly generated.
User provides three components for each direction vector
:math:`(e_{\alpha}^x, e_{\alpha}^y, e_{\alpha}^z)`. The initial guess of the vector
parameter :math:`\boldsymbol{x}_0` is then constructed as:

.. math::

	\boldsymbol{x}_0
	=(
		0, 0, 0,
		0, 0, 0,
		...,
		0, 0, 0
	)

.. _user-guide_theory-behind_energy_minimization_initial-hessian:

Initial approximation of the inverse hessian matrix
===================================================

We take an identity matrix as an initial approximation of the hessian matrix.


.. _user-guide_theory-behind_energy_minimization_gradient:

Gradient of the function F(x)
=============================

Gradient of the function :math:`F(\boldsymbol{x})` is computed analytically and written
in formulas FIXME of the paper FIXME. As we choose to update the direction vectors and
cone axis at each step of the BFGS algorithm, then the gradient with respect to these
variables can be computed as :math:`a_{\alpha}^i = t_{\alpha}^i`, where
:math:`\boldsymbol{t}_{\alpha}` is a torque vector and :math:`i = x, y, z`.

.. math::

	\boldsymbol{t}_{\alpha}
	=
	\boldsymbol{e}_{\alpha} \times \dfrac{\partial E}{\partial\boldsymbol{e}_{\alpha}}


.. _user-guide_theory-behind_energy_minimization_line-search:

Line search
===========

Line search algorithm find an optimal step length (:math:`\alpha`) for the search
direction :math:`\boldsymbol{p}_k`. It is obtained by minimizing the function

.. math::

	f(\alpha) = F(\boldsymbol{x}_k + \alpha \boldsymbol{p}_k),
	\qquad
	\dfrac{d f(\alpha)}{d \alpha} = \boldsymbol{\nabla} F(\boldsymbol{x}_k + \alpha \boldsymbol{p}_k) \boldsymbol{p}_k

enough to satisfy strong Wolfe conditions:

.. math::

	F(\boldsymbol{x}_k + \alpha\boldsymbol{p}_k)
	&\le
	F(\boldsymbol{x}_k) + c_1 \alpha_k \boldsymbol{\nabla} F(\boldsymbol{x}_k) \boldsymbol{p}_k,
	\\
	\vert\boldsymbol{\nabla} F(\boldsymbol{x}_k + \alpha\boldsymbol{p}_k)\boldsymbol{p}_k\vert
	&\le
	c_2\vert\boldsymbol{\nabla} F(\boldsymbol{x}_k)\boldsymbol{p}_k\vert

Line search algorithm:

Given :math:`\boldsymbol{x}_k` and :math:`\boldsymbol{p}_k`


1.  Set :math:`\alpha_0 = 0`, :math:`\alpha_{\text{max}} = 1.1` and :math:`\alpha_1 = 1`;
#.  :math:`i \gets 1`;
#.  While maximum number of iterations is not achieved:

    a)  Compute :math:`f(\alpha_i) = F(\boldsymbol{x}_k + \alpha_i \boldsymbol{p}_k)`;
    #)  If :math:`f(\alpha_i) > f(0) + c_1 \alpha_i f^{\prime}(0)`
        or :math:`f(\alpha_i) \ge f(\alpha_{i-1})`
        and :math:`i > 1`, then return :math:`zoom(\alpha_{i-1}, \alpha_i)`;
    #)  Compute :math:`f^{\prime}(\alpha_i) = \boldsymbol{\nabla} F(\boldsymbol{x}_k + \alpha_i \boldsymbol{p}_k) \boldsymbol{p}_k`;
    #)  If :math:`\vert f^{\prime}(\alpha_i)\vert \le -c_2 f^{\prime}(0)`,
        then return :math:`\alpha_i`;
    #)  If :math:`f^{\prime}(\alpha_i) \ge 0`,
        then return :math:`zoom(\alpha_i, \alpha_{i-1})`;
    #)  Choose :math:`\alpha_{i+1}` via :ref:`user-guide_theory-behind_energy_minimization_cubic-interpolation`;
    #)  :math:`i \gets i + 1`.


:math:`zoom` algorithm:

Given :math:`\alpha_{lo}`, :math:`\alpha_{hi}`

1.  Repeat

    a)  Interpolate :math:`\alpha_j` via :ref:`user-guide_theory-behind_energy_minimization_cubic-interpolation`;
    #)  Compute :math:`f(\alpha_j) = F(\boldsymbol{x}_k + \alpha_j \boldsymbol{p}_k)`;
    #)  If :math:`f(\alpha_j) > f(0) + c_1 \alpha_j f^{\prime}(0)`
        or :math:`f(\alpha_j) \ge f(\alpha_{lo})`,
        then :math:`\alpha_{hi} \gets \alpha_j`
    #)  Else

        i)  Evaluate
            :math:`f^{\prime}(\alpha_j) = \boldsymbol{\nabla} F(\boldsymbol{x}_k + \alpha_j \boldsymbol{p}_k) \boldsymbol{p}_k`;
        #)  If :math:`\vert f^{\prime}(\alpha_j)\vert \le -c_2 f^{\prime}(0)`,
            then return :math:`\alpha_j`;
        #)  If :math:`f^{\prime}(\alpha_j)(\alpha_{hi} - \alpha_{lo}) \ge 0`,
            then :math:`\alpha_{hi} \gets \alpha_{lo}`;
        #) :math:`\alpha_{lo} \gets \alpha_j`.


.. _user-guide_theory-behind_energy_minimization_cubic-interpolation:

Cubic interpolation method
--------------------------

Given :math:`\alpha_l`, :math:`\alpha_h` and :math:`f(\alpha_l)`, :math:`f(\alpha_h)`
and :math:`f^{\prime}(\alpha_l)`, :math:`f^{\prime}(\alpha_h)` compute new :math:`\alpha_m`
as

.. math::

	\alpha_m &= \alpha_h - (\alpha_h - \alpha_l) \dfrac{f^{\prime}(\alpha_h) + d_2 - d_1}{f^{\prime}(\alpha_h) - f^{\prime}(\alpha_l) + 2d_2}
	\\
	d_1 &= f^{\prime}(\alpha_l) + f^{\prime}(\alpha_h) - 3 \dfrac{f(\alpha_l) - f(\alpha_h)}{\alpha_l - \alpha_h}
	\\
	d_2 &= \text{sign}(\alpha_h - \alpha_l) \sqrt{d_1^2 - f^{\prime}(\alpha_l)f^{\prime}(\alpha_h)}




References
==========

.. [1] Nocedal, J. and Wright, S.J.
       Numerical optimization. New York, NY: Springer New York.
       eds., 1999.
