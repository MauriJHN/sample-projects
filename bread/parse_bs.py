#! /usr/bin/env python3

import csv
from datetime import datetime
import json
import sys
import os


# TODO: make this a prompt instead of an argument
CUSTOM_FILENAME = ""
CATEGORY_MAPPING = "categories.json"
STMTS_DIR = "statements"
OUT_FILENAME = f"statement-{datetime.today().strftime('%Y-%m-%d')}"
OUTPUT_DIR = "parsed_data"


if len(sys.argv) == 2:
    CUSTOM_FILENAME = sys.argv[1]


def categorize(description: str) -> str:
    """Check against json mapping file and return category"""
    with open(CATEGORY_MAPPING, "r") as file:
        data = json.loads(file.read())
        for category, keywords in data.items():
            for keyword in keywords:
                if keyword in description.lower():
                    print(f"Matched description: {description} with category: {category}")
                    return category

    print(f'Adding {description} as "Extra Expense"')
    return "Extra Expenses"


def _format_date(date_str: str) -> str:
    # format date in format 'YYYYMMDD' to 'YYYY-MM-DD'
    new_date_str = datetime.strftime(datetime.strptime(date_str, "%Y%m%d"), "%Y-%m-%d")
    return new_date_str


def _add_to_sorted(new_data: list, formatted_line: dict) -> list:
    """Adds `formatted_line` item and sorts it in `new_data`"""
    # TODO: create a new general way to sort by date
    sorted_data = []
    if len(new_data) == 0:
        new_data.append(formatted_line)

    for i in range(len(new_data)):
        # compares the date between each entry already in list and new entry, date in index 2 of each entry
        if new_data[i][2] >= formatted_line[2]:
            sorted_data = new_data[:i] + [formatted_line] + new_data[i:]
            return sorted_data


def format_csv_line(line: list, data_columns: list) -> list:
    """Formats the csv list into format for excel spreadsheet

    Takes a list object retrieved from iterating through a csv.reader() obj
    and modifies (item #,card #,transaction date,posting date,transaction amount,description)
    to (description, date[yyyy-mm-dd], category, amount)
    """
    date_col, description_col, amount_col = data_columns # index + 1

    date = line[date_col-1]
    description = line[description_col-1]
    amount = line[amount_col-1]

    try:
        formatted_line = [
            description,
            _format_date(date), 
            categorize(description), 
            float(amount)
        ]
    except Exception as e:
        # returns a filler row, intended for manual corrections
        return [description, date, categorize(description), 0]

    return formatted_line


def get_statement_filenames() -> list:
    """Checks if the statements directory exists, 
    creates it if not, 
    returns list of filenames inside
    
    Return:
        list containing filenames under `STMTS_DIR`
    """
    statement_dir = os.path.join(os.curdir, STMTS_DIR)

    if not os.path.exists(statement_dir):
        os.mkdir(statement_dir)
        print(f"Please copy and paste bank statements under the created {statement_dir}")
        exit(1)

    stmt_filenames = os.listdir(statement_dir)
    return stmt_filenames


def read_data(filename: str, header_line: int, data_columns: tuple) -> list:
    """Reads and formats the data contained in the file passed"""
    new_data = []
    filepath = os.path.join(os.path.curdir, STMTS_DIR, filename)

    with open(filepath, newline="") as stmt_file:
        print(f"Reading file {filename}")
        file_data = csv.reader(stmt_file, delimiter=",")
        
        for line in file_data:
            if file_data.line_num < header_line or not line: continue
            
            formatted_line = format_csv_line(line, data_columns)
            new_data = _add_to_sorted(new_data, formatted_line)

    return new_data


def get_number_input(prompt):
    """Prompts the user for a number input and validates it"""
    in_number = None
    while not in_number:
        try:
            in_number = int(input(prompt))
        except Exception as e:
            print("Please input a number")
    
    return in_number


def output_data_to_file(new_data):
    """Helper function that writes data passed in `new_data` to an output file"""
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    output_filename = f"{OUTPUT_DIR}/{CUSTOM_FILENAME if CUSTOM_FILENAME else OUT_FILENAME}.csv"

    with open(output_filename, "w+") as filename:
        print(f"Writing parsed csv data to {output_filename}")
        writer = csv.writer(filename)
        writer.writerows(new_data)


def main():
    new_data = []
    stmt_filenames = get_statement_filenames()
    date_column = get_number_input("Column number with date of transaction: ")
    desc_column = get_number_input("Column number with description: ")
    amount_column = get_number_input("Column number with amount: ")
    header_line = get_number_input("Header row number (0 if none): ")

    for filename in stmt_filenames:
        new_data += read_data(filename.rstrip(), header_line, (date_column, desc_column, amount_column))

    output_data_to_file(new_data)

if __name__ == "__main__":
    main()
