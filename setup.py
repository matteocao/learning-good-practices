from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="functions",
    version="0.0.1",
    author="Matteo Caorsi",
    author_email="matteocao@gmail.com",
    license="Apache License 2.0",
    description="A package to learn to set up a git repo",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/matteocao/learning-good-practices",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
    ],
)