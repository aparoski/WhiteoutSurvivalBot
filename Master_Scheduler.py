import pandas as pd
import numpy as np
import time


import Window_Finder
import Reader
import Image_Rec

#temp for testing
import pyautogui as p
import Helper_Funcs as HF

#Initialize Blue Stacks Windows. 
Tootie = "BlueStacks App Player"
Tootin = "BlueStacks App Player 1"
Tootily = "BlueStacks App Player 3"
Leg = "BlueStacks App Player 4"

lighthouse = True

if lighthouse:

    RootieTootie = Window_Finder.BlueStack_Window(Tootie)
for wind in [Tootily, Tootin, Tootie, Leg]:

    

    print("operating on " + wind)

    RootieTootie = Window_Finder.BlueStack_Window(wind)
    
    RootieTootie.window_to_foreground()

    print(RootieTootie.rectangle)

    print(RootieTootie.W_L)

    x1, y1, x2, y2 = RootieTootie.rectangle

    W, L  = RootieTootie.W_L

            time.sleep(march_time - 4)


#testing events and bouncing between windows
else:

    for my_window in [Tootie, Tootin, Tootily, Leg]:

        open_window = Window_Finder.BlueStack_Window(my_window)

        open_window.window_to_foreground()

        open_window.open_events()

        open_window.lucky_wheel_chip_grab()

        open_window.backout()
