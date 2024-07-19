.. _user-guide_methods_spin-rotations:

*************************
( p t f ) reference frame
*************************


.. dropdown:: Notation used on this page

  For the full set of notation rules, see :ref:`user-guide_methods_notation`.

  * .. include:: page-notations/matrices.inc
  * .. include:: page-notations/reference-frame.inc
  * .. include:: page-notations/rotations.inc

Magnopy assumes that the ground state of the spin system follows an spiral conical
arrangement, where the cone axis lies along the direction defined by
a unit vector :math:`\ket{n}`. We have accordingly defined the :math:`(u\, v\, n)`
reference frame as discussed in the previous section.

Convenience dictates that spins be quantized along a global quantization
axis, that Magnopy chooses to be precisely :math:`\ket{n}`.
This is done by singling out each ground-state spin vector
:math:`\ket{S_i^0}` and rotating it into the direction provided
by :math:`\ket{n}`, by means of local rotation operators
:math:`\boldsymbol{R}_i`.

We define a unit vector :math:`\ket{f_i}` collinear to
:math:`\ket{S_i^0}=S_i\, \ket{f_i}`. Then the figure below shows
that the unit vector coordinates in the :math:`(\,u\,v\,n\,)` basis are

.. math::
  ^n\boldsymbol{\hat{f}_{i}}=\braket{\,u\,v\,n\,|\,f_i}
  =
  \begin{pmatrix}
    \sin\theta_{i}\, \cos\phi_{i} \\
    \sin\theta_{i}\, \sin\phi_{i} \\
    \cos\theta_{i}              \\
  \end{pmatrix}

and how the vector :math:`\ket{f_i}` is rotated into :math:`\ket{n}`


.. raw:: html
  :file: ../../../images/spin-rotations-symmetric.html

.. rst-class:: plotly-figure-caption

  **Figure 1** (interactive): Vectors and angles used in the spin rotations.

--------------------------------------
Rotation operator and basis definition
--------------------------------------

The rotation operator :math:`\boldsymbol{R}_i` carrying out the above transformation
is defined as follows. Let :math:`\ket{r_i}` be a vector perpendicular to both
:math:`\ket{n}` and :math:`\ket{f_i}`. Then :math:`\ket{n}` is brought to
:math:`\ket{f_i}` by performing a rotation of angle :math:`\theta_i` about
:math:`\ket{r_i}`. The unit vector

.. math::
    ^n\boldsymbol{\hat{r_i}}
    =
    \dfrac{\boldsymbol{\hat{n}}\,\times\,^n\boldsymbol{\hat{f}_i}
      }{
      \vert\boldsymbol{\hat{n}}\,\times\,^n\boldsymbol{\hat{f}_i}\vert
      }
    =
    \begin{pmatrix}-\sin\beta \\\cos\beta  \\0\end{pmatrix}

is defined by the angle :math:`\beta` in the figure above.
The rotation operator is

.. math::
  \boldsymbol{R}_i=\boldsymbol{R_\ket{r_i}}(\theta_i)=e^{-i\,\theta_i\,\ket{r_i}\,\times}


A local reference frame :math:`(p_i\, t_i\, f_i)` is defined by
performing the same rotation :math:`\boldsymbol{R}_{\ket{r_i}}(\theta_i)` over all
the three unit vectors :math:`(u\, v\, n)`

.. math::
  \ket{p_i}&=\boldsymbol{R_i}\,\ket{u}\\
  \ket{t_i}&=\boldsymbol{R_i}\,\ket{v}\\
  \ket{f_i}&=\boldsymbol{R_i}\,\ket{n}

Therefore the rotation operator can also be expressed as

.. math::
  \boldsymbol{R}_i=\ket{\,p_i\,t_i\,f_i\,}\,\bra{\,u\,v\,n\,}

-------------------------------------
Rotation matrix and basis coordinates
-------------------------------------

The rotation operator matrix elements in the :math:`(\,u\,v\,n\,)` basis are therefore

.. math::
  ^n\boldsymbol{R_i}&=
  \braket{\,u\,v\,n\,|\,p_i\,t_i\,f_i\,}=
  \braket{\,u\,v\,n\,|\,\boldsymbol{R_i}\,|\,u\,v\,n\,}\\
   &=
  \begin{pmatrix}
    \cos\theta_i + \sin^2\phi_i\, \, (1 - \cos\theta_i) &
    -\sin\phi_i\, \cos\phi_i\, \, (1 - \cos\theta_i)    &
    \cos\phi_i\, \sin\theta_i                           \\
    -\sin\phi_i\, \cos\phi_i\, \, (1 - \cos\theta_i)    &
    \cos\theta_i + \cos^2\phi_i\, \, (1 - \cos\theta_i) &
    \sin\phi_i\, \sin\theta_i                           \\
    -\cos\phi_i\, \sin\theta_i &
    -\sin\phi_i\, \sin\theta_i &
    \cos\theta_i               \\
  \end{pmatrix}

The vector components in the :math:`(\,u\,v\,n\,)` reference frame are nothing
but the columns of the above matrix

.. math::
  ^n\boldsymbol{\hat{p}}_i
  \,=\,
  \braket{\,u\,v\,n\,|\,p_i}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\theta_i + \sin^2\phi_i\, \, (1-\cos\theta_i) \\
    -\sin\phi_i\, \cos\phi_i\, \, (1-\cos\theta_i)    \\
    -\cos\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  ^n\boldsymbol{\hat{t}}_i
  \,=\,
  \braket{\,u\,v\,n\,|\,t_i}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
  =
  \begin{pmatrix}
    -\sin\phi_i\, \cos\phi_i\,(1-\cos\theta_i)      \\
    \cos\theta_i + \cos^2\phi_i\, (1-\cos\theta_i)  \\
    \sin\phi_i\, \sin\theta_i
  \end{pmatrix}

.. math::
  ^n\boldsymbol{\hat{f}}_i
  \,=\,
  \braket{\,u\,v\,n\,|\,f_i}
  \,=\,
  ^n\boldsymbol{R}_i\, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
  =
  \begin{pmatrix}
    \cos\phi_i\, \sin\theta_i \\
    \sin\phi_i\, \sin\theta_i \\
    \cos\theta_i
  \end{pmatrix}
