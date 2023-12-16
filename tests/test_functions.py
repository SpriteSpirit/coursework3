from src import functions as func


def test_mask_card_number():
    assert func.mask_card_number("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    assert func.mask_card_number("Visa Platinum 3530191547567121") == "Visa Platinum 3530 19** **** 7121"
    assert func.mask_card_number("МИР 2052809263194182") == "МИР 2052 80** **** 4182"
    assert func.mask_card_number("Visa Platinum 3530191547567121") == "Visa Platinum 3530 19** **** 7121"

