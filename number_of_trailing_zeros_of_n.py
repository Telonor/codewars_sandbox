"""
Solution for "Number of trailing zeros of N!" kata:
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
"""


def zeros(n):
    float_five = float(5)

    result = n / float_five
    zeros = int(result)
    power = 2

    while result > 1:
        result = n / float_five ** power
        zeros += int(result)
        power += 1

    return zeros
