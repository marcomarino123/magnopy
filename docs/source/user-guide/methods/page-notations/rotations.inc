Rotation matrices are denoted by a bold capital :math:`\boldsymbol{R}` letter, whose subindex identifies
the  unit vector defining the rotation axis and whose argument indicates the rotation angle. As an example

.. math::
  \boldsymbol{R_n}(\theta)= e^{\theta\,\boldsymbol{n} \,\times}

corresponds to a rotation by an angle :math:`\theta` about an axis defined by the unit
vector :math:`\boldsymbol{\hat{n}}`

Exceptions to the above rule are as follows. A rotation matrix
:math:`\boldsymbol{R}_{\boldsymbol{r}(\phi)}(\theta)`
whose axis depends on an angle :math:`\phi` will be denoted by
:math:`\boldsymbol{R_r}(\theta,\phi)`.
The intracell and cone-pich rotation matrices
:math:`\boldsymbol{R_r}(\theta_i,\phi_i)` and :math:`\boldsymbol{R_n}(\phi_m)` introduced
:ref:`here <user-guide_methods_single-q>` will be
short-handed to :math:`\boldsymbol{R}_i` and :math:`\boldsymbol{R}_m`, respectively.
