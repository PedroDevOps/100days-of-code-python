#!/usr/bin/env python3

import re


MOVIES = """1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)""".split(
    "\n"
)


def getMoviesWithVowelsTogether(movies_list):
    pat = re.compile(
        r"""
            (?:           # non-capturing parenthesis, so I don't want store this match in groups()
            [aAeEiIoOuU]  # only vowels
            )             # closing of non-capturing parenthesis
            {2,}           # exactly 2 of the previously grouped subpattern
        """,
        re.VERBOSE,
    )

    return [
        movie for movie in movies_list if re.findall(pat, movie) != []
    ]


def getMoviesWithExactlyWords_regex(movies_list):
    for movie in movies_list:
        print("this is a Match result:{}".format(re.match(r"The", movie)))
        print("this is a search result:{}".format(re.search(r"The", movie)))
        if "The" in movie:
            m = re.search(r"The", movie)
            print(m.group())


def getMoviesWithExactly2Words(movies_List):
    pat = re.compile(
        r"""
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  """,
        re.VERBOSE,
    )
    return [pat.match(movie) for movie in movies_List]


def getMoviesThatHasThisWord(movies_list, search_word):
    return [movie for movie in movies_list if search_word.lower() in movie.lower()]


def main():
    print("This is a list of movies")
    for movie in MOVIES:
        print(movie)
    print("")
    print("And this is a list of movies that have only two words in their title")
    for movie_match in getMoviesWithExactly2Words(MOVIES):
        if movie_match is not None:
            print(movie_match.group())
    print("")
    print(
        "And This is a list of movies that have this especific word 'The' in their title"
    )
    for movie_match in getMoviesThatHasThisWord(MOVIES, "The"):
        if movie_match is not None:
            print(movie_match)
    print("")
    print(
        "And This is a list of movies that have at least two vowels together"
    )
    for movie_match in getMoviesWithVowelsTogether(MOVIES):
        print(movie_match)
    print("")

if __name__ == "__main__":
    main()
