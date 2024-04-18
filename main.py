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
print(WIDTH_BRICK)
print(HEIGHT_BRICK)
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
# Blue brick
brick_blue = Actor('element_blue_rectangle')
brick_blue.topleft = (WIDTH_BRICK, HEIGHT_BRICK)
# Green Brick
brick_green = Actor('element_green_rectangle')
brick_green.x = brick_blue.x
brick_green.y = brick_blue.y + HEIGHT_BRICK
# Grey Brick
brick_grey = Actor('element_grey_rectangle')
brick_grey.x = brick_blue.x
brick_grey.y = brick_green.y + HEIGHT_BRICK
# Purple brick
brick_purple = Actor('element_purple_rectangle')
brick_purple.x = brick_blue.x
brick_purple.y = brick_grey.y + HEIGHT_BRICK
# Red Brick
brick_red = Actor('element_red_rectangle')
brick_red.x = brick_blue.x
brick_red.y = brick_purple.y + HEIGHT_BRICK
# Yellow brick
brick_yellow = Actor('element_yellow_rectangle')
brick_yellow.x = brick_blue.x
brick_yellow.y = brick_red.y + HEIGHT_BRICK



def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    paddle.draw()
    ball.draw()
    while brick_blue.x < (WIDTH - WIDTH_BRICK):
        brick_blue.draw()
        brick_blue.x += WIDTH_BRICK
    while brick_green.x < (WIDTH - WIDTH_BRICK):
        brick_green.draw()
        brick_green.x += WIDTH_BRICK
    while brick_grey.x < (WIDTH - WIDTH_BRICK):
        brick_grey.draw()
        brick_grey.x += WIDTH_BRICK
    while brick_purple.x < (WIDTH - WIDTH_BRICK):
        brick_purple.draw()
        brick_purple.x += WIDTH_BRICK
    while brick_red.x < (WIDTH - WIDTH_BRICK):
        brick_red.draw()
        brick_red.x += WIDTH_BRICK
    while brick_yellow.x < (WIDTH - WIDTH_BRICK):
        brick_yellow.draw()
        brick_yellow.x += WIDTH_BRICK


pgzrun.go()
