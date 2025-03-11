.. _user-guide_input_model-file:

*******************************
Specification of the model file
*******************************

The model file is a file that contains all the information about the spin Hamiltonian
It is intendant to describe the structure of the crystal (cell and atoms) and the
parameters (bilinear exchange, on-site anisotropy, etc.) of the spin Hamiltonian.

The model file of magnopy can be a .txt file or an .hdf5 file.
The .txt file is a plain text file with a specific format. The .hdf5 file is a binary file
with a specific structure. These two files are designed to be completely interchangeable in
the context of magnopy. Magnopy by itself offers a conversion from one format to another.

We suggest to use |myHDF5|_ web-site to browse the content of the .hdf5 file.

Rules for the .hdf5 file
========================

* One full .txt file corresponds to the group in .hdf5 file with the attribute "type"
  set to the value "SpinHamiltonian". In this guide we reference this root group as
  "spinham/"
* All dataset's, group's, and attributes's **names** are lowercase
  (i.e "units", "spinham", "cell", ...).


Rules for the .txt file
=======================

* File is read assuming |utf-8|_ encoding (works with almost all plain text files).
* All blank lines are ignored. Line is considered to be blank if there are no other
  characters but any number of spaces (U+0020).
* Character ``#`` (U+0023) is reserved for comments. If it is read then all symbols until
  the next line symbol are ignored. Comments can appear anywhere, even inside a section
  provided that they do not break the format once they are removed. An example for the
  "Cell" section is provided below

  .. code-block:: text
    :linenos:

    ============================
    # Comment line
    Cell <Units> <Scale>
    a_x a_y a_z # Inline comment
    b_x b_y b_z
    # Comment line
    c_x c_y c_z
    ============================

* Sections are separated by 10 or more consecutive ``=`` (U+003D) symbols.
* Subsections inside each section are separated by 10 or more ``-`` (U+002D) symbols.
* All keywords are case-insensitive.
* Keywords can not contain spaces.

Rules for both files
====================
* Sections
  :ref:`user-guide_input_model-file_cell`,
  :ref:`user-guide_input_model-file_atoms`,
  are required. Other sections are optional.
* Section :ref:`user-guide_input_model-file_notation` is required if section
  :ref:`user-guide_input_model-file_exchange` or :ref:`user-guide_input_model-file_on-site`
  is present.



.. include:: cell.inc

.. include:: atoms.inc

.. include:: notation.inc

.. include:: spiral-vector.inc

.. include:: cone-axis.inc

.. include:: exchange.inc

.. include:: on-site.inc


Full specification reference
============================

.txt file
---------

.. literalinclude:: full-txt.inc
  :language: text

.hdf5 file
----------

.. literalinclude:: full-hdf5.inc
  :language: text
