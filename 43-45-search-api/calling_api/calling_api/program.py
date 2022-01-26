#!/usr/bin/env python3
from collections import defaultdict
import api


def main():
    results = []
    results_dict = defaultdict(list)
    keyword = input("What keywords to search for? <ENTER WORDS>\n")
    results = api.find_related_information_by_keyword(keyword)
    if len(results) > 0:
        print(f'It was found {len(results)} references to "{keyword}"')
    for idx, result in enumerate(results, 1):
        results_dict[idx] = result
        print(f"{idx} - {result.title} - {result.category} - {result.url}")
    api.would_you_link_to_access_one(results_dict)


if __name__ == "__main__":
    main()
