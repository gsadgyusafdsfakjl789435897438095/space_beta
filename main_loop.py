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
            if (event.type == pg.QUIT):
                return 0
        type = pg.event.event_name(event.type)
        if(type == "KeyDown"):
            #print(event.unicode, event.key, event.mod)
            if(event.key == 13):
                action = "Enter"
            if(event.key == 32):
                action = "Space"
            if(event.key == 273):
                action = "UpArrow"
            if(event.key == 276):
                action = "LeftArrow"
            if(event.key == 274):
                action = "DownArrow"
            if(event.key == 275):
                action = "RightArrow"
            if(event.key == 27):
                action = "Esc"
            if(event.key == 304):
                action = "LShift"
            if(event.key == 306):
                action = "LCtrl"    
        # send this state to the core
        info, list_to_draw = core_.handle_event(action)
        # sometimes core wants to quit game, we will handle it
        if("Exit" in info):
            done = True
        # draw all things that core wants
        dep.draw(info, list_to_draw)
        #cap the framerate
        clock.tick(40)

if __name__ == "__main__":
    init()
    main_loop()
    pg.quit()
