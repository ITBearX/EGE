'''
Исполнитель Июнь15 преобразует число на экране.
У него есть две команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
Сколько существует программ, для которых при исходном
числе 1 результатом вычисления является 45 и при этом
траектория вычислений содержит число 18?
'''


def get_num_ways(end, start):
    num_ways = [0]*(end+1)
    num_ways[start] = 1
    for number in range(start+1, end+1):
        if number % 2 != 0:
            num_ways[number] = num_ways[number-1]
        else:
            num_ways[number] = num_ways[number-1] + num_ways[number//2]
    return num_ways[end]


print(get_num_ways(45, 18) * get_num_ways(18, 1))
