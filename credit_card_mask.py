"""
Solution for "Credit Card Mask: kata:
https://www.codewars.com/kata/5412509bd436bd33920011bc
"""
UNMASKED = 4


def maskify(cc):
    return '#' * (len(cc) - UNMASKED) + cc[-UNMASKED:]
