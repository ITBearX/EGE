'''
Исполнитель Утроитель преобразует число на экране.
У него есть две команды, которым присвоены номера:
1. Прибавить 2
2. Умножить на 3
Сколько существует программ, которые число 2 преобразуют в 28?
'''


def get_num_ways(end, start):
    if end < start:
        return 0
    if end == start:
        return 1
    return get_num_ways(end, start+2) + get_num_ways(end, start*3)


print(get_num_ways(28, 2))
