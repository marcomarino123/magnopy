.. _user-guide_how-to-run:

*******************
How to run magnopy?
*******************

Magnopy has a number of pre-defined scripts that reflects its basic functionality.

Every script is intended to be executed from a command line in a following way:

.. code-block:: bash

    script-name

For any script use --help or -h option in the terminal in order to display help message
with the short summary of the arguments.


.. code-block:: bash

    script-name --help

Almost every scripts require an input in a form of parameters. Below is an example where
two parameters are passed to the script: spinham and source_type with the values of
"spinham1.txt" and "txt" correspondingly. Majority of the parameters support short names,
that are interchangeable with the long ones (i.e. ``--spinham`` / ``-s``) with the
full name being preceded by two "-" and a short one - by one "-". For the full list of
supported arguments - consult documentation page for each script.

.. code-block::

    script-name --spinham spinham1.txt --source_type txt

For the advance usage one can consult the python :ref:`api`.
