'''
На вход подается последовательность символов, заканчивающаяся символом #
Вывести на экран латинскую букву, встречающуюся чаще всего и какое количество
раз она встречается. Если несколько букв встречаются такое количество раз,
вывести их все, без разделителей.
Строчные и прописные буквы не отличаются.
'''

from string import ascii_uppercase


FILENAME = "data/27-04B.txt"

with open(FILENAME) as f:

    line = f.readline().upper()
    freq = {letter: line.count(letter) for letter in ascii_uppercase}
    highest = max(freq.values())
    print(
        "".join(
            [letter for letter in ascii_uppercase if freq[letter] == highest]
        ),
        highest,
        sep=""
    )
