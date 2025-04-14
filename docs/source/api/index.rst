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

  spinham
  energy
  bosons
  lswt
  io
  constants

Classes
=======

Top-level functions
===================

.. autosummary::
  :toctree: generated/

  solve_via_colpa
  logo

Exceptions
==========

.. autosummary::
  :toctree: generated/

  NotationError
  ColpaFailed
