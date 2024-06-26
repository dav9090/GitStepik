'''Класс HtmlTag 🌶️
HTML — это язык разметки, используемый для определения структуры веб-страниц, посещаемых пользователями. HTML предоставляет средства для создания заголовков, абзацев, ссылок, цитат и других элементов. Каждый HTML-элемент обозначается открывающим и закрывающим тегами:

<p>Если в ходе теста нет угрозы жизни, разве это вообще наука?</p>
Теги заключаются в угловые скобки. Они определяют, где элемент начинается и где он заканчивается. Единственным различием между открывающим и закрывающим тегами является косая черта, которая предшествует имени тега.

Открывающий и закрывающий теги, а также заключенное в них содержимое, могут располагаться как на одной строке (пример выше), так и на разных. Если теги и содержимое располагаются на разных строках, то сперва указывается открывающий тег, затем на следующий строке с отступом в два пробела указывается содержимое, а после на следующей строке указывается закрывающий тег, который располагается на том же уровне отступов, что и открывающий тег:

<p>
  Наука не решает вопрос Почему?, она решает вопрос А почему бы и нет?
</p>
Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

tag — HTML тег
inline — булево значение, по умолчанию равняется False
Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать HTML-код с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных строках.

Класс HtmlTag должен иметь один метод экземпляра:

print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.

Примечание 2. В качестве отступов для каждого уровня используйте два пробела.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_6/Module_6.5/Module_6.5.17
'''


class HtmlTag:
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    level = -1

    def __enter__(self):
        HtmlTag.level += 1
        if self.inline:
            print(f'{"  " * HtmlTag.level}<{self.tag}>', end='')
        else:
            print(f'{"  " * HtmlTag.level}<{self.tag}>')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            print(f'</{self.tag}>')
        else:
            print(f'{"  " * HtmlTag.level}</{self.tag}>')

        HtmlTag.level -= 1

    def print(self, text):
        if self.inline:
            print(f'{text}', end='')
        else:
            print(f'{"  " * (HtmlTag.level + 1)}{text}')


# INPUT DATA:

# TEST_1:
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_2:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_3:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')

# TEST_4:
with HtmlTag('div') as _:
    with HtmlTag('p') as paragraph:
        with HtmlTag('strong', True) as strong:
            strong.print('Notice:')
        paragraph.print('Your browser is ancient')

# TEST_5:
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
