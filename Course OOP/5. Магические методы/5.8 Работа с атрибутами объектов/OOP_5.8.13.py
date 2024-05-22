'''Класс AttrsNumberObject
Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:

attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.8/Module_5.8.13'''

class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        if item == 'attrs_num':
            self.attrs_num = len(self.__dict__)
        return object.__getattribute__(self, item)


# INPUT DATA:

# TEST_1:
music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)

# TEST_2:
music_group = AttrsNumberObject()

print(music_group.attrs_num)

# TEST_3:
music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)

# TEST_4:
music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)

# TEST_5:
person = AttrsNumberObject(name='Mark')

print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)

# TEST_6:
music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
music_group.genre = 'jazz'
print(music_group.attrs_num)
