"""
Solution for "First non-repeating character" kata:
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
"""


def first_non_repeating_letter(string):
    if not isinstance(string, basestring):
        raise ValueError()

    lowered_str = string.lower()

    for idx, char in enumerate(lowered_str):
        popped_char_string = lowered_str[:idx] + lowered_str[idx + 1:]
        if char not in popped_char_string:
            return string[idx]

    return ''
