from .projectfolder import numby
from .projectfolder import stringy
from .projectfolder import static

def test_functions_numby_add():
    assert numby.add(3, 4) == 7

def test_functions_stringy_hello():
    assert stringy.hello() == "Hello, world!"

def test_functions_static_add_int():
    assert static.add_int(1, 1) == 2
