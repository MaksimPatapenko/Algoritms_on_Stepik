from PIL import Image
from rcviz import viz


# Медленный алгоритм, для нахождения числа Фибоначчи. Изменяется экспоненциально.
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# Построение графов для чисел Фибоначчи
# old_fib1 = fib1
# fib1 = viz(fib1)
# PYTHONWARNINGS = "ignore"
# fib1(5)
# Image.open('./fib1.png').show()
