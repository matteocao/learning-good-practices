"""Tests for `hello_world` method. Catch from capsys."""
import pytest
import functions #in here, use the name is inside PYBIND11_MODULE()


def test_add():
    assert addition.add(2, 3) == 5
