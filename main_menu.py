# -*- coding: utf-8 -*-
# author: crutch lord

class Main_menu():
    def __init__(self, items_):
        self.items = items_
        #kind of items_ = ["New_game", "Back to game", "Save", "Load", "Help", "Exit"]
        self.selected = 0
    def handle(self, action):
        if(action == "Enter"):
            return(self.items[self.selected])
        if(action == "UpArrow"):
            if(self.selected != 0):
                self.selected = self.selected - 1
                return("No")
        if(action == "DownArrow"):
            if(self.selected != len(self.items)):
                self.selected = self.selected + 1
                return("No")    
    def load_page(self):
        pass
    def save_page(self):
        pass
    def help_page(self):
        pass
    
