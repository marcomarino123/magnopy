.. _contribute_tests:

*******
Testing
*******

In magnopy we rely on |pytest|_, |hypothesis|_ and |doctest|_ for testing.

Unit tests
==========

All unit tests are located in the "utest" directory.
To run the tests, you can use the following command::

    make test

Structure of the "utest" directory loosely follows the structure of the "src/magnopy" directory.

For example if you've added a new function named "rotate()" to the :py:class:`.Crystal`
class from the "src/magnopy/crystal.py" file, you should add a new test function named
"test_rotate()" to the file "utest/test_crystal.py".

Documentation tests
===================

Across the documentation there are many examples of how to use magnopy with code snippets.
These code snippets are tested using |doctest|_, which ensure that the documentation
correctly reflects an actual behavior of the code. In order to run doctests you need
to build the :ref:`documentation <contribute_documentation>` and then run the doctests using
the following command::

    make doctest
