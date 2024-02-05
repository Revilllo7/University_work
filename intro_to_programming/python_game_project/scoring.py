import pygame
import os
import subprocess
import sys
from buttons import Button

class Scoring:
    def __init__(self):
        self.player_data = {}
        self.hits = int(os.environ.get('HITS', 0))
        self.points = int(os.environ.get('POINTS', 0))

    def save_score(self, user_name):
        player_data = {
            'user_name': user_name,
            'hits': self.hits,
            'points': self.points
        }
        self.player_data[user_name] = player_data

        try:
            with open('scores.txt', 'a') as file:
                file.write(f"{player_data}\n")
        except FileNotFoundError:
            with open('scores.txt', 'w') as file:
                file.write(f"{player_data}\n")

    def display_score(self):
        pygame.init()
        res = (640, 360)
        screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Enter Your Name")

        font = pygame.font.Font("assets/font.ttf", 36)
        input_box = pygame.Rect(220, 150, 200, 60)
        color_inactive = pygame.Color('White')
        color_active = pygame.Color('Red')
        color = color_inactive
        active = False
        text = ''
        clock = pygame.time.Clock()

        save_button = Button(None, (375, 240), "Save", font, color_inactive, color_active)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive

                    if save_button.input(event.pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                        self.save_score(text)
                        pygame.quit()
                        subprocess.run([sys.executable, "scoreboard.py"])
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((30, 30, 30))

            hits_text = font.render(f"Hits: {self.hits}", True, (255, 255, 255))
            points_text = font.render(f"Points: {self.points}", True, (255, 255, 255))
            screen.blit(hits_text, (220, 50))
            screen.blit(points_text, (220, 100))

            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)

            save_button.color_change(pygame.mouse.get_pos())
            save_button.update(screen)

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    scoring = Scoring()
    scoring.display_score()
