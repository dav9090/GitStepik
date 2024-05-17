'''Класс Dice
Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней. При создании экземпляра класс должен принимать один аргумент:

sides — количество граней игрального кубика
Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов. При вызове он должен возвращать значение случайной грани игрального кубика. Например, если кубик имеет 6 граней, экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6].

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Dice нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.6/Module_5.6.11'''
import random
class Dice:

    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return random.randint(1, self.sides)




# INPUT DATA:

# TEST_1:
kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])

# TEST_2:
kingdice = Dice(2)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])

# TEST_3:
kingdice = Dice(1)

print(kingdice() == 1)
print(kingdice() in [1, 2])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])

# TEST_4:
kingdice = Dice(100)

for _ in range(100):
    print(kingdice() in range(1, 101))

# TEST_5:
kingdice = Dice(20)
print(callable(kingdice))
