import re

from collections import defaultdict


def sort_str(filtered_transactions: list[dict], word: str) -> list[dict]:
    found_operations = []
    for operation in filtered_transactions:
        if re.search(word, operation.get("description", "")):
            found_operations.append(operation)
            filtered_transactions = found_operations
        return filtered_transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""

    category_count = defaultdict(int)

    for transaction in transactions_list:
        description = transaction.get("description", "").lower()
        for category in categories:
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1
    return dict(category_count)
