'''
Алгоритм вычисления значения функции F(n), где n - натуральное число,
задан следующими соотношениями (числа Фибоначчи):
F(1) = 1
F(2) = 2
F(n) = F(n-1) + F(n-2), при n > 2
Чему равно значение функции F(17)?
'''

n = 17
f, fp = 2, 1
for i in range(3, n+1):
    f, fp = f + fp, f

print(f)
