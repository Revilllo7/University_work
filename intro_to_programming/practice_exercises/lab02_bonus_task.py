'''
Algorytm:
1. Ustaw wynik jako 0
2. Jeśli B jest nieparzyste, dodaj do wyniku A
3. A * 2, B / 2. Na liczbach całkowitych
4. Jeśli B > 0; punkt (2), jeśli B < 0; punkt (5)
5. Zwróć wynik

Przesunięcia bitowe:
<< - MNOŻENIE
>> - DZIELENIE

Przykład:
4 * 8
_________________________________________
a   b   wynik   operacja                |
________________________________________|
4   8   0       b parzyste -> (3)
8   4   0       b parzyste -> (3)
16  2   0       b parzyste -> (3)
32  1   0       b nieparzyste -> (2)
64  0   32      b < 0 -> (5)

a = 64
b = 0
wynik = 32

########################################
                                        |
Przykład:                               |
4 * 9                                   |
_________________________________________
a   b   wynik   operacja                |
________________________________________|
4   9   0       b nieparzyste -> (2)
8   4   4       b parzyste -> (3)
16  2   4       b parzyste -> (3)
32  1   4       b nieparzyste -> (2)
64  0   36      b < 0 -> (5)

a = 64
b = 0
wynik = 36
'''

a = 4
b = 8
wynik = 0                       #placeholder
while b > 0:                    #dopóki b większe od 0:
    if b % 2 == 1:                  #jeżeli reszta z dzielenia b = 1
        wynik = wynik + a               #do wyniku dodaj a
    a = a << 1                      #przesunięcie bitowe (mnożenie *2)
    b = b >> 1                      #przesunięcie bitowe (dzielnie /2)
print(wynik)                    #wydrukuj wynik
