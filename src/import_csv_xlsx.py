import os

import pandas as pd


def get_transactions_csv(csv_path: str) -> list[dict]:
    """
    Функция возвращает список словарей финансовых операций.Если файл не найден, список пустой.
    На входе - путь к файлу csv
    :param csv_path:
    :return:[dict]
    """
    list_transactions = []
    if not os.path.isfile(csv_path):
        return list_transactions

    try:
        df = pd.read_csv(csv_path, sep=";")
        list_transactions = df.to_dict(orient="records")
        return list_transactions
    except Exception:
        return list_transactions


def get_transactions_xlsx(xlsx_path: str) -> list[dict]:
    """Фунункция получает на вход путь к имени xlsx файла. Возвращает список словарей опреаций
    :param xlsx_path:
    :return:[dict]
    """
    list_transactions = []
    if not os.path.isfile(xlsx_path):
        return list_transactions

    try:
        df = pd.read_excel(xlsx_path)
        list_transactions = df.to_dict(orient="records")
        return list_transactions
    except Exception:
        return []
