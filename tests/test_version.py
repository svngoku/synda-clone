"""
Test the version attribute of the Synda package.
"""
import re

import synda


def test_version():
    """Test that the version attribute exists and has the correct format."""
    assert hasattr(synda, "__version__")
    assert isinstance(synda.__version__, str)
    assert re.match(r"^\d+\.\d+\.\d+$", synda.__version__)