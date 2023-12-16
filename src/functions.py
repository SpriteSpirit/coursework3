import json


def get_all_transactions(filename: str) -> list:
    """
    Получает все транзакции в виде списка.
    :param filename: Путь к файлу json.
    :return: Все транзакции из файла json.
    """
    with open(filename) as file:
        json_data = json.load(file)
        return json_data
