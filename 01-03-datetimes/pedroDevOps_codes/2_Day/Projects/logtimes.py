#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Extract log times from file 
Project: 100Days of code with Python
Progress: Roond1, Day2 = R1D2
"""

from datetime import datetime, date, time
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

# Open file and assin lines to a array
with open(logfile) as f:
    loglines = f.readlines()

# Extract timestamp from logline and convert it to a datetime object.
    # For example calling the function with:
        #INFO 2014-07-03T23:27:51 supybot Shutdown complete.
        #returns:
        #datetime(2014, 7, 3, 23, 27, 51)
def convert_to_datetime(line):
    # only works if there isn't another number in the line like: INFO 2014-07-03T23:27:51 supybot Killing 20 Driver objects.
    datas_from_line = re.findall('[0-9]+', line)
    d = date(int(datas_from_line[0]), int(datas_from_line[1]), int(datas_from_line[2]))
    t = time(int(datas_from_line[3]), int(datas_from_line[4]), int(datas_from_line[5]))
    datetime_with_an_event = datetime.combine(d, t)

    return datetime_with_an_event

# Extract shutdown events ("Shutdown initiated") from loglines and
# calculate the timedelta between the first and last one.
# Return this datetime.timedelta object.
def time_between_shutdowns(loglines):

    dates_with_shudown_event = []
    for line in loglines:
        if re.search('Shutdown initiated',line):
            dates_with_shudown_event.append(convert_to_datetime(line))
    
    if len(dates_with_shudown_event) > 1:
        delta_between_fisrt_and_last = dates_with_shudown_event[len(dates_with_shudown_event)-1]-dates_with_shudown_event[0]
    
    return delta_between_fisrt_and_last

# The Main Function
def main():
    print(time_between_shutdowns(loglines))

if __name__ == "__main__":
    main()