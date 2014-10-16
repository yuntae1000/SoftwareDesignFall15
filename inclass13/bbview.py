# -*- coding: utf-8 -*-
"""

"""
import pygame


class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        """ Draw the bricks and paddle on the screen"""
        self.screen.fill(pygame.Color(0, 0, 0))
        for brick in self.model.bricks:
            brick_color = pygame.Color(brick.color[0], brick.color[1],
                                       brick.color[2])
            brick_shape = pygame.Rect(brick.x, brick.y, brick.width,
                                      brick.height)
            pygame.draw.rect(self.screen, brick_color, brick_shape)
        paddle_color = pygame.Color(self.model.paddle.color[0],
                                    self.model.paddle.color[1],
                                    self.model.paddle.color[2])
        paddle_shape = pygame.Rect(self.model.paddle.x, self.model.paddle.y,
                                   self.model.paddle.width,
                                   self.model.paddle.height)
        pygame.draw.rect(self.screen, paddle_color, paddle_shape)
        pygame.display.update()
