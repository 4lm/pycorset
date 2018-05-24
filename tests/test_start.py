"""
Tests start.py in pycorset.
"""
from pycorset import start

def test_pycorset_start():
    """
    Tests, if startmain works an returns None.
    """
    assert start.main() is None
