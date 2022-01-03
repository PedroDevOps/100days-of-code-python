#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Working with time formats
Project: 100Days of code with Python
Progress: Round1, Day3 = R1D3
Bites: https://codechalleng.es/bites/128/
References:
OBS:
    flake8 was used: # flake8 work_with_times_formats.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive work_with_times_formats.py
    bandit was used: # bandit -r work_with_times_formats.py
"""

from datetime import datetime
import argparse

THIS_YEAR = 2018

# Receives a date string of 'DD MMM, YYYY'
# and converts this date str to a datetime object with strptime.
# Then it extract the year from the obtained datetime object and subtract
# it from the THIS_YEAR constant, returning the int difference.


def years_ago(str_date):
    int_diff = abs(datetime.strptime(str_date, '%d %b, %Y').year - THIS_YEAR)
    return int_diff

# Receives a date string in European format of dd/mm/yyyy
# Convert it to an American date: mm/dd/yyyy


def convert_eu_to_us_date(str_eu_date):
    str_us_date = datetime.strptime(
        str_eu_date, '%d/%m/%Y').strftime('%m/%d/%Y')
    return str_us_date

# Receives a date string in American format of mm/dd/yyyy
# Convert it to an Europian date: dd/mm/yyyy


def convert_us_to_eu_date(str_us_date):
    str_eu_date = datetime.strptime(
        str_us_date, '%m/%d/%Y').strftime('%d/%m/%Y')
    return str_eu_date


# The Main Function
# Pass the args in the command line.
def main():
    parser = argparse.ArgumentParser(description='Working with time formats')
    parser.add_argument(
        '-d',
        '--date',
        metavar='date',
        default='',
        help='a date string in this specific format DD MMM, YYYY, e.g. 8 Aug, 2015')
    parser.add_argument(
        '-eu',
        '--eu_date',
        metavar='eu_date',
        default='',
        help='a date string in European format of dd/mm/yyyy, e.g. 11/03/2002')
    parser.add_argument(
        '-us',
        '--us_date',
        metavar='us_date',
        default='',
        help='a date string in American format of mm/dd/yyyy, e.g. 12/25/2021')
    args = parser.parse_args()

    try:
        if len(args.date) > 1:
            diff = years_ago(args.date)
            print("The difference between dates is {} years".format(diff))
        if len(args.eu_date) > 1:
            americanDate = convert_eu_to_us_date(args.eu_date)
            print("The corresponding American date is {}".format(americanDate))
        if len(args.eu_date) > 1:
            europianDate = convert_us_to_eu_date(args.eu_date)
            print("The corresponding Europian date is {}".format(europianDate))
    except Exception:
        exit


if __name__ == "__main__":
    main()
