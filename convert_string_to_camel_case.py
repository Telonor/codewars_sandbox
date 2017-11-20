"""
Solution for "Convert string to camel case" kata:
https://www.codewars.com/kata/517abf86da9663f1d2000003
"""
UNDERSCORE = '_'
DASH = '-'


def to_camel_case(text):
    # empty input
    if not text:
        return text

    text = text.replace(DASH, UNDERSCORE)

    return ''.join(
        [
            word.capitalize() if (not idx and word[0].istitle()) or idx
            else word for idx, word in enumerate(text.split(UNDERSCORE))
        ]
    )
