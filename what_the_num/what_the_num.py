# -*- coding: utf-8 -*-

"""Main module."""

import requests

URL = "http://numbersapi.com/{number}/{num_type}?json"


def fetch(number, num_type):
    try:
        response = requests.get(URL.format(number=number, num_type=num_type))
    except Exception:
        raise Exception("Something went wrong. Try again.")

    if response.status_code == 404:
        raise Exception("Invalid data provided.")

    if response.status_code in [400, 500]:
        raise Exception("Something went wrong. Please try again.")

    return response.json()


def parse(response):
    # single item response
    if "text" in response:
        return {response['number']: response.get('text')}
    # multiple item responses
    else:
        return {int(key): response[key]['text'] for key in response}


def what_the_num(number, num_type):
    return parse(fetch(number, num_type))
