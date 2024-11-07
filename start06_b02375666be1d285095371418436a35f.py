
from calendar import month_name
from typing import List, Tuple, Dict, Optional, Union, Literal
import random


class WrongDate(Exception):
    def __init__(self, reason):
        self. __reason = reason

    def __repr__(self):
        return self.__reason


class Date:
    year: int
    month: int
    day: int

    @classmethod
    def __init__(self, year: int, month: Union[int, str], day: int):
        self.year = year
        self.month = month
        self.day = day
        month_name = self.monthindex.get(self.month)
        if not isinstance(self.year, int):
            raise WrongDate(f": year {self.year} is not an integer")
        if (self.year < 1900 or self.year > 2100):
            raise WrongDate(
                f": year {self.year} is not between 1900 and 2100")
        if (month_name == None):
            raise WrongDate(
                f": month {self.month} is not in a domain")
        if not isinstance(self.day, int):
            raise WrongDate(f": day {self.day} is not an integer")
        if not isleapyear(self.year):
            if (self.day < 1 or self.day > self.normalyear[month_name]):
                raise WrongDate(
                    f": day {self.day} is not between 1 and days in month")
        else:
            if (self.day < 1 or self.day > self.leapyear[month_name]):
                raise WrongDate(
                    f": day {self.day} is not between 1 and days in month")

    def weekday(self) -> str:
        day = 0
        summ = 0
        for i in range(1900, self.year):
            if isleapyear(i):
                day += 366
            else:
                day += 365
        n = self.monthindex.get(self.month)
        if not isleapyear(self.year):
            for l in range(0, n):
                summ += self.normalyear[l]
        else:
            for j in range(0, n):
                summ += self.leapyear[j]
        day = day + summ + self.day
        day = day % 7
        return self.weekdays[day]

    @classmethod
    def __repr__(self) -> str:
        return (f" {self.year}, {self.month}, {self.day}")

    @classmethod
    def __str__(self) -> str:
        day = self.day
        month = self.monthnames[self.monthindex.get(self.month)][0]
        year = self.year
        return (f" {day} {month} {year} ")

        # In monthnames, the first name is the 'preferred name', which will be used
        # when printing. Any further names are optional names.
        # One can also add different languages.

    monthnames: Tuple[List[Union[str, int]], ...] = (
        ['january', 'jan', 1, '1'], ['february', 'feb', '2', 2],
        ['march', 3, '3'],
        ['april', 4, '4'],  ['may', 5, '5'], ['june', 6, '6'],
        ['july', 7, '7'],  ['august', 8, '8'],
        ['september', 'sept', 9, '9'], ['october', 'oct', 10, '10'],
        ['november', 'nov', 11, '11'],
        ['december', 'dec', 12, '12'])

    monthindex: Dict[Union[str, int], int] = {name: ind
                                              for ind, names in enumerate(monthnames) for name in names}

    normalyear = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leapyear = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    weekdays = ('sunday', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday')


def lucky_dates():
    return [(1956, 1, 31, 'tuesday', 'birthday of Guido Van Rossumm'),
            (1945, 'october', 24, 'wednesday', 'Founding of UN'),
            (1969, 'july', 20, 'sunday', 'first moon landing'),
            (1991, 'dec', 16, 'monday', 'independence of Kazakhstan'),
            (1961, 'april', 12, 'wednesday', 'space flight of Yuri Gagarin'),
            (2022, 'september', 17, 'saturday', 'Nursultan renamed into Astana')]


def unlucky_dates():
    return [(1912, 'april', 15, 'monday', 'sinking of Titanic'),
            (1929, 'october', 29, 'tuesday',
             'Wall Street Market Crash (Black Tuesday)'),
            (1959, 'february', 3, 'tuesday', 'the day the music died'),
            (1977, 'march', 27, 'sunday', 'Los Rodeos collision'),
            (2019, 'march', 23, 'saturday', 'Astana renamed into Nursultan'),
            (2022, 'october', 21, 'friday', '!! deadline of this exercise !!')]


@staticmethod
def isleapyear(y: int) -> bool:

    if (y % 4 == 0) and (y % 100 != 0):
        return True
    elif (y % 400 == 0) and (y % 100 == 0):
        return True
    else:
        return False


def tester():
    for date in (('a', 1, 1), (2, 'x', 3), (3, 4, 'y'),
                 (1900, 'x', 12),
                 (1899, 1, 1), (1900, 1, 1), (1900, 'jan', 1),
                 (1910, 12, 31), (1911, 3.14, 8),
                 (1900, 'feb', 28), (1900, 'feb', 29),
                 ('a', 4, 5), (1899, 'jan', 25), (1910, 5, 25),
                 (1967, 'wrongember', 12), (1910, 'oct', 25), (1910, 'jan', 25.1),
                 (1919, 'feb', 29), (1920, 'feb', 29)):
        try:
            y, m, d = date
            print("testing {} {} {}". format(y, m, d))

            dt = Date(y, m, d)
            print("date = {}". format(dt))

        except WrongDate as w:
            print("   exception {}". format(w))
        print("")

    dates = lucky_dates() + unlucky_dates()
    random. shuffle(dates)

    for date in dates:
        y, m, d, w1, importance = date
        dt = Date(y, m, d)
        w2 = dt. weekday()
        print("{} : {} ({})". format(importance, dt, w2))
        if w1 != w2:
            print(
                "function weekday returned {} but correct day is {} !!!". format(w2, w1))
        print("")

    print("tests finished")


tester()
