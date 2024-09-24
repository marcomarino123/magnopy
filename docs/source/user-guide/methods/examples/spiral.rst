.. _user-guide_methods_examples_spiral:

******
Spiral
******

This last example consists of a spin lattice containing a single atom per unit cell, where
spin lie in the :math:`xy` plane displaying a spiral arrangement with wave-vector
:math:`boldsymbol{q}`. We assume here that the two reference frames :math:`(\,x\,y\,z\,)`
and :math:`(\,u\,v\,n\,)` are identical, and perform only the intracell rotation given
by :math:`\phi=0`, :math:`\theta=\pi/2`, as indicated in the figure below.
Then the intracell and intercell rotation matrices are

.. math::
  ^z\boldsymbol{R}&\,=\,e^{i\,\pi/2\,\begin{pmatrix}0\\1\\0\end{pmatrix}\times}
    \,=\,\begin{pmatrix}0&0&1\\0&1&0\\-1&0&0\end{pmatrix}\\
  ^z\boldsymbol{R}_m&\,=\,
  e^{i\,\boldsymbol{q}\cdot\boldsymbol{r}_m\,\begin{pmatrix}0\\1\\0\end{pmatrix}\times}\,=
  \,\begin{pmatrix}
  \cos(\boldsymbol{q}\cdot\boldsymbol{r}_m)&-\sin(\boldsymbol{q}\cdot\boldsymbol{r}_m)&0\\
  \sin(\boldsymbol{q}\cdot\boldsymbol{r}_m)&\cos(\boldsymbol{q}\cdot\boldsymbol{r}_m)&0\\
  0&0&1
  \end{pmatrix}

The magnetization is then

.. math::
  \boldsymbol{S}_m\,=\,^z\boldsymbol{R}_m\,^z\boldsymbol{R}\,\begin{pmatrix}0\\0\\S_i\end{pmatrix}\,=\,
  S_i\,\begin{pmatrix}
  \cos(\boldsymbol{q}\cdot\boldsymbol{r}_m)\\\sin(\boldsymbol{q}\cdot\boldsymbol{r}_m)\\0
  \end{pmatrix}

The exchange tensor becomes in the rotated reference frame


We assume the following simplifications: :math:`J^{xx}=J^{yy}` and
:math:`J^{zx}=J^{zy}=S^z=0`. Then the exchange tensor is written as follows

The classical energy expression is

=======================
Linear Spin Wave Theory
=======================
