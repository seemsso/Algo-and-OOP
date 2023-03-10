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


voted = {}

#set realisation
def check_voter(name):
    if voted.get(name):
        print('already voted')
    else:
        voted[name] = True
        print('he can vote')

check_voter("Ivan") # => he can vote
check_voter("Petr") # => he can vote
check_voter("Nikolay") # => he can vote
check_voter("Ivan") # => already voted
