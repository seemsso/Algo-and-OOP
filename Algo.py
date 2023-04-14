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

# input 9119
# output 811181

# input 765
# output 493625

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

# An isogram
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

# a = 'the-stealth-warrior'
# def to_camel_case(text):
#     res = ''
#     if text[0].isalpha():
#         res += text[0].upper()
#     up = None
#     for i, val in enumerate(text[1:]):
#         if up is not None:
#             res += up
#             up = None
#             continue
#         if not val.isalpha():
#             if i + 2 < len(text):
#                 up = text[i + 2].upper()
#         else:
#             res += val
#     return res
#
# print(to_camel_case(a))


""" Tim Roughgarden """
""" MergeSort """

# start = [1, 4, 5, 6, 2, 3, 7, 8]
# a = [1, 4, 5, 6]
# b = [2, 3, 7, 8]

# old_realisation

# i = 0
# j = 0
# res = []
# for _ in enumerate(start):
#     if i >= len(a):
#         res.append(b[j])
#         j += 1
#     elif j >= len(b):
#         res.append(a[i])
#         i += 1
#     elif a[i] < b[j]:
#         res.append(a[i])
#         i += 1
#     else:
#         res.append(b[j])
#         j += 1


# new_realisation

# a = [1, 2, 5, 7, 9, 2, 3]
# def merge(a, b):
#     res = []
#     n = len(a)
#     m = len(b)
#
#     i = 0
#     j = 0
#     while i < n and j < m:
#         if a[i] > b[j]:
#             res.append(b[j])
#             j += 1
#         else:
#             res.append(a[i])
#             i += 1
#     res += a[i:] + b[j:]
#     return res
#
# def merge_split(lst):
#     part = len(lst) // 2
#     part1 = lst[:part]
#     part2 = lst[part:]
#
#     if len(part1) > 1:
#         part1 = merge_split(part1)
#     if len(part2) > 1:
#         part2 = merge_split(part2)
#
#     return merge(part1, part2)
#
#
# print(merge_split(a))

# def interpret(command: str) -> str:
#     res = ""
#     length = len(command)
#     for i, val in enumerate(command):
#         if val.isalpha():
#             res += val
#         elif val == "(":
#             if i + 1 < length and command[i + 1] == ")":
#                 res += "o"
#     return res
#
# a = "G()(al)"


# RLE
# a = 'AAABBBCCDEFGHZZAAAXXKK'
# output = 'A3B3C2DEFGHZ2A3X2'
#
#
# def write_score(seq):
#     el = seq[0]
#     score = 1
#     lst = []
#     for i in range(1, len(seq)):
#         if seq[i] == el:
#             score += 1
#         elif score == 1:
#             lst.append(el)
#             el = seq[i]
#         else:
#             lst.append(el)
#             lst.append(str(score))
#             el = seq[i]
#             score = 1
#     return ''.join(lst)
#
#
# print(write_score(a))

# Leetcode 1221
# input -  'RLLLLRRRRL'
# output - 3

# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         res = 0
#         score_cur = 1
#         score_next = 0
#         cur = s[0]
#         for i in range(1, len(s)):
#             if s[i] != cur:
#                 score_next += 1
#             else:
#                 score_cur += 1
#             if score_cur == score_next:
#                 res += 1
#                 score_cur = 0
#                 score_next = 0
#                 cur = s[i]
#         if score_cur or score_next:
#             res += 1
#         return res

# draft
# a = [1,2,3,4,5]
#
#
# def twoSum(nums, target: int):
#     res = []
#     for i in range(len(nums) - 1):
#         if nums[i] + nums[i + 1] == target:
#             res.extend((i, i + 1))
#             return res
#     if nums[-1] + nums[-2] == target and not res:
#         res.extend((len(nums) - 1, len(nums) - 2))
#         return res
#
#
# print(twoSum(a, 5))


# 912 leetcode


