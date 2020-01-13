"""
Задача на программирование: наибольший общий делитель.

По данным двум числам 1 <= a,b <= 2 * 10^9 найдите их наибольший общий делитель.

Time Limit: 3 секунды
Memory Limit: 256 MB
"""
import time


# Алгоритм Евклида
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

# Оптимизированный алгоритм. Если b != 0 --> b = True. Аналогично с переменной "a".
# def gcd(a, b):
#     return gcd(b, a % b) if b else a


def main():
    a, b = map(int, input().split())
    start_time = time.time()
    print(gcd(a, b))
    print("Time: %s seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
