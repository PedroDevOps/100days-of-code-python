#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Rock, Paper and Scissors
Project: 100Days of code with Python
Progress: Roond1, Day13-15 = R1D13-15
"""

import random, os ,csv
from rock_paper_scissors import Roll, Player
from termcolor import colored


def print_header():
    print('---------------------------------')
    print('    15 Way Rock Paper Scissors GAME')
    print('---------------------------------')
    print()

def create_all_15_rolls():
    rolls_list = []
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            rolls_list.append(create_roll(row))
    return rolls_list


def create_roll(row: dict):
    can_defeat_list = [] 
    can_not_defeat_list = []
    roll_created = Roll("",[],[])
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    #print("Roll: {}".format(name))
    for k in row.keys():
        if row[k].strip().lower() == 'win':
            can_defeat_list.append(k) 
            #print(" * {} will defeat {}? {}".format(name, k, can_defeat))
        else:
            can_not_defeat_list.append(k)

    roll_created = Roll(name, can_defeat_list, can_not_defeat_list)
    #print(" * {} will defeat {}  but will be defeated by {}".format(roll_created.roll_name, roll_created.wins_aggainst_rolls_name_list , roll_created.losses_aggainst_rolls_name_list))
    
    return roll_created


def get_players_name():
    try:
        player_name = input ('Insert your name, please. ')
        #os.system('cls' if os.name == 'nt' else 'clear')
        print()
        return player_name 
    except Exception:
        print("Something went Wrong")

def get_random_roll(rolls_list):
    random_roll = random.choice(rolls_list)
    return random_roll

def get_match_breakdown(player1, player2):

    if len(player1.chosen_rolls_list) != 15:
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
    while count <= 15:
        p2_roll = get_random_roll(rolls) # get random roll
        p1_roll = get_random_roll(rolls) # have player choose a roll

        player2.chosen_rolls_list.append(p2_roll)
        player1.chosen_rolls_list.append(p1_roll)
        
        outcome = p1_roll.can_defeat(p2_roll)

        print("{} chose {} ".format(colored(player1.player_name, "cyan"), (colored(p1_roll.roll_name,"cyan")))) # display throws
        print("{} chose {} ".format(colored(player2.player_name, "yellow"), (colored(p2_roll.roll_name,"yellow")))) # display throws

        if p2_roll.roll_name == p1_roll.roll_name:
            print ("Nobody won round {}, It was a tie".format(colored(count,"magenta")))
        elif outcome : # display winner for this round
            print("{} beats {} ". format( (colored(p1_roll.roll_name,"cyan")), (colored(p2_roll.roll_name,"yellow")) ))
            print ("{} won round {} ".format(colored(player1.player_name, "cyan"), colored(count,"magenta")))
            player1.rounds_victories += 1
        else:
            print("{} beats {} ". format( (colored(p2_roll.roll_name,"yellow")), (colored(p1_roll.roll_name,"cyan")) ))
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
    rolls = create_all_15_rolls()

    '''
    for roll in rolls :
        print(" * {} will defeat {}  but will be defeated by {}".format(roll.roll_name, roll.wins_aggainst_rolls_name_list , roll.losses_aggainst_rolls_name_list))

    '''

    player1 = Player("John Doe")
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)
    

if __name__ == '__main__':
    main()