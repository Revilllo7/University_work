#TASK 2
n = 5
silnia = 1
while n >= 1:
    silnia = n * silnia
    n = n - 1
print(silnia)

#TASK 3
n = 5
sum = 0
while n >= 1:
    sum = n + sum
    n = n - 1
print(sum)



#TASK 4
n = 5
sum2 = 0
while n >= 1:
    sum2 = (n**2) + sum2
    n = n - 1
print(sum2)



#TASK 5
n = 5
sum3 = 0
while n >= 1:
    sum3 = (n**3) + sum3
    n = n - 1
print(sum3)


#task 6
n = 21
for i in range(1, n+1):
    if n%i == 0:
        print(i)



#TASK 7
a = 100
b = 10000
sum = a+b
count = 0
while sum >= 9:
    sum = sum//10
    count += 1
print(count)


#TASK 8
# --




#TASK 9 NIE DZIAŁA
# bin = 1001
# dec = 0
# for i in range(len(bin)):
#     if bin[i] == 1:
#         dec = 2**(len(bin)-bin[i])
# print(dec)


# TASK 10
for i in range(1,99):
    if i%5 == 1 and i%7 == 3:
        print(i)

