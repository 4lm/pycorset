def add(a, b):
    """
    Adds to numbers.

    Args:
        param1 (int): The first number.
        param2 (int): The second number.

    Returns:
        int: The sum of param1 and param2

    >>> add(1, 3)
    4
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
