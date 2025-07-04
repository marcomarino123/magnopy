.. _user-guide_cli_optimize-sd:

*******************
magnopy-optimize-sd
*******************

This scenario optimizes classical energy of the spin Hamiltonian and finds the spin
directions that describe a local minima of the energy landscape.

Help message
============
This page of documentation is written by hand and might become outdated due to the
human error. Moreover, we do not intend to cover all possible parameters of the script
in this page of the documentation. To get the automatically generated description of **all**
input parameters, that is produced by the actual version of magnopy that is installed
in you environment use

.. code-block::

    magnopy-optimize-sd --help

That should output something similar to

.. literalinclude:: help.inc
    :language: text

At the very beginning there is a syntax for the usage of the script, where required
arguments are given without brackets and optional arguments are written within brackets.
Then there is a logo of magnopy, followed by the list of supported arguments with their
short and long names and explanation of what they represent.

.. hint::

    The short (i.e. ``-sf``) and long (i.e. ``--spinham-filename``) are absolutely equivalent.
    Feel free to use either of them. The long name is usually self-explanatory and
    the short one is added purely for the convenience of the user.


Spin Hamiltonian and its source
===============================

This script works with the spin Hamiltonian that is coming from some third-party software.
At the moment magnopy supports |TB2J|_ and |GROGU|_.

.. hint::
    There is number of ways to use this script with the hand-made Hamiltonian:

    * Prepare the file that mimics the format of |TB2J|_.
    * Prepare the file that mimics the |GROGU-FF|_.
    * Prepare the spin Hamiltonian programmatically and use the scenario of this
      command-line script from within your python scripts: :py:func:`.scenarios.optimize_sd`.

To tell the script what spin Hamiltonian to use provide

* Source of the spin Hamiltonian (``-ss`` or ``--spinham-source``);
* Path to the file with the spin Hamiltonian (``-sf`` or ``--spinham-filename``)

For example, if the file with the spin Hamiltonian is located in the
"data/hamiltonians/trial1/TB2J/exchange.out" and the source of the file is |TB2J|_,
then pass to the script two parameters either in the short form

.. code-block:: bash

    magnopy-optimize-sd -ss TB2J -sf data/hamiltonians/trial1/TB2J/exchange.out

or in the long form

.. code-block:: bash

    magnopy-optimize-sd -spinham-source TB2J -spinham-filename data/hamiltonians/trial1/TB2J/exchange.out



Interpretation of the output
============================

The script print in the console the progress of the calculation. Use the stream redirect
to save it to a file

.. code-block:: bash

    magnopy-optimize-sd ... > output.txt

Some of the data and pictures will be saved in the folder with the name defined by the
value of ``-of, --output-folder`` argument.


.. .. raw:: html

..     <iframe src="../../_static/magnopy-sd.html" height="540px" width="100%"></iframe>
