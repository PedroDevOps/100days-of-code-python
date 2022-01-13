#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Test game_on.py
Project: 100Days of code with Python
Progress: Roond1, Day13-15 = R1D13-15
References:
OBS:
    # flake8 test_game_on.py
    # autopep8 --in-place --aggressive --aggressive test_game_on.py
    # bandit -r test_game_on.py

    # pytest -xv test_game_on.py
    # pytest --cov-report term-missing --cov="."
"""

from game_on import (
    player_chooses_roll,
    print_header,
    build_the_three_rolls,
    get_players_name,
    get_random_roll,
    game_loop,
)
from rock_paper_scissors import Roll, Player
from unittest.mock import patch
import random

import pytest

roll_of_a_rock = Roll("Rock", ["Scissors"], ["Paper"])
roll_of_a_paper = Roll("Paper", ["Rock"], ["Scissors"])
roll_of_a_scissor = Roll("Scissors", ["Paper"], ["Rock"])
three_rolls = [roll_of_a_rock, roll_of_a_paper, roll_of_a_scissor]


def test_print_header(capfd):

    print_header()
    out, _ = capfd.readouterr()
    expected = [
        "---------------------------------",
        "Rock Paper Scissors GAME",
        "---------------------------------",
    ]

    output = [line.strip() for line in out.split("\n") if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp


def test_build_the_three_rolls(expected_rolls=three_rolls):

    rolls = build_the_three_rolls()
    for roll, expected_roll in zip(rolls, expected_rolls):
        assert roll == expected_roll


@patch("builtins.input", side_effect=["Pedro"])
def test_get_players_name(inp, capfd):

    assert get_players_name() == "Pedro"


@patch("builtins.input", side_effect=["r", "p", "s", "j"])
def test_player_chooses_roll(
    inp,
    rolls_list=three_rolls,
    rock_roll=roll_of_a_rock,
    paper_roll=roll_of_a_paper,
    scissor_roll=roll_of_a_scissor,
):

    player = Player("Pedro")
    assert player_chooses_roll(player, rolls_list) == rock_roll
    assert player_chooses_roll(player, rolls_list) == paper_roll
    assert player_chooses_roll(player, rolls_list) == scissor_roll
    assert player_chooses_roll(player, rolls_list) == rock_roll


@patch.object(random, "choice")
def test_random_roll(roll_random, roll_list=three_rolls):
    roll_random.return_value = roll_of_a_rock
    assert get_random_roll(roll_list) == roll_of_a_rock


def test_game_loop():
    print("game_loop_method")
