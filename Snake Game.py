import pygame

pygame.init()

# Setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)

game_over = False

x1 = window_width / 2
y1 = window_height / 2

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(window, white, [x1, y1, 10, 10])
    pygame.display.update()
