'''Класс Time
Реализуйте класс Time, описывающий время на цифровых часах. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
Экземпляр класса Time должен иметь следующее неформальное строковое представление:

<количество часов в формате HH>:<количество минут в формате MM>
Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:

результатом сложения с помощью оператора + должен являться новый экземпляр класса Time, количество часов которого равно сумме часов исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
результатом сложения с помощью оператора += должен являться левый экземпляр класса Time, количество часов которого увеличено на количество часов правого экземпляра класса Time, количество минут — на количество минут правого экземпляра класса Time
Примечание 1. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Никаких ограничений касательно реализации класса Time нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.5/Module_5.5.20
'''

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24
        self.minutes = minutes
        if minutes >= 60:
            self.hours += minutes//60
            self.minutes = minutes % 60

    def __str__(self):
        return f"{self.hours:>02}:{self.minutes:>02}"

    # def __repr__(self):
    #     return '{}({}, {})'.format(self.__class__.__name__, self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Time):
            hours = (self.hours + other.hours) % 24
            minutes = self.minutes+other.minutes
            if minutes >= 60:
                hours += minutes // 60
                minutes = minutes % 60
            return Time(hours, minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.hours = self.hours % 24

            self.minutes += other.minutes
            if self.minutes >= 60:
                self.hours += self.minutes // 60
                self.minutes = self.minutes % 60
            return self
        return NotImplemented

# INPUT DATA:

# TEST_1:
time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

# TEST_2:
time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

# TEST_3:
time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)

# TEST_4:
time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1 + time2)

# TEST_5:
t = Time(13, 0)
print(t)
id1 = id(t)

t += Time(2, 30)
id2 = id(t)
print(t)
print(id1 == id2)

# TEST_6:
t = Time(13, 0)
times = [(68, 74), (74, 63), (82, 77), (97, 91), (42, 42), (28, 69), (26, 97), (88, 84), (50, 57), (95, 6), (100, 72),
         (18, 17), (76, 38), (9, 5), (65, 11), (16, 9), (56, 64), (57, 93), (35, 22), (57, 68), (100, 95), (6, 59),
         (34, 97), (55, 88), (69, 95), (50, 70), (38, 68), (19, 74), (79, 28), (42, 45), (34, 74), (27, 89), (74, 17),
         (59, 35), (83, 65), (50, 18), (82, 62), (34, 64), (23, 11), (62, 55), (28, 41), (16, 52), (62, 85), (95, 27),
         (56, 59), (45, 31), (82, 39), (45, 22), (22, 39), (28, 78), (68, 72), (97, 22), (68, 45), (6, 19), (62, 69),
         (17, 29), (53, 86), (44, 52), (70, 68), (6, 33), (83, 89), (96, 66), (7, 40), (68, 68), (63, 77), (48, 35),
         (68, 40), (13, 57), (55, 94), (10, 97), (41, 90), (72, 6), (80, 69), (69, 90), (53, 94), (65, 40), (73, 60),
         (99, 13), (32, 95), (65, 75), (79, 5), (11, 58), (41, 49), (88, 66), (13, 43), (88, 23), (67, 64), (65, 9),
         (90, 91), (26, 21), (77, 84), (71, 36), (59, 73), (41, 23), (86, 22), (90, 24), (67, 50), (5, 9), (12, 29),
         (17, 6)]

for hour, minute in times:
    new_time = t + Time(hour, minute)
    print(new_time)

# TEST_7:
t = Time(40, 80)
print(t.__add__([]))
print(t.__iadd__('bee'))

# TEST_8:
t = Time(22, 0)
t += Time(3, 0)
print(t)

# TEST_9:
t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)