""""FIRST STEPS WITH CLASSES AND OOP ON PYTHON """

# class Mem:
#
#     """Documentation"""
#     a = 1
#     b = 3
#
#     def func1(self):
#         ...
#
#
# setattr(Mem, 'c', 5)
# print(getattr(Mem, 'c', 5))
# print(hasattr(Mem, 'c')) => True
# ekz1 = Mem()
# ekz1.a = 5
# ekz2 = Mem()

# print(ekz2.a) => 1
# print(ekz1.a) => 5
# print(Mem.__doc__) => Documentation

# class Car:
#     pass
#
# setattr(Car, "model", "Тойота")
# setattr(Car, "color", "Розовый")
# setattr(Car, "number", "П111УУ77")
# print(Car.__dict__["color"]) => Розовый

#
# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
#
#
# print(getattr(Dictionary, 'rus_word', False))


# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
# p1 = Person()
#
# print(hasattr(Person, 'job'))
# import random

""" CLASS METHODS TRAINING """

# class MediaPlayer():
#
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# media2.play()


# class Graph():
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         a = []
#         for i in self.data:
#             if (i >= self.LIMIT_Y[0]) and (i <= self.LIMIT_Y[1]):
#                 a.append(int(i))
#         print(*a)
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# import sys


# class StreamData():
#
#     def create(self, fields, lst_values):
#         if len(fields) == len(lst_values):
#             self.__dict__ = dict(zip(fields, lst_values))
#         return bool(self.__dict__)
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = [1, 2, 3]
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
# sr = StreamReader()
# data, result = sr.readlines()
#
# print(result)
# print(data.__dict__)


# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for i in data:
#             for ind, val in enumerate(i.split(' ')):
#                 self.lst_data.append({self.FIELDS[ind]: val})
#
#     def select(self, a, b):
#         return self.lst_data[a: b + 1]
#
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.lst_data)


# import sys


# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a: b + 1]
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.lst_data)


# class Translator:
#     d = {}
#
#     def add(self, eng, rus):
#         if eng not in self.d:
#             self.d[eng] = []
#             self.d[eng].append(rus)
#         else:
#             if rus not in self.d[eng]:
#                 self.d[eng].append(rus)
#
#
#     def remove(self, eng):
#         del self.d[eng]
#
#     def translate(self, eng):
#         return self.d[eng]
#
#
# tr = Translator()
# sdata = '''tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молок'''
# trans = [tr.add(eng, ru) for eng, ru in [d.split(' - ') for d in sdata.split('\n')]]
# tr.remove('car')
# tr.translate('go')
# print(*tr.translate('go'))


""" __INIT__"""

# class Money:
#
#     def __init__(self, x, y=0):
#         self.money = x
#
#
# my_money = Money(100)
# your_money = Money(1000)


# class Point:
#
#     def __init__(self, x=0, y=0, color="black"):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(y, y) for x, y in enumerate(range(2000), start=1) if y % 2 != 0]
# points[1] = Point(3, 3, 'yellow')


# class Line:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
#
# import random
#
# elements = []
# for el in range(5):
#     a, b, c, d = [random.randrange(0, 1000) for i in range(4)]
#     elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))
#
# print(elements)


# class TriangleChecker:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: (type(x) in (int, float)) and x >= 0, (self.a, self.b, self.c))):
#             return 1
#         elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
#             return 2
#         else:
#             return 3
#
#
# a, b, c = map(int, input().split())
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


# class Graph:
#
#     def __init__(self, data):
#         self.data = data[:]
#         self.is_show = True
#
#     def set_data(self, data):
#         self.data = data[:]
#
#     def show_table(self):
#         if self.is_show:
#             print(f"{' '.join(map(str, self.data))}")
#         else:
#             print("Отображение данных закрыто")
#
#     def show_graph(self):
#         if self.is_show:
#             print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
#         else:
#             print("Отображение данных закрыто")
#
#     def show_bar(self):
#         if self.is_show:
#             print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
#         else:
#             print("Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
#
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class Motherboard:
#
#     def __init__(self, name, cpu, total_mem_slots=4, *mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = total_mem_slots
#         self.mem_slots = mem_slots[: self.total_mem_slots]
#
#     def get_config(self):
#         return [f"Материнская плата: {self.name}','Центральный процессор: {self.cpu.name},"
#                 f" {self.cpu.fr}','Слотов памяти: {self.total_mem_slots}',"
#                 "Память:" + '; '.join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))
#                 ]
#
#
# mb = Motherboard("ASUS", CPU('Ryzen 5700', 3800), 3, Memory('G-skill', 4000), Memory('HyperX', 3600))
# print(mb.get_config())


