from src.external_api import get_amount
from unittest.mock import patch


@patch('requests.get')
def test_get_amount(mock_get):
    mock_get.return_value.json.return_value = ({'result': 718136.825706})
    transaction = {
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
    assert get_amount(transaction) == 718136.825706
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={'apikey': 'GDMlx48T2gzAlrimYFXDAHY2W90b0KFe'})
