import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def test_card_number_generator():
    card_gen = card_number_generator(100, 102)
    assert next(card_gen, None) == '0000 0000 0000 0100'
    assert next(card_gen, None) == '0000 0000 0000 0101'
    assert next(card_gen, None) == '0000 0000 0000 0102'
    assert next(card_gen, None) is None

    card_gen = card_number_generator(9999999999999998, 9999999999999999)
    assert next(card_gen, None) == '9999 9999 9999 9998'
    assert next(card_gen, None) == '9999 9999 9999 9999'
    assert next(card_gen, None) is None
    assert next(card_gen, None) is None


def test_transaction_descriptions():
    desc_gen = transaction_descriptions([{"description": "Перевод со счета на счет"},
                                         {"description": "Перевод организации"}])
    assert next(desc_gen, None) == 'Перевод со счета на счет'
    assert next(desc_gen, None) == 'Перевод организации'
    assert next(desc_gen, None) is None


def test_filter_by_currency_usd():
    curr_gen = filter_by_currency([
        {"id": 142264268,
         "operationAmount": {
             "currency": {
                "code": "USD"
             }
         }
         },
        {"id": 142264269,
         "operationAmount": {
             "currency": {
                "code": "CNY"
             }
         }
         }
    ], 'USD')
    assert next(curr_gen, None) == {"id": 142264268, "operationAmount": {"currency": {
                        "code": "USD"}}}
    assert next(curr_gen, None) is None


def test_filter_by_currency_rub():
    curr_gen = filter_by_currency([
        {"id": 142264268,
         "operationAmount": {
             "currency": {
                "code": "USD"
             }
         }
         },
        {"id": 142264269,
         "operationAmount": {
             "currency": {
                "code": "CNY"
             }
         }
         }
    ], 'RUB')
    assert next(curr_gen, None) is None
    assert next(curr_gen, None) is None


def test_filter_by_currency_eur():
    eur_gen = filter_by_currency(transactions, currency="EUR")
    assert next(eur_gen, None) is None


def test_transaction_descriptions_fix(param_description):
    desc_gen = transaction_descriptions(transactions)
    assert next(desc_gen, None) == param_description[0]
    assert next(desc_gen, None) == param_description[1]
    assert next(desc_gen, None) == param_description[2]
    assert next(desc_gen, None) == param_description[3]
    assert next(desc_gen, None) == param_description[4]
    assert next(desc_gen, None) is None

