import csv
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
    if os.path.isfile(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as csvfile:
                list_transactions = list(csv.DictReader(csvfile))
                return list_transactions
        except csv.Error:
            return list_transactions
    else:
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
