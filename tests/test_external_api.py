# import json
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_to_rub

trans_dict = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}
result_dict = {
    "success": True,
    "query": {
        "from": "EUR",
        "to": "USD",
        "amount": 1
        },
    "info": {
        "timestamp": 1792819445,
        "rate": 1.120234
    },
    "date": "2026-10-24",
    "result": 1.120234
}

@patch('requests.request')
def test_convert_to_rub():
    mock_request = Mock()
    requests.request = mock_request
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = result_dict
    assert convert_to_rub(trans_dict) == 1.120234


@patch('requests.request')
def test_convert_to_rub_fail(mock_request):
    mock_request.return_value.status_code = 400
    # mock_request.return_value.json.return_value = result_dict
    assert convert_to_rub(trans_dict) is None
