#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Sum & Subtract dates, working with deltatime type
Project: 100Days of code with Python
Progress: Round1, Day3 = R1D3
Bites: https://codechalleng.es/bites/67/
References:
OBS:
    flake8 was used: # flake8 finish_date.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive finish_date.py
    bandit was used: # bandit -r finish_date.py
"""

from datetime import date, timedelta
import argparse

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    finalDate = start_100days + timedelta(days=100)
    return finalDate


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    days_between = abs((pybites_founded - pycon_date).days)
    return days_between


# The Main Function
# Pass the args in the command line.
def main():
    parser = argparse.ArgumentParser(
        description=' Working with dates')
    args = parser.parse_args()

    try:
        date_aux = get_hundred_days_end_date()
        days_aux = get_days_between_pb_start_first_joint_pycon()
    except Exception:
        exit


if __name__ == "__main__":
    main()
