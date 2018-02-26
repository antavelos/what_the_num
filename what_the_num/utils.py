# -*- coding: utf-8 -*-

"""Helper functions module."""

import re

TYPES = ["trivia", "math", "date", "year"]

DATE_REGEX = re.compile('^(0?[1-9]|1[0-2])/(0?[1-9]|1[0-9]|2[0-9]|3[0-1])$')
RANGE_REGEX = re.compile('^\d+(\.\.\d+)?((,\d+))*?$')


def _match_regex(pattern, string):
    try:
        return pattern.match(string).group() == string
    except AttributeError:
        return False


def is_date(string):
    return _match_regex(DATE_REGEX, string)


def is_range(string):
    return _match_regex(RANGE_REGEX, string)


def is_valid_number(number):
    return isinstance(number, int) or \
        number == "random" or \
        is_date(str(number)) or \
        is_range(str(number))
