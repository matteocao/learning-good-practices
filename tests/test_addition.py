"""Tests for `addition.add` method. Catch from capsys."""
import pytest
import addition #the name is inside PYBIND11_MODULE()


def test_add():
    assert addition.add(2, 3) == 5
