# # TASK 1
#
# def silnia(n):
#     if n > 0:
#         return silnia(n - 1) * n
#     elif n == 0:
#         return 1
#     else:
#         return "nie liczymy silni z ujemnych"
#
# print(silnia(5))
#
#
#
#
#
# # TASK 2
# def fib(n):
#     if n <= 1:          #fib(0) i fib(1)    nie wiem co z ujemnymi
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(10))
#
#
#
#
#
# # TASK 3
# def epsilon(n):
#     if n == 0:
#         return 0
#     return 1/n + epsilon(n - 1)
#
# print(epsilon(10))
#
#
#
#
#
# # TASK 4
# def squared(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return squared(n - 1) + n + (n - 1)
#
# print(squared(5))
#
#
#
#
#
# # TASK 5
# def sum_even(n):
#     if n <= 1:
#         return 0
#     else:
#         if n % 2 == 0:
#             return n + sum_even(n - 2)
#         else:
#             return sum_even(n - 1)
#
# print(sum_even(5))  #6
#
#
#
#
#
# # TASK 6
# def binary_search(x, lista, left, right):
#     if left <= right:
#         mid = left + (right - left) // 2
#
#         if lista[mid] == x:
#             return True
#         elif lista[mid] > x:
#             return binary_search(x, lista, left, mid - 1)
#         else:
#             return binary_search(x, lista, mid + 1, right)
#     else:
#         return False
#
# x = 5
# lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# print(binary_search(x,lista,0, len(lista)-1))   #True
#
#
#
#
#
# # TASK 7
# def power(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * power(a, b - 1)
#
#
# print(power(5, 2))  #25
#
#
#
#
#
# # TASK 8
#
#
#
#
#
# # TASK 9
# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_digits(n // 10)
#
# print(sum_digits(123456789))    #45
#
#
#
# # KARTKÓWKA Z REKURENCJI
# def fun(n):
#     print(n)
#     if n > 100:
#         return n - 10
#     else:
#         return fun(fun(n+11))
#
# print(fun(99))
#
#
#

# 10*

def head(head):
    head = head[0]
    return head

# print(head([1,2,3,4,5,6,7]))



# 11*
def tail(tail_list):
    tail_list = tail_list[1:]
    return tail_list

# print(tail([1,2,3,4,5,6,7]))

# 12*                                           # NIE WIEM
def isEmpty(empty_list):
    if len(empty_list) == 0:
        return True
    else:
        return False

# print(isEmpty([]))


def rewers(reverse_list):
    while isEmpty(reverse_list) != True:
        return rewers(tail(tail(reverse_list)).append(head(reverse_list)))



print(rewers([1,2,3,4,5,6,7]))