'''
Вывод таблицы истинности логической функции для задания 2.
Заменить выражение в func на соответствующую варианту функцию
'''


def func(x, y, z):
    return y and x or y and not z


print("x y z -> f")
print("-" * 12)
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(x, y, z, "->", int(func(x, y, z)))
