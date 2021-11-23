import functools
from functools import wraps


def is_vowel(ch):
    return ch in 'aiuoye'


def vowel_filter(func):
    @functools.wraps(func)
    def wrapper():
        result = func()
        return [c for c in result if is_vowel(c)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())