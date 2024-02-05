#TASK 2
def isPermutation(L1, L2):
    if len(L1) != len(L2):
        return False
    else:
        set1 = set(L1)
        set2 = set(L2)

        if set1 == set2:
            return True
        else:
            return False



# TASK 3
songs_ratings = {
    'Shine bright like a diamond': 1,
    'Turn back to black': 3,
    'Howling tides': 5,
    'Pokerface': 7,
    'Worlds Collide': 9,
    'Ta piosenka jest napisana dla pieniędzy': 10,
    'Najlepsze HITY': 2,
    'Dynasty': 5,
    'Still Here': 4,
    'Numb': 6,
}

for song, rating in songs_ratings.items():
    if rating == 5:
        print(song, rating)


#TASK 4
def replace(d,v,e):
    for key, value in d.items():
        if value == v:
            d[key] = e



#TASK 5
#NIE ROZUMIEM TREŚCI


#TASK 6
#LONG



#TASK 7
#REQUIRES TASK 6


#TASK 8

def roman_to_arabic(roman_numeral):
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    arabic_numeral = 0
    prev = 0

    for char in reversed(roman_numeral):
        value = roman_dict[char]

        if  value >= prev:
            arabic_numeral = arabic_numeral + value
        else:
            arabic_numeral = arabic_numeral - value

        prev = value
    return arabic_numeral
print(roman_to_arabic("MMXD"))