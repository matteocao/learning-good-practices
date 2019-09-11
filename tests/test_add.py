"""Tests for `hello_world` method. Catch from capsys."""
import pytest
from functions import adds

def test_add():
    assert adds.add(2, 3) == 5
