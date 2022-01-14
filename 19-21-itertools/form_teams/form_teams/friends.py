#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Using itertools.cycle
Project: 100Days of code with Python
Progress: Round1, Day17 = R1D19
challenge: https://codechalleng.es/bites/17/
"""
import itertools


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)
    else:
        return itertools.combinations(friends, team_size)
