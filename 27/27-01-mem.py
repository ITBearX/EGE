'''
Найти максимальное произведение двух различных элементов последовательности,
которое кратно 6. Под различными понимаются не различные значения,
а различные номера в последовательности
'''

FILENAME = "data/27-01B.txt"


def main():
    with open(FILENAME) as f:

        size = int(f.readline())
        max_x6, max_x3, max_x2 = 0, 0, 0
        max_first, max_second = 0, 0
        for line in f:
            num = int(line)
            if num > max_first:
                max_first, max_second = num, max_first
            if num % 6 == 0:
                if num > max_x6:
                    max_x6 = num
            elif num % 3 == 0:
                if num > max_x3:
                    max_x3 = num
            elif num % 2 == 0:
                if num > max_x2:
                    max_x2 = num

        prod1 = max_x2 * max_x3
        prod2 = max_x6 * (max_first if max_x6 != max_first else max_second)
        print(max(prod1, prod2))


if __name__ == "__main__":
    main()
