'''
У ростовщика скопилось некоторое количество векселей.
Каждый вексель соответствует целому количеству рублей.
Найти минимальную сумму денег, которую он НЕ сможет выдать,
используя имеющиеся векселя, и количество векселей, которые
он должен будет использовать, чтобы выдать сумму на 1 рубль
меньше.
'''

from itertools import accumulate


FILENAME = "data/26-01.txt"

with open(FILENAME) as f:
    size = f.readline()
    bills = [int(line) for line in f]
    bills.sort()
    for n, (b, s) in enumerate(zip(bills[1:], accumulate(bills)), start=1):
        if s + 1 < b:
            print(s + 1, n)
            break
