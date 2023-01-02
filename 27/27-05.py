'''
На вход программы подается последовательность символов,
заканчивающаяся символом #
Найти слово максимальной длины, не длинее 15 символов.
Слова отделяются пробелами, знаками препинания .,; или
переносом строки
'''

import re

FILENAME = "data/27-05B.txt"

with open(FILENAME) as f:
    words = []
    for line in f:
        words.extend(re.split(r"[ .,;#]", line))
    print(max(filter(lambda w: len(w) <= 15, words), key=len))
