import pandas as pd
import numpy as np
import time


import Window_Finder
import Reader
import Image_Rec
import Data
import Map_Interact

#temp for testing
import pyautogui as p
import Helper_Funcs as HF

#Initialize Blue Stacks Windows. 
Tootie = "BlueStacks App Player"
Tootin = "BlueStacks App Player 1"
Tootily = "BlueStacks App Player 3"
Leg = "BlueStacks App Player 4"

schedule = Data.Window_Dataframe()

polar_rally = "Polar_Rally"
beast_hunt = "Beast_Hunt"
Troop_Training = "Troop_Training" + "Troop_Type"

beast_count = 0

App = Window_Finder.BlueStack_Window(Tootie)
App1 = Window_Finder.BlueStack_Window(Tootin)
App3 = Window_Finder.BlueStack_Window(Tootily)
App4 = Window_Finder.BlueStack_Window(Leg)

Windows_in_view = [App, App1, App3]

#develop account config in the future which will contain these values
account_polar_level_dict = {Tootie : 6, Tootin : 4, Tootily : 3, Leg : 3}

#beginning of schedule we will need to instantiate the schedule
schedule = Data.Window_Dataframe()

#polar Rally
#start with first function to iterate over each viewable window and send a rally march out
def send_polars(x1, y1, W, L, accounts):
    """iterates over Bluestack windows. sends a polar rally for each and
    assigns march time to teach window"""
    for app in accounts:
        
        x1, y1, x2, y2 = app.rectangle

        W, L = app.W_L

        app.march_time = Map_Interact.polar_sender(x1, y1, W, L, account_polar_level_dict[app.name])

        

#second function scans each window to determine when the rally has departed
#then adds the march time to the schedule
def check_all_rallies(x1, y1, W, L, accounts):
    for app in accounts:
        
        x1, y1, W, L = app.rectangle

        W, L = app.W_L




#third function scans schedule for latest event and triggers first function

        






