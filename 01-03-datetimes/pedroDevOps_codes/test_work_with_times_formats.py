#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Working with time formats
Project: 100Days of code with Python
Progress: Round1, Day3 = R1D3
Bites: https://codechalleng.es/bites/128/
References:
OBS:
    flake8 was used: # flake8 test_work_with_times_formats.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive test_work_with_times_formats.py
    bandit was used: # bandit -r test_work_with_times_formats.py
"""

from work_with_times_formats import convert_eu_to_us_date, convert_us_to_eu_date, years_ago

def test_convert_eu_to_us_date():
    line1 = '25/04/1986'
    line2 = '13/12/2040'
    line3 = '29/03/2000'
    assert convert_eu_to_us_date(line1) == '04/25/1986'
    assert convert_eu_to_us_date(line2) == '12/13/2040'
    assert convert_eu_to_us_date(line3) == '03/29/2000'

def test_convert_us_to_eu_date():
    line1 = '05/24/1986'
    line2 = '01/14/2022'
    line3 = '12/31/1999'
    assert convert_us_to_eu_date(line1) == '24/05/1986'
    assert convert_us_to_eu_date(line2) == '14/01/2022'
    assert convert_us_to_eu_date(line3) == '31/12/1999'


def test_years_ago():
    diff = years_ago('8 Aug, 2015')
    assert diff == 3