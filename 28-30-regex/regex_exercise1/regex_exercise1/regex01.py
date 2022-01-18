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
    for movie in movies_List:
        print(movie, pat.match(movie))


def main():
    print(MOVIES)
    getMoviesWithExactly2Words(MOVIES)


if __name__ == "__main__":
    main()
