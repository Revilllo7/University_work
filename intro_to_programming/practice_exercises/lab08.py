# TASK 1
# SORTOWANIE PRZEZ WSTAWIANIE
# SPRAWDŹ CO JEŚLI NOWY ELEMENT JEST NAJMNIEJSZY LUB RÓWNY ZERO
def wstaw(lista):
    i = 1

    while i < len(lista):
        x = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > x:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = x
        i = i + 1
    return lista

print(wstaw([1,3,5,6,4,0]))




# TASK 2                                                              ??????????????????????????????????????????????????
def wstaw(lista):
    i = 1

    while i < len(lista):
        x = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > x:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = x
        i = i + 1
    return lista

print(wstaw([1,3,5,6,4,0]))




# TASK 3






# TASK 4
# def same_number_same_index(lista):
#     index = 0
#     for i in range(len(lista)):
#         for j in range(len(lista[i])):
#             if lista[i][j] == lista[j+1][i]:
#                 index = j
#         print(lista)
#
#
#
# print(same_number_same_index([[1,2,3,4,5], [5,2,3,4,1], [6,7,3,14]]))



# TASK 5
def difference_of_neighbours(lista):
    difference = []
    absolute = 0
    for i in range(len(lista)-1):
        absolute = lista[i] - lista[i+1]
        difference.append(abs(absolute))
    return difference

print(difference_of_neighbours([1,1,3,4,4,5,7]))





# TASK 6
def repeating(lista):
    repeats = []
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            repeats.append(lista[i])
    return repeats
print(repeating([1,1,3,4,4,5,6,7]))


# TASK 7
def mean_value(lista):
    mean = []
    for i in range(len(lista)):
        if lista[i].type != int:
            break
        else:
            mean.append(lista[i])
    return mean

print(mean_value([1,4,"l",5,10,"o",20,"l"]))