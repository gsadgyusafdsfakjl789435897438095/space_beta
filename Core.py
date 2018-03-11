# -*- coding: utf-8 -*-
import os.path
from game_scenario import Scenario
from icon import Infobar, Popup, Baggage
from main_menu import Main_menu 

class Core():
    def __init__(self):
        self.state = "start_main_menu"
        self.start_main_menu = Main_menu(["New_game", "Load", "Help", "Exit"])
        self.main_menu = Main_menu("Back to game", "New_game", "Save", "Load", "Help", "Exit")
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        
    def start_game(self):
        self.scenario_path = os.path.join(self.main_dir, 'scenarios')
        
    def handle_event(self, action):
        #there we handle keyboard events
        info = 'yoooo'
        list_to_draw = []
        if(self.state == "start_main_menu" or self.state == "main_menu"):
            info, list_to_draw = handle_main_menu(action)
        return info, list_to_draw
        
    def handle_main_menu(self, action):
        if(self.state == "start_main_menu"):
            info = self.start_main_menu.handle(action)
            list_to_draw = [self.start_main_menu]
            return info, list_to_draw
        if(self.state == "main_menu"):
            info = self.main_menu.handle(action)
            list_to_draw = [self.main_menu]
            return info, list_to_draw
            
    def move(self):
        pass
if __name__ == "__main__":
    print("i suck big dicks")

