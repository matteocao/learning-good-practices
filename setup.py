import os
import re
import sys
import platform
import subprocess

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion
from pybind11 import get_include

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]


setup(
    name="py-lgp",
    version="0.0.1",
    author="Matteo Caorsi",
    author_email="matteocao@gmail.com",
    license="Apache License 2.0",
    description="A package to learn to set up a git repo and CI/CD",
    long_description=readme,
    long_description_content_type="text/rst",
    url="https://github.com/matteocao/learning-good-practices",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
	"Operating System :: OS Independent",
    ],
    ext_modules=[
        Extension(
            'addition',['functions/main.cpp'],
            include_dirs=[get_include()],
            language='c++',
            extra_compile_args=['-std=c++11']
        )
    ],
    cmdclass={'build_ext':build_ext}
)
