'''
В файле содержится последовательность целых чисел от -10000 до 10000.
Определить количество пар последовательности, в которых элементы разные,
большее из из чисел пары четно, а меньшее нечетно, и при этом хотя бы
один элемент пары больше среднего арифметического нечетных элементов
последовательности. Под парой подразумеваются два идущих подряд элемента.
Вывести количество найденных пар, а затем наименьшую сумму элементов
таких пар.
'''

from statistics import mean


FILENAME = "data/17-01.txt"

with open(FILENAME) as f:

    numbers = [int(line) for line in f]
    odd_mean = mean(filter(lambda n: n % 2 != 0, numbers))

    pairs = zip(numbers[:-1], numbers[1:])
    proper_sums = []

    for a, b in pairs:
        if a != b and (a > odd_mean or b > odd_mean):
            s = a + b
            if s % 2 != 0 and max(a, b) % 2 == 0:
                proper_sums.append(s)

    print(len(proper_sums), min(proper_sums))
