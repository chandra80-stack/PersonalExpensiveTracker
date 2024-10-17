from datetime import datetime

from com.iitk.constants.ExpConstants import REQUIRED_KEYS, DATE_FORMAT, DATE, CATEGORY, DESC, AMOUNT


def validate_exp_data(exp_data):
    is_data_valid = True
    for key in exp_data:
        if key not in REQUIRED_KEYS:
            # print("entered data is incomplete  ")
            is_data_valid = False
            break
        else:
            value = exp_data[key]
            if value is None or value == "":
                is_data_valid = False
                break
            else:
                if key == DATE:
                    if not validate_date(value):
                        is_data_valid = False
                        break
                if key == CATEGORY or DESC:
                    if not validate_str_datatype(value):
                        is_data_valid = False
                        break
                if key == AMOUNT:
                    if not validate_int_datatype(value):
                        is_data_valid = False
                        break

    return is_data_valid


def validate_date(date_string):
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_str_datatype(input_value):
    if isinstance(input_value, str):
        return True
    else:
        return False


def validate_int_datatype(input_value):
    try:
        if isinstance(int(input_value), int):
            return True
        else:
            return False
    except ValueError:
        return False
