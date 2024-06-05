'''
 Класс LoopTracker🌶️
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент
empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора
first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение AttributeError с текстом:
Исходный итерируемый объект пуст
last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
Последнего элемента нет
Класс LoopTracker должен иметь один метод экземпляра:

is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.10/Module_6.1.21
'''

import copy
class LoopTracker:
    def __init__(self, iterable):
        self.it = iter(iterable)
        self.iterable = list(iterable)
        self.access = 0
        self.empty_access = 0
        self.__last = '123123'

    def __iter__(self):
        return self.it
    def __next__(self):
        try:
            s = next(self.it)
            self.access += 1
            self.__last = s
            return s
        except StopIteration:
            self.empty_access += 1


    @property
    def accesses(self):
        return self.access
    @property
    def empty_accesses(self):
        return self.empty_access
    @property
    def first(self):
        try:
            return self.iterable[0]
        except:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.__last == '123123':
            raise AttributeError('Последнего элемента нет')
        return self.__last
    def is_empty(self):
        p = copy.deepcopy(self.it)
        try:
            next(p)
            return False
        except StopIteration:
            return True



# INPUT DATA:

# TEST_1:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))
print('test 1 passed')
# TEST_2:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)
print('test 2 passed')
# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)
print('test 3 passed')
# TEST_4:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)
print('test 4 passed')
# TEST_5:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass

print(loop_tracker.empty_accesses)
print('test 5 passed')
# TEST_6:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
print('test 6 passed')
# TEST_7:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))
print('test 7 passed')
# TEST_8:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)

# TEST_11:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())

# TEST_13:
loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))
