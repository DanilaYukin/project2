import json


def get_transaction_list(my_file: str) -> list:
    """Функция принимает на вход путь к файлу в формате json и возвращает список"""
    try:
        with open(my_file, 'r', encoding="utf-8") as f:
            try:
                transaction_list = json.load(f)
                if transaction_list == []:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    return transaction_list


if __name__ == '__main__':
    print(get_transaction_list("..\\data\\operations.json"))
