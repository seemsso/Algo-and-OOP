""" REPEAT PYTHON BASE WITH MARK LUTZ BOOK """

""" INT/FLOAT """
# import math
# a = 5.5
# b = 6.1
# c = 3.0
# d = 7.7357575

# print(math.floor(a)) => 5
# print(math.floor(-2.5))
# print(round(d, 2)) => 7.74

# a = int(input())
# print(bin(a))
# mask = int(0b00001010)
# a = a ^ mask
# print(a)
# print(bin(a))

# import random
#
# a = input().split()
# b = random.sample(a, 3)
# print(b)

# SET
# a = input().split()
# a = set(a)
# print(a)


""" 6.DYNAMIC TYPES """

# a = [1, 2, 3]
# b = a[:]
# c = a
# print(a == b) => True
# print(a is b) => False - это разные объекты
# print(a is c) => True
# НО ЕСЛИ ЭТО ЧИСЛА - ТО IS укажет True,
# даже если объекты разные -- из-за КЕШИРОВАНИЯ

# import sys
# a = 5.5
# print(sys.getrefcount(5.5)) СЧЕТЧИК ИСПОЛЬЗОВАНИЯ КЕШИРУЕМОГО ОБЪЕКТА


""" 7.STR """

# a = '123'
# a = a[::2]
# print(a)

# a = "dsa as           "
# print(a.isalpha()) => False
# print(len(a.rstrip())) #=> 6
# print(len(a)) #=> 17

# a = [1, 2, 3]
#
# print(a[:1])


""" LIST """

# x = {'a': 1, 'b': 2, 'c': 3}
# y = {'d': [1, 2, 3]}
# print(x.get('a', 'oh shit'))
# x.setdefault('2', 5) #{'a': 1, 'b': 2, 'c': 3, '2': 5}
# print(x)
# print(x.values())
#
# x[99] = 'memes'
# print(x)

# print(x.update(y))

""" WHILE/FOR """

# x = 'kekl'
# while x:
#     ...

# a = [1, 2, [5, 6], 3]
# b = []
# for i in a:
#     if type(i) == int:
#         i += 10
#     b.append(i)
# print(b)

# a = [('name', 'city',), ('age', 'orders')]

""" IN DATA BASE """

# for i, j in a:
#     print(i, j)


""" FILE READING """

# file = open('C:\\Users\\Вадим\\Desktop\\testpy.txt')
# while True:
#     char = file.read(1)
#     if not char:
#         break
#     print(char)


# for line in open('C:\\Users\\Вадим\\Desktop\\testpy.txt'):
#     print(line.rstrip())

# s = 'spam'
#
# for i in range(len(s)):
#     s = s[1:] + s[:1]
#     print(s, end=' ')
# print(s)


# L = [1, 2, 3]
# for i in range(len(L)):
#     X = L[i:]+L[:i]
#     print(X, end=' ')

# S = 'abcdefghijk'
# for i in S[::2]:
#     print(i, end=' ')
# print(S[::2], sep=' ')

# L = [1, 2, 3]
# print(id(L))
#
# for i in range(len(L)):
#     L[i] += 1
# print(id(L))

""" ZIP/MAP """
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
#
# L3 = {}
#
# for k, v in zip(L1, L2):
#     L3[k] = v
#
# L4 = dict(zip(L1, L2))
# print(L3) => {1: 4, 2: 5, 3: 6}
# print(L4) => {1: 4, 2: 5, 3: 6}

# list1 = [1, 'meme', 'kek', 56.5]
#
# for i, j in enumerate(list1):
#     print(i, j, end=' ; ')

# D = dict(a=1, b=2, c=3)
# a = iter(D.values())
# print(next(a))
# print(next(a))
# print(next(a))


# Sample Input:
#
# 10 5 4 -3 2 0 5 10 3
# Sample Output:
#
# 10 5 4 3

# a = list(map(int, input().split()))
# b = list(set(a))
# a = sorted(b, reverse=True)[:4]
#
# print(*a)


# Sample Input:
#
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65
# Sample Output:
#
# 67 14 9 11 10 3


# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())), reverse=True)
#
# c = [i + j for (i,j) in zip(a, b)]
# print(*c)


# Sample Input:
#
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500
# Sample Output:
#
# яблоко линейка бумага


# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst_in1 = [i.split(":") for i in lst_in]
#
# d = {int(v): k for k, v in lst_in1}
#
#
# def check3_lower(dct):
#     dct = sorted(dct.items())
#     lst = [dct[i][1] for i in range(3)]
#     return lst
#
#
# res = check3_lower(d)
# print(*res)

""" FUNCTIONS """

# def func1(prm1, prm2):
#     result = []
#     for i in prm1:
#         if i in prm2:
#             result.append(i)
#
#     return result

#
# a = 'scrammers'
# b = 'what is the scam?'
# print(func1(a, b)) => ['s', 'c', 'a', 'm', 'm', 'e', 's']


# def maker(a):
#     def action(b):
#         return a * b
#
#     return action
#
# a = maker(7)
# print(a(5))


# def func1(a):
#     return lambda b: b * a
#
#
# b = func1(5)
# print(b(3)) => 15

# def func1(arg1):
#     a = arg1
#
#     def wrapper(arg2):
#         b = arg2
#         return a, b
#     return wrapper
#
#
# a = func1(5)
# print(a(7))

# def tester(start):
#     def nested(label):
#         print(label, nested.state)
#         nested.state += 1
#
#     nested.state = start
#     return nested


""" FUNC PRMS/ARGUMENTS """

# def func1(a):
#     a[0] = [1, 2]
#
# x = [4, 5, 6]
# func1(x)
# print(x)


