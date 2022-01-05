#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: 
Project: 100Days of code with Python
Progress: Round1, DayX = R1DX
Challenge: https://pybit.es/codechallenge13.html
References:
OBS:
    flake8 was used: # flake8 template.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive template.py
    bandit was used: # bandit -r template.py
"""

from datetime import date, timedelta
import argparse

def get_1():
    """Return a int number"""
    return 0


def get_2():
    """Return the int number"""
    return 0


# The Main Function
# Pass the args in the command line.
def main():
    parser = argparse.ArgumentParser(
        description=' Working with XXXXX')
    args = parser.parse_args()

    try:
        _aux1 = get_1()
        _aux2 = get_2()
    except Exception:
        exit


if __name__ == "__main__":
    main()
