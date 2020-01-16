"""
Задача на программирование: покрыть отрезки точками

По данным "n" отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
хотя бы одну из точек.
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих "n" строк содержит по два числа 0≤l≤r≤10^90, задающих
начало и конец отрезка. Выведите оптимальное число "m" точек и сами "m" точек. Если таких множеств точек несколько,
выведите любое из них.

Sample Input 1:
4
4 7
1 3
2 5
5 6

Sample Output 1:
2
3 6
"""


def dots(segments):
    resulting_segments = []
    while len(segments) > 0:
        if len(segments) < 2:
            seg = segments.pop()
            resulting_segments.append(seg)
        else:
            a, b = segments[0], segments[1]
            if b[0] <= a[1]:
                left, right = b[0], b[1] if b[1] <= a[1] else a[1]
                overlapping = (left, right)
                segments = segments[2:]
                segments = [overlapping] + segments
            else:
                resulting_segments.append(segments[0])
                segments = segments[1:]
    return [x[1] for x in resulting_segments]


n = int(input())
segments = []
for i in range(n):
    segments.append(tuple(map(int, input().split())))
segments.sort(key=lambda x: (x[0], x[1]))
result = dots(segments)
print(len(result))
print(' '.join(map(str, result)))
