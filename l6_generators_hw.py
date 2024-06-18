# Модуль №9. Инструменты функционального программирования. Генераторы.

def all_variants(string):
    for length in range(len(string)):
        for i in range(len(string) - length):
            yield string[i: i + length + 1]


a = all_variants('abcdef')
for i in a:
    print(i)
