"""
Entry point of this example application.
"""
from pycorset.functions.numby import add
from pycorset.functions.stringy import hello
from pycorset.functions.static import add_int


def main() -> None:
    """
    Prints the return value of some functions.
    """
    print(add(1, 2))
    print(add_int(1, 2.5))
    print(hello())


if __name__ == "__main__":
    main()
