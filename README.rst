.. -*- mode: rst -*-

|Travis|_ |PyPi|_ 

.. |Travis| image:: https://api.travis-ci.org/matteocao/learning-good-practices.svg?branch=master
.. _Travis: https://travis-ci.org/matteocao/learning-good-practices



learning-good-practices
=======================


This repo contains a simple, fully functional architecture of an hypothetical python package. Useful for learning the basics.

The *documentation* can be found here: <https://learning-good-practices.readthedocs.io/en/latest/>

The PyPI version can be found here: <https://test.pypi.org/project/py-lgp/0.0.1/>.

To update the PyPI version, first build it

.. code-block:: python

   python setup.py sdist bdist_wheel


And then upload it to PyPI:

.. code-block:: bash

   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
