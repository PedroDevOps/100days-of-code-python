#!/usr/bin/env python3

import logbook
import sys

import research


def main():
    print("Avengers research (2015)")
    print()
    structured_avengers_Data = research.init()

    print("The oldest 5 Avengers to join are:")
    avengers = research.who_is_the_oldest_avenger(structured_avengers_Data)
    for idx, avenger in enumerate(avengers[:5], 1):
        print(
            f"{idx} - {avenger.Name_Alias} joined the Avegenrs Initiative in {avenger.Full_Reserve_Avengers_Intro} {avenger.Year}, more than {avenger.Years_since_joining} year of work"
        )
    print()

    print("The 5 most recent Avengers to join are:")
    avengers = research.who_is_the_most_recent_avenger(structured_avengers_Data)
    for idx, avenger in enumerate(avengers[:5], 1):
        print(
            f"{idx} - {avenger.Name_Alias} joined the Avegenrs Initiative in {avenger.Full_Reserve_Avengers_Intro} {avenger.Year}, more than {avenger.Years_since_joining} year of work"
        )
    print()

    print("The 5 Avengers that died the most:")
    avengers = research.who_died_the_most(structured_avengers_Data)
    for idx, avenger in enumerate(avengers[:5], 1):
        print(f"{idx} - {avenger[0]}")
    print()

    avengers = research.is_there_a_avenger_called(structured_avengers_Data)
    for idx, avenger in enumerate(avengers, 1):
        print(f"{idx} - {avenger.Name_Alias}")
    print()

def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = "Logging initialized, level: {}, mode: {}".format(
        level, "stdout mode" if not filename else "file mode: " + filename
    )
    logger = logbook.Logger("Startup")
    logger.notice(msg)


if __name__ == "__main__":
    init_logging()
    main()
