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


def get_all_jeeps(cars_dict=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    car_string = ""
    for model in cars_dict['Jeep']:
        if car_string == "":
            car_string = model
        else:
            car_string = car_string + ", " + model
    return car_string


def get_first_model_each_manufacturer(cars_dict=cars):
    """return a list of matching models (original ordering)"""
    matching_models_list = []
    for models_list in cars_dict.values():
        matching_models_list.append(models_list[0])
    return matching_models_list


def get_all_matching_models(cars_dict=cars, grep='Trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matching_models_list = []
    for models_list in cars_dict.values():
        for model in models_list:
            if grep.lower() in model.lower():
                matching_models_list.append(model)
    return matching_models_list


def sort_car_models(cars_dict=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    cars_dict_sorted = {}
    for manufacture, models_list in cars_dict.items():
        cars_dict_sorted[manufacture] = sorted(models_list)
    return cars_dict_sorted


def main():
    '''
    This is the main function
    '''
    print("Main Function")
    print(get_all_jeeps(cars))
    print(get_first_model_each_manufacturer(cars))
    print(get_all_matching_models(cars))
    print(sort_car_models(cars))


if __name__ == '__main__':
    main()
