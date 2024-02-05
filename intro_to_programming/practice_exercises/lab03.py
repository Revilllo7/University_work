# TASK 2
n = 5
while n>=1:
    print(n*"*")
    n -= 1

# TASK 3
n = 5
for i in range(1,n+1):
    print(((n-i)*" ")+(i*"*"))


# TASK 4
n = 5
for i in range(n+1):
    print(i*"*")


# TASK 5
n = 5
for i in range(n+1):
    print((i*" ")+(n-i)*"*")



# TASK 6
n = 5
for i in range(n+1):
    print(i*"* ")



# task 7
n = 17
for i in range(n+1):
    print(((n-i)*" ")+(i*" *")+((n-i)*" "))
print((n-2)*" "+"|___|")





# TASK 8
n = 6
silnia = 1
for i in range(1, n):
    silnia = i * silnia
print(silnia)




# TASK 9
n = 10
sum = 0
for i in range(1,n):
    sum = i + sum
print(sum)




#TASK 10
n = 5
prev = 0
for i in range(1, n+1):
    current = i
    sum = current + prev
    print(sum)
    prev = current




# TASK 11
prev = 0
for i in range(1,11):
    print(prev+i)
    prev = prev + i


#TASK 12
for i in range(0,5):
    print(2**i)
    print(-2**i)



#TASK 13
for i in range(2,800):
    if i >= 2:
        prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)




#TASK 14
a = 32
b = 74
wynik_14 = 0
for i in range(1, min(a, b) +1):
    if a % i == 0 and b % i == 0:
        wynik_14 = i
print(i)


#TASK 15
# Print the header
print("Multiplication Table:")

# Print the column headers
for i in range(1, 11):
    print(f"\t{i}", end="")
print("\n" + "-" * 90)

# Print the multiplication table
for i in range(1, 11):
    print(f"{i} |", end="")
    for j in range(1, 11):
        result = i * j
        print(f"\t{result}", end="")
    print()



#TASK 16



#TASK 17