#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose:
Project: 100Days of code with Python
Progress: Round1, Day5 = R1D5
Challenge: https://pybit.es/codechallenge13.html
References: work with various data structures
OBS:
    flake8 was used: # flake8 movie_data.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive movie_data.py
    bandit was used: # bandit -r movie_data.py
Requirements:
    Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data.
    Take movies of year >= 1960.
    Print the top 20 highest rated directors with their movies ordered desc on rating.
"""

import csv
import os
from collections import defaultdict, namedtuple
from typing import Counter, Dict

MOVIE_DATA = 'movie_metadata.csv'
MOVIE_DATA_SMALL = 'movie_metadata_small.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''
    Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)
    '''
    try:
        os.chdir('../Data')
        movies_directors_defaultdict = defaultdict(list)
        with open(MOVIE_DATA) as csvfile:
            lines = csv.DictReader(csvfile)
            for row in lines:
                if ((row['title_year']) != ""):
                    if(int(row['title_year']) >= MIN_YEAR):
                        director_name = row['director_name']
                        movie_info = Movie(title=row['movie_title'].replace('\xa0', ''), year=int(row['title_year']), score=float(row['imdb_score']))
                        movies_directors_defaultdict[director_name].append(movie_info)
                    movies_directors_defaultdict[director_name].sort(key=lambda x: x[2], reverse=True)
                else:
                    continue
        return movies_directors_defaultdict
    except Exception:
        print("Something went wrong inside get_movies_by_director()")
        exit


def get_average_scores(directors_defaultdict):
    """
    Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest score in descending order. 
    return only the top NUM_TOP_DIRECTORS highest rated directors
    Only take directors into account with >= MIN_MOVIES
    
    """
    try:
        Directors_avg = namedtuple('Directors_avg','director_name average_score')
        directors_avg_score_list = []
        for director, list_of_movies in directors_defaultdict.items():
            if len(list_of_movies) >= MIN_MOVIES:
                directors_avg = Directors_avg(director_name=director,average_score=_calc_mean(list_of_movies))
                directors_avg_score_list.append(directors_avg)
            directors_avg_score_list.sort(key=lambda x: x[1], reverse=True)
        return directors_avg_score_list[:NUM_TOP_DIRECTORS]
    except Exception:
        print("Something went wrong inside get_average_scores(directors)")
        exit


def _calc_mean(director_movies_list):
    '''
    Helper method to calculate mean of list of Movie namedtuples
    '''
    imdb_score_sum = 0
    for movie in director_movies_list:
        imdb_score_sum += movie.score
    imdb_score_mean = imdb_score_sum / len(director_movies_list)
    return round(imdb_score_mean,1)


def print_results(directors_avg_score_list, directors_defaultdict):
    '''
    Print directors ordered by highest average rating. 
    For each director print his/her movies also ordered by highest rated movie.
    '''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    i = 0
    for directors_name, avg_score in directors_avg_score_list:
        print('{}. {} {}'.format(i, directors_name, round(avg_score, 1)))
        print(sep_line)
        for movie in directors_defaultdict[directors_name]:
            print("{}] {} {}".format(movie.year,movie.title,round(movie.score,1)))
        i = i + 1
        print()


def main():
    '''
    This is the main function
    '''
    directors_defaultdict = get_movies_by_director()
    directors_avg_score_list = get_average_scores(directors_defaultdict)
    print_results(directors_avg_score_list, directors_defaultdict)


if __name__ == '__main__':
    main()
