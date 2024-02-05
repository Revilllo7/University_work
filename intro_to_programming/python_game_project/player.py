import pygame

class Player:

    def __init__(self, screen, size=101, player_sprite="assets/Player_Sprite.png"):
        self.size = size
        self.image = pygame.image.load(player_sprite)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)

        self.jump_height = 10
        self.velocity_y = 0
        self.gravity = 1
        self.is_jumping = True

        self.direction = 1
        self.flip = False

        self.arrow_size = (25, 10)
        self.arrow_color = (255, 255, 255)
        self.arrow_start_pos = None
        self.arrow_end_pos = None
        self.is_shooting = False

    def shoot_arrow(self):
        if self.is_shooting:
            if self.arrow_start_pos and self.arrow_end_pos:
                num_points = 100
                points = []

                for t in range(num_points + 1):
                    gravity = 1
                    alpha = t / num_points
                    x = int((1 - alpha) * self.arrow_start_pos[0] + alpha * self.arrow_end_pos[0])
                    y = int((1 - alpha) * self.arrow_start_pos[1] + alpha * self.arrow_end_pos[1] - gravity * (alpha * (1 - alpha)) * self.screen.get_height())

                    points.append((x, y))

                pygame.draw.lines(self.screen, self.arrow_color, False, points, 2)
    def update_arrow(self):
        if self.is_shooting:
            self.arrow_start_pos = self.rect.center
            self.arrow_end_pos = pygame.mouse.get_pos()

    def move(self, keys):
        speed = 5

        if pygame.mouse.get_pressed()[0]:
            if not self.is_shooting:
                self.is_shooting = True
                self.update_arrow()
        else:
            if self.is_shooting:
                self.is_shooting = False
                self.shoot_arrow()

        if not self.is_shooting:
            if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                if not self.is_jumping:
                    self.is_jumping = True
                    self.velocity_y = self.jump_height

            if self.is_jumping:
                self.velocity_y -= self.gravity
                self.rect.y -= self.velocity_y

                if self.rect.y >= self.screen.get_height() - self.size:
                    self.rect.y = self.screen.get_height() - self.size
                    self.is_jumping = False
                    self.velocity_y = 0

            # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            #     self.rect.y += speed if self.rect.y < self.screen.get_height() - self.size else 0  # Move down
            # Nie ma już możliwości chodzenia w dół, ale kod zostawiam sobie na przyszłość
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.flip = True
                self.direction = -1
                self.rect.x -= speed if self.rect.x > 0 else 0  # Move left
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.flip = False
                self.direction = 1
                self.rect.x += speed if self.rect.x < self.screen.get_width() - self.size else 0  # Move right

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
