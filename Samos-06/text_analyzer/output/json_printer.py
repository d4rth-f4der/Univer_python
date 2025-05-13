import json

def print_json(stats: dict):
    json_output = json.dumps(stats, indent=4, ensure_ascii=False)

    print(json_output)