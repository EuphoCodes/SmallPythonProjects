"""Birthday Paradox, by EuphoCodes https://euphocodes.com
idea from https://en.wikipedia.org/wiki/Birthday_problem

In probability theory, the birthday problem asks for the probability that,
in a set of n randomly chosen people, at least two will share a birthday."""

import datetime, random

def getBirthdays(numberOfBirthdays):
    #returns a list of birthdays given a number of birthdays.
    birthdays = []
    for i in range(numberOfBirthdays):
        #datetime.date takes the args in order (year, month, day) like all dates should be.
        startOfYear = datetime.date(2023, 1, 1)

        #get a random day of the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear +randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    #tests if every index in the birthday list is unique.
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique so nothing is returned.

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA