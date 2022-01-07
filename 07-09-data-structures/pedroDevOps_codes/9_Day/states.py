#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Work with lists and dicts
Project: 100Days of code with Python
Progress: Round1, Day9 = R1D9
Challenge: https://codechalleng.es/bites/89/
References: Playing with lists and dicts
OBS:
    flake8 was used: # flake8 states.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive states.py
    bandit was used: # bandit -r states.py
Requirements:
    Given the provided cars dictionary:


"""

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(states_list=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    states_nth_list = []
    iterator_nth = n
    while iterator_nth <= len(states_list):
        states_nth_list.append(states_list[(iterator_nth-1)])
        iterator_nth = (iterator_nth) + n 
    return states_nth_list


def get_state_abbrev(state_name, us_state_abbrev_dict=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    state_abbrev_str =  us_state_abbrev_dict.get(state_name,NOT_FOUND )
    return state_abbrev_str


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if isinstance(data, list):
        longest_state = max(data, key=len)
    if isinstance(data, dict):
        longest_state = max(data.keys(), key=len)
    return longest_state


def combine_state_names_and_abbreviations(us_state_abbrev_dict=us_state_abbrev,
                                          states_list=states):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list. The resulting list
       has both sorted, so:
       ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
       (see also test_combine_state_names_and_abbreviations)"""
    states_list = sorted(states_list)
    states_list_len = len(states_list)   
    combined_state_names_and_abreviations_list = sorted(list(us_state_abbrev_dict.values()))[0:10]
    for x in range(10, 0, -1):
        combined_state_names_and_abreviations_list.append(states_list[states_list_len-(x)])
    return combined_state_names_and_abreviations_list


def main():
    '''
    This is the main function
    '''
    print("Main Function")
    print(get_longest_state(states))
    print(get_longest_state(us_state_abbrev))
    print(combine_state_names_and_abbreviations(us_state_abbrev,states))



if __name__ == '__main__':
    main()