# class Solution:
#     def sortArray(self, nums):
#         def merge_res(a, b):
#             res = []
#             n = len(a)
#             m = len(b)
#             i = 0
#             j = 0
#             while i < n and j < m:
#                 if a[i] < b[j]:
#                     res.append(a[i])
#                     i += 1
#                 else:
#                     res.append(b[j])
#                     j += 1
#             res += a[i:] + b[j:]
#             return res
#
#         def recursion(nums):
#             mid = len(nums) // 2
#             arr1 = nums[:mid]
#             arr2 = nums[mid:]
#
#             if len(arr1) >= 2:
#                 arr1 = recursion(arr1)
#             if len(arr2) >= 2:
#                 arr2 = recursion(arr2)
#
#             return merge_res(arr1, arr2)
#
#         final = recursion(nums)
#         return final

# itmo 15
# a = [17, 2, 9, 5, 3, 1, 10]
#
#
# def select_sort(lst):
#     for i in range(1, len(lst)):
#         j = i
#         while j > 0 and a[j] < a[j - 1]:
#             a[j - 1], a[j] = a[j], a[j - 1]
#             j -= 1
#     return lst
#
#
# print(select_sort(a))


"""2160"""
# my_list = 1549
# def minimumSum(num):
#     lst = sorted(map(int, list(str(my_list))))
#     print(lst)
#     num1 = lst[0] * 10 + lst[2]
#     if num1 > 0:
#         num2 = lst[1] * 10 + lst[3]
#     else:
#         num1 = lst[2]
#         num2 = lst[3]
#
#     return num1 + num2
#
# print(minimumSum(my_list))


"""1859"""

# a = "is2 sentence4 This1 a3"
#
# def sortSentence(s: str) -> str:
#     lst = s.split()  # [is2,sen4,This1,a3]
#     dct = {}
#     res = []
#     for i in range(len(lst)):
#         dct[int(lst[i][-1]) - 1] = lst[i][:-1]
#     # dct -> {0:This, 1:is, 2:a, 3:sen}
#     for i in range(len(lst)):
#         res.append(dct[i])
#     # res -> [This, is, a, sen]
#     result = ' '.join(res)
#     return result
#
# print(sortSentence(a))
#
#
# def sortSentence2(s: str) -> str:
#     words = s.split()
#     ans = [""] * len(words)
#     for word in words:
#         ans[int(word[-1]) - 1] = word[:-1]
#     return " ".join(ans)


# 1464
# nums = [3, 4, 5, 2]


# output = (5-1) * (4-1) = 12
# def maxProduct(nums):
#     max1 = 0
#     max2 = 0
#     for i in range(len(nums)):
#         if nums[i] > max1:
#             max2 = max1
#             max1 = nums[i]
#         elif nums[i] > max2:
#             max2 = nums[i]
#     return (max1 - 1) * (max2 - 1)


# Через heapq(бинарное дерево и СД куча)

# import heapq
# def maxProduct(nums):
#     heap = [-1]
#     for num in nums:
#         if num > heap[0]:
#             if len(heap) == 2:
#                 heapq.heappop(heap)
#             heapq.heappush(heap, num)
#
#     return (heap[0] - 1) * (heap[1] - 1)


# import heapq


# def minimumOperations(nums) -> int:
#     maximum = 0
#     for i in range(len(nums)):
#         if nums[i] > maximum:
#             maximum = nums[i]
#     heapq.heapify(nums)
#     score = 0
#     cnt = 0
#     while maximum > 0:
#         nums[0] -= cnt
#         if nums[0] > 0:
#             el = heapq.heappop(nums)
#             cnt += el
#             maximum -= el
#             score += 1
#         else:
#             heapq.heappop(nums)
#     return score
#
# a = [1, 3, 5, 5, 7, 9]
# minimumOperations(a)


# def kWeakestRows(mat, k: int):
#     return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

