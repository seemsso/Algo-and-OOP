""" BINARY SEARCH """

def binary_search(list, item):
    low = 0
    res = 0
    high = len(list) - 1

    while low <= high:
        res += 1
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return f"Score iteration: {res} for value {mid}"
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

lst = [i for i in range(100)]
print(binary_search(lst, 32))

