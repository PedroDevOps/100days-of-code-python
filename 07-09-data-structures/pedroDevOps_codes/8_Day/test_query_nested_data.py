#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Test test_query_nested_data.py 
Project: 100Days of code with Python
Progress: Roond1, Day8 = R1D8
"""

# Just execute with pytest, like:
# ubuntu@DESKTOP:~/ pytest test_query_nested_data.py
# or
# ubuntu@DESKTOP:~/ pytest -xv test_query_nested_data.py


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def test_get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    pass


def test_get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    pass


def test_get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def test_sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass