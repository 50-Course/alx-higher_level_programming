#!/usr/bin/python3
"""
Creates an object from a JSON file

Functions:
    - load_from_json
"""
import json


def load_from_json_file(filename):
    """ Loads object from JSON file."""

    with open(filename) as file:
        return json.load(file)
