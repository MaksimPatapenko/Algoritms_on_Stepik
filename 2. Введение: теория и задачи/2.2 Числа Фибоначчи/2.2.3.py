"""
Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю.

Даны целые числа (1 <= n <= 10^18) и (2 <= m <= 10^5), необходимо найти остаток от деления n-го числа Фибоначчи на m.

Time Limit: 3 секунды
Memory Limit: 256 MB
"""
import time


def fib_mod(n, m):
    k = 0
    lst = [0, 1]  # Период Пизано всегда начинается с 0, 1
    # Заполняем период Пизано остатками от деления на "m"
    for i in range(2, 6*m):
        lst.append((lst[i - 1] + lst[i - 2]) % m)
        k += 1
        if (lst[i] == 1) and (lst[i-1] == 0):
            break
    return lst[(n % k)]


def main():
    n, m = map(int, input().split())
    start_time = time.time()
    print(fib_mod(n, m))
    print("Time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
