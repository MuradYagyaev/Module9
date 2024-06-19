# Модуль №9. Инструменты функционального программирования. Декораторы.

def is_prime(func):
    def my_decor(*args):
        result = func(*args)
        if result < 0:
            result1 = -result
        else:
            result1 = result
        if type(result1) is float:
            print('Число с плавающей точкой:', end=' ')
        elif result1 == 1 or result1 == 0:
            number_type = 'Натуральное число'
        elif result1 == 2:
            number_type = 'Простое'
        elif result1 > 2:
            number_type = 'Простое'
            for i in range(2, result1 // 2 + 1):
                if result1 % i == 0:
                    number_type = 'Составное'
                    break
        print(number_type, end=': ')
        return result
    return my_decor

@is_prime
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 3, 6))
print(sum_three(50, 112, 277))
print(sum_three(11, 10, 9))
