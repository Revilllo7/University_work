import pygame
from buttons import Button
import os
import sys
import subprocess

pygame.init()

def read_scores(filename="scores.txt"):
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            # Use eval to convert the string representation of the dictionary to an actual dictionary
            scores = [eval(line.strip()) for line in file]
        return scores
    else:
        print("ERROR: file doesn't exist, create one!")
        return []

def bubble_sort(scores):
    n = len(scores)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if scores[j]['points'] < scores[j + 1]['points']:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]

def display_scores(screen, font):
    scores = read_scores()
    bubble_sort(scores)

    y_offset = 150
    for rank, score in enumerate(scores, start=1):
        player = score['user_name']
        hits = str(score['hits'])
        points = str(score['points'])

        rank_text = font.render(str(rank), True, (255, 255, 255))
        player_text = font.render(player, True, (255, 255, 255))
        time_text = font.render(hits, True, (255, 255, 255))

        try:
            points_value = int(points)
        except ValueError:
            points_value = 0

        points_text = font.render(str(points_value), True, (255, 255, 255))

        screen.blit(rank_text, (150, y_offset))
        screen.blit(player_text, (350, y_offset))
        screen.blit(time_text, (750, y_offset))
        screen.blit(points_text, (950, y_offset))

        y_offset += 50

def main():
    res = (1280, 720)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Scoreboard")
    background = pygame.image.load("assets/background_scoreboard.png")
    screen.blit(background, (0, 0))
    font_path = "assets/font.ttf"
    font_size = 36
    font = pygame.font.Font(font_path, font_size)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            scoreboard_mouse_pos = pygame.mouse.get_pos()
            scoreboard_button = Button(image=pygame.image.load("assets/Button_border.png"), pos=(640, 640),
                                       text_input="Go back to menu", font=font, base_color="White",
                                       hover_color="#F51B14")
            for button in [scoreboard_button]:
                button.color_change(scoreboard_mouse_pos)
                button.update(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    subprocess.run([sys.executable, "menu.py"])
                    sys.exit()

        display_scores(screen, font)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
