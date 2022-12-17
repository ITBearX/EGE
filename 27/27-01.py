'''
Найти максимальное произведение двух различных элементов последовательности,
которое кратно 6. Под различными понимаются не различные значения,
а различные номера в последовательности
'''

FILENAME = "data/27-01B.txt"

with open(FILENAME) as f:

    size = int(f.readline())
    numbers = [int(line) for line in f]

    prod1 = (
        max(filter(lambda n: n % 2 == 0 and n % 3 != 0, numbers), default=0) *
        max(filter(lambda n: n % 3 == 0 and n % 2 != 0, numbers), default=0)
    )

    max_x6 = max(filter(lambda n: n % 6 == 0, numbers), default=0)
    max_first = max(numbers)
    numbers.remove(max_first)
    max_second = max(numbers)
    prod2 = max_x6 * (max_first if max_x6 != max_first else max_second)

    print(max(prod1, prod2))
