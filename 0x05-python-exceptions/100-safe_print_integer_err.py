#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as inst:
        sys.stderr.write("Exception: {}".format(inst))
        return False
    else:
        return True

    print()
