from .projectfolder import numby
from .projectfolder import stringy

def test_functions_numby_add():
    assert numby.add(3,4) == 7

def test_functions_stringy_hello():
    assert stringy.hello() == "Hello, world!"
