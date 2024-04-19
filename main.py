import random

import pgzero
import pgzrun
import pygame.transform

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
TITLE = "Breakout"
WIDTH = 800
HEIGHT = 500
# Brick Size
brick_img = pygame.image.load('images/element_blue_rectangle.png')
WIDTH_BRICK = brick_img.get_width()
HEIGHT_BRICK= brick_img.get_height()
screen_limit = WIDTH - WIDTH_BRICK

#
x = WIDTH_BRICK
y = HEIGHT_BRICK
brick_image_list = ['element_blue_rectangle', 'element_green_rectangle', 'element_grey_rectangle', 'element_purple_rectangle', 'element_red_rectangle', 'element_yellow_rectangle']

########## Text #################
# Définition de la couleur et de la police du texte
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36
FONT_NAME = "arial"

# Variable pour stocker l'état du texte (visible ou non)
text_visible = True
# End Game
game_over = False
game_win = False

# Background
background_img = pygame.image.load('images/purple_nebula.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
# Paddle
paddle = Actor('paddlered')
paddle.x = WIDTH / 2
paddle.y = HEIGHT - 50
# Ball
ball = Actor('ballgrey')
ball.x = paddle.x
ball.y = paddle.y - paddle.height

# Ball direction
direction = random.randint(0,1)
if direction == 0:
    ball_x_direction = 2
    ball_y_direction = 2
else:
    ball_x_direction = -2
    ball_y_direction = 2

brick_list = []

def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))

    paddle.draw()
    ball.draw()
    for brick in brick_list:
        brick.draw()

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")
    if game_win:
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")

def create_brick(image, x, y):
    bar_x = x
    bar_y = y
    while bar_x < screen_limit:
        brick = Actor(image)
        brick.topleft = (bar_x, bar_y)
        bar_x += WIDTH_BRICK
        brick_list.append(brick)


def moving_paddle():
    if keyboard.left and paddle.left > 0:
        paddle.x -= 4
    elif keyboard.right and paddle.right < WIDTH :
        paddle.x += 4
def moving_ball():
    global ball_x_direction, ball_y_direction
    ball.x -= ball_x_direction
    ball.y -= ball_y_direction
    if (ball.x <= 0) or (ball.x >= WIDTH) :
        ball_x_direction *= -1
    if ball.y <= 0:
        ball_y_direction *= -1


def update():
    global ball_x_direction, ball_y_direction, game_win, game_over
    moving_paddle()
    moving_ball()
    for brick in brick_list:
        if ball.colliderect(brick):
            brick_list.remove(brick)
            ball_x_direction *= -1
    if not brick_list:
        game_win = True

    if ball.colliderect(paddle):
        direction = random.randint(0,1)
        if direction:
            ball_y_direction *= -1
    if ball.y >= HEIGHT:
        game_over = True

for img in brick_image_list:
    create_brick(img,x, y)
    y += HEIGHT_BRICK

pgzrun.go()
