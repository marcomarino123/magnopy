.. _user_guide_scripts_convert-tb2j:

********************
magnopy-convert-tb2j
********************

Small script that convert spin Hamiltonian from the results of |TB2J|_ package
(typically a file named "exchange.out") to the magnopy format.

Parameters
==========

.. _magnopy-convert-tb2j_input-filename:

-if, --input-filename
---------------------
Relative or absolute path to the "exchange.out" file,
including the name and extension of the file. If ends with ".hdf5", then the Hamiltonian
is saved in a binary format, otherwise it is saved in a txt format.

.. code-block:: text

    required


.. _magnopy-convert-tb2j_output-filename:

-of, --output-filename
----------------------
Relative or absolute path to the output file.

.. code-block:: text

    default : "spinham.txt"


.. _magnopy-convert-tb2j_output-filename:

-f, --format
------------
Whether to save Hamiltonian in a binary or human-readable (txt) format.
If ``format == "hdf5"`` then ".hdf5" is added to the
:ref:`_magnopy-convert-tb2j_output-filename` (and ".txt" is removed if present).
Overwrites the behavior based on the extension of the
:ref:`_magnopy-convert-tb2j_output-filename`

.. code-block:: text

    default : None
    choices: "txt" or "hdf5"


.. _magnopy-convert-tb2j_output-filename:

-v, --verbose
-------------
Whether to output statistics of the progress. Take no value.
