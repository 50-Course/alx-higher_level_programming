#!/usr/bin/python3
"""
Returns JSON representation of a string

Functions:
    - to_json_string
"""


def to_json_string(my_obj):
    if my_obj is not None:
        import json

        text = json.dumps(my_obj)
    return text
