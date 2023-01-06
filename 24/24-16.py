'''
Файл состоит из прописных латинских букв и цифр.
Будем считать, что это натуральные числа, разделенные буквами.
Найти самое большое число, которое меньше чем 10**9
'''

from string import digits

FILENAME = "data/24-16.txt"

with open(FILENAME) as f:
    num_str, max_num = "0", 0
    for char in f.readline():
        if char in digits:
            num_str += char
        else:
            num = int(num_str)
            if max_num < num < 1e9:
                max_num = num
            num_str = "0"
    print(max_num)
