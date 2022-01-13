import pytest
from unittest.mock import patch
import random

from comprehensions import exercise, __version__

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
]

NAMES_title = [
    "Arnold Schwarzenegger",
    "Alec Baldwin",
    "Bob Belderbos",
    "Julian Sequeira",
    "Sandra Bullock",
    "Keanu Reeves",
    "Julbob Pybites",
    "Bob Belderbos",
    "Julian Sequeira",
    "Al Pacino",
    "Brad Pitt",
    "Matt Damon",
]

NAMES_title_reverse = [
    "Schwarzenegger Arnold ",
    "Baldwin Alec",
    "Belderbos Bob",
    "Sequeira Julian ",
    "Bullock Sandra ",
    "Reeves Keanu ",
    "Pybites Julbob ",
    "Belderbos Bob ",
    "Sequeira Julian ",
    "Pacino Al ",
    "Pitt Brad ",
    "Damon Matt ",
]


def test_version():
    assert __version__ == "0.1.0"


def test_exercise_get_title_names(names_list=NAMES):
    assert exercise.get_title_names(names_list) == NAMES_title


@pytest.mark.parametrize(
    "normal_name, reversed_name",
    [
        ("Arnold Schwarzenegger", "Schwarzenegger Arnold"),
        ("Alec Baldwin", "Baldwin Alec"),
        ("Bob Belderbos", "Belderbos Bob"),
        ("Julian Sequeira", "Sequeira Julian"),
        ("Sandra Bullock", "Bullock Sandra"),
        ("Keanu Reeves", "Reeves Keanu"),
        ("Julbob Pybites", "Pybites Julbob"),
        ("Bob Belderbos", "Belderbos Bob"),
        ("Julian Sequeira", "Sequeira Julian"),
        ("Al Pacino", "Pacino Al"),
        ("Brad Pitt", "Pitt Brad"),
        ("Matt Damon", "Damon Matt"),
    ],
)
def test_get_reverse_name(normal_name, reversed_name):
    assert exercise.get_reverse_name(normal_name) == reversed_name


@patch.object(random, 'sample')
def test_gen_pairs(random_pair):
    random_pair.return_value = 'Arnold', 'Keanu'
    pairs = exercise.gen_pairs()
    assert next(pairs) == "Arnold teams up with Keanu"
