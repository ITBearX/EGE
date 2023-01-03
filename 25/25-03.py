'''
Найти среди целых чисел, больших 150000, такие, что среди их
нетривиальных делителей (отличных от 1 и самого числа), есть
такой, который оканчивается на 2 или 3 и больше 4.
Найдите 6 таких наименьших чисел и для каждого их них
наибольший нетривиальный делитель, оканчивающийся на 2 или 3.
'''


def find_div(n):

    def check(d):
        return d > 4 and d % 10 in (2, 3)

    div, m = 0, 2
    while m * m <= n:
        if n % m == 0:
            if check(n//m):
                return n//m
            if check(m):
                div = m
        m += 1
    return div


number, cnt = 150000, 0
while cnt < 6:
    number += 1
    div = find_div(number)
    if div > 0:
        cnt += 1
        print(number, div)
