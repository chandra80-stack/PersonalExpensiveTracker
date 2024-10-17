import com.iitk.service.ExpensiveServiceProcessor as exp_service
from com.iitk.constants.ExpConstants import PRINT_MANU, PRINT_ADD_EXP, PRINT_VIEW_EXP, PRINT_TRACK_EXP, PRINT_SAVE_EXP, \
    PRIN_EXIT, ENTER_CHOICE
from com.iitk.utils.FileOprationsUtil import load_file


# Function to display an interactive menu to prompt the user for expense details
def print_menu():
    print("\n", PRINT_MANU)
    print(PRINT_ADD_EXP)
    print(PRINT_VIEW_EXP)
    print(PRINT_TRACK_EXP)
    print(PRINT_SAVE_EXP)
    print(PRIN_EXIT)


# Function to execute the appropriate functionality based on the user input
def execute_expensive_menu():
    # Loading the CSV file details to list
    exp_list = load_file()
    if not exp_list:
        exp_list = []

    # Looping the menu till user enter exit option
    while True:
        print_menu()
        choice = input(ENTER_CHOICE)

        # Check if the input is a digit and between 1 and 5
        if choice.isdigit() and 1 <= int(choice) <= 5:
            choice = int(choice)  # Convert to integer after validation
            if choice == 1:
                print("Adding expensive details...")
                ds = exp_service.add_expense()
                exp_list.append(ds)
            elif choice == 2:
                print("View expensive details...")
                if not exp_list:
                    print("exp_list is empty")
                else:
                    exp_service.view_expense(exp_list)
            elif choice == 3:
                print("Tracking expensive details...")
                if not exp_list:
                    print("exp_list is empty")
                else:
                    exp_service.track_budget(exp_list)
            elif choice == 4:
                print("Saving expensive details...")
                if not exp_list:
                    print("exp_list is empty")
                else:
                    exp_service.save_expense(exp_list)
            elif choice == 5:
                print("Exiting...")
                break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")
