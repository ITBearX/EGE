'''
На вход программы подается: в первой строке количество
троек входных чисел. Далее - тройки целых чисел.
Нужно выбрать из каждой тройки одно число так, чтобы
сумма всех выбранных чисел была максимальна и не кратна 10
В ответе должна быть сумма выбранных чисел
'''

FILENAME = "data/27-08B.txt"


def process_triple(triple):

    n1, n2, max_n = triple
    if n1 > n2:
        n2, n1 = n1, n2
    if n2 > max_n:
        max_n, n2 = n2, max_n

    d1, d2 = max_n - n1, max_n - n2
    min_diff = 100000
    if d1 % 10 != 0:
        min_diff = d1
    if d2 % 10 != 0 and d2 < min_diff:
        min_diff = d2

    return max_n, min_diff


with open(FILENAME) as f:

    max_s, min_diff = 0, 100000
    for _ in range(int(f.readline())):
        number, diff = process_triple(map(int, f.readline().split()))
        max_s += number
        if diff < min_diff:
            min_diff = diff

    if max_s % 10 == 0:
        max_s -= min_diff

    print(max_s)
