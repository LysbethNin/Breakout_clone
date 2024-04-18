import pgzero
import pgzrun
import pygame.transform

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
TITLE = "Breakout"
WIDTH = 800
HEIGHT = 500

background_img = pygame.image.load('images/purple_nebula.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

paddle = Actor('paddlered')
paddle.x = WIDTH / 2
paddle.y = HEIGHT - 50

ball = Actor('ballgrey')
ball.x = paddle.x
ball.y = paddle.y - paddle.height

brick_blue = Actor('element_blue_rectangle')
brick_blue.topleft = (brick_blue.width, brick_blue.height)

brick_green = Actor('element_green_rectangle')
brick_green.x = brick_blue.x
brick_green.y = brick_blue.y + brick_green.height


# TODO element_grey_rectangle
brick_grey = Actor('element_grey_rectangle')
brick_grey.x = brick_blue.x
brick_grey.y = brick_green.y + brick_grey.height
# TODO element_purple_rectangle
brick_purple = Actor('element_purple_rectangle')
brick_purple.x = brick_blue.x
brick_purple.y = brick_grey.y + brick_purple.height
# TODO element_red_rectangle
brick_red = Actor('element_red_rectangle')
brick_red.x = brick_blue.x
brick_red.y = brick_purple.y + brick_red.height
# TODO element_yellow_rectangle
brick_yellow = Actor('element_yellow_rectangle')
brick_yellow.x = brick_blue.x
brick_yellow.y = brick_red.y + brick_yellow.height

def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    paddle.draw()
    ball.draw()
    while brick_blue.x < (WIDTH - brick_blue.width):
        brick_blue.draw()
        brick_blue.x += brick_blue.width
    while brick_green.x < (WIDTH - brick_green.width):
        brick_green.draw()
        brick_green.x += brick_green.width
    while brick_grey.x < (WIDTH - brick_grey.width):
        brick_grey.draw()
        brick_grey.x += brick_grey.width
    while brick_purple.x < (WIDTH - brick_purple.width):
        brick_purple.draw()
        brick_purple.x += brick_purple.width
    while brick_red.x < (WIDTH - brick_red.width):
        brick_red.draw()
        brick_red.x += brick_red.width
    while brick_yellow.x < (WIDTH - brick_yellow.width):
        brick_yellow.draw()
        brick_yellow.x += brick_yellow.width


pgzrun.go()
