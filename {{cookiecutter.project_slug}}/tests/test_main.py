"""Tests for the main module."""

import pytest
from {{ cookiecutter.project_slug }}.main import hello_world


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert isinstance(result, str)
    assert "{{ cookiecutter.project_name }}" in result
    assert "Hello, World" in result


def test_hello_world_not_empty():
    """Test that hello_world returns a non-empty string."""
    result = hello_world()
    assert result.strip() != ""
