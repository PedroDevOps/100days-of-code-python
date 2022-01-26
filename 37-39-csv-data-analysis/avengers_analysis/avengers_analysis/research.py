import os
import csv
import collections
import time
import re

from functools import wraps
from collections import defaultdict
from typing import List


Record = collections.namedtuple(
    "record",
    "URL,Name_Alias,Appearances,Current,"
    "Gender,Probationary_Introl,Full_Reserve_Avengers_Intro,"
    "Year,Years_since_joining,Honorary,Death1,Return1,Death2,"
    "Return2,Death3,Return3,Death4,Return4,Death5,Return5,Notes",
)


def timeit(func):
    """Decorator to time a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before calling the decorated function
        start = time.time()

        # call the decorated function
        result = func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(f"== {func.__name__} took {float(end-start)} seconds to complete")
        return result

    return wrapper


def init() -> List[Record]:
    """open the csv file and extract the information

    return the information to a global list of records
    the records are namedtuples that have all the information retrived by DictReader
    """
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, "../data", "avengers.csv")

    with open(filename, "r", encoding="utf-8") as raw_data_file:
        reader = csv.DictReader(raw_data_file)

        data = []
        for row in reader:
            record = parse_row(row)
            data.append(record)
    return data


def parse_row(row) -> Record:
    """ """
    row["Appearances"] = int(row["Appearances"])
    row["Years_since_joining"] = int(row["Years_since_joining"])
    return Record(**row)


# @timeit
def who_is_the_oldest_avenger(data: List[Record]) -> List[Record]:
    return sorted(data, key=lambda r: r.Years_since_joining, reverse=True)


# @timeit
def who_is_the_most_recent_avenger(data) -> List[Record]:
    return sorted(data, key=lambda r: r.Years_since_joining)


# @timeit
def who_died_the_most(data) -> List:
    deaths_dict = defaultdict(list)

    for avenger_record in data:
        deaths_score = sum(
            10 ** idx
            for idx in range(1, 6)
            if getattr(avenger_record, f"Death{idx}") == "YES"
        )
        deaths_dict[avenger_record.Name_Alias] = deaths_score

    return sorted(deaths_dict.items(), key=lambda x: x[1], reverse=True)


# @timeit
def is_there_a_avenger_called(data) -> List[Record]:

    try:
        name = input("Is there a avenger called ..... or with this words ..... in their name? \n")

        avergers_list = [avenger_record for avenger_record in data if (re.search(name.lower(), (avenger_record.Name_Alias).lower())) is not None] 
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

    return sorted(avergers_list, key=lambda r: r.Name_Alias)
