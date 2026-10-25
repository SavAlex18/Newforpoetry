import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY_RATE = os.getenv("API_KEY_RATE")


def convert_to_rub(transaction: dict) -> float | None:
    """
    Функция конвертации валюты из USD и EUR в рубли принимает на вход словарь с данными о транзакции
    Функция конвертации валюты из USD и EUR в рубли возвращает сумму транзакции в рублях, тип данных float
    """
    amount_api = transaction.get("operationAmount", None).get("amount", None)
    code_api = transaction.get("operationAmount", None).get("currency", None).get("code", None)
    payload = {}
    my_headers = {
        "apikey": API_KEY_RATE,
    }
    new_url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_api}&amount={amount_api}"

    response = requests.request("GET", new_url, headers=my_headers, data=payload)

    status_code = response.status_code
    if status_code == 200:
        rate = response.json()
        return rate["result"]
    return None


if __name__ == "__main__":
    trans_dict = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    print(convert_to_rub(trans_dict))
#     amount = trans_dict.get("operationAmount", None).get("amount", None)
#     code = trans_dict.get("operationAmount", None).get("currency", None).get("code", None)
#     result_dict = {
#     "success": True,
#     "query": {
#         "from": "EUR",
#         "to": "USD",
#         "amount": 1
#         },
#     "info": {
#         "timestamp": 1792819445,
#         "rate": 1.120234
#     },
#     "date": "2026-10-24",
#     "result": 1.120234
# }

#   https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1
