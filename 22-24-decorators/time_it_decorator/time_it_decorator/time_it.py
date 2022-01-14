#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Decorators
Project: 100Days of code with Python
Progress: Roond1, Day22-24 = R1D22-24
"""

from functools import wraps
import time


def timeit(func):
    """Decorator to time a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before calling the decorated function
        print("== starting timer")
        start = time.time()

        # call the decorated function
        func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(f"== {func.__name__} took {int(end-start)} seconds to complete")

    return wrapper


@timeit
def generate_report():
    """Function to generate revenue report"""
    time.sleep(2)
    print("(actual function) Done, report links ...")


def main():
    generate_report()


if __name__ == "__main__":
    main()
