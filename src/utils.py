import json
from pathlib import Path

def get_operations(json_path: str) -> dict:
    operations = list()
    filename = Path(json_path)
    if not filename.is_file():
        return operations

    try:
        with open(json_path, encoding='utf-8') as json_file:
            operations = json.load(json_file)
            return operations
    except(FileNotFoundError, json.decoder.JSONDecodeError,OSError):
        return []






if __name__ == '__main__':
    json_path = './data/operations.json'
    print(get_operations(json_path))

    ...