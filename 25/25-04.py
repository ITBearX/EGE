'''
Найти среди целых чисел, принадлежащих отрезку [100000; 300000],
такие, у которых наименьшая разница между максимальным и минимальным
нетривиальными делителями (отличными от 1 и самого числа), но
при этом эта разница больше 0.
Для каждого найденного числа вывести мин. и макс. делители
в порядке возрастания произведения этих делителей.
'''


START, END = 100000, 300000


def find_divs(n):
    m = 2
    while m * m < n:
        if n % m == 0:
            return m, n//m
        m += 1
    return None


divs_data = []
for number in range(START, END+1):
    divs = find_divs(number)
    if divs is not None:
        divs_data.append(divs)

a, b = min(divs_data, key=lambda d: d[1] - d[0])
min_spread = b - a

result = [(a, b) for a, b in divs_data if b - a == min_spread]
result.sort(key=lambda d: d[0] * d[1])

for a, b in result:
    print(a, b)
