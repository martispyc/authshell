import json

def load(database="../data/data_main.json", text=True, formatted=False):
    with open(database) as f: return json.load(f)
    