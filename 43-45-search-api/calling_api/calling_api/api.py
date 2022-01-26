#!/usr/bin/env python3
from functools import wraps
from random import choice
import time
from typing import List
import webbrowser

import requests
import collections

Result = collections.namedtuple("Result", "category, id, url, title, description")


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


#@timeit
def find_related_information_by_keyword(keyword: str) -> List[Result]:
    url = f"https://search.talkpython.fm/api/search?q={keyword}"

    resp = requests.get(url)
    resp.raise_for_status()

    found_results = resp.json()

    return [Result(**reference) for reference in found_results.get("results")]


def would_you_link_to_access_one(result_dict: dict):
    if result_dict:
        choice = int(
            input(
                f"Would you like to know more about which one? 1-{len(result_dict)} \n"
            )
        )
        webbrowser.open(f"https://talkpython.fm{result_dict[choice].url}", new=2)
