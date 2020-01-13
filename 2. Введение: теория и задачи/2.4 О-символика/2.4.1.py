"""
Знай сложности алгоритмов: https://habr.com/ru/post/188010/


"""
import numpy as np
import math
import operator

x = 100000
ls = {
    'log2(n!)': np.log2(x ^ 2),
    'n^log2n': x ** np.log2(x),
    '4^n': 4 ** x,
    'log2n ^2': (np.log2(x)) ** 2,
    '2^3n': 2 ** (3 * x),
    'n/log5n': x / math.log(x, 5),
    '3^log2n': 3 ** np.log2(x),
    '2^2^n': 2 ** (x ^ 2),
    'sqrt(n)': np.sqrt(x),
    'log2 log2 x': np.log2(np.log2(x)),
    'n!': np.math.factorial(x),
    'n^sqrt(n)': x ** int(np.sqrt(x)),
    'log3n': math.log(x, 3),
    '7^log2n': 7 ** np.log2(x),
    '2^n': 2 ** x,
    'sqrt(log4n)': np.sqrt(math.log(x, 4)),
    '(log2n)^log2n': np.log2(x) ** np.log2(x),
    'n^2': x ** 2
}

sorted_ls = sorted(ls.items(), key=operator.itemgetter(1))
print(*sorted_ls, sep='\n')
