.. _user_guide_scripts_minimize-energy:

***********************
magnopy-minimize-energy
***********************

Minimizes classical energy of the spin Hamiltonian, assuming one of the three states:

* Ferromagnetic
* Antiferromagnetic
* Spiral

.. warning::
    The spiral case is in active testing phase and might give unstable results and/or
    troubles with convergence.

Parameters
==========

.. _magnopy-minimize-energy_spinham:

-sh, --spinham
--------------
Relative or absolute path to the file with spin Hamiltonian,
including the name and extension of the file.

* If ends with ".hdf5", then the Hamiltonian is assumed to be provided in a binary
  format.

* If it ends with ".txt", then the Hamiltonian is assumed to be provided in
  human-readable magnopy's format.

* If it ends with the "exchange.out", then the Hamiltonian is assumed to be coming from
  |TB2J|_.

* In all other cases magnopy's human-readable format is assumed.

.. code-block:: text

    required

.. _magnopy-minimize-energy_spinham-format:

-shf, --spinham-format
----------------------
If given, then overwrites the behavior based on the :ref:`magnopy-minimize-energy_spinham`.

.. code-block:: text

    default : None
    choices : "txt" or "hdf5" or "tb2j"

.. _magnopy-minimize-energy_ground-state-type:

-gst, --ground-state-type
-------------------------
Type of the ground state to be assumed. By default it performs optimization of all three
supported ground states. Either "all" or any combination of others, separated by spaces.

.. code-block:: text

    default : "all"
    choices : "all" or "ferro" or "antiferro" or "spiral"

.. _magnopy-minimize-energy_magnetic-field:

-mf, --magnetic-field
---------------------
External magnetic field. Given in the same reference frame as the parameters of the
Hamiltonian from :ref:`magnopy-minimize-energy_spinham`. Three numbers: ``H_x H_y H_z``.

.. code-block:: text

    nargs : 3
    default : None
    type : float

.. _magnopy-minimize-energy_seedname:

-os, --output_seedname
----------------------
Seedname that is used for various output files.

.. code-block:: text

    default : "minim"
