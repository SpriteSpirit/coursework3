from src import functions as func


def test_mask_card_number():
    assert func.mask_card_number("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    assert func.mask_card_number("Visa Platinum 3530191547567121") == "Visa Platinum 3530 19** **** 7121"
    assert func.mask_card_number("МИР 2052809263194182") == "МИР 2052 80** **** 4182"
    assert func.mask_card_number("Visa Platinum 3530191547567121") == "Visa Platinum 3530 19** **** 7121"


def test_mask_account_number():
    assert func.mask_account_number("Счет 35158586384610753655") == "Счет **3655"
    assert func.mask_account_number("Счет 90417871337969064865") == "Счет **4865"
    assert func.mask_account_number("Счет 45735917297559088682") == "Счет **8682"
    assert func.mask_account_number("Счет 95782287258966264115") == "Счет **4115"


def test_mask_date():
    assert func.mask_date("2019-02-12T00:08:07.524972") == "12.02.2019"
    assert func.mask_date("2018-07-06T22:32:10.495465") == "06.07.2018"
    assert func.mask_date("2018-09-27T14:26:24.629306") == "27.09.2018"
    assert func.mask_date("2018-06-08T16:14:59.936274") == "08.06.2018"


def test_check_valid_transactions_data(file_fixture):
    assert func.check_valid_transactions_data(file_fixture) == [
        {'id': 86608620, 'state': 'EXECUTED', 'date': '2019-08-16T04:23:41.621065',
         'operationAmount': {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на счет', 'from': 'MasterCard 8826230888662405',
         'to': 'Счет 96119739109420349721'},
        {'id': 185048835, 'state': 'EXECUTED', 'date': '2019-05-06T00:17:42.736209',
         'operationAmount': {'amount': '74895.83', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 27921306202254867520',
         'to': 'Счет 49884962711830774470'},
        {'id': 422035015, 'state': 'EXECUTED', 'date': '2019-02-27T03:59:25.921176',
         'operationAmount': {'amount': '69311.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на счет', 'from': 'MasterCard 8847384717023026',
         'to': 'Счет 85458008326755993377'},
        {'id': 917824439, 'state': 'EXECUTED', 'date': '2019-07-18T12:27:13.355343',
         'operationAmount': {'amount': '82139.20', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на карту', 'from': 'Visa Platinum 6942697754917688',
         'to': 'МИР 2956603572573342'},
        {'id': 736942989, 'state': 'EXECUTED', 'date': '2019-09-06T00:48:01.081967',
         'operationAmount': {'amount': '6357.56', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Gold 3654412434951162',
         'to': 'Счет 59986621134048778289'}]


def test_get_last_transactions(file_fixture):
    assert func.get_last_transactions(3, file_fixture) == [
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        },
        {
            "id": 86608620,
            "state": "EXECUTED",
            "date": "2019-08-16T04:23:41.621065",
            "operationAmount": {
                "amount": "6004.00",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8826230888662405",
            "to": "Счет 96119739109420349721"
        },
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {
                "amount": "82139.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342"
        },
    ]