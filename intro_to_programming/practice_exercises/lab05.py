# task 1
list_1 = [6, 7, 19, 20, 63, 72, 91, 100]
for i_1 in range(0, len(list_1), 2):
    print(list_1[i_1])
print("task 1 ^")

# task 2
list_2 = ["word", "sentence", "alphabets"]
for i_2 in range(len(list_2)):
    print("(", list_2[i_2], ",", len(list_2[i_2]), ")")
print("task 2 ^")

# task 3
list_3 = [0, 1, 2, 3, 4, 5, 10]
elem_3 = 5
for i_3 in range(len(list_3)):
    if elem_3 == list_3[i_3]:
        print("yes")
    if i_3 == len(list_3) and elem_3 != list_3[i_3]:
        print("no")
print("task 3 ^")

# task 4
list_4 = [[1, 2, 3, 4], [5, 6, 7, 8]]
#for i_4 in range(len(list_4)):
#    for j_4 in range(len(list_4[i_4])):
#       print(list_4[j_4])
#print("task 4 ^")
#nie działa

# task 5
list_5 = [0, 1, 2, 3, 4, 5]
print(list_5)
x_5 = 0
Y_5 = 0
if list_5[0] != list_5[-1]:
    x_5 = list_5[-1]
    y_5 = list_5[0]
    list_5[0] = x_5
    list_5[-1] = y_5
print(list_5)
print("task 5 ^")

# task 6
#import random
n_6 = 3
#for
print("task 6 ^")
#nie działa

# task 7
scalar = 3
list_7 = [[1, 2, 4, 6], [2, 3, 4, 5], [12, 3, 4, 5]]
print("input:", list_7, scalar)
for i_7 in range(len(list_7)):
    for j_7 in range(len(list_7[i_7])):
        list_7[i_7][j_7] = list_7[i_7][j_7] * scalar
print("output", list_7, scalar)
print("task 7 ^")

# task 8
# list_8 = []
# sec_list_8 = []
# for i in range(1, 21, 1):
#     list_8.append(i)
# sec_list_8 = list_8[::-1]
# thi_list_8 = [[list_8][int(sec_list_8)]]
# print(thi_list_8)
#nie działa

# task 9
list_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sec_list_9 = [11, 12, 13]
list_9[-1] = sec_list_9[0]
for i_9 in range(1, len(sec_list_9), 1):
    list_9.append(sec_list_9[i_9])
print(list_9)
print("task 9 ^")

# task 10
list_10 = [[1, 2, 3], [7, 8, 9], [4, 5, 6]]
previous = 0
sum = 0
results_list = []
for i_10 in range(len(list_10)):
    for j_10 in range(len(list_10[i_10])):
        previous = j_10+1
        sum = sum + previous
    results_list.append(sum)
print(results_list)
#nie działa

# task 11
matrices = [[a, b, c], [d, e, f], [g, h, i]]
