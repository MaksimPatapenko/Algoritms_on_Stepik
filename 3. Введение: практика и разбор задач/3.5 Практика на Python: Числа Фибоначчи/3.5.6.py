import time
from matplotlib import pyplot as plt


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


# Перенесем все алгоритмы из пунктов 3.5.1, 3.5.3, 3.5.4 соответственно:
# 3.5.1
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# 3.5.3
def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


# 3.5.3
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# print(timed(fib1, 20))
# print(timed(memo, 20))  # fib2
# print(timed(fib3, 20))


# Построим график зависимости времени работы от аргумента функций fib1 и fib3
def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


print(compare([fib3], list(range(200))))
