"""
Задача на программирование: различные слагаемые

По данному числу 1≤n≤10^9 найдите максимальное число 'k', для которого 'n' можно представить как сумму 'k' различных
натуральных слагаемых. Выведите в первой строке число 'k', во второй — 'k' слагаемых.

Sample Input 1:
4

Sample Output 1:
2
1 3

Time Limit: 5 секунд
Memory Limit: 256 MB
"""

lst = []
n = int(input())
a, b = 1, n-1
while b > a:
    lst.append(a)
    a += 1
    b -= a
lst.append(n-sum(lst))
print(len(lst))
print(*lst)
