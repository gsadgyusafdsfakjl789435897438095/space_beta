# -*- coding: utf-8 -*-
# author: crutch lord

# this is main loop of game

import pygame as pg
from core import Core
from depictor import Depictor



def init():
    # all things those must be done only once before start pygame drawing
    # mb ask about screen resolution or smth
    pass

def main_loop():
    pg.init()
    clock = pg.time.Clock()
    done = False
    # create example of game core
    core_ = Core()
    # create example of game renderer
    dep = Depictor()
    # there starts main loop
    while not done:
        # handle keyboard events
        for event in pg.event.get():
            if (event.type == QUIT):
                return 0
        keystate = pg.key.get_pressed()
        # send this state to the core
        info, list_to_draw = core_.handle_event(keystate)
        # sometimes core wants to quit game, we will handle it
        if("exit" in info):
            done = True
        # draw all things that core wants
        dep.draw(info, list_to_draw)
        #cap the framerate
        clock.tick(40)

if __name__ == "__main__":
    init()
    main_loop()
    pg.quit()