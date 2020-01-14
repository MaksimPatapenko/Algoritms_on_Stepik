from PIL import Image
from rcviz import viz


cache = {}


# Быстрый алгоритм, для нахождения числа Фибоначчи. Берём готовое число из кэша. Для больших аргументах -
# упирается в ограничение.
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n - 2)
    return cache[n]


print(fib2(800))
