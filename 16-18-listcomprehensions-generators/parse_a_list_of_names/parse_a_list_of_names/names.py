#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Parse a List of names usinng comprehensions
Project: 100Days of code with Python
Progress: Round1, Day17 = R1D17
Challenge: https://codechalleng.es/bites/5/

"""

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    first_second_names = [full_name.split() for full_name in names]
    return [
        " ".join(name)
        for name in sorted(first_second_names, key=lambda x: x[-1], reverse=True)
    ]


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_names = [full_name.split()[0] for full_name in names]
    return list(sorted(first_names, key=len, reverse=False))[0]
