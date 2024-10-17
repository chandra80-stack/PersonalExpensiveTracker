import csv

from com.iitk.constants.ExpConstants import FILEPATH, FILENAME


def save_file(exp_list):
    # Define the CSV file path
    csv_file_path = FILEPATH + FILENAME

    # Save the data to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        if exp_list:
            dict_writer = csv.DictWriter(csv_file, fieldnames=exp_list[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(exp_list)
            return csv_file_path
        else:
            return None


def load_file():
    exp_list = []
    # Define the CSV file path
    csv_file_path = FILEPATH + FILENAME

    # Retrieve data from the CSV file
    try:
        with open(csv_file_path, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file)
            retrieved_data = list(dict_reader)
            return retrieved_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        # Handle the error, maybe create the file or log the issue
        with open(csv_file_path, 'w') as file:
            file.write('This file did not exist, so I created it.')
    # Add the retrieved data to the existing list
    return exp_list
