import json
import logging
from pathlib import Path

Path('logs').mkdir(exist_ok=True)

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations(local_json_path: str) -> list:
    """
    Функция по строке, которая должна содержать путь к файлу json, возвращает список словарей
    если файл не найден или пустой, возвращается пустой список
    Args:str
    """
    operations = []
    filename = Path(local_json_path)
    logger.info(f'В utils передано имя файла: {filename}')
    if not filename.is_file():
        logger.error(f'{filename} не является правильным именем файла, возможно, папка, выход из utils')
        return operations
    try:
        with open(local_json_path, encoding="utf-8") as json_file:
            operations = json.load(json_file)
            logger.info(f'Файл {filename} прочитан')
            return operations
    except (FileNotFoundError, json.decoder.JSONDecodeError, OSError) as ex:
        logger.error(f'При попытке чтения {filename} как json файл, возникло исключение {ex}')
        return operations
