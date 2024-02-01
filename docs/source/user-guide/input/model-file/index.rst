.. _user-guide_input_model-file:

*******************************
Specification of the model file
*******************************

* File is read assuming |utf-8|_ encoding (works with almost all plain text files).
* All blank lines are ignored. Line is considered to be blank if there are no other
  characters but any number of spaces (U+0020).
* Character ``#`` (U+0023) is reserved for comments. If it is read then all symbols until
  the next line symbol are ignored. Comments can appear anywhere, even inside a section
  provided that they do not break the format once they are removed. An example for the
  "Cell" section is provided below

  .. code-block:: text
    :linenos:

    ==========
    # Comment line
    Cell <Units> <Scale>
    a_x a_y a_z # Inline comment
    b_x b_y b_z
    # Comment line
    c_x c_y c_z
    ==========

* Sections are separated by 10 or more consecutive ``=`` (U+003D) symbols.
* Subsections inside each section are separated by 10 or more ``-`` (U+002D) symbols.
* All keywords are case-insensitive.
* Keywords can not contain spaces.
* Sections
  :ref:`user-guide_input_model-file_cell`,
  :ref:`user-guide_input_model-file_atoms`,
  :ref:`user-guide_input_model-file_notation`
  are required.
* At least one of the sections
  :ref:`user-guide_input_model-file_exchange`,
  :ref:`user-guide_input_model-file_on-site`
  is required.
* Section :ref:`user-guide_input_model-file_ground-state` is optional.

Each section is described in details below.

.. note::
  If keyword name is enclosed as <keyword>, then it is optional.


.. include:: cell.inc

.. include:: atoms.inc

.. include:: notation.inc

.. include:: ground-state.inc

.. include:: exchange.inc

.. include:: on-site.inc
