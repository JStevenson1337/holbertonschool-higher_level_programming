#!/usr/bin/python3
""" Add two integers """


def add_integer(a, b=98):
    """ Add two integers

    Args:
        a (int): [Mandatory int to pass in]
        b (int): [Optional int to pass in]
    Returns:
        int: [Sum of a and b]
    """
    try:
        if isinstance(a, int):
            pass
        elif isinstance(a, float):
             a = int(a)
        else:
            raise TypeError
    except Exception:
        raise TypeError("a must be an integer")

    try:
        if isinstance(b, int):
            pass
        elif isinstance(b, float):
            b = int(b)
        else:
            raise TypeError
    except Exception:
        raise TypeError("b must be an integer")

    return a + b



print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
