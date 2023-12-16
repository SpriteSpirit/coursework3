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


def format_transactions(transaction: dict) -> str:
    """
    Форматирует все данные в заданном формате и подготавливает их к выводу.
    :param transaction: Валидная транзакция в виде словаря.
    :return: Отформатированный вывод информации по транзакции по указанному шаблону.
    """
    date = mask_date(transaction['date'])
    description = transaction['description']

    mask_account_from = mask_account_number(transaction['from'])
    mask_card_from = mask_card_number(transaction['from'])
    _from = mask_account_from if 'Счет' in transaction['from'] else mask_card_from

    mask_account_to = mask_account_number(transaction['to'])
    mask_card_to = mask_card_number(transaction['to'])
    _to = mask_account_to if 'Счет' in transaction['to'] else mask_card_to

    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['name']

    return (f"{date} {description}\n"
            f"{_from} -> {_to}\n"
            f"{amount} {currency}\n")


def check_valid_transactions_data(transactions_list: list) -> list:
    """
    Делает сортировку данных по заданным параметрам.
    :param transactions_list: Список всех транзакций.
    :return: Отсортированный и валидный список транзакций.
    """
    transfer_transaction = [
        transaction for transaction in transactions_list
        if transaction.get('state') == 'EXECUTED' and
        all(key in transaction for key in ('date', 'from', 'to', 'description')) and
        'operationAmount' in transaction and
        all(key in transaction['operationAmount'] for key in ('amount', 'currency')) and
        'name' in transaction['operationAmount']['currency']
    ]

    return transfer_transaction
