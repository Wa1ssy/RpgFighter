import random
import time

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

def show_title():
    print(r"""
  _____   _____    _____       ______  _____  _____  _    _  _______  ______  _____  
 |  __ \ |  __ \  / ____|     |  ____||_   _|/ ____|| |  | ||__   __||  ____||  __ \ 
 | |__) || |__) || |  __      | |__     | | | |  __ | |__| |   | |   | |__   | |__) |
 |  _  / |  ___/ | | |_ |     |  __|    | | | | |_ ||  __  |   | |   |  __|  |  _  / 
 | | \ \ | |     | |__| |     | |      _| |_| |__| || |  | |   | |   | |____ | | \ \ 
 |_|  \_\|_|      \_____|     |_|     |_____|\_____||_|  |_|   |_|   |______||_|  \_\
                                                                                     
                                                                                          
    """)

class Character:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.level = 1
        self.xp = 0
        self.defeated = 0
        self.inventory = ["Potion", "Mana Potion"]