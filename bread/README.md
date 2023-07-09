# Financial Analysis

*This is still a work in progress project*

This script helps categorize expenses given a worksheet containing bank statement data for any account.

## Description

This script attempts to categorize transactions in a bank statement using a personal categorization model. The goal of the script is to be able to categorize transactions from statements downloaded from any bank portal.

### Input

The input is bank statements downloaded in csv format from banking portals. They can be multiple files and have to be stored under the `statements/` directory inside the project.

### Output

The script outputs the collection of parsed data from all files under `statements/` into a csv file under the directory `output/` (also inside the project)

## Future Enhancements

1. New script that helps a user add categories
2. Interactive prompt to modify invalid entries detected by the script