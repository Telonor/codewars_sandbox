"""
Solution for "Regex validate PIN code" kata:
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
"""
import re


def validate_pin(pin):
    return re.match('^(:?\d{4}|\d{6})$', pin) is not None
