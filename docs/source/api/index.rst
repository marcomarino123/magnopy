.. module:: magnopy

.. _api:

*************
API reference
*************

:Release: |version|

The main interface to the package should be imported as

.. doctest::

  >>> import magnopy

Sub-modules
===========
.. toctree::
  :maxdepth: 1

  io
  scenarios
  constants

Classes
=======

.. autosummary::
    :toctree: generated/

    Convention
    SpinHamiltonian
    Energy
    LSWT

Functions
=========

.. autosummary::
  :toctree: generated/

  solve_via_colpa
  span_local_rf
  span_local_rfs
  logo
  multiprocess_over_k

Parameter converters
====================

.. autosummary::
  :toctree: generated/

  converter22
  converter422

Exceptions
==========

.. autosummary::
  :toctree: generated/

  ConventionError
  ColpaFailed
