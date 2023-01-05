'''
Значение арифметического выражения:
9**200 + 3**100 - 7 (через ** обозначено возведение в степень)
записали в системе счисления с основанием 3.
Сколько цифр 2 содержится в этой записи?
'''


def convert_base(number, base):
    symbols = "0123456789abcdef"
    s = ""
    while number > 0:
        s += symbols[number % base]
        number //= base
    return s[::-1]


print(convert_base(9**200 + 3**100 - 7, 3).count("2"))
