""" BINARY SEARCH """

# def binary_search(list, item):
#     low = 0
#     res = 0
#     high = len(list) - 1
#
#     while low <= high:
#         res += 1
#         mid = int((low + high) / 2)
#         guess = list[mid]
#         if guess == item:
#             return f"Score iteration: {res} for value {mid}"
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None
#
# lst = [i for i in range(100)]
# print(binary_search(lst, 32))


""" CHOICE SORT """

# def find_small(arr):
#     small = arr[0]
#     small_i = 0
#
#     for i in range(1, len(arr)):
#         if arr[i] < small:
#             small = arr[i]
#             small_i = i
#     return small_i
#
#
#
# def sort_lst(arr):
#     newArr = []
#     for i in range(len(arr)):
#         small = find_small(arr)
#         newArr.append(arr.pop(small))
#     return newArr
#
#
# a = [1, 3, 2, 10, 25, 7]
# print(sort_lst(a)) # =>  [1, 2, 3, 7, 10, 25]



""" RECURSION with stack """


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# print(factorial(7))


# def count_elements(lst):
#     if not lst:
#         return 0
#     return 1 + count_elements(lst[1:])
#
#
#
# a = [1, 2, 3, 7, 10]
#
# print(count_elements(a)) #3
#
#
#
# def sum_lst(lst):
#     sum = 0
#     for i in lst:
#         if lst:
#             sum += i
#             i += sum_lst(lst[i:])
#     return sum
#
# print(sum_lst(a))  #6


""" QUICKSORT """

# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     elif len(arr) == 2:
#         if arr[0] > arr[1]:
#             return arr
#         else:
#             return arr[1] + arr[0]
#     else:
#         main = arr[0]
#         low = [i for i in arr[1:] if i < main]
#         big = [i for i in arr[1:] if i > main]
#         return quicksort(low) + [main] + quicksort(big)
#
#
# lst = [3, -5, 100, 1, -10, 50, 14]
# print(quicksort(lst))



# def longest(a1, a2):
#     a1 = set(a1)
#     print(a2)
#     a2 = set(a2)
#     print(a2)
#     res = a1 | a2
#     return res


""" HASH TABLES """


# voted = {}
#
# #set realisation
# def check_voter(name):
#     if voted.get(name):
#         print('already voted')
#     else:
#         voted[name] = True
#         print('he can vote')

# check_voter("Ivan") # => he can vote
# check_voter("Petr") # => he can vote
# check_voter("Nikolay") # => he can vote
# check_voter("Ivan") # => already voted


"""  Breadth - First Search  """

# graph = {}
# graph["me"] = ['alice', 'bob', 'claire']
# graph["bob"] = ['ann', 'peggy']
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []
#
# print(graph)
#
# # queue in PY
# from collections import deque
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if seller(person):
#                 print(f'It\'s {person}')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# def seller(name):
#     return name == "bob"
#
#
# print(search("me"))


""" Dijkstra algorithm """

# graph = dict()
# graph["start"] = dict()
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
# graph["a"] = dict()
# graph["a"]["final"] = 1
# graph["b"] = dict()
# graph["b"]["a"] = 3
# graph["b"]["final"] = 5
# graph["final"] = dict()
#
# infinity = float("inf")
# costs = dict()
# costs["a"] = 6
# costs["b"] = 2
# costs["final"] = infinity
#
#
#
#
# parents = dict()
# parents["a"] = "start"
# parents["b"] = "start"
# parents["in"] = None
#
#
#
#
# checked_node = []
#
#
# def find_lowest(node):
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in checked_node:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
#
# node = find_lowest(costs)
# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     checked_node.append(node)
#     node = find_lowest(costs)


""" greedy algorithm """

# states = {"wa", "mt", "id", "tch", "ca"}
#
# stations = dict()
#
# stations["kone"] = {"wa", "mt"}
# stations["5fm"] = {"ca", "wa"}
# stations["jamfm"] = {"id", "tch", "mt"}
#
# final_stations = set()
#
# while states:
#     best_station = None
#     states_covered = set()
#
#     for station, states_for_station in stations.items():
#         covered = (states & states_for_station)
#         if len(covered) > len(states_covered):
#             best_station = station
#             states_covered = covered
#             states -= states_covered
#             final_stations.add(best_station)
#
# print(final_stations)

""" Dynamic programming """

# if word_a[i] == word_b[j]:
#     cell[i][j] = cell[i - 1][j - 1] + 1
# else:
#     cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])

""" Data structures curse """




""" Training Codewars """

#input 9119
#output 811181

#input 765
#output 493625

# a = 922
# #output 8144
# def square_digits(num):
#     trans = str(num)
#     string = ''
#     for i in trans:
#         string += str((int(i) ** 2))
#     return int(string)
#
#
# print(square_digits(a))

#An isogram
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

# a = 'moOse'
# def is_isogram(string):
#     string = string.lower()
#     if not string:
#         return True
#     cur = ''
#     for i in string:
#         if i in cur:
#             return False
#         cur += i
#     return True
#
# print(is_isogram(a))
#
# a = '3279'
# def fake_bin(x):
#     res = ''
#     for i in x:
#         if int(i) >= 5:
#             res += "1"
#         else:
#             res += "0"
#     return res
#
# print(fake_bin(a))


# input  'the_stealth_warrior'
# output "theStealthWarrior"

a = 'the-stealth-warrior'
def to_camel_case(text):
    res = ''
    if text[0].isalpha():
        res += text[0].upper()
    up = None
    for i, val in enumerate(text[1:]):
        if up is not None:
            res += up
            up = None
            continue
        if not val.isalpha():
            if i + 2 < len(text):
                up = text[i + 2].upper()
        else:
            res += val
    return res

print(to_camel_case(a))

