.. -*- mode: rst -*-

|Travis|_ |Documentation|_ |Azure|_

.. |Travis| image:: https://api.travis-ci.org/matteocao/learning-good-practices.svg?branch=master
.. _Travis: https://travis-ci.org/matteocao/learning-good-practices

.. |Documentation| image:: https://readthedocs.org/projects/learning-good-practices/badge/?version=latest
.. _Documentation: https://learning-good-practices.readthedocs.io/en/latest/

.. |Azure| image:: https://dev.azure.com/matteocaorsi/matteocao/_apis/build/status/matteocao.learning-good-practices?branchName=master
.. _Azure: https://dev.azure.com/matteocaorsi/matteocao/_apis/build/status/matteocao.learning-good-practices


Binder compatible
=================

The `requirements.txt` file specifies the dependencies needed for the example. Just click on the icon:
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/matteocao/learning-good-practices/master?filepath=examples%2Fsimple.ipynb


learning-good-practices
=======================


This repo contains a simple, fully functional architecture of an hypothetical python package. Useful for learning the basics.

The *documentation* can be found here: <https://learning-good-practices.readthedocs.io/en/latest/>

The *PyPI version* can be found here: <https://test.pypi.org/project/py-lgp/0.0.1/>.

To update the PyPI version, first build it

.. code-block:: python

   python setup.py sdist bdist_wheel



And then upload it to PyPI:

.. code-block:: bash

   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
