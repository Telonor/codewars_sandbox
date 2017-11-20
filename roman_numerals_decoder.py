"""
Solution for "Roman Numerals Decoder" kata:
https://www.codewars.com/kata/51b6249c4612257ac0000005
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
    result = 0
    for arabic, roman in CONVERT_TABLE:
        while n.startswith(roman):
            result += arabic
            n = n[len(roman):]

    return result
