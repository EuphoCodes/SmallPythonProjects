"""Birthday Paradox, by EuphoCodes https://euphocodes.com
idea from https://en.wikipedia.org/wiki/Birthday_problem

In probability theory, the birthday problem asks for the probability that,
in a set of n randomly chosen people, at least two will share a birthday."""

import datetime, random


def get_birthdays(number_of_birthdays):
    start_of_year = datetime.date(2023, 1, 1)
    return [start_of_year + datetime.timedelta(random.randint(0, 364)) for _ in range(number_of_birthdays)]


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthday_a in enumerate(birthdays):
        for birthday_b in birthdays[a + 1:]:
            if birthday_a == birthday_b:
                return birthday_a


def format_date(date):
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    month_name = MONTHS[date.month - 1]
    return f'{month_name} {date.day}'


MAX_BIRTHDAYS = 1000
SIMULATIONS_NUM = 100000

while True:
    num_b_days = input('How many birthdays shall I generate? (Max 1000)\n> ')
    if num_b_days.isdecimal() and (0 < int(num_b_days) <= MAX_BIRTHDAYS):
        num_b_days = int(num_b_days)
        break

print(f'Here are {num_b_days} birthdays:')
birthdays = get_birthdays(num_b_days)
print(", ".join(format_date(birthday) for birthday in birthdays))

match = get_match(birthdays)
if match:
    print(f'multiple people have a birthday on {format_date(match)}')
else:
    print('there are no people with the same birthday.')

print(f'running {SIMULATIONS_NUM} simulations')
input('Press Enter to begin...')
sim_match = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(num_b_days)
    if get_match(birthdays) != None:
        simMatch = sim_match + 1
probability = round(sim_match / SIMULATIONS_NUM * 100, 2)

print(
    f"Out of {SIMULATIONS_NUM} simulations of {num_b_days} people, there was a matching birthday in that group {sim_match} times.")
print(f"This means that {num_b_days} people have a {probability}% chance of having a matching birthday in their group.")
