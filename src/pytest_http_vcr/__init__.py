"""A pytest plugin that records and replays all HTTP interactions using a VCR-style cassette and a local HTTP server."""

from pytest_http_vcr.cli import main

from pytest_http_vcr.core import __version__

__all__ = ["__version__", "main"]
