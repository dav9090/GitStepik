'''Класс Temperature
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия. При создании экземпляра класс должен принимать один аргумент:

temperature — температура в градусах по шкале Цельсия
Класс Temperature должен иметь один метод экземпляра:

to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
Класс Temperature должен иметь один метод класса:

from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры
Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:

<температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:

при приведении к типу bool значением экземпляра класса Temperature должно являться значение True, если его температура выше нуля, или False в противном случае
при приведении к типу int значением экземпляра класса Temperature должна являться его температура в виде целого числа с отброшенной дробной частью
при приведении к типу float значением экземпляра класса Temperature должна являться его температура в виде вещественного числа

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Temperature нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.7/Module_5.7.11'''

class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return 9/5*self.temperature+32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls(5/9*(temperature-32))

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

# INPUT DATA:

# TEST_1:
t = Temperature(5.5)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

# TEST_2:
t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))

# TEST_3:
t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

# TEST_4:
t = Temperature.from_fahrenheit(-459.67)

print(t)
print(bool(t))
print(int(t))
print(f'{float(t):.2f}')
print(f'{t.to_fahrenheit():.2f}')

# TEST_5:
data = [54.36, -9, -155, -165, 128, 49.74, -46, 112, -47.25, -129, 82.6, -73.6, -39, -78.4, 44, 3.11, -52.8, 59, -68.52,
        172, 55, -55.18, 88, -51, -88.37, 82, 31.8, -50, -44.99, 75.33, -15.71, 125, 192, -17.79, 72.1, -179, 52, -193,
        62.28, -95.63, 94.43, -14.92, 36, -4, -71.6, 169, -74, -147, -45.89, 32.19, 85.9, -46.59, 0.28, 119, 56.31,
        -70.37, 71, -66, -11, 169, 42, -169, -91, 40.12, 4.72, -197, 135, -136, -98.78, 0, -58, -64.44, 200, -31.8,
        -75.18, -11.75, 4, -65.92, -35.47, 19.76, 27, -71, -142, 75.75, -28.41, -7, 72.25, -188, 56.53, 9, 17.44, 30,
        -1.53, 170, 53.12, -144, 6.39, -71.0, 169, -71.43, -75.36]

for item in data:
    t = Temperature(item)
    print(bool(t))

# TEST_6:
t = Temperature.from_fahrenheit(132.7)
print(t)