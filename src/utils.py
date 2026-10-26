import json
from pathlib import Path


def get_operations(local_json_path: str) -> list:
    """
    Функция по строке, которая должна содержать путь к файлу json, возвращает список словарей
    если файл не найден или пустой, возвращается пустой список
    Args:str
    """
    operations = []
    filename = Path(local_json_path)
    if not filename.is_file():
        return operations
    try:
        with open(local_json_path, encoding="utf-8") as json_file:
            operations = json.load(json_file)
            return operations
    except (FileNotFoundError, json.decoder.JSONDecodeError, OSError):
        return operations
