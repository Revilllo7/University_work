# task 1
def bigger_number(x, y):
    if x > y:
        return x
    else:
        return y
print(bigger_number(5, 4))
print("1^")

# task 2
print(bigger_number(bigger_number(5, 4), 6))
print("2^")

# task 3
def sum_of_list(x):
    previous_3 = 0
    sum_3 = 0
    for i_3 in range(len(x)):
        previous_3 = x[i_3]
        sum_3 = sum_3 + previous_3
    return sum_3
print((sum_of_list([1, 4, 5])))
print("3^")

# task 4
def product_of_list(x):
    product_4 = 1
    for i_4 in range(len(x)):
        previous_4 = x[i_4]
        product_4 = product_4 * previous_4
    return product_4
print(product_of_list([1, 4, 5]))
print("4^")

# task 5
def reverse_string(x):
    text_5 = x[::-1]
    print(text_5)
reverse_string("wirus")
print("5^")

# task 6
def between_hundred_and_thousand(x):
    if x >= 100 and x <= 1000:
        return "funkcja zawiera się między 100 a tysiąc"
    else:
        return "funkcja nie zawiera się między 100 a tysiąc"
print(between_hundred_and_thousand(105))
print("6^")

# task 7
def non_repeating_list(x):
    list_7 = x
    add_list = []
    for i_7 in range(len(list_7)):
        flag = False
        for j_7 in range(len(add_list)):
            if list_7[i_7] == add_list[j_7]:
                flag = True
        if flag == False:
            add_list.append(list_7[i_7])
    return add_list

print(non_repeating_list([5, 3, 5, 9, 3, 2, 1]))
print("7^")

# task 8
def is_prime(x):
    if x == 1:
        return False
    elif x > 1:
        for i_8 in range(2, x):
            if (x % i_8) == 0:
                return False
        else:
            return True
    else:
        return False
print(is_prime(5))
print("8^")

# task 9
def remove_odd(x):
    list_9 = x
    even_list = []
    for i_9 in range(len(list_9)):
        if (list_9[i_9] % 2) == 0:
            even_list.append(list_9[i_9])

    return even_list
print(remove_odd([5, 5, 6, 10, 13, 7, 8, 6, 1]))
print("9^")


# task 10
def pangram(x):
    pangram = x.lower()
    pangram = pangram.replace(" ","")
    alphabet ="abcdefghijklmnopqrstwxyz"    #można go zmienić
    var = 0
    for i_10 in alphabet:
        if i_10 in pangram:
            var = var + 1
    if var == len(alphabet):
        return "the sentence is a pangram"
    else:
        return "the sentence is not a pangram"
print(pangram("the Quick brown fox jumps over the lazy dog"))
print("10^")

# task 11
def years_to_mins(x):
    leap_days = x//4
    normal_year = x * 365 * 24 * 60
    leap_year = leap_days * 24 * 60
    return normal_year + leap_year
print(years_to_mins(5))
print("11^")


# task 12
def is_sorted_increasing(x):
    list = x
    for i_12 in range(1, len(list)-1):
        if list[i_12] > list[i_12+1]:
            return True
        else:
            return False
print(is_sorted_increasing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("12^")

# task 13
def exists_in(list, x):
    elem = x
    flag = False

    for i_13 in range(len(list)):
        if list[i_13] == elem:
            flag = True
    return flag
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(exists_in(list,11))
print("13^")

# task 14
def exists_in_sorted(x):
    elem = x
    flag = False
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i_14 in range(len(list)):
        if i_14 == elem:
            flag = True
    return flag
print(exists_in_sorted(3))
print("14^")

# task 15
def swap_elements(list, x, y):
    list[x-1], list[y-1] = list[y-1], list[x-1]
    return list

print(swap_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 3))
print("15^")

# task 16
def is_positive(x):
    if x > 0:
        return 1
    else:
        return 0

# a + b > c
# a + c > b
# b + c > a
# all > 0

def can_triangle(a, b, c):
    if is_positive(a) and is_positive(b) and is_positive(c) == 1:
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return 1
        else:
            return 0

print(can_triangle(3, 4,5))
print("16^")