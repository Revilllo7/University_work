#zadanie 2
# word = "słowo"

#zadanie 3
list_3 = [6, 7, 10]
previous_3 = 0
sum_3 = 0
for i_3 in range(0, len(list_3)):
    previous_3 = list_3[i_3]
    sum_3 = sum_3 + previous_3
print(sum_3)

#zadanie 4
list_4 = [6, 7, 10]
previous_4 = 0
sum_4 = 1
for i_4 in range(0, len(list_4)):
    previous_4 = list_4[i_4]
    sum_4 = sum_4 * previous_4
print(sum_4)

#zadanie 5
list_5 = [1, 23, 65, 87, 99]
print(max(list_5))

#zadanie 6
list_6 = [1, 23, 0, 65, 87, 99]
min_6 = min(list_6)
print(min(list_6))
minimum_list = list_6.count(min(list_6))
for i_6 in range(0, len(list_6)):
    if list_6[i_6] == min_6:
        print(i_6+1)        #+1 by pokazać pozycje dla człowieka, nie licząc indeksu od 0


#zadanie 7
# list_7 = [46, 27, 74, 64, 73, 21, 15, 10]   #2nd biggest is 73
# max_7 = max(list_7)
# second_biggest = 0
# hold_value = 0
# for i_7 in range(1, len(list_7)):
#     if list_7[i_7] != max_7:
#         if hold_value >= second_biggest:
#             hold_value = second_biggest
#

#zadanie 8
list_8 = ["słowo", "o", "i", "kolejne", "słowo"]
for i_8 in range(0, len(list_8)):
    if len(list_8[i_8]) >= 3:
        print(list_8[i_8])

#zadanie 9
list_9_1 = [1, 2, 4, 8, 16, 32, 64]
list_9_2 = [1, 3, 5, 7, 9, 11, 13, 15]
list_length = 0
a_9_1 = max(list_9_1)               #sprawdzamy czy listy mają tą samą długość
b_9_1 = list_9_1.index(a_9_1)
a_9_2 = max(list_9_2)
b_9_2 = list_9_2.index(a_9_2)
if b_9_1 >= b_9_2:              #dłuższa lista zostaje zapisana pod length
    list_length = b_9_1
else:
    list_length = b_9_2

for i_9 in range(0, list_length):
    if list_9_1[i_9] == list_9_2[i_9]:
        print("TAK")

#zadanie 10
list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i_10 in range(0, len(list_10)):
    if list_10[i_10] % 2 == 0:
        print(i_10)

#zadanie 11
number = 372
list_single = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
list_teens = ["jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
list_decimal = [ "dwadzieścia", "trzydzieści", "czterdzieści", "pięcdziesiąt", "sześćdziediąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięcdziesiąt"]
list_hundred = ["sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
if number < 10:
    print(list_single[number])
if number > 10 and number < 20:
    print(list_teens[((number%10)-1)])
if number > 20 and number < 99:
    print(list_decimal[(round(number//10))-2], list_single[(number % 10)])
if number > 100 and number < 120:
    print(list_hundred[0], list_teens[(number%10)-1])
if number > 119 and number < 1000:
    print(list_hundred[round(number//100)-1], list_decimal[((number%100)//10)-2], list_single[round(number%10)])

#zadanie 12
#

#zadanie 13
word = "kajak"
placeholder = ""
for i_13 in word:
    placeholder = i_13 + placeholder
if (word == placeholder):
    print("jest palindromem")
else:
    print("nie jest palindromem")