# class Cart:
#
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f'{x.name}: {x.price}' for x in self.goods]
#
#
# class Table:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# cart.add(TV('Samsung', 69999))
# cart.add(TV('Sony', 49990))
# cart.add(Table('IKEA', 14990))
# cart.add(Notebook('Macbook M1', 89990))
# cart.add(Notebook('Xiaomi Redmibook', 79000))
# cart.add(Cup('Кружка 300мл с рисунком', 299))
#
# print(cart.get_list())


# class ListObject:
#
#     def __init__(self, data: str):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst_in = ['1. Первые шаги в ООП',
#           '1.1 Как правильно проходить этот курс',
#           '1.2 Концепция ООП простыми словами',
#           '1.3 Классы и объекты. Атрибуты классов и объектов',
#           '1.4 Методы классов. Параметр self',
#           '1.5 Инициализатор init и финализатор del',
#           '1.6 Магический метод new. Пример паттерна Singleton',
#           '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     cur = ListObject(lst_in[i])
#     obj.link(cur)
#     obj = cur

""" Magic Method __new__ """

# class AbstractClass:
#
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
#
#
# abstract = AbstractClass()
#
#
# # print(abstract)
#
#
# # input only 5objs,next == 5
# class SingletonFive:
#     name = []
#
#     def __new__(cls, *args, **kwargs):
#         if len(cls.name) < 5:
#             cls.name.append(super().__new__(cls))
#         return cls.name[-1]
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]


# print(objs)


# TYPE_OS = 1  # 1 - Windows; 2 - Linux
#
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#     objs = None
#
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             objs = super().__new__(DialogWindows)
#         else:
#             objs = super().__new__(DialogLinux)
#         objs.name = args[0]
#         return objs


# class Factory:
#
#     def build_sequence(self):
#         self.lst = []
#         return self.lst
#
#     def build_number(self, string):
#         self.res = float(string)
#         return self.res
#
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# ld = Loader()
# s = input()
# res = ld.parse_format(s, Factory())


# """classmethod and @staticmethod"""
#
# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str or not (3 <= len(name) <= 50) or not(set(name) < set(cls.CHARS_CORRECT)):
#             raise ValueError("некорректное поле name")
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str or not (3 <= len(name) <= 50) or not (set(name) < set(cls.CHARS_CORRECT)):
#             raise ValueError("некорректное поле name")
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()


"""Access public,private,protected"""

# class Clock:
#     cur = []
#
#     def __init__(self, time=0):
#         if self.cur:
#             el = len(self.cur) - 1
#             time = el
#         self.__time = time
#         self.cur.append(time)
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         if type(tm) == int and (0 <= tm < 100_000):
#             return True
#         else:
#             return False
#
#
# clock = Clock(4530)
# clock.set_time(15)
# print(clock.get_time())  # 15
# clock.set_time(100000)
# clock.set_time(-1)
# clock.set_time('2')
# clock.set_time(0.1)
# print(clock.get_time())


# class Money:
#
#     def __init__(self, money):
#         self.__money = 0
#         if self.__check_money(money):
#             self.__money = money
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.get_money()
#
#     @classmethod
#     def __check_money(cls, money):
#         if type(money) is int:
#             return True
#         return False
#
#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120


# class Book:
#
#
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price


# class Line:
#
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def set_coords(self, *args):
#         self.__x1, self.__y1, self.__x2, self.__y2 = args
#
#     def get_coords(self):
#         self.coords = self.__x1, self.__y1, self.__x2, self.__y2
#         return self.coords
#
#     def draw(self):
#         print(*self.get_coords())
#
# a = Line(1, 2, 3, 4)
# s = a.get_coords()
# print(s)  # (1, 2, 3, 4)
# a.draw()  # 1 2 3 4