# def func2(a, b):
#     a = 2
#     b = {3: '5', 4: 'kek'}
#     return a, b
#
# x = 1
# y = [5, 2]
# print(x, y) =>  1 [5, 2]
# func2(x, y)
# print(x, y) => 1 [5, 2]
# x, y = func2(x, y)
# print(x, y) => 2 {3: '5', 4: 'kek'}

# x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(*zip(x, x, x, x))


# def func(a, b=1, c=3):
#     print(a, b, c)
#
# func(1, 2)

# print(type((1, 2)))


""" RECURSION AND LAMBDA FUNCS """

# def mysum(L):
#     if not L:
#         return 0
#     else:
#         return L[0] + mysum(L[1:])
#
#
# print(mysum([1, 3, 7, 9]))

# L = [1, 2, 3, 5]
#
# sum = 0
# while L:
#     sum += L[0]
#     L = L[1:]
# else:
#     print(sum)

# L = [2, 4, 10, 11, 3]
# sum = 0
#
# for x in L:
#     sum += x
#
# print(sum)


# L = [1, 2, [3, 4, [5]], 7]
#
# def sum_list(a):
#     summer = 0
#     for x in a:
#         if not isinstance(x, list):
#             summer += x
#         else:
#             summer += sum_list(x)
#     return summer
#
# print(sum_list(L))

# L = [1, 2, 4, 6, [2, 3, [5, 6, [7]]]]
#
# def sumtree(a):
#     tot = 0
#     items = list(a)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             tot += front
#         else:
#             items.extend(front)
#     return tot
#
# print(sumtree(L))


# FILTER AND REDUCE
#
# import functools
# a = [1, 2, 3, 45, 90, 120, -121]
# a_map = list(map((lambda x: x ** 2), a))
# a_filter = list(filter(str, a))
# a_reduce = functools.reduce((lambda x, y: x + y), a)
# print(a, a_map, a_filter, a_reduce, sep="\n")


# import sys
# import random
#
# random.seed(1)
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst = [[int(i) for i in x.split()] for x in lst_in]
#
# transform = list(map(list, zip(*lst)))
#
# random.shuffle(transform)
#
# lst_finish = list(map(list, zip(*transform)))
# for i in lst_finish:
#     print(*i)


""" GENERATORS """

# For files:
# [line.rstrip for line in open("testpy.txt").readlines()] -without '\n'

# listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
# [] -table, () - str, in () values
# list(map((lambda row: row[1]), listoftuple))


# def ups(line):
#     for sub in line.split(","):
#         yield sub.lower()
#
# print(tuple(ups("ABC,DEF,GH"))) => ('abc', 'def', 'gh')
# a = {i : s for i, s in enumerate(ups('AB,CD,EF'))}
# print(a) => {0: 'ab', 1: 'cd', 2: 'ef'}


# a = (i ** 2 for i in [1, 2, 3, 4])
# print(iter(a) is a)
# b = iter(a)
# print(next(b))
#
# c = iter(a)
# print(next(c))

# saved position in yield
# def func():
#     yield from [1, 2, 3, 4]
#
# a = iter(func())
# b = iter(func())
# print(next(a))
# print(next(b))
# print(next(a))
# print(next(b))


""" sorted(key=func) or sort(key=func) """

# rivers = ['Лена', 'Енисей', 'Волга', 'Дон']
#
# rivers_len = sorted(rivers, key=len,reverse=True)
# print(*rivers_len)


# import sys
#
# lst_in = ['ножницы=100', 'котелок=500',
#           'спички=20', 'зажигалка=40', 'зеркальце=50']
#
# dct = {x[0]: x[1] for x in [x.split("=") for x in lst_in]}
# dct_sort = sorted(list(dct.items()), key=lambda x: int(x[1]), reverse=True)
#
# print(*[x[0] for x in dct_sort])


# INDEX

# notes = ['до', 'фа', 'соль', 'до', 'ре', 'фа', 'ля', 'си']
#
# orig = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# transform_notes = sorted(notes, key= lambda x: orig.index(x))
# print(*transform_notes)

""" isinstance """

# def get_add(a, b):
#     if type(a) in (int, float) and type(b) in (int, float):
#         return a + b
#     elif type(a) == str and type(a) == type(b):
#         return a + b
#     else:
#         return None
#
# print(get_add(5, 19))
# print(get_add(5, 19.5))
# print(get_add(5.5, 19.3))
# print(get_add(5, "str"))
# print(get_add("str", "str"))
# print(get_add(5, "str"))
# print(get_add(5, True))


# def get_sum(a):
#     res = sum(filter(lambda x: type(x) is int, a))
#     return res
# print(get_sum([1, 4, 10, "str", True]))

# def get_even_sum(a):
#     res = sum(filter(lambda x: type(x) is int and x % 2 == 0, a))
#     return res
#
# print(get_even_sum([1, 4, 10, "str", True]))


# def get_list_dig(lst):
#     res = list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), lst))
#     return res
#
# print(get_list_dig([1, -4, 10.5, "str", True]))


""" all and any """

# a = [2, 4, 6, 8, 22, 56]
#
# print(all(map(lambda x: x % 2 == 0, a))) # => True

# a = [8.2, -11.0, 20.0, 3.4, -1.2]
#
# print(any(map(lambda x: x < 0, a))) # => True

# a = ["str1", "str2", 3, "str3"]
# def is_string(coll):
#     return all(map(lambda x: isinstance(x, str), coll))
#
# print(is_string(a)) # => False


# a = [3, 3, 3, 2, 3, 3]
#
# print("отчислен" if any(map(lambda x: x < 3, a)) else "учится") # => отчислен

