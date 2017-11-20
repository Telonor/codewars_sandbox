"""
Solution for "Roman Numerals Encoder" kata:
https://www.codewars.com/kata/51b62bf6a9c58071c600001b
"""
CONVERT_TABLE = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
)


def solution(n):
    result = ''
    for arabic, roman in CONVERT_TABLE:
        while n >= arabic:
            result += roman
            n -= arabic

    return result
