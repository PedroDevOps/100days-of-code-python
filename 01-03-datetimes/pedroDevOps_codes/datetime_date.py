#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Playing around with classes date and datetime
Project: 100Days of code with Python
Progress: Roond1, Day1 = R1D1
"""

from datetime import date


# This is the main fucntion
def main():
    print(
        "Today is {}, a wonderful day to begin my 100days of code with Python".format(
            date(
                2021,
                12,
                26,
            )
        )
    )

    myBirthday = date(1986, 4, 21)
    myWifeBirthday = date(1988, 6, 19)
    myWeddingDate = date(2018, 6, 19)

    print("My Birthday is on {}".format(myBirthday))
    print("My Wife's Birthday is on {}".format(myWifeBirthday))
    print("We got Married on {}".format(myWeddingDate))

    # today = datetime.today()
    # print (type(today))
    # <class 'datetime.datetime'>
    # today_date = date.today()
    # print (type(today_date))
    # <class 'datetime.date'>
    # datetime.date(2021, 1, 19)

    # Compare the difference between both spouses
    if myBirthday < myWifeBirthday:
        print(
            "I am "
            + str(compareDates(myWifeBirthday, myBirthday).days)
            + " days older than your wife!"
        )
        print(
            "I am "
            + str((compareDates(myWifeBirthday, myBirthday).days) * 24 * 60 * 60)
            + " seconds older than your wife!"
        )
    else:
        print(
            "I am "
            + str(compareDates(myWifeBirthday, myBirthday).days)
            + " days younger than your wife!"
        )
        print(
            "I am "
            + str((compareDates(myWifeBirthday, myBirthday).days) * 24 * 60 * 60)
            + " seconds younger than your wife!"
        )


# Compare two dates and return the diference between both
def compareDates(date1, date2):
    delta = date1 - date2
    return delta


if __name__ == "__main__":
    main()
