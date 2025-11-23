"""CLI module for pytest_http_vcr."""

from argparse import ArgumentParser

from pytest_http_vcr._version import __version__


def generate_cli_parser() -> ArgumentParser:
    """Generate the argument parser for the pytest_http_vcr CLI."""
    parser = ArgumentParser(
        description="A pytest plugin that records and replays all "
        "HTTP interactions using a VCR-style cassette and a local HTTP server."
    )
    parser.add_argument("--version", action="version", version=__version__)
    return parser


def main() -> None:
    """Entry point for the pytest_http_vcr command-line interface."""
    parser = generate_cli_parser()
    _ = parser.parse_args()
