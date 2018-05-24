from .projectfolder import start

def test_pycorset_start():
    assert start.main() == None
