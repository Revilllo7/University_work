_Python game project
date started: 21/12/2023
date finished: 21/01/2023_


**idea:
Archery game that utilises the competitiveness of the sport
and works as a way to see who can get more points in a set amount of time**


![Bullseye](assets/Bullseye.png)
<pre>



    
</pre>

## todo
- [✅] Make a MENU
- [✅] Add settings? (only hosts scoreboard)
- [✅] Add quit button
- [ ] Create the game:
- - [✅] Scoring system
- - [✅] Arrow physics
- - [abandoned] Stamina/Hold bar (since holding a strung bow is tiresome)
- - [✅] Timer
- - [✅/❌] Graphics:
    - [✅] character 
    - [✅] ground
    - [abandoned] animations
    - [❌] background
- - [abandoned] X and Y axis shot (shot predictor exists, however it's baaad...)
- - [abandoned] hit animations?
  
<pre>




    
</pre>


## Captain log: a list of all the things implemented
1. created a repo, made a run.py file, got the pygame lib
2. created a menu that changes displays between: "start game", "settings", "quit"
3. created buttons file that is responsible for: initialising buttons, updating buttons, detecting inputs, changing color on hover for visual clarity.
4. added custom font.
5. added images, however, they require fixing, due to resolution issues. Need to make my own.
6. fixed centring issues, fixed resolution issues, made my own background and button borders.
7. Added player character
8. Added player movement
9. Added gravity and jumping
10. Added shot indicator on Q
11. START takes you to the game
12. SETTINGS -> SCOREBOARD takes you to the scoreboard
13. Scoreboard looks for scores.txt file and prints them out correctly sorting as it goes
14. Added background image for the menu. play and settings sections have their special backgrouns, alongside scoreboards.
15. Added player collision with walls
16. Added hitboxes for player to hit
17. Added points
18. Added Timer
19. Timer with 0 seconds ends game
20. Added number of hits
21. Added user name inputs
22. Added scoring.py which saves the data into a file
23. Added player_dictionaries
24. Fixed final bugs
25. Added the player_test file with all the tests used while making the game, however running them in that file will cause errors, cause
they are being used out of context
26. Adding logos, fixing up the README. tidying up
<pre>




    
</pre>



### KRYTERIA oceny
1 . podział projektu na pliki (2pkt)
- ✅ – mam podział na 7 plików, które importują z siebie dane i przesyłają sobie funkcje

2.  własne funkcje + testy 5 pkt (po 1 pkt za funkcję i test do niej)
- ✅ – mnóstwo własnych funkcji, player_tests.py zawiera testy do funkcji

3 użycie list, krotek, słowników (1,5 pkt)
- ✅ lista – points w player.py
- ✅ krotka – points w player.py / player_data w scoring.py
- ✅ słownik – player_data w scoring.py
  
Wszystkie są potem wykorzystywane w innej części pliku:
lista do rysowania paraboli
krotka i słownik są odczytywane dla scoreboarda


4. lista  najwyżej punktowanych odbytych gier (wraz z imieniem/nazwą gracza).(1pkt)
- ✅ – scores.txt

5. odczyt i zapis do pliku (1 pkt)
- ✅ – Scoring.py zapisuje do pliku, scoreboard odczytuje

6. algorytm  (np sortowanie) (2 pkt)
- ✅ – scoreboard utylizuje sortowanie bąbelkowe do sortowania wyników graczy

7. kompletność rozwiązania (2,5 pkt)
- ✅ – całość jest grywalna i nie wymaga zamykania programu lub wpisywania informacji do konsoli

8. akademicki poziom (5 pkt)
- Użycie biblioteki Pygame
- Użycie os, subsystem, sys
- Zmienne systemowe
- Time
- Menu
<pre>



    
</pre>


| Ocena | Max punkty | Wynik |
| :----: | :----: | :----: |
| podział na pliki:   |    2    | 2 |
| własne funkcje + testy:        |   5     | 5 |
| użycie list, krotek, słowników:    |  1,5 | 1,5 |
| scoreboard:   |  1 | 1 |
| odczyt i zapis plików:  |  1  | 1 |
| algorytm (sortowanie):  |  2  | 2 |
| kompletność rozwiązania:   |   2,5 | 2,5 |
|akademicki poziom:  |   5  | 5 |

Projekt uzyskał max. ilość punktów i uzyskał ocenę 100%

Project earned the max amount of points and scored me a 100% for the grade
