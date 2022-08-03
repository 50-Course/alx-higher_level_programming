#!/usr/bin/python3
"""
File: Saves object to Text file in JSON format

Functions:
    - save_to_json_file
"""
import json


def save_to_json_file(my_obj, file_name):
    """Saves JSON object to an output file"""

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
    f.close()