# import heapq
# def kWeakestRows(mat,k):
#     m = len(mat)
#     dct = dict()
#     for i in range(m):
#         for j in range(len(mat[i])):
#             dct[i] = dct.get(i, 0) + mat[i][j]
#     heap = []
#     for k, v in dct.items():
#         heapq.heappush(heap, (v, k))
#     res = [heapq.heappop(heap)[1] for _ in range(k)]
#     return res
#
#
# k = 3
# mat = [[1, 1, 0, 0, 0],
#        [1, 1, 1, 1, 0],
#        [1, 0, 0, 0, 0],
#        [1, 1, 0, 0, 0],
#        [1, 1, 1, 1, 1]]
#
# print(kWeakestRows(mat, k))


# 1
# nums = [3, 2, 4, 1, 7, 10, 5], target = 6
# output -> [1, 2] - arr with index values for sum in target

# nums = [3, 2, 4, 1, 7, 10, 5]
# target = 6
# def twoSum(nums, target):
#     dct = {}
#     for i in range(len(nums)):
#         dct[nums[i]] = i
#     for i in range(len(nums)):
#         find_sec = target - nums[i]
#         if find_sec in dct and dct[find_sec] != i:
#             return [i, dct[find_sec]]

# print(twoSum(nums, target))


# 1512 Number of Good Pairs
# in [1,2,3,1,1,3]
# out 4

# in [1,1,1,1]
# out 6


# def numIdenticalPairs(nums) -> int:
#     dct = {}
#     score = 0
#     for i in range(len(nums)):
#         dct[nums[i]] = dct.get(nums[i], 0) + 1
#     for i in range(len(nums) - 1, 0, -1):
#         dct[nums[i]] -= 1
#         if dct[nums[i]]:
#             score += dct[nums[i]]
#     return score
#
# nums = [1,2,3,1,1,3]
# print(numIdenticalPairs(nums))


# 20 leetcode
# def isValid(str):
#     stack = []
#     dct = {
#         "(": ")",
#         "{": "}",
#         "[": "]"
#     }
#     for i in s:
#         if i in dct:
#             stack.append(i)
#         elif not stack or dct[stack.pop()] != i:
#             return False
#     return not stack
#
# s = "({}[])"
#
# print(isValid(s))


# a = [3, 4, 4, 5, 2]
#
#
# def count_sort(lst):
#     minimum = min(lst)  # 2
#     maximum = max(lst)  # 5
#     k = maximum - minimum + 1  # 4
#     count = [0] * k  # [1,1,2,1]
#     for val in lst:
#         count[val - minimum] += 1
#     nowpos = 0
#     for i in range(0, k):  # [0,1,2,3]
#         for j in range(count[i]):
#             lst[nowpos] = i + minimum
#             nowpos += 1


# num1 = 1351
# num2 = 3514
#
#
# def check_nums(x, y):
#     def count_num(value):
#         count = [0] * 10
#         while value > 0:
#             last_dig = value % 10
#             count[last_dig] += 1
#             value //= 10
#         return count
#
#     count_x = count_num(x)
#     count_y = count_num(y)
#     for i in range(10):
#         if count_x[i] != count_y[i]:
#             return False
#     return True
#
#
# print(check_nums(num1, num2))


# 2367 leetcode

# nums = [0, 1, 4, 6, 7, 10]
# diff = 3
#
#
# def arithmeticTriplets(nums, diff: int) -> int:
#     n = len(nums)
#     res = 0
#     dct = {}
#     for i in range(n):
#         dct[nums[i]] = i
#     for i in range(n - 1, 0, -1):
#         if (nums[i] - diff * 2) in dct and (nums[i] - diff) in dct:
#             res += 1
#     return res


# 2006
# nums = [3,2,1,5,4,2]
# k = 2
#
# # O(nlogn)
# def countKDifference(nums, k: int) -> int:
#     nums = sorted(nums, reverse=True)
#     dct = {}
#     result = 0
#     for i in range(len(nums)):
#         dct[nums[i]] = dct.get(nums[i], 0) + 1
#     for i in range(len(nums)):
#         if (nums[i] - k) in dct:
#             cur = dct.pop(nums[i], 0) * dct[nums[i] - k]
#             result += cur
#     return result
#
#
# print(countKDifference(nums, k))
#
# # O(n)
# def countKDifference2(nums, k: int) -> int:
#     dct = {}
#     result = 0
#     for i in nums:
#         if i + k in dct:
#             result += dct[i + k]
#         if i - k in dct:
#             result += dct[i - k]
#         dct[i] = dct.get(i, 0) + 1
#     return result
#
# print(countKDifference2(nums, k))


