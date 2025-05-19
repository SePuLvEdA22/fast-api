import json

def load_json():
    with open('./data/data.json', 'r') as file:
        data = json.load(file)
        return data