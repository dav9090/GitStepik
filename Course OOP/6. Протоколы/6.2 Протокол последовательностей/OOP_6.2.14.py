'''
​​​​​Класс OrderedSet
Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан, начальный набор элементов считается пустым
Класс OrderedSet должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного множества
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества, если он в нем присутствует
При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.

Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы, реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют равную длину и содержат равные элементы без учета их расположения.

Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.

Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_6/Module_6.2/Module_6.2.14
'''
import copy


# 4 тест # TEST_4:
# True
# False
# True
# False
# False
class OrderedSet:

    def __init__(self, iterable=[]):
        self.iterable = []
        for i in iterable:
            if i not in self.iterable:
                self.iterable.append(i)

    def add(self, item):
        if item not in self.iterable:
            self.iterable.append(item)


    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        return iter(self.iterable)

    def __contains__(self, item):
        return item in self.iterable

    def __eq__(self, other):

        if isinstance(other, OrderedSet):
            return all(i == j for i, j in zip(self.iterable, other.iterable))
        if isinstance(other, list):
            return False
            #return all(i == j for i, j in zip(self.iterable, other))
        if isinstance(other, set):
            return set(self.iterable) == set(other)
        if isinstance(other, (int, float)):
            if not isinstance(self.iterable, (int, float)):
                return NotImplemented
            return False

        return set(self.iterable) == set(other)

    def __lt__(self, other):
        if isinstance(other, OrderedSet):
            return self.iterable < other.iterable
        return set(self.iterable) < set(other)


# INPUT DATA:

# TEST_1:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

# TEST_2:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

# TEST_3:
orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

# TEST_4:
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)

# TEST_5:
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

# TEST_6:
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)

# TEST_7:
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))
