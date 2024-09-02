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

leg = Window_Finder.BlueStack_Window(Leg)

x1, y1, x2, y2 = leg.rectangle

W, L = leg.W_L

#play around with a beast hunt to figure out scheduling 
while beast_count < 27:

    error_int = 0

    leg.march_time = Map_Interact.Beast_Search(x1, y1, W, L, 21)

    schedule.add(leg.name, leg.hwnd, beast_hunt, leg.march_time, "s")

    #scan schedule for when beast returns
    while error_int < 5000:

        

        






