#!/usr/bin/python3

def safe_print_division(a, b):
    while True:
        try:
            result = a / b
            break
        except ZeroDivisionError:
            break
        finally:
            if b == 0:
                print("Inside result: {}".format(None))
            else:
                print("Inside result: {}".format(a/b))
            

