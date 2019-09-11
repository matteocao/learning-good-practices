"""Tests for `hello_world` method. Catch from capsys."""
import pytest
from functions import add

def test_add():
    assert add.add(2, 3) == 5
