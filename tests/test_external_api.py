from src.external_api import convert_to_rub
from unittest.mock import patch


@patch('requests.get')
def test_covert_to_rub(mock_get):
    mock_get.retur_value.json.return_value = ({'result': 60})
    assert convert_to_rub(20, 'USD')
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20", headers={'apikey': 'GDMlx48T2gzAlrimYFXDAHY2W90b0KFe'})
