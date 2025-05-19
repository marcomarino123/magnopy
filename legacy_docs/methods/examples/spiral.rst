.. _user-guide_methods_examples_spiral:

*************************
Spiral Spin configuration
*************************

This last example consists of a spin lattice containing a single atom per unit cell, where
spin lie in the :math:`xy` plane displaying a spiral arrangement with wave-vector
:math:`\boldsymbol{q}`. We assume here that the two reference frames :math:`(\,x\,y\,z\,)`
and :math:`(\,u\,v\,n\,)` are identical, and perform only the intracell rotation given
by :math:`\phi=0`, :math:`\theta=\pi/2`, as indicated in the figure below.


.. image::
  ../../../../images/spiral.pdf

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
  \boldsymbol{S}_m\,=\,^z\boldsymbol{R}_m\,^z\boldsymbol{R}\,\begin{pmatrix}0\\0\\S_i\end{pmatrix}
  \,=\,S_i\,\begin{pmatrix}
  \cos(\boldsymbol{q}\cdot\boldsymbol{r}_m)\\\sin(\boldsymbol{q}\cdot\boldsymbol{r}_m)\\0
  \end{pmatrix}

The exchange tensor assumes the following form in the rotated reference frame

.. math::
  ^{sz}\tilde{\boldsymbol{J}}_{\boldsymbol{d}}=
  \begin{pmatrix}
  \left(J^{xy,+}_{\boldsymbol{d}}+i\,D^z_{\boldsymbol{d}}\right)\,
  e^{-i\,\boldsymbol{q}\cdot\boldsymbol{d}}&
  \left(J^{xy,-}_{\boldsymbol{d}}-i\,S^z_{\boldsymbol{d}}\right)\,
  e^{i\,\boldsymbol{q}\cdot(2\,\boldsymbol{r}_m+\boldsymbol{d})}&
  \frac{1}{\sqrt{2}}\,\left(J^{xz}_{\boldsymbol{d}}-i\,J^{yz}_{\boldsymbol{d}}\right)\,
  e^{i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}\\
  \left(J^{xy,-}_{\boldsymbol{d}}+i\,S^z_{\boldsymbol{d}}\right)\,
  e^{-i\,\boldsymbol{q}\cdot(2\,\boldsymbol{r}_m+\boldsymbol{d})}&
  \left(J^{xy,+}_{\boldsymbol{d}}+i\,D^z_{\boldsymbol{d}}\right)\,
  \,e^{i\,\boldsymbol{q}\cdot\boldsymbol{d}}&
  \frac{1}{\sqrt{2}}\,\left(J^{xz}_{\boldsymbol{d}}+i\,J^{yz}_{\boldsymbol{d}}\right)\,
  \,e^{-i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}\\
  \frac{1}{\sqrt{2}}\,\left(J^{zx}_{\boldsymbol{d}}+i\,J^{zy}_{\boldsymbol{d}}\right)
  \,e^{-i\,\boldsymbol{q}\cdot(\boldsymbol{r}_m+\boldsymbol{d})}&
  \frac{1}{\sqrt{2}}\,\left(J^{zx}_{\boldsymbol{d}}-i\,J^{zy}_{\boldsymbol{d}}\right)&
  J^{zz}_{\boldsymbol{d}}
  \end{pmatrix}
  +2,delta_{\boldsymbol{d},0}\,
  \begin{pmatrix}
      A^{xy,+}&A^{xy,-}\,e^{2\,i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}&
      \frac{1}{\sqrt{2}}\,(A^{xz}-i\,A^{yz})\,e^{i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}\\
      A^{xy,-}\,e^{-2\,i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}&A^{xy,+}&
      \frac{1}{\sqrt{2}}\,(A^{xz}+i\,A^{yz})\,e^{-i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}\\
      \frac{1}{\sqrt{2}}\,(A^{xz}+i\,A^{yz})\,e^{-i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}&
      \frac{1}{\sqrt{2}}\,(A^{xz}-i\,A^{yz})\,e^{i\,\boldsymbol{q}\cdot\boldsymbol{r}_m}&A^{zz}
  \end{pmatrix}

The classical energy expression is

