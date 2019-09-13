"""Tests for `hello_world` method. Catch from capsys."""
import pytest
from functions import hello_world


def test_hello_world(capsys):
    """Correct `name` argument prints"""
    hello_world("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out


def test_hello_world_exc(capsys):
    """Correct type for `name`"""
    with pytest.raises(TypeError):
        assert hello_world.hello_world(1)
