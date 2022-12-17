'''
Найти минимальное произведение двух элементов последовательности
'''

FILENAME = "data/27-03B.txt"

with open(FILENAME) as f:

    size = int(f.readline())
    numbers = [int(line) for line in f]

    pos = sorted(filter(lambda n: n >= 0, numbers))
    neg = sorted(filter(lambda n: n < 0, numbers))

    if len(pos) == 0:
        print(neg[-1] * neg[-2])
    elif len(neg) == 0:
        print(pos[0] * pos[1])
    else:
        print(neg[0] * pos[-1])
