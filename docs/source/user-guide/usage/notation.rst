.. _user-guide_usage_notation:

********
Notation
********

For the theoretical background of the notation problem and why it is important see
:ref:`user-guide_theory-behind_notation`.

Magnopy implements a compact :py:class:`.Notation` class to store the notation of the
spin Hamiltonian. It stores all parameters that define notation in one data structure.

.. doctest::

    >>> from magnopy import Notation
    >>> notation = Notation(multiple_counting = True, spin_normalized = False, c1 = 1, c21 = 1)
    >>> notation.name
    'custom'
    >>> notation.multiple_counting
    True
    >>> notation.c21
    1.0
    >>> notation.summary()
    custom notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are not normalized;
      * c1 = 1.0;
      * c21 = 1.0;
      * Undefined c22 factor;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.

There are two boolean properties (:py:attr:`.Notation.multiple_counting` and
:py:attr:`.Notation.spin_normalized`) and eleven constants that fully define the
notation of the spin Hamiltonian.

Notation is one of three objects that are required for the creation of the
:py:class:`.SpinHamiltonian` class. It is stored as an its attribute
:py:attr:`.SpinHamiltonian.notation`.

Modified notation
=================

Every instance of the notation class is meant to be static, therefore the properties of
the notation can not be changed

.. doctest::

    >>> notation.multiple_counting = False
    Traceback (most recent call last):
    ...
    AttributeError: It is intentionally forbidden to set properties of notation. Use correct methods of SpinHamiltonian class to change notation.

If you need to have a new notation, then create a new instance of the
:py:class:`.Notation` class.

For that purpose notation class has a method :py:meth:`.Notation.get_modified` that
allows you to change several properties of notation while keeping the other ones intact

.. doctest::

    >>> new_notation = notation.get_modified(c1=-1.0, c33 = 1.0)
    >>> new_notation.summary()
    custom notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are not normalized;
      * c1 = -1.0;
      * c21 = 1.0;
      * Undefined c22 factor;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * c33 = 1.0;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.


Pre-defined notations
=====================

Magnopy gives access to the predefined notations of the spin Hamiltonian from other
popular codes

.. doctest::

    >>> tb2j_notation = Notation.get_predefined("tb2j")
    >>> vampire_notation = Notation.get_predefined("vampire")
    >>> tb2j_notation.summary()
    tb2j notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are normalized to 1;
      * Undefined c1 factor;
      * c21 = -1.0;
      * c22 = -1.0;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.
    >>> vampire_notation.summary()
    vampire notation where
      * Bonds are counted multiple times in the sum;
      * Spin vectors are normalized to 1;
      * Undefined c1 factor;
      * c21 = -1.0;
      * c22 = -0.5;
      * Undefined c31 factor;
      * Undefined c32 factor;
      * Undefined c33 factor;
      * Undefined c41 factor;
      * Undefined c421 factor;
      * Undefined c422 factor;
      * Undefined c43 factor;
      * Undefined c44 factor.

To see all supported codes see :py:meth:`.Notation.get_predefined`.
