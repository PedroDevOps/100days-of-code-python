from regex_exercise1 import __version__
from regex_exercise1.regex01 import getMoviesWithExactlyWords


MOVIES = """1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)""".split("\n")


def test_getMoviesWithExactlyWords(movies_list=MOVIES):
    expected = ["2. The Godfather (1972)", "10. The Wizard of Oz (1939)"]
    assert getMoviesWithExactlyWords(movies_list) == expected


def test_version():
    assert __version__ == "0.1.0"
