'''
Исполнитель Увеличитель преобразует число на экране.
У него есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
Сколько существует программ, для которых при исходном числе 2 результатом
является число 45, и траектория вычислений содержит 14 и НЕ содержит 20?
'''


def get_num_ways(end, start, avoid):
    if end < start or start == avoid:
        return 0
    if end == start:
        return 1
    return (
        get_num_ways(end, start + 1, avoid) +
        get_num_ways(end, start * 2, avoid) +
        get_num_ways(end, start * 3, avoid)
    )


print(get_num_ways(45, 14, 20) * get_num_ways(14, 2, 20))
