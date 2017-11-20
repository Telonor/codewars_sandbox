"""
Solution for "Not very secure" kata:
https://www.codewars.com/kata/526dbd6c8c0eb53254000110
"""
import re
ptr = re.compile(r'^[a-zA-Z0-9]+$')


def alphanumeric(string):
    return bool(ptr.match(string))
