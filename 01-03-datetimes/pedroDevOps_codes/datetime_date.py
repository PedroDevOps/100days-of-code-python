#!/usr/bin/env python3

from datetime import date
from datetime import datetime

# This is the main fucntion
def main():
    print("Today is {}, a wonderful day to begin my 100days of code with Python".format(date(2021, 12, 17,)))
    
    myBirthday = date(1986, 4, 21)
    myWifeBirthday = date(1988, 6, 19)
    print("My Birthday is on {}".format(myBirthday))
    today = datetime.today()

    type(today)
    # <class 'datetime.datetime'>

    today_date = date.today()

    today_date
    # datetime.date(2021, 1, 19)

    type(today_date)
    # <class 'datetime.date'>

    today_date.month
    # 1

    today_date.year
    # 2021

    today_date.day
    # 19
    christmas = date(today_date.year, 12, 25)
    christmas
    # datetime.date(2021, 12, 25)

    # We need to use != & == rather than is / is not for comparison. Sorry for the mistake in the video.
    if christmas != today_date:
        print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
    else:
        print("Yay it's Christmas!")
        

# Compare two dates and return the diference between both
def compareDates(date1,date2):
    return delta


if __name__ == "__main__":
  main()
