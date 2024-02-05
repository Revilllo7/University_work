import pygame, os, sys, math, subprocess
from player import Player
from hitbox import Hitbox
from buttons import Button
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Bullseye_game")
player = Player(screen)
hitbox_rect = pygame.Rect(500, 300, 25, 25)
hitbox = Hitbox(hitbox_rect)
counter = 0
points = 0
clock = pygame.time.Clock()
timer_font = pygame.font.Font(None, 36)
timer_color = (255, 255, 255)
timer_position = (10, 10)
counter_font = pygame.font.Font(None, 36)
counter_color = (255, 255, 255)
counter_position = (10, 50)
points_font = pygame.font.Font(None, 36)
points_color = (255, 255, 255)
points_position = (10, 90)
GAME_RUNNING = 0
GAME_OVER = 1
game_state = GAME_RUNNING
start_time = 60
current_time = start_time
timer_started = False
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
save_button_image = None
save_button_pos = (res[0] // 2, res[1] // 2 + 250)
save_button_text = "Save game"
save_button_font = pygame.font.Font("assets/font.ttf", 36)
save_button_base_color = (255, 255, 255)
save_button_hover_color = (255, 0, 0)
save_button = Button(save_button_image, save_button_pos, save_button_text, save_button_font, save_button_base_color, save_button_hover_color)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not timer_started and (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
            timer_started = True
        if event.type == timer_event and timer_started and game_state == GAME_RUNNING:
            current_time -= 1
            if current_time <= 0:
                game_state = GAME_OVER
        if game_state == GAME_OVER:
            save_button.input(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN and save_button.input(pygame.mouse.get_pos()):
                os.environ['HITS'] = str(counter)
                os.environ['POINTS'] = str(points)
                pygame.quit()
                subprocess.run([sys.executable, "scoring.py"])
                sys.exit()
    keys = pygame.key.get_pressed()
    if game_state == GAME_RUNNING:
        player.move(keys)
        if hitbox.is_clicked():
            distance = math.sqrt((player.rect.centerx - hitbox.rect.centerx)**2 + (player.rect.centery - hitbox.rect.centery)**2)
            if distance > 1000:
                points += 5
            elif distance > 750:
                points += 4
            elif distance > 500:
                points += 3
            elif distance > 250:
                points += 2
            else:
                points += 1
            counter += 1
            hitbox.move_to_random_position(*res)
    screen.fill((0, 0, 0))
    if game_state == GAME_RUNNING:
        player.draw()
        player.shoot_arrow()
        pygame.draw.rect(screen, (255, 0, 0), hitbox_rect, 2)
        timer_text = timer_font.render(f"Time: {current_time}s", True, timer_color)
        screen.blit(timer_text, timer_position)
        counter_text = counter_font.render(f"Hits: {counter}", True, counter_color)
        screen.blit(counter_text, counter_position)
        points_text = points_font.render(f"Points: {points}", True, points_color)
        screen.blit(points_text, points_position)
    elif game_state == GAME_OVER:
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(res[0] // 2, res[1] // 2 - 50))
        screen.blit(game_over_text, game_over_rect)
        final_counter_text = counter_font.render(f"Final Hits: {counter}", True, (255, 255, 255))
        final_points_text = points_font.render(f"Final Points: {points}", True, (255, 255, 255))
        final_counter_rect = final_counter_text.get_rect(center=(res[0] // 2, res[1] // 2 + 70))
        final_points_rect = final_points_text.get_rect(center=(res[0] // 2, res[1] // 2 + 110))
        screen.blit(final_counter_text, final_counter_rect)
        screen.blit(final_points_text, final_points_rect)
        save_button.update(screen)
    pygame.display.update()
    clock.tick(60)