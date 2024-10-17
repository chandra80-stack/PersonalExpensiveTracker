import calendar

from com.iitk.constants.ExpConstants import DATE_PROMPT, CATEGORY_PROMPT, AMOUNT_PROMPT, DESC_PROMPT, ERROR_INCOMPLETE
from com.iitk.utils.ExpCalculation import calc_exp_by_month
from com.iitk.utils.FileOprationsUtil import save_file
from com.iitk.validation.DataValidation import validate_exp_data


# Function to add the personal expansive details in the form of dictionary
def add_expense():
    date_exp = input(DATE_PROMPT)
    category = input(CATEGORY_PROMPT)
    spend_amount = input(AMOUNT_PROMPT)
    description = input(DESC_PROMPT)
    ds = {'date': date_exp, 'category': category.lower(), 'amount': spend_amount, 'description': description.lower()}
    return ds


# Function to view and validate the personal expansive details
def view_expense(expensive_list):
    for exp_data in expensive_list:
        print(exp_data)
        if not validate_exp_data(exp_data):
            print(ERROR_INCOMPLETE)


# Function to Tract the personal expansive details and display warning message if budget is exceeded and
# display the information if any balance is available
def track_budget(exp_list):
    exp_limit_per_month = int(input("Enter the total amount they want to budget for the month :"))
    ds_monthly_exp = calc_exp_by_month(exp_list)
    for key in ds_monthly_exp:
        year_month = key.split("-")
        if ds_monthly_exp[key] > exp_limit_per_month:
            print("You have exceeded your budget! for the month of", calendar.month_name[int(year_month[1])], "in year",
                  year_month[0])
        elif ds_monthly_exp[key] < int(exp_limit_per_month):
            exp_balance = exp_limit_per_month - ds_monthly_exp[key]
            print("You have", exp_balance, "left balance for the month of", calendar.month_name[int(year_month[1])],
                  "in year", year_month[0])


# Save the entered personal expansive details in csv file for future use
def save_expense(exp_list):
    csv_file_path = save_file(exp_list)
    if csv_file_path:
        print(f"Data saved to {csv_file_path}")
    else:
        print("No data to Save")

