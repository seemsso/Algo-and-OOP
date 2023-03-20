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


class Line:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)



import random

elements = []
for el in range(5):
    a, b, c, d = [random.randrange(0, 1000) for i in range(4)]
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))

print(elements)