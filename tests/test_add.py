"""Tests for `hello_world` method. Catch from capsys."""
import pytest
import addition


def test_add():
    assert addition.add(2, 3) == 5
