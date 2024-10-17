from datetime import datetime

from com.iitk.validation.DataValidation import validate_date, validate_int_datatype


def calc_exp_by_month(exp_list):
    ds_monthly_exp = {}
    for ds in exp_list:
        yyyy_mm_dd_date = ds['date']
        if validate_date(yyyy_mm_dd_date):
            date_object = datetime.strptime(yyyy_mm_dd_date, "%Y-%m-%d")
            yyyy_mm_date = str(date_object.year) + "-" + str(date_object.month)
            if validate_int_datatype(ds['amount']):
                if yyyy_mm_date in ds_monthly_exp:
                    ds_monthly_exp[yyyy_mm_date] = ds_monthly_exp[yyyy_mm_date] + int(ds['amount'])
                else:
                    ds_monthly_exp[yyyy_mm_date] = int(ds['amount'])
    return ds_monthly_exp