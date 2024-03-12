.. _user-guide_installation:

************
Installation
************

Requirement for Magnopy installation are:

* |Python|_ (>=3.8)
* |NumPy|_
* |Wulfric|_ (>=0.3)

Most likely you already have Python installed on your machine
(if not check these links: |Python-installation|_).

Magnopy can be installed with :ref:`pip <installation-pip>`
or from :ref:`source <installation-source>`.

Check Python
============

The easiest way to check if you have python installed
is to run the following command in your terminal:

.. code-block:: console

   python

If you see something like that, then you have python installed:

.. code-block:: console

   Python 3.10.9 (main, Dec 15 2022, 18:25:35) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

In most cases ``python`` command launches python3,
however if it launches python2,
then you may need to use ``python3`` instead
(and ``pip3`` instead of ``pip`` in the following).

.. hint::
   Use ``exit()`` or press ctrl+D to close the python console.

.. _installation-pip:

pip
===

To install Magnopy, run (you may need to use ``pip3``):

.. code-block:: console

   pip install magnopy

.. _installation-source:

Installing from source
======================

* Clone the project to your local computer:

.. code-block:: python

   git clone https://github.com/magnopy/magnopy.git

* Change the directory:

.. code-block:: python

   cd magnopy

* To install Magnopy, run (you may need to use ``pip3``):

.. code-block:: console

   pip install magnopy

Update
======

If you want to update the package to the latest available version (|version|)
type the following in your terminal (you may need to use ``pip3``):

.. code-block:: console

   pip install magnopy --upgrade
