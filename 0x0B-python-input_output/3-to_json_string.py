#!/usr/bin/python3
"""
Returns JSON representation of a string

Functions:
    - to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Converts python object to a JSON representation

    Returns:
        JSON
    """
    if my_obj:
        text = json.dumps(my_obj)
    return text
