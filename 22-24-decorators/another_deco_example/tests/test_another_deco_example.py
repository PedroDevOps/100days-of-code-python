from another_deco_example import __version__
from another_deco_example.decorators import get_profile


def test_version():
    assert __version__ == '0.1.0'


def test_get_profile(capfd):
    get_profile(
        "julian",
        False,
        "basketball",
        "soccer",
        pythonista="special honor of the community",
        topcoder="2017 code camp",
    )

    out = capfd.readouterr()[0]
    expected = ["hi from decorator - args:", "('julian', False, 'basketball', 'soccer')",
                "Positional arguments (required):  julian", 'Keyword arguments (not required, default values):  False',
                "Arbitrary argument list (sports):  ('basketball', 'soccer')", "Arbitrary keyword argument dictionary (awards):  {'pythonista': 'special honor of the community', 'topcoder': '2017 code camp'}",
                "hi again from decorator - kwargs:", "{'pythonista': 'special honor of the community', 'topcoder': '2017 code camp'}"]

    output = [line.strip() for line
              in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp
