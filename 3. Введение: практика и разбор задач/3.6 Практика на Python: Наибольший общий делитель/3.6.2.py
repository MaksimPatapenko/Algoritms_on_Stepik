"""
Тест на нахождение двух целых неотрицательных чисел (gcd)
"""
import random


def test(gcd, n_iter=100):
    """
    Тест проверяет переданную ему функцию gcd на корректность.
    :param gcd:
    :param n_iter:
    :return:
    """
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0
