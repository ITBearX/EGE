'''
Исполнитель Июнь15 преобразует число на экране.
У него есть две команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
Сколько существует программ, для которых при исходном
числе 1 результатом вычисления является 45 и при этом
траектория вычислений содержит число 18?
'''


def get_num_ways(number, start):
    if number < start:
        return 0
    if number == start:
        return 1
    if number % 2 == 0:
        return get_num_ways(number//2, start) + get_num_ways(number-1, start)
    return get_num_ways(number - 1, start)


print(get_num_ways(45, 18) * get_num_ways(18, 1))
