'''
Коля собирает монеты номиналом 1, 2, 3, 5, 10, 15, 20, 50 по годам.
Каждый номинал был обязательно отчеканен в каждый год.
Скольких видов монет с 1961 по 1991 годы не хватает мальчику в коллекции
и какова наибольшая сумма номиналов недостающих монет в самый "провальный"
год с точки зрения отсутствующих номиналов?

В файле в первой строке количество собранных монет.
В последующих строках по два числа: год чеканки и номинал монеты
'''

FILENAME = "data/26-20.txt"
START_YEAR, END_YEAR = 1961, 1991
VALUES = {1, 2, 3, 5, 10, 15, 20, 50}

need = len(VALUES)
collected = {year: set() for year in range(START_YEAR, END_YEAR + 1)}

with open(FILENAME) as f:
    num = int(f.readline())
    for line in f:
        year, coin = tuple(map(int, line.split()))
        if START_YEAR <= year <= END_YEAR and coin in VALUES:
            collected[year].add(coin)
    print(sum(need - len(coins) for year, coins in collected.items()))
    print(sum(VALUES) - min(sum(coins) for year, coins in collected.items()))
