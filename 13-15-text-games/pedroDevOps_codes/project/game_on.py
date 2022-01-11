#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Rock, Paper and Scissors
Project: 100Days of code with Python
Progress: Roond1, Day13-15 = R1D13-15
"""

import random, os
from rock_paper_scissors import Roll, Player
from termcolor import colored


roll_rock = Roll('Rock', ['Scissors'],  ['Paper'])
roll_paper = Roll('Paper', ['Rock'],['Scissors'])
roll_scissors = Roll('Scissors', ['Paper'], ['Rock'])


def print_header():
    print('---------------------------------')
    print('    Rock Paper Scissors GAME')
    print('---------------------------------')
    print()


def build_the_three_rolls():
    rolls = [ roll_rock , roll_paper, roll_scissors ]
    return rolls


def get_players_name():
    try:
        player_name = input ('Insert your name, please. ')
        #os.system('cls' if os.name == 'nt' else 'clear')
        print()
        return player_name 
    except Exception:
        print("Something went Wrong")

def player_chooses_roll(player, rolls_list):
    choice = input("{}, please chose one option: [r]ock, [p]aper or [s]cissors ".format(colored(player.player_name, "cyan")))
    print()
    chosen_roll = Roll("",[],[])
    if choice == 'r':
        for roll in rolls_list:
            if roll.roll_name == 'Rock':
                chosen_roll = roll
    elif choice == 'p':
        for roll in rolls_list:
            if roll.roll_name == 'Paper':
                chosen_roll = roll
    elif choice == 's':
        for roll in rolls_list:
            if roll.roll_name == 'Scissors':
                chosen_roll = roll
    else:
        for roll in rolls_list:
            if roll.roll_name == 'Rock':
                chosen_roll = roll

    return chosen_roll

def get_random_roll(rolls_list):
    random_roll = random.choice(rolls_list)
    return random_roll

def get_match_breakdown(player1, player2):

    if len(player1.chosen_rolls_list) != 3:
        exit
    else:
        count = 1
        print("Match Breakdown:")
        for player1_roll, player2_roll in  zip(player1.chosen_rolls_list, player2.chosen_rolls_list):
            print("Round {}: ({}) {} vs {} ({}) ".format(
                count, 
                colored(player1.player_name, "cyan"), 
                colored(player1_roll.roll_name, "cyan"), 
                colored(player2_roll.roll_name,"yellow"),
                colored(player2.player_name, "yellow"))
                ) #
            count +=1


def game_loop(player1, player2, rolls):

    count = 1
    while count <= 3:
        p2_roll = get_random_roll(rolls) # get random roll
        p1_roll = player_chooses_roll(player1, rolls) # have player choose a roll

        player2.chosen_rolls_list.append(p2_roll)
        player1.chosen_rolls_list.append(p1_roll)
        
        outcome = p1_roll.can_defeat(p2_roll)

        print("{} chose {} ".format(colored(player1.player_name, "cyan"), p1_roll.roll_name)) # display throws
        print("{} chose {} ".format(colored(player2.player_name, "yellow"), p2_roll.roll_name)) # display throws
        print()

        if p2_roll.roll_name == p1_roll.roll_name:
            print ("Nobody won round {}, It was a tie".format(count))
        elif outcome : # display winner for this round
            print ("{} won round {} ".format(colored(player1.player_name, "cyan"), colored(count,"magenta")))
            player1.rounds_victories += 1
        else:
            print ("{} won round {} ".format(colored(player2.player_name, "yellow"), colored(count,"magenta")))
            player2.rounds_victories += 1
        print()
        count += 1

    get_match_breakdown(player1, player2)

    # Compute who won
    if player1.rounds_victories == player2.rounds_victories:
        print ("Nobody won the game, It was a tie! {} x {}. ".format(colored(player1.player_name,"green"), colored(player1.rounds_victories,"green"), colored(player2.rounds_victories ,"red")))
    elif player1.rounds_victories > player2.rounds_victories:
        print("{} won the game by {} x {}. ".format(colored(player1.player_name,"green"), colored(player1.rounds_victories,"green"), colored(player2.rounds_victories ,"red")))
    else:
        print("{} won the game by {} x {}. ".format(colored(player2.player_name,"green"), colored(player2.rounds_victories,"green"), colored(player1.rounds_victories, "red")))


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)
    

if __name__ == '__main__':
    main()