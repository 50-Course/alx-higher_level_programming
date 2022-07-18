#!/bin/python3
import typing

def safe_print_integer(value: typing.Any) -> bool:
   try:
       if isinstance(value, int):
           return True
       else:
           return False
   except ValueError:
       raise
