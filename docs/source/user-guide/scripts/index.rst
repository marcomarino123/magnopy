.. _user-guide_scripts:

*********************
Magnopy as a blackbox
*********************

Magnopy is a python library and for more flexibility should be used within user's python
script. Nevertheless, we do not want to make it available to the people who does not
know python and offer a bunch of scripts that can perform most common tasks. The guides
below explain how each script works and what can it do.

Every script is intended to be executed from a command line

.. code-block:: bash

    script-name

For any script use --help or -h option in the terminal to display help message with the
short summary of the arguments.


.. code-block:: bash

    script-name --help

Almost every script requires some parameter as an input. Below is an example where
two parameters are passed to the script: spinham and source_type with the values of
"spinham1.txt" and "txt" correspondingly. Majority of the parameters support two
interchangeable names: a short one and a long oneshort (i.e. ``-s`` and ``--spinham``).
Long name is alwayseing preceded by two "-" and a short one by one "-".

.. code-block::

    script-name --spinham spinham1.txt --source_type txt


.. toctree::
    :maxdepth: 1

    #TODO
