from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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
                "name": "USD"
             }
         }
         },
        {"id": 142264269,
         "operationAmount": {
             "currency": {
                "name": "CNY"
             }
         }
         }
    ], 'USD')
    assert next(curr_gen, None) == {"id": 142264268, "operationAmount": {"currency": {
                        "name": "USD"}}}
    assert next(curr_gen, None) is None


def test_filter_by_currency_rub():
    curr_gen = filter_by_currency([
        {"id": 142264268,
         "operationAmount": {
             "currency": {
                "name": "USD"
             }
         }
         },
        {"id": 142264269,
         "operationAmount": {
             "currency": {
                "name": "CNY"
             }
         }
         }
    ], 'RUB')
    assert next(curr_gen, None) is None
    assert next(curr_gen, None) is None
