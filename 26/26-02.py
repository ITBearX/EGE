'''
Предприятию требуется закупить большое количество различных вагонов.
На рынке имеется множество предложений по вагонам, каждый из которых
имеет свою цену. Для закупки выделяются средства таким образом, чтобы
купить все виды вагонов, и при этом как можно больше вагонов каждого
вида, но не потратить на каждый вид вагонов сумму денег, большую чем S.
Определить, сколько всего вагонов удастся купить и какая общая сумма
денег будет потрачена.

В файле в первой строке через пробел: количество вагонов на рынке и
лимит суммы денег на каждый вид вагонов.
В последующих строках по два числа через пробел: номер вида вагона и
цена этого вагона.
'''

FILENAME = "data/26-02.txt"

with open(FILENAME) as f:

    num_offers, max_purchase = map(int, f.readline().split())
    wagons = dict()
    for line in f:
        wag_type, price = map(int, line.split())
        wagons.setdefault(wag_type, []).append(price)

    num, total = 0, 0
    for wag_type, offers in wagons.items():
        purchase = 0
        for price in sorted(offers):
            if purchase + price > max_purchase:
                break
            purchase += price
            num += 1
        total += purchase

    print(num, total)
