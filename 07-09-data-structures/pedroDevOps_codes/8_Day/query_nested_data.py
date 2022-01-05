#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Work with data structure
Project: 100Days of code with Python
Progress: Round1, Day8 = R1D8
Challenge: https://codechalleng.es/bites/21/
References: Query a nested data structure
OBS:
    flake8 was used: # flake8 query_nested_data.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive query_nested_data.py
    bandit was used: # bandit -r query_nested_data.py
Requirements:
    Given the provided cars dictionary:
    Get all Jeeps
    Get the first car of every manufacturer.
    Get all vehicles containing the string Trail in their names (should work for other grep too)
    Sort the models (values) alphabeticall
"""

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass


def main():
    '''
    This is the main function
    '''
    print("Main Function")


if __name__ == '__main__':
    main()