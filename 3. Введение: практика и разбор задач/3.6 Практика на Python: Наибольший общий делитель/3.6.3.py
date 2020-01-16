"""
Наивный алгоритм нахождения наибольшего общего делителя (НОД).
"""


def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a,b) + 1)):  # функция reversed для перебора в обратном порядке
        if d == 0 or a % d == b % d == 0:
            return d


print(gcd1(0, 0))
