#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Using itertools.cycle
Project: 100Days of code with Python
Progress: Round1, Day17 = R1D19
challenge: https://codechalleng.es/bites/65/
"""

import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DICT}", DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
    valid dictionary words. Use _get_permutations_draw and provided
    dictionary"""
    return [word for word in _get_permutations_draw(draw) if word in dictionary]


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
    use itertools.permutations (order of letters matters)"""
    all_words = []
    for word_size in range(len(draw), 1, -1):
        draw_permutations = list(itertools.permutations(draw, word_size))
        #all_words.extend([''.join(permutation).lower() for permutation in draw_permutations if (''.join(permutation)).lower() not in all_words])
        words_of_n_size = []
        for permutation in draw_permutations:
            if ("".join(permutation)).lower() not in words_of_n_size:
                words_of_n_size.append(("".join(permutation)).lower())
        all_words.extend(words_of_n_size)
    return all_words


def main():
    draw = "T, I, I, G, T, T, L"
    draw_splited = draw.split(", ")
    print(get_possible_dict_words(draw_splited))


if __name__ == "__main__":
    main()
