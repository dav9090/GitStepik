'''Класс Filter
Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов. При создании экземпляра класс должен принимать один аргумент:

predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение True.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Filter нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.6/Module_5.6.14'''

class Filter:

    def __init__(self, predicate = None):
        self.predicate = predicate
        if self.predicate is None:
            self.predicate = bool


    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


# INPUT DATA:

# TEST_1:
leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))

# TEST_2:
more_than_five = Filter(lambda x: x > 5)
numbers = [13, 1, 4, 10, 10, 7]

print(more_than_five(numbers))

# TEST_3:
non_empty = Filter(None)

sequence = ([], False, 1, (), 'Linus Torvalds', {5, 6, 7}, True, {}, set(), '')
print(non_empty(sequence))

# TEST_4:
int_digits = Filter(lambda x: isinstance(x, int))

digits = [25759615.72, -9587762.56, -484.7, 5414, 4290, 2089384922248.2, 8.71, 79544971044.96, -74.49, 6206, 9458,
          291588.56, 5399, 4927, 3942, 57953980234.91, 833, -6741.67, 9725, 6794, 7207, 1410, 8225, 5673.9, 5826, 2641,
          1114, 9171, -18145574565225.8, 1386, 789, -4206.48, 3799, -1.81, 17188782342720.3, 9727, 1178, 4307, 135.49,
          53830.85, -23714.99, 7535, 2568, -8.14, 3882, 1366, 8083, 2171, 2176, -5.75, -528164181.88, 336, -97.99, 7562,
          23091544796.66, 2021, 3029, 9342, 1579.93, 1903, 4084, 7084, 9659, 47078386.76, 5566, 6158.41, 926, 9337,
          9166, 1651762632245.22, 4186, 18862478.24, 6262, 8594, 212, 15422064.78, 3783, 6564, 3130, 3703, 2544, -59.33,
          0.41, -49349065413725.0, 9329323372.46, 8.8, 8801, -48204534.25, 7837, 2138, 3125, -694424298989.1,
          54427539603.1, 1800, 383, 6796, 767, -711.35, 887749021822.9, 7980268.97]
print(int_digits(digits))

# TEST_5:
no_more_than_six = Filter(lambda x: len(x) <= 6)

words = ['everybody', 'Congress', 'model', 'likely', 'information', 'meeting', 'hard', 'reduce', 'visit', 'stuff',
         'line', 'standard', 'from', 'help', 'usually', 'need', 'small', 'teacher', 'himself', 'century', 'reason',
         'something', 'year', 'president', 'buy', 'case', 'ten', 'certainly', 'fear', 'special', 'goal', 'include',
         'suffer', 'traditional', 'explain', 'me', 'into', 'executive', 'husband', 'health', 'five', 'minute', 'want',
         'trip', 'see', 'politics', 'money', 'still', 'task', 'our', 'environment', 'beat', 'stay', 'quickly', 'above',
         'increase', 'since', 'front', 'suggest', 'amount', 'will', 'production', 'hit', 'probably', 'present',
         'science', 'improve', 'discover', 'scientist', 'state', 'total', 'speak', 'administration', 'experience',
         'media', 'determine', 'cut', 'with', 'reveal', 'finish', 'short', 'share', 'new', 'eight', 'worker', 'someone',
         'beyond', 'various', 'modern', 'most', 'brother', 'room', 'interest', 'a', 'agreement', 'treat', 'break',
         'none', 'serious', 'cup']

print(no_more_than_six(words))

# TEST_6:
empty_elements = Filter(lambda x: not x)

sequence = [(1, 2, 3), [], set(), 'Beegeek', {}, {1: '12'}, False, True, '', [2023, 4]]
print(empty_elements(sequence))