'''Класс ColoredPoint
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

x — координата точки по оси
?
x
y — координата точки по оси
?
y
color — цвет точки
Класс ColoredPoint должен иметь три свойства:

x — свойство, доступное только для чтения, возвращающее координату точки по оси
?
x
y — свойство, доступное только для чтения, возвращающее координату точки по оси
?
y
color — свойство, доступное только для чтения, возвращающее цвет точки
Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и !=. Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.

Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение, вычисленное с помощью функции hash() на основе кортежа, первым элементом которого является координата точки по оси
?
x, вторым — координата точки по оси
?
y, третьим — цвет точки.

Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.10/Module_5.10.13
'''

class ColoredPoint:
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def color(self):
        return self.__color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, '{self.color}')"

    def __hash__(self):
        return hash((self.x, self.y, self.color))

    def __eq__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return (self.x, self.y, self.color) == (other.x, other.y, other.color)





# INPUT DATA:

# TEST_1:
point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))

# TEST_2:
points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)

# TEST_3:
point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')

# TEST_4:
point1 = ColoredPoint(10, 20, 'black')
point2 = ColoredPoint(10, 20, 'black')

print(point1 == point2)
print(point1 != point2)

# TEST_5:
points = [ColoredPoint(10, 100, 'OliveDrab'), ColoredPoint(73, 76, 'SpringGreen'), ColoredPoint(67, 98, 'Black'),
          ColoredPoint(98, 86, 'DarkGray'), ColoredPoint(28, 29, 'LightYellow'), ColoredPoint(38, 73, 'Coral'),
          ColoredPoint(79, 41, 'DarkGray'), ColoredPoint(51, 83, 'DarkGreen'), ColoredPoint(40, 95, 'BlanchedAlmond'),
          ColoredPoint(84, 65, 'Azure'), ColoredPoint(30, 9, 'DarkSlateBlue'), ColoredPoint(5, 59, 'SkyBlue'),
          ColoredPoint(98, 24, 'Chartreuse'), ColoredPoint(60, 8, 'LightCyan'), ColoredPoint(94, 31, 'YellowGreen'),
          ColoredPoint(36, 30, 'DarkOliveGreen'), ColoredPoint(49, 30, 'Beige'), ColoredPoint(36, 28, 'Chocolate'),
          ColoredPoint(19, 95, 'AntiqueWhite'), ColoredPoint(13, 13, 'AntiqueWhite'),
          ColoredPoint(78, 46, 'LightCoral'), ColoredPoint(56, 25, 'LightSkyBlue'), ColoredPoint(34, 12, 'Magenta'),
          ColoredPoint(49, 22, 'SlateGray'), ColoredPoint(89, 8, 'DarkGoldenRod'), ColoredPoint(39, 84, 'Salmon'),
          ColoredPoint(73, 96, 'MintCream'), ColoredPoint(10, 65, 'MintCream'), ColoredPoint(67, 48, 'Peru'),
          ColoredPoint(76, 13, 'Orchid'), ColoredPoint(11, 73, 'Olive'), ColoredPoint(12, 88, 'Silver'),
          ColoredPoint(89, 85, 'PaleVioletRed'), ColoredPoint(68, 6, 'Purple'), ColoredPoint(56, 64, 'Red'),
          ColoredPoint(7, 25, 'LightGray'), ColoredPoint(41, 76, 'Salmon'), ColoredPoint(28, 99, 'CornflowerBlue'),
          ColoredPoint(47, 7, 'LightSeaGreen'), ColoredPoint(85, 100, 'PeachPuff'), ColoredPoint(5, 86, 'Cyan'),
          ColoredPoint(68, 11, 'Violet'), ColoredPoint(49, 31, 'Violet'), ColoredPoint(93, 55, 'LightCyan'),
          ColoredPoint(8, 42, 'PeachPuff'), ColoredPoint(46, 43, 'Teal'), ColoredPoint(67, 36, 'Navy'),
          ColoredPoint(64, 50, 'Olive'), ColoredPoint(8, 59, 'PaleTurquoise'), ColoredPoint(79, 69, 'Salmon'),
          ColoredPoint(81, 37, 'Fuchsia'), ColoredPoint(86, 84, 'Orchid'), ColoredPoint(25, 100, 'DeepSkyBlue'),
          ColoredPoint(12, 15, 'IndianRed'), ColoredPoint(9, 71, 'LimeGreen'), ColoredPoint(88, 23, 'WhiteSmoke'),
          ColoredPoint(12, 89, 'DodgerBlue'), ColoredPoint(12, 19, 'BurlyWood'), ColoredPoint(12, 66, 'MediumOrchid'),
          ColoredPoint(59, 55, 'PaleGreen'), ColoredPoint(15, 86, 'Black'), ColoredPoint(65, 98, 'DarkOliveGreen'),
          ColoredPoint(86, 83, 'DarkGoldenRod'), ColoredPoint(9, 85, 'DarkOliveGreen'),
          ColoredPoint(73, 46, 'WhiteSmoke'), ColoredPoint(77, 88, 'Beige'), ColoredPoint(43, 64, 'MediumBlue'),
          ColoredPoint(95, 84, 'DodgerBlue'), ColoredPoint(11, 63, 'DarkGray'), ColoredPoint(28, 71, 'DarkSalmon'),
          ColoredPoint(11, 81, 'AliceBlue'), ColoredPoint(80, 26, 'LightCoral'), ColoredPoint(97, 35, 'Tomato'),
          ColoredPoint(12, 82, 'Sienna'), ColoredPoint(100, 23, 'Moccasin'), ColoredPoint(45, 95, 'SeaGreen'),
          ColoredPoint(94, 70, 'LightYellow'), ColoredPoint(63, 76, 'Beige'), ColoredPoint(29, 16, 'FireBrick'),
          ColoredPoint(21, 42, 'HotPink'), ColoredPoint(65, 63, 'DarkOrange'), ColoredPoint(31, 14, 'HotPink'),
          ColoredPoint(55, 67, 'DarkSeaGreen'), ColoredPoint(98, 86, 'YellowGreen'),
          ColoredPoint(60, 36, 'LightSteelBlue'), ColoredPoint(11, 32, 'RoyalBlue'), ColoredPoint(14, 93, 'Red'),
          ColoredPoint(72, 74, 'Fuchsia'), ColoredPoint(53, 98, 'AntiqueWhite'), ColoredPoint(20, 33, 'Gold'),
          ColoredPoint(64, 24, 'LightCyan'), ColoredPoint(96, 58, 'PapayaWhip'), ColoredPoint(57, 79, 'SlateGray'),
          ColoredPoint(47, 75, 'MediumSpringGreen'), ColoredPoint(79, 73, 'Silver'), ColoredPoint(60, 36, 'DodgerBlue'),
          ColoredPoint(86, 12, 'Linen'), ColoredPoint(9, 7, 'RoyalBlue'), ColoredPoint(77, 70, 'Navy'),
          ColoredPoint(83, 66, 'LightCyan')]

for point in points:
    print(point.x, point.y, point.color)

# TEST_6:
point = ColoredPoint(71, 42, 'Indigo')

not_supported = [6952, 208621309.925047, 'Крестик на моей груди, на него ты погляди', False,
                 {'whom': True, 'administration': 1862, 'collection': 56102.956722026},
                 (-326.5668977995, True, 'Темный, мрачный коридор, Я на цыпочках, как вор', 975006604.874278),
                 [3599, 26637.9272286489, 'JeGfEEwKXxCoxlTBTYnL', -25690105773711.2],
                 {'izPmPJcBqaYBUfrSHpin', -850300479586.218, 22.2224616976328}]

for item in not_supported:
    print(item == point)

# TEST_7:
coloredpoint = ColoredPoint(85, 100, 'PeachPuff')
print(coloredpoint.__eq__(1))
print(coloredpoint.__ne__(1.1))

# TEST_8:
coloredpoint = ColoredPoint(1, 2, 'yellow')

try:
    coloredpoint.x = 2
except AttributeError as e:
    print(type(e))

try:
    coloredpoint.y = 3
except AttributeError as e:
    print(type(e))

try:
    coloredpoint.color = 'black'
except AttributeError as e:
    print(type(e))