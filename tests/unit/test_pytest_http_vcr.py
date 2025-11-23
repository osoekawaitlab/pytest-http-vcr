"""Unit tests for pytest_http_vcr exports."""

import re

import pytest_http_vcr


def test_pytest_http_vcr_exports_version() -> None:
    """Test that pytest_http_vcr exports the correct version."""
    assert re.match(r"^\d+\.\d+\.\d+$", pytest_http_vcr.__version__)
