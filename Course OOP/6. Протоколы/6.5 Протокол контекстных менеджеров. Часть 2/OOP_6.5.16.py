'''Класс AdvancedTimer
Реализуйте класс AdvancedTimer. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса AdvancedTimer должен являться многоразовым контекстным менеджером, который замеряет время выполнения кода внутри каждого блока with.

Также экземпляр класса AdvancedTimer должен иметь четыре атрибута:

last_run — число, представляющее время выполнения кода внутри последнего блока with
runs — список чисел, каждое из которых представляет время выполнения какого-либо кода внутри блока with. Первый элемент списка должен представлять собой время выполнения кода внутри первого блока with, второй элемент — внутри второго блока with, и так далее
min — число, представляющее минимальное время выполнения кода внутри блока with среди всех замеров
max — число, представляющее максимальное время выполнения кода внутри блока with среди всех замеров
Если экземпляр класса AdvancedTimer ни разу не использовался для замера скорости выполнения какого-либо блока кода, значения атрибутов last_run, min и max должны равняться None.

Примечание 1. Наглядные примеры использования класса AdvancedTimer продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс AdvancedTimer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_6/Module_6.5/Module_6.5.16
'''

from time import perf_counter

class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.last_run = perf_counter()
        self.copy_last_run = self.last_run
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last_run = perf_counter() - self.last_run
        self.runs.append(perf_counter() - self.copy_last_run)
        if not self.min or self.runs[-1] < self.min:
            self.min = self.runs[-1]
        if not self.max or self.runs[-1] > self.max:
            self.max = self.runs[-1]



# INPUT DATA:

# TEST_1:
timer = AdvancedTimer()

print(timer.runs)
print(timer.last_run)
print(timer.min)
print(timer.max)

# TEST_2:
from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))

# TEST_3:
from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)

with timer:
    sleep(0.7)

with timer:
    sleep(1)

print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.min, 1))
print(round(timer.max, 1))

# TEST_4:
import time


def func1():
    time.sleep(1.3)
    return


def func2():
    time.sleep(1.7)
    return


def func3():
    time.sleep(1.1)
    return


def func4():
    time.sleep(0.3)
    return


timer = AdvancedTimer()

funcs = [func2, func1, func4, func3]

for func in funcs:
    with timer:
        func()

print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.last_run, 1))
print(round(timer.min, 1))
print(round(timer.max, 1))
