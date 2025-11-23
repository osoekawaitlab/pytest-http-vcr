"""End-to-end tests for pytest_http_vcr."""

import re
import subprocess


def test_pytest_http_vcr_prints_version() -> None:
    """Test that pytest_http_vcr prints the version."""
    result = subprocess.run(
        ["pytest_http_vcr", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert re.match(r"^\d+\.\d+\.\d+$", result.stdout.strip())
