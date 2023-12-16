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


def mask_card_number(card_number: str) -> str:
    """
    Создает маску-шаблон для скрытия номера карты.
    :param card_number: Номер карты с указанием платежной системы.
    :return: Маска номера карты по заданному шаблону.
    """
    return f"{card_number[:-16]}{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Создает маску-шаблон для скрытия номера счета.
    :param account_number: Номер счета, включая слово Счет.
    :return: Маска номера счета по заданному шаблону.
    """
    return f"{account_number[:-20]}**{account_number[-4:]}"


def mask_date(date: str) -> str:
    """
    Создает маску-шаблон для вывода даты по заданному формату.
    :param date: Дата транзакции вместе со временем.
    :return: Отформатированная дата по шаблону ДД.ММ.ГГГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"