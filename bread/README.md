# Financial Analysis

- [Financial Analysis](#financial-analysis)
  - [Description](#description)
    - [Input](#input)
    - [Output](#output)
  - [Usage](#usage)
    - [Downloading statments](#downloading-statments)
  - [Future Enhancements](#future-enhancements)

*This is still a work in progress project*

This script helps categorize expenses given a worksheet containing bank statement data for any account.

## Description

This script attempts to categorize transactions in a bank statement using a personal categorization model. The goal of the script is to be able to categorize transactions from statements downloaded from any bank portal.

### Input

The input is bank statements downloaded in csv format from banking portals. They can be multiple files and have to be stored under the `statements/` directory inside the project.

### Output

The script outputs the collection of parsed data from all files under `statements/` into a csv file under the directory `output/` (also inside the project)

## Usage

### Downloading statments

1. Login to your bank portal
2. Download bank statement(s) in `.csv` format
3. Copy the bank statement(s) to this project under a directory named `statments/` (might need to create it first), the location for the bank statements should look something like:
   ```
   /path/to/project/bread/statements/bank_statement1.csv
   ```
   *(you can also execute the script and the program will create the directory)*

To execute the script make sure you have python installed on your system.

1. Open the terminal (MacOS) or command prompt on (Windows)
2. Navigate to the directory containing the script
3. Execute the script and fill in the prompts

## Future Enhancements

1. New script that helps a user add categories
2. Interactive prompt to modify invalid entries detected by the script