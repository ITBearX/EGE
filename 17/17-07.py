'''
Рассматривается множество целых чисел, принадлежащих
отрезку [1425; 9605], которые делятся на 3 или 4 и не делятся
на 5, 7, 9.
Найти сотое по порядку такое число и количество не таких чисел
на этом отрезке
'''

START, END = 1425, 9605


def is_valid(num):
    if num % 3 and num % 4:  # не делится ни на 3, ни на 4
        return False
    if num % 5 and num % 7 and num % 9:  # не делится на 5, 7 и 9
        return True
    return False


valid_numbers = [num for num in range(START, END+1) if is_valid(num)]

print(
    valid_numbers[99],
    END - START + 1 - len(valid_numbers)
)
