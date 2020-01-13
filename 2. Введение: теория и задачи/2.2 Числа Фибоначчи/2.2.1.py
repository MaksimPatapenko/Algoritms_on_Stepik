"""
Задача на программирование: небольшое число Фибоначчи.

Дано целое число 1 <= n <= 40, необходимо вычислить n-e число Фибоначчи (напомним, что F0 = 0, F1 = 1 и
Fn = Fn-1 + Fn-2 при n >= 2).

Time Limit: 3 секунды
Memory Limit: 256 MB
"""
import time


def fib(n):
    fib0, fib1 = 0, 1
    for i in range(n - 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1


def main():
    n = int(input())
    start_time = time.time()
    print(fib(n))
    print("Time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
