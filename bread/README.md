# Financial Analysis

- [Financial Analysis](#financial-analysis)
  - [Description](#description)
    - [Input](#input)
    - [Output](#output)
  - [Usage](#usage)
    - [Customizing Category Parsing Data](#customizing-category-parsing-data)
    - [Downloading statements](#downloading-statements)
    - [Executing the Script](#executing-the-script)
  - [Future Enhancements](#future-enhancements)

*This is still a work in progress project*

This script helps categorize expenses given a worksheet containing bank statement data for any account.

## Description

This project attempts to categorize transactions in a bank statement using a customizable categorization model. The goal of the program is to be able to categorize transactions from statements downloaded from any bank portal.

Additionally, this project includes a script to populate the `categories.json` file. This makes things easier for the user when customizing how data is parsed for each category.

### Input

The input is bank statements downloaded in csv format from banking portals. They can be multiple files and have to be stored under the `statements/` directory inside the project.

### Output

The script outputs the collection of parsed data from all files under `statements/` into a csv file under the directory `output/` (also inside the project)

## Usage

To properly use this program you will need to follow the sections below in order.

### Customizing Category Parsing Data

To execute this script make sure you have python installed on your system.

There is a `categories.json` file included that already has custom data inside it.

1. Open the terminal (MacOS) or command prompt on (Windows)
2. Navigate to the directory containing the script (should be something like `path/to/sample-projects/bread/`)
3. Execute the script by entering `python add_categories.py`
4. Follow the prompts to customize category data

### Downloading statements

1. Login to your bank portal
2. Download bank statement(s) in `.csv` format (only works for `csv` formats)
3. Navigate to the project's directory: `cd /absolute/path/to/sample-projects/bread/`
4. Create directory named `statements/` under `bread/` by executing: `mkdir bread`
   - If `statements/` is already created, make sure to delete other bank statements inside
   - `statements/` should only contain documents downloaded from a single bank (see next step)
5. Copy the bank statement(s) from the location they were downloaded to into `statements/`, the location for the bank statements should look something like:
   ```
   /path/to/sample-projects/bread/statements/bank_statement1.csv
   ```

### Executing the Script

To execute this script make sure you have python installed on your system.

1. Open the terminal (MacOS) or command prompt on (Windows)
2. Navigate to the directory containing the script (should be something like `path/to/sample-projects/bread/`)
3. Execute the script by entering `python parse_bs.py`
4. Follow the prompts to parse the data

## Future Enhancements

- [x] New script that helps a user add categories
- [ ] Interactive prompt to modify invalid entries detected by the script