'''
Определить максимальную длину последовательности одинаковых символов в файле
'''

FILENAME = "data/24-01.txt"

with open(FILENAME) as f:
    line = f.readline()
    series = []
    cnt = 1
    for cur_char, prev_char in zip(line[1:], line[:-1]):
        if cur_char == prev_char:
            cnt += 1
        else:
            series.append(cnt)
            cnt = 1
    print(max(series))
