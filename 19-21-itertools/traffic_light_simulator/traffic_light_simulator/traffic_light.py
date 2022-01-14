#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Using itertools.cycle
Project: 100Days of code with Python
Progress: Round1, Day17 = R1D19

"""
import itertools
import time
import random
from termcolor import colored

COLORS = [colored("Red", "red"), colored("Green", "green"), colored("Yellow", "yellow")]
traffic_light_rotation = itertools.cycle(COLORS)


def cycle_through():

    for light in traffic_light_rotation:
        traffic_intensity = random.randint(0, 3)
        print(f"The traffic intensity is {traffic_intensity} right now")
        print(f"The traffic ligth is {light}")
        if light == colored("Red", "red"):
            time.sleep(3 + traffic_intensity)
        elif light == colored("Green", "green"):
            time.sleep(2 + traffic_intensity)
        elif light == colored("Yellow", "yellow"):
            time.sleep(1 + traffic_intensity)


def main():
    print("Main Function")
    cycle_through()


if __name__ == "__main__":
    main()
