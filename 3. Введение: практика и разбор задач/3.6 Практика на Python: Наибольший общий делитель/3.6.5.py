"""
Другая версия алгоритма Евклида.
"""


def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)
# Пример: gcd3(24, 9) -> gcd3(6, 9) -> gcd3(6, 3) -> gcd3(0, 3) -> return 3
