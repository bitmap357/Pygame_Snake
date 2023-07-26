import pygame

pygame.init()

# Setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(window, white, [400, 300, 10, 10])
