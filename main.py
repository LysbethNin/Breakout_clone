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


def draw():
    screen.clear()
    screen.blit(background_img, (0,0))
    paddle.draw()
    ball.draw()


pgzrun.go()
