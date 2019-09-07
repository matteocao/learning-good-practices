"""Tests for `hello_world` method."""
import pytest
from functions import hello_world


def test_hello_world(capsys):
    """Correct name argument prints"""
    hello_world("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out