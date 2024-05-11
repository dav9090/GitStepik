'''Класс SuperString
Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:

string — значение строки
Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:

<значение строки>
Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.

Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:

результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n
результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.

Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_5/Module_5.5/Module_5.5.11
'''

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    # def __repr__(self):
    #     return '{}({}, {})'.format(self.__class__.__name__, self.x, self.y)

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented


    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return SuperString(self.string * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            m = len(self.string) / other
            return SuperString(self.string[:int(m):])
        return NotImplemented

    def __lshift__(self, other):        #<<
        if isinstance(other, (int, float)):
            if other >= len(self.string):
                return SuperString('')
            m = len(self.string) - other
            return SuperString(self.string[:m:])
        return NotImplemented

    def __rshift__(self, other):            #>>
        if isinstance(other, (int, float)):
            if other >= len(self.string):
                return SuperString('')
            m = len(self.string) - (len(self.string) - other)
            return SuperString(self.string[m::])
        return NotImplemented



# INPUT DATA:

# TEST_1:
s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

# TEST_2:
s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

# TEST_3:
s = SuperString('beegeek')

print(s << 4)
print(s >> 3)

# TEST_4:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

# TEST_5:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} >> {i} =', s >> i)

# TEST_6:
names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон', 'Добромысл',
         'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир', 'Орест',
         'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен', 'Велимир',
         'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
         'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
         'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан', 'Гордей',
         'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
         'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
         'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
         'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

for name in names:
    person = SuperString(name)
    print(person * 2, 2 * person, person / 2)

# TEST_7:
s = SuperString('beegeek')
for i in range(1, 9):
    print(f'{s} / {i} =', s / i)

# TEST_8:
superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))

# TEST_9:
s1 = SuperString('bee')
s2 = SuperString('geek')

new_s1 = s1 << 1
new_s2 = s2 >> 1
new_s3 = s1 + s2
new_s4 = s1 * 2
new_s5 = s2 / 2

print(new_s1, type(new_s1))
print(new_s2, type(new_s2))
print(new_s3, type(new_s3))
print(new_s4, type(new_s4))
print(new_s5, type(new_s5))