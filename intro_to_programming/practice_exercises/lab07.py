# # TASK 1
# import random
# def random_whole_numbers(n):
#     whole_numbers = []
#     for i in range(n):
#         whole_numbers.append(random.randint(1,100))
#     return whole_numbers
# print(random_whole_numbers(5))
#
# def random_whole_numbers_nofor(n):
#     whole_numbers = []
#     while n > 0:
#         whole_numbers.append(random.randint(1,100))
#         n = n - 1
#     return whole_numbers
# print(random_whole_numbers_nofor(5))

# UKRYTE DO 6
def sort(lista):
    sort.lista = lista

# TASK 2
# def sort_with_FOR(n):
#     list_2 = []
#     var = 0
#     for i in range(n):
#         list_2.append(random.randint(var, var+10))
#         var = var + 5
#     return list_2
# print(sort_with_FOR(10))
#
# def sort_with_while(n):
#     list_2 = []
#     var = 0
#     i = 0
#     while i < n:
#         list_2.append(random.randint(var, var+10))
#         var = var + 10
#         i = i + 1
#     return list_2
# print(sort_with_while(10))



# TASK 3
def index(x, list_3):
    index = 0
    flag = False

    for i in range(len(list_3)):
        if list_3[i] == x:
            index = i
            flag = True
    if flag != False:
        return index
    else:
        return "out of scope"
print(index(9,[10, 8, 4, 2, 1, 6, 7, 2]))

def index_while(x, list_3):
    index = 0
    i = 0
    flag = False

    while i < len(x):
        if list_3 == x:
            index = i
        i = i + 1
    if flag != False:
        return index
    else:
        return "out of scope"
print(index(2,[10, 8, 4, 2, 1, 6, 7, 2]))



# BINARY SEARCH
def binary_search(x, list_x):
    low = 0
    mid = 0
    high = len(list_x) - 1

    while low <= high:
        mid = (low + high) // 2

        if list_x[mid] == x:
            return mid
        elif list_x[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return False



# TASK 4
def index_sorted(x, list_4):
    index = binary_search(x, list_4)

    if index != False:
        while index < len(list_4) - 1 and list_4[index + 1] == x:
            index = index + 1
        return index
    else:
        return -1
# print(index_sorted(10, [9, 10, 15, 24, 33, 47, 60, 63, 76, 89, 100]))


# TASK 5
#
# def bigger_smaller_equal_x_with_for(x):
#     list = [5, 3, 2, 1, 7, 19, 20, 21, 1, 6, 7, 9, 10, 11, 15]
#     bigger = 0
#     smaller = 0
#     equal = 0
#     for i in range(len(list)):
#         if x == list[i]:
#             equal = equal + 1
#         else:
#             if x < list[i]:
#                 bigger = bigger + 1
#             else:
#                 smaller = smaller + 1
#
#     return "bigger than x",bigger, "smaller than x", smaller,"equal x", equal
# print(bigger_smaller_equal_x_with_for(10))
#
#
# def bigger_smaller_equal_x(x):
#     list = [5, 3, 2, 1, 7, 19, 20, 21, 1, 6, 7, 9, 10, 11, 15]
#     bigger = 0
#     smaller = 0
#     equal = 0
#     i = 0
#     while i <= len(list):
#         if x == list[i-1]:
#             equal = equal +1
#             i = i +1
#         else:
#             if x < list[i-1]:
#                 bigger = bigger + 1
#                 i = i + 1
#             else:
#                 smaller = smaller + 1
#                 i = i + 1
#
#     return "bigger than x",bigger-1, "smaller than x", smaller,"equal x", equal
# print(bigger_smaller_equal_x(15))


# TASK 6
def bigger_smaller_equal_sorted(x, list_6):
    i = index_sorted(x, list_6)
    equal = 0

    while list_6[i] == x:
        equal = equal + 1
        i = i - 1

    smaller = index_sorted(x, list_6) - equal + 1
    bigger = len(list_6) - smaller - equal

    print("bigger than x", bigger)
    print("equal x", equal)
    print("smaller than x", smaller)

bigger_smaller_equal_sorted(7, sorted([5, 3, 2, 1, 7, 19, 20, 21, 1, 6, 7, 9, 10, 11, 15]))
#
#
# # TASK 7
#
# def f(x):
#     return ((x**3)-(2*x**2)+x-7)
#
# def bijection(a, b, epsilon):
#     while abs(a - b) > epsilon:
#         x1 = (a + b) / 2
#
#         if abs(f(x1)) <= epsilon:
#             break
#         else:
#             if f(x1) * f(a) < 0:
#                 b = x1
#             else:
#                 a = x1
#     return (a + b) / 2
# print(bijection(0, 3, 0.2))
#
#
#
#
# # TASK 8
#
# def root(n):
#     kd = 1
#     kg = n
#
#     while True:
#         if kg - kd <= 1:
#             return False
#         else:
#             j = (kg + kd) / 2
#             if j == n:
#                 return n
#             else:
#                 if j > n:
#                     kg = j
#                 else:
#                     if j < n:
#                         kd = j
# print(root(16))
#
#
#
#
#
#
# # TASK 9
# def index_max(list_9, max):
#     i = 0
#     max_i = 0
#     while i < max:
#         if list_9[i] > list_9[max_i]:
#             max_i = i
#         i = i + 1
#
#     return max_i
#
# def sort_max(list_9):
#     max = len(list_9) - 1
#
#     while max > 1:
#         max_i = index_max(list_9, max)
#         if (max_i != max - 1):
#             list_9[max], list_9[max_i] = list_9[max_i], list_9[max]
#         max = max - 1
#
#     return list_9
#
# list_9 = [10, 8, 4, 2, 1, 6, 7, 2]
# print(index_max(list_9, len(list_9)))
# print(sort_max(list_9))
#
#
#
#
#
# # TASK 10
#
# def BubbleSort(list_10):
#     n = len(list_10)
#     i = 0
#
#     while i < n:
#         swap = False
#         j = 0
#
#         while j < n - i - 1:
#             if list_10[j] > list_10[j+1]:
#                 list_10[j], list_10[j+1] = list_10[j+1], list_10[j]
#                 swap = True
#             j = j + 1
#         i = i + 1
#         if not swap:
#             break
#
#     return list_10
# print(BubbleSort([5, 3, 2, 1, 7, 19, 20, 21, 1, 6, 7, 9, 10, 11, 15]))
#
#
#
#
#
# # TASK 11
#
# def swap(list_11, x):
#     i = 0
#     j = 0
#
#     while i < x:
#         while j < len(list_11) - x:
#             print(j, (j + x)%len(list_11))
#             list_11[j], list_11[(j + x)%len(list_11)] = list_11[(j + x)%len(list_11)], list_11[j]
#             j = j + 1
#         i = i + 1
#
#     return list_11
# print(swap([5, 3, 2, 1, 7, 19, 20, 21, 1, 6, 7, 9, 10, 11, 15], 3))