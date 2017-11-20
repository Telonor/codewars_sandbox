"""
Solution for "Unique In Order" kata:
https://www.codewars.com/kata/54e6533c92449cc251001667
"""


def unique_in_order(iterable):
    return [
        x for idx, x in enumerate(iterable) if not idx or x != iterable[idx-1]
    ]
