#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description="Prints the number and list of arguments")
parser.add_argument("String", type=str)
args = parser.parse_args() 

def parse(*args, **argv):
    if not args and argv:
        return "0 arguments"
    print("{}: arguments\n".format(len(argv)))
    for index, arg in enumerate(argv):
        print("{}: {}".format(index, arg))

