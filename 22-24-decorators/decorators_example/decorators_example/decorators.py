#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Decorators
Project: 100Days of code with Python
Progress: Roond1, Day22-24 = R1D22-24
"""

from functools import wraps


def make_html(element):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Before
            result = f"<{element}>"
            # Call Fuction
            result = result + function(*args, **kwargs)
            # After
            result = result + (f"</{element}>")
            return result

        return wrapper

    return decorator
