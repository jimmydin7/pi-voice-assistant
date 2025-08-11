import json


CONFIG_PATH = "data/config.json"

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

ASSISTANT_NAME = config.get('name')

