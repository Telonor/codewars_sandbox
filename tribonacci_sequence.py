"""
Solution for "Tribonacci Sequence" kata:
https://www.codewars.com/kata/556deca17c58da83c00002db
"""


def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    result = signature
    for i in xrange(n - len(signature)):
        result.append(result[i] + result[i + 1] + result[i + 2])

    return result
