"""
Solution for "Convert PascalCase string into snake_case" kata:
https://www.codewars.com/kata/529b418d533b76924600085d
"""


def to_underscore(val):
    result = []

    for idx, char in enumerate(str(val)):
        if char.isalpha() and char.isupper():
            char = char.lower()

            if idx:
                char = '_{char}'.format(char=char)

            result.append(char)

        else:
            result.append(char)

    return ''.join(result)
