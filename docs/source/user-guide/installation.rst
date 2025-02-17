.. _user-guide_installation:

************
Installation
************

Requirement for magnopy installation are:

* |Python|_ (>=3.9)

And several libraries:

.. literalinclude:: ../../../requirements.txt


Magnopy can be installed with :ref:`pip <user-guide_installation_pip>` or from
:ref:`source <user-guide_installation_source>`.

Do you have Python?
===================

Most likely Python is already installed on your machine (if not check these links:
|Python-installation|_).

The easiest way to check if you have python installed is to run the following command in
your terminal::

  python

If you see something like::

  Python 3.10.9 (main, Dec 15 2022, 18:25:35) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

then you have it.

In most cases ``python`` command launches python3, however if it launches python2, then
you may need to use ``python3`` instead (and ``pip3`` instead of ``pip`` in the following).

.. hint::
  Use ``exit()`` or press ``ctrl+D`` to close python console.

.. _user-guide_installation_pip:

Installation with pip
=====================

To install magnopy use the command (you may need to use ``pip3``)::

  pip install magnopy

.. _user-guide_installation_source:

Installation from source
========================

* Clone the project to your local computer::

    git clone git@github.com:magnopy/magnopy.git

* Change the directory::

    cd magnopy

* Install the requirements::

    pip install -r requirements.txt

* To install magnopy, run (you may need to use ``pip3``)::

    pip install .

Update
======

If you want to update the package to the latest available version (|version|),
then use the command (you may need to use ``pip3``)::

  pip install magnopy --upgrade
