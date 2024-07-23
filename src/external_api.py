import os

import requests
from dotenv import load_dotenv


def convert_to_rub(amount, currency):
    """Функция принимает на вход транзакцию и возвращает ее сумму"""
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        load_dotenv()

        api_token = os.getenv("API_KEY")
        headers = {"apikey": api_token}
        response = requests.get(url, headers=headers)
        return response.json()["result"]
    else:
        return amount


if __name__ == "__main__":
    print(convert_to_rub(20, "USD"))
