def filter_by_state(dictionary_list: list[dict : str | int], state: str = "EXECUTED") -> list[dict : str | int]:
    """Функция принимает на вход список словарей и возвращает новый список
    в котором state соответсвует принимаемому значению"""
    new_list = []

    for i in dictionary_list:
        if i.get("state") == state:
            new_list.append(i)

    return new_list


def sort_by_date(original_list: list[dict : str | int], reverse_list: bool = True) -> list[dict : str | int]:
    """Функция принимает на вход список словарей и возвращает список
    отсортированный по убыванию date даты"""
    new_dict_list = sorted(original_list, key=lambda original_list: original_list["date"], reverse=reverse_list)
    return new_dict_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
