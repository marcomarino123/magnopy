.. _user-guide_methods_xyz-to-uvn:

**********************
Change from xyz to uvn
**********************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.txt
  * .. include:: page-notations/matrix.txt
  * .. include:: page-notations/reference-frame.txt
  * .. include:: page-notations/bra-ket.txt


Here we discuss how the spin vectors and exchange matrices are
changing under the change from the given to the chosen reference frame.

As shown in the :ref:`previous section <user-guide_methods_uvn-choice>`
the rotation matrix :math:`\boldsymbol{R_{rf}}` rotate :math:`\vert xyz\rangle`
reference frame to the :math:`\vert uvn\rangle`

.. math::
  \vert uvn\rangle
  =
  \boldsymbol{R_{rf}} \vert xyz \rangle
  \Rightarrow
  \langle uvn \vert
  =
  \langle xyz \vert \boldsymbol{R_{rf}}^{\dagger}
  =
  \langle xyz R_{rf} \vert

.. math::
  \langle xyz \vert R_{rf} \vert xyz \rangle
  =
  \langle xyz \vert uvn \rangle

Let us first work with the arbitrary (spin) vector :math:`\vert S\rangle`:

.. math::
  \langle uvn \vert S \rangle
  =
  \langle xyz R_{rf} \vert S\rangle
  =
  \langle xyz \vert R_{rf}^{\dagger} \vert S \rangle
  =
  \langle xyz \vert R_{rf}^{\dagger} \vert xyz \rangle
  \langle xyz \vert S \rangle

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
  Rotation matrix :math:`\boldsymbol{R_{rf}}` is explicitly written in the
  :math:`\vert xyz\rangle` reference frame in the
  :ref:`previous section <eq:uvn-choice-rot-matrix>`.

Next, we write the equations for the exchange matrices:

.. math::
  \langle uvn \vert J \vert uvn \rangle
  =
  \langle uvn \vert xyz \rangle
  \langle xyz \vert J \vert xyz \rangle
  \langle xyz \vert uvn \rangle
  =
  \langle xyz \vert R_{rf}^{\dagger}
  \vert xyz \rangle
  \langle xyz \vert J \vert xyz \rangle
  \langle xyz \vert
  R_{rf}
  \vert xyz \rangle

In a matrix form this result is written as:

.. math::
  \begin{pmatrix}
    J_{ab}^{uu} & J_{ab}^{uv} & J_{ab}^{un} \\
    J_{ab}^{vu} & J_{ab}^{vv} & J_{ab}^{vn} \\
    J_{ab}^{nu} & J_{ab}^{nv} & J_{ab}^{nn} \\
  \end{pmatrix}
  = \boldsymbol{R_{rf}}^{\dagger}
  \begin{pmatrix}
    J_{ab}^{xx} & J_{ab}^{xy} & J_{ab}^{xz} \\
    J_{ab}^{yx} & J_{ab}^{yy} & J_{ab}^{yz} \\
    J_{ab}^{zx} & J_{ab}^{zy} & J_{ab}^{zz} \\
  \end{pmatrix} \boldsymbol{R_{rf}}

.. important::
  In the following pages the reference frame :math:`\vert uvn\rangle`
  is often used, where :math:`\hat{n}` is a cone axis.
