'''Класс TreeBuilder 🌶️🌶️
Дерево — одна из наиболее широко распространённых структур данных в информатике, эмулирующая древовидную структуру в виде набора связанных узлов.



Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13. Узлы без потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13.

Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово строить древовидную структуру данных (дерево).

Класс TreeBuilder должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
structure() — метод, возвращающий структуру дерева в виде вложенных списков
Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего блока with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева, возвращаемой методом structure().

Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел, тот, в свою очередь, другой, и так далее.

Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева выводится лишь после ее построения.

Примечание 3. Наглядные примеры использования класса TreeBuilder продемонстрированы в тестовых данных.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Класс TreeBuilder должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 6. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_6/Module_6.5/Module_6.5.18
'''

class TreeBuilder:
    def __init__(self):
        self.tree = {}
        self.l = []
    level = 0
    def __enter__(self):
        self.tree.setdefault(type(self).level, [])
        type(self).level += 1

    def add(self, node):
        self.tree.setdefault(type(self).level, []).append(node)

    def __exit__(self, *args, **kwargs):
        temp = self.tree[type(self).level]
        self.tree[type(self).level] = []
        if temp:
            self.tree[type(self).level-1].append(temp)
        type(self).level -= 1

    def structure(self):
        if self.tree:
            return self.tree[0]
        else:
            return []

    # def add(self, node):
    #     self.tree.append(node)
    # def structure(self):
    #     return self.tree
    #
    # def __enter__(self):
    #     return self
    # def __exit__(self, *args):
    #     return False


# INPUT DATA:

# TEST_1:
tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass

print(tree.structure())

# TEST_2:
tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure())

# TEST_3:
tree = TreeBuilder()

with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)

print(tree.structure())

# TEST_4:
tree = TreeBuilder()

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
    with tree:
        pass

print(tree.structure())

# TEST_5:
tree = TreeBuilder()

tree.add(0)
print(tree.structure())

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        pass

print(tree.structure())

with tree:
    tree.add(5)
    with tree:
        tree.add(6)
    with tree:
        tree.add(7)
        with tree:
            tree.add(8)

print(tree.structure())

# TEST_6:
tree = TreeBuilder()

tree.add('root')
with tree:
    tree.add('first child')
    tree.add('second child')
    with tree:
        tree.add('grandchild')
    tree.add('bastard')
    with tree:
        pass
    tree.add('another bastard')

print(tree.structure())

# TEST_7:
tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure())

# TEST_8:
tree1 = TreeBuilder()
tree2 = TreeBuilder()

tree1.add('1st')

with tree1:
    tree1.add('2nd')
    with tree1:
        tree1.add('3rd')
    tree1.add('4th')
    with tree1:
        pass

print(tree1.structure())
print(tree2.structure())