import pygame
import random

class Hitbox:
    def __init__(self, rect):
        self.rect = rect
        self.prev_left_click = False

    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left_click, _, _ = pygame.mouse.get_pressed()


        if left_click and not self.prev_left_click and self.rect.collidepoint(mouse_x, mouse_y):
            self.prev_left_click = True
            return True
        else:
            self.prev_left_click = left_click
            return False

    def move_to_random_position(self, screen_width, screen_height):
        new_x = random.randint(0, screen_width - self.rect.width)
        new_y = random.randint(0, screen_height - self.rect.height)
        self.rect.topleft = (new_x, new_y)