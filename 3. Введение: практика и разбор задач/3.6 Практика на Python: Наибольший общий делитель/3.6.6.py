"""
Рекурсивная реализация алгоритма Евклида.
"""


def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)
