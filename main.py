#pong
import pygame
from ball import Ball
from paddle import Paddle

pygame.init()

size = [320, 240]
screen = pygame.display.set_mode(size)

mouse_y = 0

ball = Ball([0,0], 5)
print(ball.radius, ball.position)

paddle1 = Paddle([0,0], 10, 4)

paddle2 = Paddle([0,0], 10, 4)


game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

        mouse_y = pygame.mouse.get_pos()[1]
        print(mouse_y)
