"""
Задача на программирование: непрерывный рюкзак

Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2*10^6. Каждая из следующих 'n' строк
задаёт стоимость 0≤ci≤2*10^6 и объем 0≤wi≤2*10^6 предмета (n, ci, W, wi - целые числа). Выведите максимальную стоимость
частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально
уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000

Time Limit: 5 секунд
Memory Limit: 256 MB
"""


def calculation(c, items):
    capacity = c
    sack_value = 0
    while len(items) > 0:
        value, volume, value_per_unit = items[0]
        if capacity > 0:
            if capacity >= volume:
                sack_value += volume * value_per_unit
                capacity -= volume
            else:
                sack_value += capacity * value_per_unit
                break
        items = items[1:]
    return '%.3f' % sack_value


n, c = map(int, input().split())
items = []

for i in range(n):
    total_value, volume = map(int, input().split())
    value_per_unit = total_value / volume
    items.append((total_value, volume, value_per_unit))

items.sort(key=lambda x: x[2], reverse=True)
print(calculation(c, items))

