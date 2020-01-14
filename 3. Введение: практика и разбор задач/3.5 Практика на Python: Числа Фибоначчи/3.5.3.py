from functools import lru_cache


def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

######################################################################################
# Плюсом подхода с декораторами, является то, что мы можем использовать его с функцией,
# которая ничего про кеширование не знает.
######################################################################################


# fib1 = memo(fib1)
# print(fib1(80))

# Вместо декоратора memo можно использовать готовый декоратор lru_cache из модуля functools
fib1 = lru_cache(maxsize=None)(fib1)
print(fib1(8000))
