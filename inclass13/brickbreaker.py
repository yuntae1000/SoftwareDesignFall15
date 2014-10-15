# -*- coding: utf-8 -*-
"""
This codeshare is being used by SoftDes Fall 2014 to work on a brickbreaker example

Created on Tue Oct 14 2014

@author: Amon Millner, building upon Paul Ruvolo’s Spring 2014 SoftDes example
"""

import pygame
from pygame.locals import *
import random
import math
import time
import bbmodel
import bbview
import bbcontroller

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = bbmodel.BrickBreakerModel()
    view = bbview.PyGameWindowView(model,screen)
    #controller = bbcontroller.PyGameMouseController(model)
    controller = bbcontroller.PyGameKeyboardController(model)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            #if event.type == MOUSEMOTION:
                #controller.handle_mouse_event(event)
            if event.type == KEYDOWN:
                controller.handle_key_event(event)
        view.draw()
        time.sleep(.001)

    pygame.quit()
