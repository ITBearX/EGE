'''
Исполнитель Утроитель преобразует число на экране.
У него есть две команды, которым присвоены номера:
1. Прибавить 2
2. Умножить на 3
Сколько существует программ, которые число 2 преобразуют в 28?
'''


def get_num_ways(number, start):
    if number < start:
        return 0
    if number == start:
        return 1
    num_ways = get_num_ways(number - 2, start)
    if number % 3 == 0:
        num_ways += get_num_ways(number // 3, start)
    return num_ways


print(get_num_ways(28, 2))
