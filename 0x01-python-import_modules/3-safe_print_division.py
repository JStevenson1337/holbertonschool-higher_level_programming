#!/usr/bin/python3


def safe_print_division(a, b):
    while True:
        try:
            a / b
            break
        except ZeroDivisionError:
            break
        finally:
            if b != 0:
                print("Inside result: {}".format(a / b))
                return (a / b)
            else:
                print("Inside result: {}".format(None))