.. math::
  E^{cl}=\frac{S^2}{2}\,\sum_\boldsymbol{d}\,
  \left(J^{xy,+}\,\cos(\boldsymbol{q}\cdot\boldsymbol{d})+
  D^z\,\sin(\boldsymbol{q}\cdot\boldsymbol{d})+S^2\,A^{xy,+}
  \right)

We assume the following simplifications: :math:`J^{xx}=J^{yy}`, :math:`A^{xx}=A^{yy}` and
:math:`J^{zx}=J^{zy}=S^z=0`, :math:`A^{zx}=A^{zy}=0`. Then the exchange tensor is
written as follows

.. math::
  ^{sz}\tilde{\boldsymbol{J}}_{\boldsymbol{d}}=
  \begin{pmatrix}
    \left(J^{xy,+}_{\boldsymbol{d}}+i\,D^z_{\boldsymbol{d}}\right)\,
  e^{-i\,\boldsymbol{q}\cdot\boldsymbol{d}}&0&0\\
  0&\left(J^{xy,+}_{\boldsymbol{d}}+i\,D^z_{\boldsymbol{d}}\right)\,
  \,e^{i\,\boldsymbol{q}\cdot\boldsymbol{d}}&0\\
  0&0&J^{zz}_{\boldsymbol{d}}
  \end{pmatrix}
  +2\,\delta_{\boldsymbol{d},0}\,
  \begin{pmatrix}A^{xy,+}&0&0\\0&A^{xy,+}&0\\0&0&A^{zz}\end{pmatrix}

=======================
Linear Spin Wave Theory
=======================

We find that only the lowest harmonic :math:`p=0` contributes to the LSWT Hamiltonian, so that

.. math::
  T^0(\boldsymbol{k})&\,=\,\frac{S}{2}\,
  \left(J^{zz}(\boldsymbol{k})-2\,(A^{xy,+}-A^{zz}) +
    \frac{J^{xy,+}(\boldsymbol{k}+\boldsymbol{q})+J^{xy,+}(\boldsymbol{k}-\boldsymbol{q})}{2}
    -2\,J^{xy,+}(\boldsymbol{q})
    -i\,\frac{D^z(\boldsymbol{k}+\boldsymbol{q})-D^z(\boldsymbol{k}-\boldsymbol{q})}{2}
    +2\,i\,D^z(\boldsymbol{q})\right)\\
  \Delta^0(\boldsymbol{k})&\,=\,\frac{S}{2}\,\left(J^{zz}(\boldsymbol{k})-2\,(A^{xy,+}-A^{zz}) -
    \frac{J^{xy,+}(\boldsymbol{k}+\boldsymbol{q})+J^{xy,+}(\boldsymbol{k}-\boldsymbol{q})}{2}
    +i\,\frac{D^z(\boldsymbol{k}+\boldsymbol{q})-D^z(\boldsymbol{k}-\boldsymbol{q})}{2}
    \right)


The Magnetic Brillouin Zone must fulfill the condition
:math:`M_q\,\boldsymbol{q}=\boldsymbol{G}`, and can be very large, but it is diagonal.
Therefore

.. math::
  {\cal H}(\boldsymbol{k})=
  \begin{pmatrix}
  T^0(\boldsymbol{k})&\Delta^0(\boldsymbol{k})\\\Delta^0(\boldsymbol{k})&T^0(\boldsymbol{k})
  \end{pmatrix}

Diagonalizing the dynamic matrix :math:`{\cal M}(\boldsymbol{k})` the magnon spectrum is

.. math::
  \omega(\boldsymbol{k})=
  \frac{S}{2}\,\sqrt{(T^0(\boldsymbol{k}))^2-(\Delta^0(\boldsymbol{k}))^2}

A final simplification is achieved if :math:`D^z=0` since then the known dispersion
relation of an helical magnet is recovered

.. math::
  S\,\sqrt{\left(J^{zz}(\boldsymbol{k})-2\,(A^{xy,+}-A^{zz})-J^{xy,+}(\boldsymbol{k})\right)\,
  \left(\frac{J^{xy,+}(\boldsymbol{k}+\boldsymbol{q})+J^{xy,+}(\boldsymbol{k}-\boldsymbol{q})}{2}
  -J^{xy,+}(\boldsymbol{q})\right)}
