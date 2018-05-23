from pycorset.functions import add
from pycorset.functions import hello
from pycorset.functions import add_int

def main() -> None:
    print(add(1, 2))
    print(add_int(1, 2.5))
    print(hello())

if __name__ == "__main__":
    main()
