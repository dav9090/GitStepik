'''Класс RomanNumeral🌶️🌶️
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен принимать один аргумент:

number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.

Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

Примечание 4. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.7/Module_5.7.12'''
from functools import total_ordering
@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    romanNumeralMap = (('M', 1000),
                       ('CM', 900),
                       ('D', 500),
                       ('CD', 400),
                       ('C', 100),
                       ('XC', 90),
                       ('L', 50),
                       ('XL', 40),
                       ('X', 10),
                       ('IX', 9),
                       ('V', 5),
                       ('IV', 4),
                       ('I', 1))
    @classmethod
    def to_roman(cls, n):
        if n == 0:
            return 'N'

        result = ""
        for numeral, integer in cls.romanNumeralMap:
            while n >= integer:
                result += numeral
                n -= integer
        return result
    @classmethod
    def from_roman(cls, s):

        if s == 'N':
            return 0

        result = 0
        index = 0
        for numeral, integer in cls.romanNumeralMap:
            while s[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result


    def __str__(self):
        return f'{self.number}'

    def __int__(self):
        return int(self.from_roman(self.number))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumeral(self.to_roman(self.from_roman(self.number)+other.from_roman(other.number)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return RomanNumeral(self.to_roman(self.from_roman(self.number)-other.from_roman(other.number)))
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.from_roman(self.number) == other.from_roman(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.from_roman(self.number) < other.from_roman(other.number)
        return NotImplemented


# INPUT DATA:

# TEST_1:
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

# TEST_2:
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

# TEST_3:
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_6:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V')

print(number)
print(int(number))

# TEST_7:
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))
