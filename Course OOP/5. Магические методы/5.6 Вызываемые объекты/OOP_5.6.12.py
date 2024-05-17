''' Класс QuadraticPolynomial
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — коэффициент
�
a квадратного трехчлена
b — коэффициент
�
b квадратного трехчлена
c — коэффициент
�
c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса QuadraticPolynomial должен возвращать значение выражения
c — коэффициенты квадратного трехчлена.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.6/Module_5.6.12'''

class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c



# INPUT DATA:

# TEST_1:
func = QuadraticPolynomial(1, 2, 1)

print(func(1))
print(func(2))

# TEST_2:
func = QuadraticPolynomial(1, 3, 4)

print(func(1))
print(func(2))

# TEST_3:
coefficients = [(167, 121, 106), (91, 69, 180), (76, 185, 94), (65, 117, 134), (115, 108, 105), (15, 198, 90),
                (66, 28, 98), (131, 105, 130), (92, 119, 103), (139, 95, 147), (32, 137, 148), (51, 40, 170),
                (146, 129, 89), (174, 126, 185), (146, 31, 89), (53, 68, 198), (129, 182, 186), (152, 111, 48),
                (77, 96, 94), (44, 92, 154), (63, 92, 148), (164, 187, 158), (107, 8, 70), (174, 33, 81), (48, 152, 68),
                (107, 166, 40), (192, 81, 177), (14, 6, 161), (146, 172, 109), (148, 161, 157), (109, 108, 29),
                (179, 88, 15), (164, 123, 26), (138, 23, 52), (44, 96, 26), (137, 21, 85), (143, 123, 178),
                (127, 116, 71), (188, 181, 78), (171, 7, 75), (170, 195, 129), (111, 158, 69), (175, 150, 158),
                (162, 81, 198), (74, 51, 35), (138, 116, 173), (116, 186, 141), (100, 78, 37), (148, 148, 99),
                (91, 153, 161), (196, 13, 33), (198, 63, 63), (195, 103, 191), (38, 162, 71), (48, 122, 170),
                (14, 180, 107), (6, 131, 35), (119, 183, 160), (88, 59, 45), (150, 138, 9), (109, 123, 84),
                (65, 117, 139), (91, 22, 196), (162, 184, 169), (121, 21, 26), (45, 98, 23), (20, 7, 57), (190, 185, 4),
                (26, 30, 45), (10, 181, 196), (42, 80, 64), (189, 57, 100), (145, 185, 34), (47, 15, 24), (171, 31, 77),
                (180, 179, 44), (98, 114, 196), (98, 34, 153), (83, 88, 199), (51, 90, 0), (148, 155, 94),
                (72, 163, 182), (103, 7, 67), (35, 123, 116), (194, 171, 154), (113, 99, 16), (5, 143, 48), (47, 89, 5),
                (164, 166, 166), (49, 103, 48), (172, 37, 39), (168, 125, 91), (179, 39, 31), (119, 9, 146),
                (48, 172, 40), (174, 30, 34), (129, 42, 47), (62, 108, 124), (184, 162, 194), (80, 138, 117)]

digits = [6, 151, 188, 86, 108, 0, 12, 24, 41, 34, 160, 57, 126, 189, 110, 90, 136, 162, 168, 69, 97, 17, 158, 38, 183,
          159, 54, 134, 18, 184, 107, 200, 194, 125, 85, 129, 179, 11, 4, 10, 36, 155, 176, 143, 52, 49, 173, 137, 37,
          5, 79, 45, 21, 157, 35, 47, 146, 104, 148, 7, 48, 63, 191, 56, 101, 83, 64, 22, 116, 75, 113, 109, 123, 59,
          58, 95, 135, 169, 118, 31, 121, 150, 53, 88, 91, 153, 127, 180, 14, 190, 71, 193, 42, 2, 195, 3, 139, 197, 61,
          78]

for i in range(len(coefficients)):
    a, b, c = coefficients[i]
    func = QuadraticPolynomial(a, b, c)
    print(func(digits[i]))