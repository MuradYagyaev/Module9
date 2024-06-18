# Модуль №9. Инструменты функционального программирования. Генераторные сборки.

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


def create_operation(operation):
    if operation == 'add':
        def operator(x, y):
            return x + y
    elif operation == 'subtract':
        def operator(x, y):
            return x - y
    elif operation == 'multiply':
        def operator(x, y):
            return x * y
    elif operation == 'divide':
        def operator(x, y):
            return x / y
    elif operation == 'exponent':
        def operator(x, y):
            return x ** y
    return operator

def square(x):
    return x ** 2


# Задача 1: Фабрика Функций
print('Фабрика Функций.')
my_func_add = create_operation('add')
print(f'Функция суммирования: {my_func_add(2, 3)}')
my_func_multiply = create_operation('multiply')
print(f'Функция умножения: {my_func_multiply(2, 3)}')
my_func_exponent = create_operation('exponent')
print(F'Функция возведения в степень: {my_func_exponent(2, 3)}')

# Задача 2: Лямбда-Функции
print('Лямбда-Функции.')
my_square = lambda x: x ** 2
print(f'Результат лямбда-функции: {my_square(5)}')
print(f'Результат функции square: {square(5)}')

# Вызываемые Объекты
print('Вызываемые Объекты.')
rectangle = Rect(5, 4)
print(f'Площадь прямоуголника a={rectangle.a} b={rectangle.b}: {rectangle()}')