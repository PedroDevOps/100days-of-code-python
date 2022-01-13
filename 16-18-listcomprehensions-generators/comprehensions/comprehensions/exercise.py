#!/usr/bin/env python3

import random

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


def get_title_names(names_list=NAMES):
    return [name.title() for name in names_list]


def get_reverse_name(full_name):
    first_name, last_name = full_name.split()
    return f"{last_name} {first_name}"


def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        first, second = None, None
        while first == second:
            first, second = random.sample(first_names, 2)
        yield f"{first} teams up with {second}"


def main():
    """
    This is the main function
    """
    for name in get_title_names(NAMES):
        print(get_reverse_name(name))
    pairs = gen_pairs()
    for _ in range(10):
        print(next(pairs))


if __name__ == "__main__":
    main()
