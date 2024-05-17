'''Декоратор @CountCalls
Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции. Счетчик вызовов должен быть доступен по атрибуту calls.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CountCalls, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.6/Module_5.6.16'''

import functools
calls = 0
def CountCalls(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper


@CountCalls
def add(a, b):
    return a + b


print(add(1, 2))
print(add(2, 3))
print(add.calls)