# 561
# nums1 = [1,4,3,2]
# #out = 4 min(1, 2) + min(3, 4)
#
# nums2 = [6,2,6,5,1,2]
# #out = 9 min(1, 2) + min(2, 5) + min(6, 6)
# def arrayPairSum(nums) -> int:
#     # nums = [1, 2, 3, 5, 7, 7, 8, 8, 10, 10] -> 1 + 3 + 7 + 8 + 10 = 29
#     counter = len(nums) // 2
#     if counter > 1:
#         nums.sort()
#         result = nums[0] + nums[-2]  # 1 + 10 = 11
#     else:
#         return min(nums)
#     if counter > 2:
#         for i in range(2, len(nums) - 2, 2):  # +3 +7 +8
#             result += nums[i]
#     return result
#
# print(arrayPairSum(nums1))
# print(arrayPairSum(nums2))


# 1684
# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
#
#
# # word in allowed
# # out = 2 ['aaab', 'baa']
#
# #Затратно по памяти,создаем set для каждого элемента в массиве words
# def countConsistentStrings(allowed: str, words) -> int:
#     check = set(allowed)
#     score = 0
#     for el in words:
#         if check >= set(el):
#             score += 1
#     return score
#
#
# print(countConsistentStrings(allowed, words))
#
#
# #better -> O(n*k), где k- длина каждой строчки
# def countConsistentStrings2(allowed: str, words) -> int:
#     check = set(allowed)
#     score = 0
#     for word in words:
#         for i in word:
#             if i not in check:
#                 score += 1
#     return len(words) - score
#
# print(countConsistentStrings2(allowed, words))


# BINARY SEACRH
# a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target = 3
#
# #bug theme
# #2089
# def targetIndices(nums, target):
#     nums.sort()
#     l = -1
#     r = len(nums)
#     if r > 1:
#         result = []
#         while r > l + 1:  # [1, 2, 4, 5, 6]  # target 2
#             mid = (l + r) // 2
#             if nums[mid] >= target:
#                 r = mid  # idx2 -> 4
#             else:
#                 l = mid
#         if r < len(nums) and nums[r] == target:
#             result.append(r)
#             while r + 1 < len(nums) and nums[r] == nums[r + 1]:
#                 result.append(r + 1)
#                 r += 1
#         return result
#     else:
#         if nums[0] == target:
#             return [0]
#         else:
#             return []
#
# print(targetIndices(a, target))


# 1351
# grid = [[3,-1,-3,-3,-3],[2,2,3,3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]]
#
# def countNegatives(grid) -> int:
#     n = len(grid[0])
#     def bin_search(arr):
#         l, r = -1, n
#         if r > 1:
#             while r > l + 1:
#                 mid = abs(l + r) // 2
#                 if arr[mid] < 0:
#                     r = mid
#                     if r <= 0:
#                         return n
#                 else:
#                     l = mid
#                     if l > n:
#                         return 0
#             return n - r
#         elif r == 1 and arr[0] < 0:
#             return n
#         else:
#             return 0
#
#     return sum([bin_search(arr) for arr in grid])
# print(countNegatives(grid))


# 9 without str()
a = 101  # palindrome True/False


def isPalindrome(x: int) -> bool:
    hashmap = {}
    if x < 0:
        return False
    else:
        cur = 0
        while x:
            last = x % 10
            hashmap[cur] = last
            cur += 1
            x //= 10
    start = 0

    while cur > start:
        if hashmap[start] == hashmap[cur - 1]:
            start += 1
            cur -= 1
        else:
            return False
    return True


print(isPalindrome(a))
