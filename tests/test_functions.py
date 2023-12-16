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


