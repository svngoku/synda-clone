"""
Test the CLI functionality.
"""
import subprocess
import sys


def test_cli_help():
    """Test that the CLI help command works."""
    result = subprocess.run(
        [sys.executable, "-m", "synda.cli.app", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Usage:" in result.stdout
    assert "synda" in result.stdout


def test_cli_version():
    """Test that the CLI version command works."""
    result = subprocess.run(
        [sys.executable, "-m", "synda.cli.app", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0