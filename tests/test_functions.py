"""
Tests all functions in pycorset.functions.
"""
from pycorset.functions import numby
from pycorset.functions import stringy
from pycorset.functions import typed


def test_numby_add():
    """
    Tests, if numby.add adds two numbers.
    """
    assert numby.add(3, 4) == 7


def test_stringy_hello():
    """
    Tests, if string.hello returns "Hello, world".
    """
    assert stringy.hello() == "Hello, world!"


def test_typed_add_int():
    """
    Tests, if static.add_int adds numbers.
    """
    assert typed.add_int(1, 1) == 2
