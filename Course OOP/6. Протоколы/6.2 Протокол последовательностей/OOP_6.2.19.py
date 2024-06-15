'''
Класс Grouper🌶️🌶️
Нередко нам приходится группировать объекты по определенному признаку. Например, строки можно сгруппировать по их длине или первому символу. Реализуйте класс Grouper, описывающий объект, который группирует элементы некоторого итерируемого объекта на основе ключевой функции. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект
key — ключевая функция
Элементы попадают в одну группу, если при их передаче в ключевую функцию она возвращает один и тот же результат.  Например, elem1 и elem2 попадают в одну группу, если key(elem1) == key(elem2). Значение key(elem1) будем называть ключом группы, а elem1 и elem2 — элементами группы по этому ключу.

Класс Grouper должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в нужную группу экземпляра класса Grouper
group_for() — метод, принимающий в качестве аргумента произвольный объект, определяющий, в какую группу экземпляра класса Grouper попадет этот объект, и возвращающий ключ этой группы
При передаче экземпляра класса Grouper в функцию len() должно возвращаться количество групп в нем.

Помимо этого, экземпляр класса Grouper должен быть итерируемым объектом, то есть позволять перебирать свои группы, например, с помощью цикла for. В данном случае группа — это кортеж, первым элементом которого является ключ группы, вторым — список элементов группы. Группы при итерировании могут располагаться в произвольном порядке.

Также экземпляр класса Grouper должен поддерживать операцию проверки на принадлежность с помощью оператора in, в которой проверяется наличие в экземпляре класса Grouper группы с искомым ключом.

Наконец, экземпляр класса Grouper должен позволять получать элементы группы по ключу. В данном случае элементы группы должны быть представлены в виде списка, при этом элементы в списке должны располагаться в том порядке, в котором они были добавлены.

Примечание 1. Экземпляр класса Grouper не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса Grouper измениться  не должен.

Примечание 2. Реализация класса Grouper может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_6/Module_6.2/Module_6.2.19
'''
import copy


class Grouper:

    def __init__(self, iterable, key):
        self.key = key
        self.iterable = copy.deepcopy(iterable)
        self.lst = {}
        for i in self.iterable:
            if key(i) not in self.lst:
                self.lst[key(i)] = []
        for i in self.lst:
            for j in self.iterable:
                if i == self.key(j):
                    self.lst[i].append(j)

    def add(self, obj):
        if self.key(obj) not in self.lst:
            self.lst[self.key(obj)] = [obj]
        else:
            self.lst[self.key(obj)].append(obj)

    def group_for(self, obj):
        return self.key(obj)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __delitem__(self, key):
        del self.lst[key]

    def __iter__(self):
        return iter(self.lst.items())

    def __contains__(self, item):
        return item in self.lst


# INPUT DATA:

# TEST_1:
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])

# TEST_2:
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(3 in grouper)
print('bee' in grouper)

# TEST_3:
grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(len(grouper))

# TEST_4:
grouper = Grouper(['hi'], key=lambda s: s[0])

print(grouper.group_for('hello'))
print(grouper.group_for('bee'))
print(grouper['h'])
print('b' in grouper)

# TEST_5:
data = [504, 506, 503, 507, 507, 508, 504, 510, 500, 503, 501, 502, 503, 502, 502, 510, 502, 500, 503, 508, 508, 502,
        507, 500, 502, 501, 502, 504, 505, 505, 500, 501, 507, 504, 509, 507, 508, 508, 502, 510, 503, 501, 505, 501,
        510, 505, 500, 507, 510, 507, 506, 507, 501, 502, 504, 506, 501, 501, 506, 502, 508, 505, 509, 509, 502, 506,
        507, 505, 505, 507, 503, 505, 504, 510, 505, 503, 508, 508, 504, 504, 510, 501, 506, 503, 502, 508, 507, 503,
        501, 506, 505, 506, 504, 504, 505, 503, 507, 504, 507, 510]

grouper = Grouper(data, key=lambda x: x % 2 == 0)
print(grouper[True])
print(grouper[False])

# TEST_6:
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

grouper = Grouper(persons, key=lambda x: x.height)
print(sorted(grouper))

# TEST_7:
grouper = Grouper([], key=lambda x: x)
print(*grouper)

# TEST_8:
d = list(range(1, 100))
grouper = Grouper(d, bool)
print(*grouper)

d.append(100)
print(*grouper)

# TEST_9:
d = range(1, 100)
grouper = Grouper(d, bool)
print(*grouper)

grouper.add(100)
print(*grouper)
