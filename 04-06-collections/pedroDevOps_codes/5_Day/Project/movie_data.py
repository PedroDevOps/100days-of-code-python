#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose:
Project: 100Days of code with Python
Progress: Round1, Day5 = R1D5
Challenge: https://pybit.es/codechallenge13.html
References:
OBS:
    flake8 was used: # flake8 movie_data.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive movie_data.py
    bandit was used: # bandit -r movie_data.py
"""

import csv
import os
from collections import defaultdict, namedtuple
from typing import Dict

MOVIE_DATA = 'movie_metadata.csv'
MOVIE_DATA_SMALL = 'movie_metadata_small.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    try:
        os.chdir('../Data')
        movies_directors_defaultdict = defaultdict(list)
        with open(MOVIE_DATA_SMALL) as csvfile:
            lines = csv.DictReader(csvfile)
            for row in lines:
                director_name = row['director_name']
                movie_info = Movie(
                    title=row['movie_title'].replace(
                        '\xa0', ''), year=row['title_year'], score=float(
                        row['imdb_score']))
                movies_directors_defaultdict[director_name].append(movie_info)
        return movies_directors_defaultdict
    except Exception:
        print("Something went wrong inside get_movies_by_director()")
        raise


def get_average_scores(all_directors_defaultdict):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    try:
        for directors_name, list_of_movies in all_directors_defaultdict.items():
            if len(list_of_movies) < 1:
                del all_directors_defaultdict[directors_name]
        return all_directors_defaultdict
    except Exception:
        print("Something went wrong inside get_average_scores(directors)")
        exit


def _calc_mean(list_of_movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    count = 0.0
    n = 0
    # print(movies)
    for movie in list_of_movies:
        count = count + movie.score
        n = n + 1
    print()
    mean = count / n

    return mean


def print_results(filtered_directors_defaultdict):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    i = 0
    for directors_name, list_of_movies in filtered_directors_defaultdict.items():
        print(
            '{}. {} {}'.format(
                i,
                directors_name,
                _calc_mean(list_of_movies)))
        print(sep_line)
        for movie in list_of_movies:
            print("{}] {} {}".format(movie.year, movie.title, movie.score))
        i = i + 1
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    all_directors_defaultdict = get_movies_by_director()
    filtered_directors_defaultdict = get_average_scores(
        all_directors_defaultdict)

   # for directors_name,list_of_movies in filtered_directors_defaultdict.items():
   #     print ("The key value is a {}".format(type(directors_name)))
   #     print ("The value is a {}".format(type(list_of_movies)))

    #directors = get_average_scores(directors)
    print_results(filtered_directors_defaultdict)


if __name__ == '__main__':
    main()
