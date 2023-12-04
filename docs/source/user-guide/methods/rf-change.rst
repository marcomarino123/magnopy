.. _user-guide_methods_rf-change:

*****************************
Change of the reference frame
*****************************

.. dropdown:: Notation used on this page

  * :math:`\vec{v}` - is a vector.
  * :math:`\hat{v}` - is a unit vector, corresponding to the
    vector :math:`\vec{v}`.
  * :math:`\times` - means cross product for vectors.
  * "reference frame" = "coordinate system" = "basis"
  * On this page all vectors and matrices are written in the
    :math:`\hat{x}\hat{y}\hat{z}` reference frame.
  * For this page we adopt bra-ket notation.


Here we discuss how the spin vectors and exchange matrices are
changing under when we move from the given to the chosen reference frame.

As shown in the :ref:`previous section <user-guide_methods_rf-choice>`
the rotation matrix :math:`R` rotate :math:`\vert xyz\rangle` reference frame
to the :math:`\vert uvn\rangle`:

.. math::
  \vert uvn\rangle = R\vert xyz\rangle \Rightarrow
  \langle uvn\vert = \langle xyz\vert R^T = \langle xyzR\vert

Let us first work with the arbitrary (spin) vector :math:`\vert S\rangle`:

.. math::
  \langle uvn\vert S\rangle
  = \langle xyzR\vert S\rangle
  = \langle xyz\vert R^T\vert S\rangle
  = \langle xyz\vert R^T\vert xyz\rangle\langle xyz\vert S\rangle

Let us write this result explicitly:

.. math::
  \begin{pmatrix}
    S_u \\
    S_v \\
    S_n \\
  \end{pmatrix}
  =
  \begin{pmatrix}
    R_{xx} & R_{xy} & R_{xz} \\
    R_{yx} & R_{yy} & R_{yz} \\
    R_{zx} & R_{zy} & R_{zz} \\
  \end{pmatrix}
  \begin{pmatrix}
    S_x \\
    S_y \\
    S_z \\
  \end{pmatrix}

.. note::
  Rotation matrix :math:`R` is explicitly written in the
  :math:`\vert xyz\rangle` reference frame in the
  :ref:`previous section <eq:rf-choice-rot-matrix>`.

Next, we write the equations for the exchange matrices:

.. math::
  \langle uvn\vert J_{ij}\vert uvn\rangle
  = \langle xyz\vert R^T J_{ij} R\vert xyz\rangle
  = \langle xyz\vert R^T
  \vert xyz\rangle\langle xyz\vert
  J_{ij}
  \vert xyz\rangle\langle xyz\vert
  R\vert xyz\rangle

In a matrix form this result is written as:

.. math::
  \begin{pmatrix}
    J_{uu} & J_{uv} & J_{un} \\
    J_{vu} & J_{vv} & J_{vn} \\
    J_{nu} & J_{nv} & J_{nn} \\
  \end{pmatrix}
  = R^T
  \begin{pmatrix}
    J_{xx} & J_{xy} & J_{xz} \\
    J_{yx} & J_{yy} & J_{yz} \\
    J_{zx} & J_{zy} & J_{zz} \\
  \end{pmatrix} R







.. important::
  In the following pages the reference frame :math:`\vert uvn\rangle`
  is often used, where :math:`\hat{n}` is a cone axis.