# class Point:
#
#     def __init__(self, *args):
#         if self.__check_coords(*args):
#             self.__x, self.__y = args
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     @classmethod
#     def __check_coords(cls, *args):
#         for i in args:
#             if type(i) not in (int, float):
#                 return False
#         return True
#
# class Rectangle:
#
#     def __init__(self, *args):
#         if len(args) == 4:
#             self.__sp = args[0], args[1]
#             self.__ep = args[2], args[3]
#         else:
#             self.__sp = args[0]
#             self.__ep = args[1]
#
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         if type(self.__sp) != Point:
#             print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}")
#         else:
#             print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords}")
#
#
#
# rect = Rectangle(0, 0, 20, 34)


# from random import randint
# from string import ascii_lowercase, ascii_uppercase, digits
#
# class EmailValidator:
#     chars = ascii_uppercase + ascii_lowercase + digits + '_@.'
#     random_chars = ascii_uppercase + ascii_lowercase + digits + '_'
#
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def check_email(cls, email):
#         if not cls.__is_email_str(email) or not set(email) <= set(cls.chars):
#             return False
#         divide = email.split('@')
#         if len(divide) != 2 or len(divide[0]) > 100 \
#                 or len(divide[1]) > 50 \
#                 or '.' not in divide[1] or email.count('..') > 0:
#             return False
#
#     @staticmethod
#     def __is_email_str(email):
#         return type(email) is str
#
#     @classmethod
#     def get_random_email(cls):
#         symbols = random.randint(1, 5)
#         length = len(cls.random_chars) - 1
#         return ''.join(cls.random_chars[randint(0, length)] for i in range(symbols)) + '@gmail.com'

#
# class Car:
#
#     def __init__(self, model):
#         self.__model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if (isinstance(model, str)) and (len(model) in range(2, 100)):
#             self.__model = model
#
# car = Car('kek')
# print(car.model)
# car.model = 'Toyota'
# print(car.model)


# class WindowDlg:
#
#     def __init__(self, title, width, height):
#         if isinstance(title, str):
#             self.__title = title
#         if type(width) in (int, float) and type(height) in (int, float):
#             self.__width = width
#             self.__height = height
#
#     @property
#     def title(self):
#         return self.__title
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if type(width) in (int, float) and (0 <= width <= 10000):
#             self.__width = width
#             self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if type(height) in (int, float) and (0 <= height <= 10000):
#             self.__height = height
#             self.show()
#
#     def show(self):
#         print(f"{self.title}: {self.width}, {self.height}")


# self.__x = self.__y = 0
# self.x = x
# self.y = y
#
#
# return (vector.x * vector.x) + (vector.y * vector.y)

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         if self.check_value(x) and self.check_value(y):
#             self.x = x
#             self.y = y
#
#     @classmethod
#     def check_value(cls, value):
#         return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD
#
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, val):
#         if self.check_value(val):
#             self.__x = val
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, val):
#         if self.check_value(val):
#             self.__y = val
#
#     @staticmethod
#     def norm2(vector):
#         return (vector.x * vector.x) + (vector.y * vector.y)


# from math import sqrt
# class PathLines:
#
#
#     def __init__(self, *val):
#         self.lst = [LineTo(0, 0)]
#         for el in val:
#             self.add_line(el)
#
#     def get_path(self):
#         return self.lst[1:]
#
#     def get_length(self):
#         coords = ((self.lst[i - 1], self.lst[i]) for i in range(1, len(self.lst)))
#         return sum(map(lambda t: sqrt(pow(t[0].x - t[1].x, 2) + pow(t[0].y - t[1].y, 2)), coords))
#
#     def add_line(self, line):
#         self.lst.append(line)
#
#
#
#
# class LineTo:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# p = PathLines(LineTo(1, 2))
# print(p.get_length())  # 2.23606797749979
# p.add_line(LineTo(10, 20))
# p.add_line(LineTo(5, 17))
# print(p.get_length())  # 28.191631669843197
# m = p.get_path()
# print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True
#
# h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
# print(h.get_length())  # 71.8992593599813
#
# k = PathLines()
# print(k.get_length())  # 0
# print(k.get_path())  # []


