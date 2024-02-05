tuple1 = ("Apple", [10, 20, 30], (15, 25, 35))
for i in range(len(tuple1)):
    for j in range(len(tuple1[i])):
        if tuple1[i][j] == 20:
            print(tuple1[i][j])


tuple2 = (1,2,3,4)
a = tuple2[0]
b = tuple2[1]
c = tuple2[2]
d = tuple2[3]
print(a)
print(b)
print(c)
print(d)


tuple3 = (1,2,3,4)
tuple4 = (5,6,7,8)
tuple3, tuple4 = tuple4, tuple3
print(tuple3)
print(tuple4)


aTuple = (1,2,3,4,5,1,6,1)
count = 0
for i in range(len(aTuple)):
    if aTuple[i] == 1:
        count += 1
print(count)