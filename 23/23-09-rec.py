'''
Исполнитель Увеличитель преобразует число на экране.
У него есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
Сколько существует программ, для которых при исходном числе 2 результатом
является число 45, и траектория вычислений содержит 14 и НЕ содержит 20?
'''


def get_num_ways(number, start, avoid):

    if number < start or number == avoid:
        return 0
    if number == start:
        return 1

    num_ways = get_num_ways(number-1, start, avoid)
    if number % 2 == 0:
        num_ways += get_num_ways(number//2, start, avoid)
    if number % 3 == 0:
        num_ways += get_num_ways(number//3, start, avoid)
    return num_ways


print(get_num_ways(45, 14, 20) * get_num_ways(14, 2, 20))
