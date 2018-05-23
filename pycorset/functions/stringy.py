def hello():
    """
    Returns the str "Hello, world!".

    >>> hello()
    'Hello, world!'
    """
    return "Hello, world!"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
