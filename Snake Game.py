# imports
import pygame
import random

# initializing pygame
pygame.init()

# Setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Setting colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# setting game status and declaring score
game_over = False
score = 0

# setting the starting point of the snake
x1 = window_width / 2
y1 = window_height / 2

# movement of the snake
x1_change = 0
y1_change = 0

# growing the body of the snake
snake_body = []
length_of_snake = 1

# Setting points for the food
foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
foody = round(random.randrange(0, window_height - 10) / 10) * 10.0


# clock for the game
clock = pygame.time.Clock()

# the main game loop
while not game_over:
    # when the game quits
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

    # Adding changes to original position
    x1 = x1 + x1_change
    y1 = y1 + y1_change

    # Creating boundaries for the game
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = True

    # Creating the movement of the snake
    window.fill(black)

    # Creating the body of the snake
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    # Adding the extra parts to the body
    snake_body.append(snake_head)

    # Keeping the body as a body
    if len(snake_body) > length_of_snake:
        del snake_body[0]

    # Adding a condition for the game to be over
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    # Setting the font and displaying the score value
    font_style = pygame.font.SysFont(None, 50)
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    # Adding the food item and also making the snake longer when the food is picked
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
        foody = round(random.randrange(0, window_height - 10) / 10) * 10.0
        length_of_snake += 1
        score += 1

    # Food items
    pygame.draw.rect(window, red, [foodx, foody, 10, 10])
    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], 10, 10])
    pygame.display.update()
    clock.tick(10)
