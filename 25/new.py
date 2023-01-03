START = 1415
STOP = 9925


def is_valid(number):
    if number % 7 != 0:
        return False
    if number % 3 == 0:
        return False
    if number % 5 == 0:
        return False
    if number % 13 == 0:
        return False
    if number % 49 == 0:
        return False
    return True


cnt = 0
s = 0
for number in range(START, STOP+1):
    if is_valid(number):
        cnt += 1
        s += number
print(cnt, s)


valid_numbers = [
    number for number in range(1415, 9926)
    if is_valid(number)
]

print(len(valid_numbers), sum(valid_numbers))
