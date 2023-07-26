import pygame
import random

pygame.init()

# Setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_over = False

x1 = window_width / 2
y1 = window_height / 2

x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
foody = round(random.randrange(0, window_height - 10) / 10) * 10.0



clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Check for arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 = x1 + x1_change
    y1 = y1 + y1_change

    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = True


    window.fill(black)

    pygame.draw.rect(window, red, [400, 300, 10, 10])
    pygame.draw.rect(window, white, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(30)
