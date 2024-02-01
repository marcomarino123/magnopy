.. _user-guide_input_model-file_atoms:

Atoms
=====

.. code-block:: text
  :linenos:

  ==========
  Atoms <Units>
  A1 i j k <spin1>
  A2 i j k <spin2>
  A3 i j k <spin3>
  ==========

* line 1: Section separator (10 or more ``=`` symbols)
* line 2: One or two entries, separated by spaces:

  - ``Atoms`` keyword. Only the first letter is actually checked.
  - (optional) ``<Units>``. One of the predefined keywords.
    Defines the units of the atom's coordinates. Allowed values are

    - ``Relative`` (default)

      Atom coordinates are relative to the cell vectors:
      :math:`\boldsymbol{r} = i\boldsymbol{a} + j\boldsymbol{a} + k\boldsymbol{c}`
    - ``Angstrom``

      Atom coordinates are absolute and given in Angstroms.
      :math:`\boldsymbol{r} = (i, j, k)^T`
    - ``Bohr``

      Atom coordinates are absolute and given in Bohr.
      :math:`\boldsymbol{r} = (i, j, k)^T`

    Note: Only the first letter is actually checked.

* line 3: Information about the first atom, five, seven or eight entries, separated by spaces:

  - ``A1`` - atom's label. Any string, that does not contain "#" or space symbols and
    starts with a letter (lowercase or uppercase) or a number.
    Atom's labels have to be unique.
  - ``i`` - first coordinate.
  - ``j`` -  second coordinate.
  - ``k`` - third coordinate.
  - (optional) ``<spin1>`` -  spin of the first atom. Spins are given in Bohr magnetons.
    Either one, three or four entries separated by space:

    - :math:`S` - spin value. It is oriented along
      :math:`z` direction, i.e. :math:`\boldsymbol{S} = (0,\,0,\,S)^T`.

    - :math:`S_x` :math:`S_y` :math:`S_z` - spin vector.
      :math:`\boldsymbol{S} = (S^x,\,S^y,\,S^z)^T`.
    - :math:`S_x` :math:`S_y` :math:`S_z` :math:`S` - direction of spin vector and its value.
      The module of the vector is ignored and the provided value is used.

      .. math::
        \boldsymbol{S^{dir}} &= (S^x,\,S^y,\,S^z)^T

        \boldsymbol{S} &= S\,\dfrac{\boldsymbol{S^{dir}}}{S^{dir}}
    - :math:`p\phi` :math:`t\theta` :math:`S` - polar (:math:`p\phi`) and
      azimuthal (:math:`t\theta`) angles and spin Value. Order is arbitrary.
      Two angles, that define the direction of the spin as described
      :ref:`here <user-guide_methods_spin-rotations>`. :math:`p` and :math:`t` are used
      to distinguish this case from the spin vector one, i.e.

      - ``p30 t90 0.5`` - two angles and value
      - ``30 90 0.5`` - spin vector

      Angles are given in degrees :math:`0^{\circ} \le \phi \le 360^{\circ}`,
      :math:`0^{\circ} \le \theta \le 180^{\circ}`

      :math:`\boldsymbol{S} = S\,(\cos\phi\sin\theta,\,\sin\phi\sin\theta,\,\cos\theta)^T`

* line 4: Information about the second atom.
* line 5: Information about the third atom.
* line 6: Section separator (10 or more ``=`` symbols)

.. dropdown:: Examples

  Below we list a few ways to provide the same two atoms with the same positions and
  without the spin.

  The cell for all provided cases is

  .. code-block:: text

    ==========
    Cell
    1 0 0
    0 2 0
    0 0 3
    ==========

  .. code-block:: text

    ==========
    Atoms
    Fe1 0 0 0.5
    Fe2 0.1 0.5 0
    ==========

  .. code-block:: text

    ==========
    Atoms Relative
    Fe1 0 0 0.5
    Fe2 0.1 0.5 0
    ==========

  .. code-block:: text

    ==========
    Atoms Angstrom
    Fe1 0 0 1.5
    Fe2 0.1 1 0
    ==========

  .. code-block:: text

    ==========
    Atoms Bohr
    Fe1 0         0           2.8345891869386555
    Fe2 0.18897261246257702 1.8897261246257702 0
    ==========

  Below we list a few ways to provide two atoms with the same spin in each case.

  .. code-block:: text

    ==========
    Atoms
    #               Sx                 Sy                 Sz
    Fe1 0   0   0.5 1.2247448713915892 1.2247448713915892 1
    #               Sx Sy Sz
    Fe2 0.1 0.5 0   0  0  2
    ==========

  .. code-block:: text

    ==========
    Atoms
    #               Sx Sy Sz                S
    Fe1 0   0   0.5 3  3  2.449489742783178 2
    #               S
    Fe2 0.1 0.5 0   2
    ==========

  .. code-block:: text

    ==========
    Atoms
    #               phi  theta S
    Fe1 0   0   0.5 p45  t60   2
    #               Sx Sy Sz S
    Fe2 0.1 0.5 0   0  0  1  2
    ==========

  .. code-block:: text

    ==========
    Atoms
    #               theta phi S
    Fe1 0   0   0.5 t60   p45 2
    #               S theta phi
    Fe2 0.1 0.5 0   2 t0    p0
    ==========

  .. code-block:: text

    ==========
    Atoms
    #               theta S phi
    Fe1 0   0   0.5 t60   2 p45
    #               S phi theta
    Fe2 0.1 0.5 0   2 p0  t0
    ==========

  .. code-block:: text

    ==========
    Atoms
    #               phi S theta
    Fe1 0   0   0.5 p45 2 t60
    #               S phi theta
    Fe2 0.1 0.5 0   2 p29 t0 # Note that phi can be anything if t is 0 or 180
    ==========
