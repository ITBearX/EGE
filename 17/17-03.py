'''
В файле содержится последовательность целых чисел от -10000 до 10000.
Определить количество троек последовательности, в которых все три числа
не оканчиваются на 5, и максимальное число, входящее в такую тройку.
Под тройкой подразумеваются три идущих подряд элемента.
'''

FILENAME = "data/17-03.txt"

with open(FILENAME) as f:

    numbers = [int(line) for line in f]
    triples = zip(numbers[:-2], numbers[1:-1], numbers[2:])

    proper_triples = [
        triple for triple in triples
        if all(map(lambda x: x % 10 != 5, triple))
    ]
    print(len(proper_triples), max(map(max, proper_triples)))
