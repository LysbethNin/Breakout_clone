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

brick_list = []

def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    paddle.draw()
    ball.draw()
    for brick in brick_list:
        brick.draw()

def create_brick(image, x, y):
    bar_x = x
    bar_y = y
    while bar_x < screen_limit:
        brick = Actor(image)
        brick.topleft = (bar_x, bar_y)
        bar_x += WIDTH_BRICK
        brick_list.append(brick)


def update():
    if keyboard.left and paddle.left > 0:
            paddle.x -= 4
    elif keyboard.right and paddle.right < WIDTH :
        paddle.x += 4

for img in brick_image_list:
    create_brick(img,x, y)
    y += HEIGHT_BRICK

pgzrun.go()
