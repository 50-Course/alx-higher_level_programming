#!/usr/bin/python3
'''
file: 6-from_json_string.py
functions:
-> from_json_string
'''

import json


def from_json_string(my_str):
    ''' returns an object represented by a JSON string '''

    return json.loads(my_str)
