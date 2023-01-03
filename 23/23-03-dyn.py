'''
Исполнитель Утроитель преобразует число на экране.
У него есть две команды, которым присвоены номера:
1. Прибавить 2
2. Умножить на 3
Сколько существует программ, которые число 2 преобразуют в 28?
'''


def get_num_ways(end, start):
    num_ways = [0]*(end+1)
    num_ways[start] = 1
    for number in range(start+1, end+1):
        if number % 3 != 0:
            num_ways[number] = num_ways[number-2]
        else:
            num_ways[number] = num_ways[number-2] + num_ways[number//3]
    return num_ways[end]


print(get_num_ways(28, 2))
