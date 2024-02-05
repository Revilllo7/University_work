#TASK 2
print("Hello World!")



#TASK 3
print("jeden z wierszy J. Tuwima np kliknij")



#TASK 4
a = 5
b = 6
if a == b:
    print("TAK")
else:
    print("NIE")



#TASK 5
c = 5
if c % 2 == 0:
    print("Zmienna parzysta")
else:
    print("Zmienna nieparzysta")


#TASK 6
d = 5
e = 10
if d > e:
    print("d większe")
elif e < d:
    print("e większe")
else:
    print("liczby równe")



#TASK 7
f = 3
g = 4
h = 5
if f > g:
    if f > h:
        print(f)
    else:
        print(h)
elif g > f:
    if g > h:
        print(h)
    else:
        print(g)


# TASK 8
#BEZ MAX
#IT'S JUST LONG TO DO



# TASK 9
# y = ax + b
# x0 = -b/a
b = 10
a = 2
print((-b)/a)



# TASK 10
a = 1
b = 4
c = 10
delta = (b**2) - (4*a*c)
x1 = (-b + delta) / (2*a)
x2 = (-b - delta) / (2*a)
print(x1, x2)



#TASK 11
a = 974
single = (a%100)%10
decimal = (a%100)//10
hundred = (a//100)
print(single)
print(decimal)
print(hundred)