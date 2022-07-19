#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (TypeError, ValueError, ZeroDivisionError, Exception):
        return None
    finally:
        print("{:2f}".format(result))

    return result
