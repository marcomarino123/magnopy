.. _user-guide_cli_magnopy-lswt:

************
magnopy-lswt
************

This scenario runs a calculation for the given spin Hamiltonian at the level of the
linear spin wave theory and outputs majority of the results that magnopy can compute.



Help message
============
This page of documentation is written by hand and might become outdated due to the
human error. Moreover, we do not intend to cover all possible parameters of the script
in this page of the documentation. To get the automatically generated description of **all**
input parameters, that is produced by the actual version of magnopy that is installed
in you environment use

.. code-block::

    magnopy-lswt --help

That should output something similar to

.. literalinclude:: help.inc
    :language: text

At the very beginning there is a syntax for the usage of the script, where required
arguments are given without brackets and optional arguments are written within brackets.
Then there is a logo of magnopy, followed by the list of supported arguments with their
short and long names and explanation of what they represent.

.. hint::

    The short (i.e. ``-sf``) and long (i.e. ``--spinham-filename``) are absolutely equivalent.
    Feel free to use either of them. The long name usually is self-explanatory and
    the short one is added purely for the convenience of the user.

.. code-block::

    magnopy-lswt -sf spinHamiltonian.txt

Interpretation of the output
============================

The script print in the console the progress of the calculation. Use the stream redirect
to save it to a file

.. code-block:: bash

    magnopy-lswt ... > output.txt

Some of the data and pictures will be saved in the folder with the name defined by the
value of ``-of, --output-folder`` argument.
