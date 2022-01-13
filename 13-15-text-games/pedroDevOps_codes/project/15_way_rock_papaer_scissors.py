#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Rock, Paper and Scissors
Project: 100Days of code with Python
Progress: Roond1, Day13-15 = R1D13-15
"""


class Roll:
    def __init__(
        self, roll_name, wins_aggainst_rolls_name_list, losses_aggainst_rolls_name_list
    ):
        self.roll_name = roll_name
        self.wins_aggainst_rolls_name_list = wins_aggainst_rolls_name_list
        self.losses_aggainst_rolls_name_list = losses_aggainst_rolls_name_list

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (
                self.roll_name == other.roll_name
                and self.wins_aggainst_rolls_name_list
                == other.wins_aggainst_rolls_name_list
                and self.losses_aggainst_rolls_name_list
                == other.losses_aggainst_rolls_name_list
            )
        return False

    def can_defeat(self, aggainst_roll):
        won = False
        for roll_defeated_by_myself in self.wins_aggainst_rolls_name_list:
            if roll_defeated_by_myself == aggainst_roll.roll_name:
                won = True
        return won


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.chosen_rolls_list = []
        self.rounds_victories = 0
