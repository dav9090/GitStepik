'''
Класс Peekable ??
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс Peekable должен иметь один метод экземпляра:

peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.10/Module_6.1.20
'''
import itertools
import copy
class Peekable:
    def __init__(self, iterable):

        self.peeked, self.it = itertools.tee(iterable, 2)
        self.flag = False
        self.counter = 0


    def __iter__(self):
        return self
    def __next__(self):
        self.counter += 1
        return next(self.it)





    def peek(self, default='lol'):

        p = copy.deepcopy(self.peeked)
        if self.counter > 0:
            for _ in range(self.counter):
                try:
                    next(self.peeked)
                except StopIteration:
                    if default == 'lol':
                        raise StopIteration
                    return default

        if default == 'lol':
            s = next(self.peeked)
            self.peeked = p
            return s

        s = next(self.peeked, default)
        self.peeked = p
        return s


# INPUT DATA:

# TEST_1:
iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)

# TEST_2:
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# TEST_3:
iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))

# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

# TEST_5:
from itertools import islice

iterator = Peekable([n ** 2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))

# TEST_6:
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))

# TEST_7:
from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')