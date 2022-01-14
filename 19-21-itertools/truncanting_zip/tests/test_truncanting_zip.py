from truncanting_zip import __version__
from truncanting_zip.event import get_attendees


def test_version():
    assert __version__ == "0.1.0"


def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output
