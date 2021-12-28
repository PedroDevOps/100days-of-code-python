#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Create your own Pomodoro Timer
Project: 100Days of code with Python
Progress: Roond1, Day3 = R1D3
"""

from datetime import timedelta, datetime
from time import sleep, strftime
from os import system

def countdown(title, time_to_focus, time_to_rest):
    system('clear')
    stop_time = datetime.now() + time_to_focus
    go_time = stop_time + time_to_rest

    # Loop for the focus time
    while datetime.now() < stop_time:
        delta = stop_time - datetime.now()
        totalMinute, second = divmod(delta.seconds, 60)
        hour, minute = divmod(totalMinute, 60)
        print(title,f"{hour}:{minute:02}:{second:02}",end='\r')
        sleep(1)
    
    print("Well done! Let's rest for: {}".format(time_to_rest))
    
    # Loop for the break time
    while datetime.now() < go_time:
        delta = go_time - datetime.now()
        totalMinute, second = divmod(delta.seconds, 60)
        hour, minute = divmod(totalMinute, 60)
        print(title,f"{hour}:{minute:02}:{second:02}",end='\r')
        sleep(1)
       
def pomodoro_timer(title, interval_time, rest_time):
    keep_using_timer = True
    while keep_using_timer:
        try:
            countdown(title, interval_time, rest_time)
            #break_time = int(input('Break Duration (in minutes or anything else to stop): '))
            #timer('Break:', duration)
            keep_using_timer = False
        except:
            break



# The Main Function
def main():
    pomodoro_timer("Pomodoro timer", timedelta(seconds=6), timedelta(seconds=4))

if __name__ == "__main__":
    main()