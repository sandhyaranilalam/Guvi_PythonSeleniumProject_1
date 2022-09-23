import json


def read_json(file):
    with open(file, 'r') as f:
        json_data = json.load(f)
        return json_data
