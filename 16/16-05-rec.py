'''
Алгоритм вычисления значения функции F(n), где n - целое
неотрицательное число, задан следующими соотношениями:
F(0) = 0
F(1) = 1
F(2) = 3
F(n) = F(n-2) + F(n/2) + 1, при n > 2 и n - четно,
F(n) = F(n-1) + F(n-3), при n > 2 и n - нечетно.
Чему равно значение функции F(35)?
'''


def f(n):
    if n < 2:
        return n
    if n == 2:
        return 3
    if n % 2 == 0:
        return f(n-2) + f(n//2) + 1
    return f(n-1) + f(n-3)


print(f(35))
