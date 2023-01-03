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
    num_ways = [0]*(end+1)
    num_ways[start] = 1
    for number in range(start, end+1):
        if number != avoid:
            current = num_ways[number]
            if number+1 <= end:
                num_ways[number+1] += current
            if number*2 <= end:
                num_ways[number*2] += current
            if number*3 <= end:
                num_ways[number*3] += current
        else:
            num_ways[number] = 0
    return num_ways[end]


print(get_num_ways(45, 14, 20) * get_num_ways(14, 2, 20))
