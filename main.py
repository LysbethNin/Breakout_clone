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

brick_image_list = ['element_blue_rectangle', 'element_green_rectangle', 'element_grey_rectangle', 'element_purple_rectangle', 'element_red_rectangle', 'element_yellow_rectangle']
brick_list = []


def create_brick(image, x, y):
    brick = Actor(image)
    brick.topleft = (x, y)
    return brick

y = HEIGHT_BRICK
for img in brick_image_list:
    brick = create_brick(img, WIDTH_BRICK, y)
    brick_list.append(brick)
    y += HEIGHT_BRICK


def place_row_bricks(brick):
    screen_limit = WIDTH - WIDTH_BRICK
    while brick.x < WIDTH - WIDTH_BRICK:
        brick.draw()
        brick.x += WIDTH_BRICK


def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    paddle.draw()
    ball.draw()
    for brick in brick_list:
        place_row_bricks(brick)


pgzrun.go()
