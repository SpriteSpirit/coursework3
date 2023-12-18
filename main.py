from src.functions import *

if __name__ == '__main__':
    all_data = get_all_transactions('src/operations.json')
    valid_data = get_last_transactions(5, check_valid_transactions_data(all_data))
    display_last_transactions(valid_data)
