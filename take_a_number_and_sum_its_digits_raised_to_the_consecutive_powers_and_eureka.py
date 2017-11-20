"""
Solution for "Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....Eureka!!" kata:
https://www.codewars.com/kata/take-a-number-and-sum-its-digits-raised-to-the-consecutive-powers-and-dot-dot-dot-eureka/train/python/59230065f970492c29000016
"""


def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    result = []

    for c in myxrange(a, b + 1):
        if c < 10:
            result.append(c)
        else:
            buff = 0
            for idx, ch in enumerate(str(c)):
                buff += int(ch) ** (idx + 1)

            if buff == c:
                result.append(c)
    return result
