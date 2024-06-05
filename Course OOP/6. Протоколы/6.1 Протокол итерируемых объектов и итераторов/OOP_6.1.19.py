'''
Класс RandomLooper
Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.10/Module_6.1.19
'''
import random

class RandomLooper:
    def __init__(self, *iterables):
        self.s = []
        for i in iterables:
            self.s.extend(i)
        random.shuffle(self.s)
        self.iterables = iter(self.s)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.iterables)


# INPUT DATA:

# TEST_1:
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))

# TEST_2:
colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))

# TEST_3:
from string import ascii_letters

domains = ['huynh.biz', 'riley.net', 'herman.org', 'tran-guerrero.com', 'martinez.com', 'riley-moore.info', 'allen.com',
           'lopez.com', 'santiago.com', 'moran-craig.com', 'smith-graves.com', 'smith.com', 'johnson.biz',
           'gregory-smith.com', 'smith.com', 'douglas.com', 'marshall.com', 'henry-garcia.com', 'gardner.biz',
           'allen.com']

work = {'Public librarian', 'Horticulturist, commercial', 'Archaeologist', 'Neurosurgeon', 'Investment analyst',
        'Energy manager', 'Conservation officer, historic buildings', 'Town planner',
        'Research scientist (physical sciences)', 'Dancer', 'Financial adviser', 'Human resources officer',
        'Meteorologist', 'Water quality scientist', 'Call centre manager', 'Surveyor, rural practice',
        'Sports administrator', 'Electronics engineer', 'Pharmacist, hospital', 'Local government officer'}

phone_numbers = ('934.394.1303x57945', '178-222-6477x229', '+1-656-770-5470x078', '+1-297-950-6100',
                 '(931)443-0778x87575', '329-788-0662', '+1-955-232-3577x6474', '001-562-654-3195x083', '854.344.9086',
                 '546-622-8169', '(161)097-6037', '(539)319-3442', '001-874-988-4679x3997', '079-860-8803x913',
                 '2410563363', '(852)061-7986x980', '393.485.5132', '+1-089-015-3223x3791', '(010)648-5657x225',
                 '497.913.4838x8085')

names = {'Frank Oconnor': 'FO', 'Brittany Mccoy': 'BM', 'Ariana Jackson': 'AJ', 'Jeffrey Smith': 'JS',
         'Oscar Gay': 'OG', 'Eric Hanson': 'EH', 'Anthony Robinson': 'AR', 'Ricky Garcia': 'RG', 'Derrick Cruz': 'DC',
         'Brittany Simpson': 'BS', 'Richard Tran': 'RT', 'Denise Hernandez': 'DH', 'Michael Lin': 'ML',
         'James James': 'JJ', 'Jacob Saunders': 'JS', 'Stephanie Sherman': 'SS', 'John Austin': 'JA',
         'Benjamin Mason': 'BM', 'Corey Brown': 'CB', 'Gregory Adams': 'GA'}

randomlooper = RandomLooper(domains, work, phone_numbers, names, ascii_letters)
print(list(randomlooper))

# TEST_4:
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)