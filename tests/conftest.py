import pytest


@pytest.fixture
def file_fixture():
    return [
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
            "id": 185048835,
            "state": "EXECUTED",
            "date": "2019-05-06T00:17:42.736209",
            "operationAmount": {
                "amount": "74895.83",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 27921306202254867520",
            "to": "Счет 49884962711830774470"
        },
        {
            "id": 422035015,
            "state": "EXECUTED",
            "date": "2019-02-27T03:59:25.921176",
            "operationAmount": {
                "amount": "69311.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8847384717023026",
            "to": "Счет 85458008326755993377"
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
    ]


@pytest.fixture
def valid_data():
    return [
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
