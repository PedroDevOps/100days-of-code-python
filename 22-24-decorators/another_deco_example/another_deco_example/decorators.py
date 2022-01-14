#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Decorators
Project: 100Days of code with Python
Progress: Roond1, Day22-24 = R1D22-24
"""

from functools import wraps


def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("hi from decorator - args:")
        print(args)
        result = function(*args, **kwargs)
        print("hi again from decorator - kwargs:")
        print(kwargs)
        return result

    # return wrapper as a decorated function
    return wrapper


@show_args
def get_profile(name, active=True, *sports, **awards):
    print("Positional arguments (required): ", name)
    print("Keyword arguments (not required, default values): ", active)
    print("Arbitrary argument list (sports): ", sports)
    print("Arbitrary keyword argument dictionary (awards): ", awards)


def main():
    get_profile(
        "julian",
        False,
        "basketball",
        "soccer",
        pythonista="special honor of the community",
        topcoder="2017 code camp",
    )


if __name__ == "__main__":
    main()
