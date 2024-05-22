'''Класс Logger
Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать никаких аргументов.

Предполагалось, что при установке или изменении значения атрибута экземпляра класса Logger будет выводиться текст:

Изменение значения атрибута <имя атрибута> на <новое значение атрибута>
Также планировалось, что при удалении атрибута будет выводиться текст:

Удаление атрибута <имя атрибута>
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Logger.

Примечание. Никаких ограничений касательно реализации класса Logger нет, она может быть произвольной.

Примечание 2. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.8/Module_5.8.9'''

class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
       # self.name = value
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)


# INPUT DATA:

# TEST_1:
obj = Logger()

obj.attr = 1
del obj.attr

# TEST_2:
obj = Logger()

obj.name = 'pygen'
obj.rating = '5*'
obj.ceo = 'Timur'
del obj.rating
obj.rating = '6*'

# TEST_3:
obj = Logger()
words = ['he', 'yard', 'today', 'reach', 'somebody', 'PM', 'contain', 'light', 'half', 'occur', 'culture', 'thought',
         'think', 'law', 'short', 'animal', 'control', 'well', 'audience', 'help', 'to', 'race', 'ball', 'garden',
         'life', 'show', 'cultural', 'program', 'name', 'wish', 'year', 'president', 'different', 'however',
         'difficult', 'have', 'station', 'risk', 'child', 'machine', 'strong', 'baby', 'space', 'operation', 'street',
         'eat', 'improve', 'work', 'major', 'will', 'try', 'green', 'able', 'would', 'prevent', 'audience', 'happy',
         'fear', 'candidate', 'campaign', 'else', 'discussion', 'seem', 'star', 'common', 'education', 'service', 'bit',
         'see', 'prevent', 'southern', 'standard', 'prove', 'friend', 'their', 'law', 'product', 'population', 'decide',
         'west', 'report', 'we', 'for', 'pull', 'early', 'fight', 'discover', 'growth', 'best', 'especially', 'realize',
         'still', 'economy', 'maintain', 'her', 'test', 'how', 'understand', 'rather', 'down']

digits = [677, 718, 990, 22, 434, 636, 921, 677, 515, 931, 630, 455, 571, 467, 311, 500, 180, 994, 117, 171, 601, 773,
          671, 506, 752, 283, 963, 847, 846, 357, 848, 18, 645, 827, 752, 737, 116, 539, 597, 258, 562, 632, 483, 394,
          377, 772, 339, 743, 490, 279, 483, 478, 151, 475, 145, 545, 318, 686, 12, 552, 551, 884, 335, 628, 156, 484,
          860, 2, 649, 445, 517, 328, 196, 229, 156, 699, 678, 442, 986, 190, 279, 852, 627, 246, 985, 877, 498, 437,
          599, 879, 96, 576, 631, 235, 827, 607, 818, 304, 291, 958]

for name, value in zip(words, digits):
    setattr(obj, name, value)
    if value % 2 == 0:
        delattr(obj, name)

# TEST_4:
obj = Logger()

excluded = ['explain', 'much', 'determine', 'response', 'realize', 'wait', 'television', 'million', 'think', 'water',
            'purpose', 'treat', 'both', 'land', 'condition', 'mission', 'air', 'public', 'cultural', 'ok', 'ever',
            'run', 'institution', 'smile', 'industry', 'person', 'leave', 'watch', 'tell', 'while', 'total',
            'interview', 'whom', 'staff', 'technology', 'successful', 'measure', 'country', 'let', 'every', 'design',
            'control', 'realize', 'rather', 'citizen', 'food', 'return', 'pass', 'person', 'week']

for item in excluded:
    try:
        delattr(obj, item)
    except (KeyError, AttributeError):
        print('Класс', obj.__class__.__name__, 'не имеет атрибута', item)