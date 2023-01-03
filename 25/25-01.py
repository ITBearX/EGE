'''
Среди чисел, принадлежащих отрезку [150000; 200000],
найти имеющие ровно 48 различных натуральных делителей,
не считая 1 и самого числа.
Для каждого найденного числа вывести самый большой делитель,
в порядке возрастания делителей
'''

START, END = 150000, 200000


def find_divs(n):
    divs = set()
    m = 2
    while m * m <= n:
        if n % m == 0:
            divs.update({m, n//m})
        m += 1
    return divs


result = []
for number in range(START, END+1):
    divs = find_divs(number)
    if len(divs) == 48:
        result.append(max(divs))
print(sorted(result))
