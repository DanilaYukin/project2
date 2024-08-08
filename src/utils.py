import json
import logging
import pandas as pd

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_list(my_file: str) -> list:
    """Функция принимает на вход путь к файлу в формате json и возвращает список"""
    try:
        logger.info("Открываем файл")
        with open(my_file, "r", encoding="utf-8") as f:
            try:
                transaction_list = json.load(f)
                if transaction_list == []:
                    return []
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка: {ex}")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []

    return transaction_list


def xls_open(my_file):
    """Открывает excel файл"""
    df = pd.read_excel(my_file)
    return df.to_dict()


def csv_open(my_file):
    """Открывает csv файл"""
    df = pd.read_csv(my_file)
    return df.to_dict()


def json_open(my_file):
    """Открывает json файл"""
    with open(my_file, 'r') as file:
        date = json.load(file)
        return date


if __name__ == "__main__":
    print(get_transaction_list("../data\\operations.json"))
    print(xls_open("../data/transactions_excel.xlsx"))
    print(csv_open("../data/transactions.csv"))