# class StringValue:
#
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.check_value(value):
#             setattr(instance, self.name, value)
#
#     def check_value(self, value):
#         return isinstance(value, str) and self.min_length <= len(value) <= self.max_length
#
#
# class PriceValue:
#
#     def __init__(self, max_value):
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.check_value(value):
#             setattr(instance, self.name, value)
#
#     def check_value(self, value):
#         return type(value) in (int, float) and 0 <= value <= self.max_value
#
#
# class Product:
#     name = StringValue(2, 50)
#     price = PriceValue(10000)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class SuperShop:
#     goods = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         if product in self.goods:
#             self.goods.remove(product)


""" Inheritance """

# class Animal:
#
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#
# class Cat(Animal):
#
#     def __init__(self, name, old, color, weight):
#         super().__init__(name, old)
#         self.color = color
#         self.weight = weight
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.color, self.weight}"
#
#
# class Dog(Animal):
#
#     def __init__(self, name, old, breed, size):
#         super().__init__(name, old)
#         self.breed = breed
#         self.size = size
#
#     def get_info(self):
#         return f"{self.name}: {self.old}, {self.breed, self.size}"


# class Singleton:
#     cur = None
#     single = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls == Singleton:
#             if cls.single is None:
#                 cls.single = object.__new__(cls)
#         if cls.cur is None:
#             cls.cur = object.__new__(cls)
#         return cls.cur
#
#
# class Game(Singleton):
#
#     def __init__(self, name):
#         if 'name' not in self.__dict__:
#             self.name = name


""" issubclass """

# class ListInteger(list):
#
#     def __init__(self, lst):
#         for el in lst:
#             self.check_value(el)
#         super().__init__(lst)
#
#     def check_value(self, el):
#         if type(el) != int:
#             raise TypeError('можно передавать только целочисленные значения')
#
#
#     def __setitem__(self, key, value):
#         self.check_value(value)
#         super().__setitem__(key, value)
#
#
#
#     def append(self, value):
#         self.check_value(value)
#         super().append(value)


""" super() """

# class Book:
#
#     def __init__(self, title, author, pages, year):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#
# class DigitBook(Book):
#
#     def __init__(self, title, author, pages, year, size, frm):
#         super().__init__(title, author, pages, year)
#         self.size = size
#         self.frm = frm

# class Student:
#     def __init__(self, fio, group):
#         self._fio = fio  # ФИО студента (строка)
#         self._group = group  # группа (строка)
#         self._lect_marks = []  # оценки за лекции
#         self._house_marks = []  # оценки за домашние задания
#
#     def add_lect_marks(self, mark):
#         self._lect_marks.append(mark)
#
#     def add_house_marks(self, mark):
#         self._house_marks.append(mark)
#
#     def __str__(self):
#         return f"Студент {self._fio}: оценки на лекциях:" \
#                f" {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"
#
#
# class Mentor:
#     def __init__(self, fio, subject):
#         self._fio = fio
#         self._subject = subject
#
#
# class Lector(Mentor):
#
#     def set_mark(self, student, mark):
#         student.add_lect_marks(mark)
#
#     def __str__(self):
#         return f"Лектор {self._fio}: предмет {self._subject}"
#
#
# class Reviewer(Mentor):
#
#     def set_mark(self, student, mark):
#         student.add_house_marks(mark)
#
#     def __str__(self):
#         return f"Эксперт {self._fio}: предмет {self._subject}"


# lector = Lector("Балакирев С.М.", "Информатика")
# reviewer = Reviewer("Гейтс Б.", "Информатика")
# students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
# persons = [lector, reviewer]
# lector.set_mark(students[0], 4)
# lector.set_mark(students[1], 2)
# reviewer.set_mark(students[0], 5)
# reviewer.set_mark(students[1], 3)
# for p in persons + students:
#     print(p)


""" try/except """


# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# pt = Point(1, 2)
# print(getattr(pt, 'z', "Атрибут с именем z не существует"))



# lst_in = input().split()
# result = 0
# for i in range(len(lst_in)):
#     try:
#         cur = int(lst_in[i])
#         result += cur
#     except:
#         pass
# print(result)

