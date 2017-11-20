"""
Solution for "Stop gninnipS My sdroW!" kata:
https://www.codewars.com/kata/5264d2b162488dc400000001
"""
MIN_CHARS = 5


def spin_words(sentence):
    return ' '.join(
        [
            word[::-1] if len(word) >= MIN_CHARS else word
            for word in sentence.split(' ')
        ]
    )
