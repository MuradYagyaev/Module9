# Модуль №9. Инструменты функционального программирования. Итераторы.

class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        if self.start % 2:
            self.i = self.start - 1
        else:
            self.i = self.start - 2
        return self

    def __next__(self):
        self.i += 2
        if self.i > self.end:
            raise StopIteration()
        return self.i



enum_1 = EvenNumbers(10, 25)
for i in enum_1:
    print(i)
