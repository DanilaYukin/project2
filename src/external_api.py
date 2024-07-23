import os

import requests
from dotenv import load_dotenv


def get_amount(transaction, cur):
    """Функция принимает на вход транзакцию и возвращает ее сумму"""

    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur}&from={currency}&amount={amount}"

        load_dotenv()

        api_token = os.getenv("API_KEY")
        headers = {"apikey": api_token}
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        print(f"Статус код {status_code}")
        return response.json()['result']
    else:
        return amount


if __name__ == '__main__':
    print(get_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
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
        }))
