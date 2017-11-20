"""
Solution for "Sum of Digits / Digital Root" kata:
https://www.codewars.com/kata/541c8630095125aba6000c00
"""


def digital_root(n):
    n = abs(int(n))
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
