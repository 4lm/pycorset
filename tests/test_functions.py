"""
Tests all functions in pycorset.functions.
"""
from pycorset.functions import numby
from pycorset.functions import stringy
from pycorset.functions import static


def test_functions_numby_add():
    """
    Tests, if numby.add adds two numbers.
    """
    assert numby.add(3, 4) == 7


def test_functions_stringy_hello():
    """
    Tests, if string.hello returns "Hello, world".
    """
    assert stringy.hello() == "Hello, world!"


def test_functions_static_add_int():
    """
    Tests, if static.add_int adds numbers.
    """
    assert static.add_int(1, 1) == 2
