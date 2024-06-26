'''Класс RaiseTo
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень. При создании экземпляра класс должен принимать один аргумент:

degree — показатель степени
Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса RaiseTo должен возвращать значение x в степени degree.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RaiseTo нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.6/Module_5.6.10'''
class RaiseTo:

    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return eval(f'{x} ** {self.degree}')

# INPUT DATA:

# TEST_1:
raise_to_two = RaiseTo(2)

print(raise_to_two(2))
print(raise_to_two(3))
print(raise_to_two(4))

# TEST_2:
raise_to_three = RaiseTo(3)
raise_to_four = RaiseTo(4)

print(raise_to_three(3))
print(raise_to_four(2))

# TEST_3:
raise_to_ten = RaiseTo(10)
digits = [150, 191, 2, 184, 195, 83, 158, 153, 85, 183, 21, 64, 179, 79, 10, 69, 52, 49, 189, 48, 57, 58, 78, 190, 17,
          118, 90, 104, 53, 129, 86, 159, 11, 121, 136, 146, 61, 18, 31, 113, 200, 59, 176, 97, 169, 91, 173, 12, 162,
          110, 95, 197, 135, 34, 41, 54, 7, 127, 155, 160, 56, 35, 151, 4, 88, 143, 101, 42, 38, 0, 125, 45, 137, 24,
          109, 22, 3, 47, 139, 71, 193, 75, 116, 180, 37, 134, 63, 108, 157, 5, 123, 6, 126, 148, 188, 194, 36, 168, 14,
          107]

for digit in digits:
    print(raise_to_ten(digit))

# TEST_4:
raise_to_zero = RaiseTo(0)
raise_to_negativ = RaiseTo(-1)
digits = [124, 215, 515, 2353654, 1247, 54, 2145, 925, 245, 2156, 26]

for digit in digits:
    print(raise_to_zero(digit), raise_to_negativ(digit), sep='; ')