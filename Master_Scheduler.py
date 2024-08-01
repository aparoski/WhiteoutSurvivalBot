import pandas as pd
import numpy as np
import time


import Window_Finder
import Reader
import Image_Rec

#temp for testing
import pyautogui as p

#Initialize Blue Stacks Windows. 
Tootie = "BlueStacks App Player"
Tootin = "BlueStacks App Player 1"
Tootily = "BlueStacks App Player 3"
Leg = "BlueStacks App Player 4"

lighthouse = False

if lighthouse:

    RootieTootie = Window_Finder.BlueStack_Window(Tootin)

    print(RootieTootie.rectangle)

    print(RootieTootie.W_L)

    march_time = None
    #error int for testing
    error_int = 0
    while march_time != -100 and error_int < 15:
        error_int += 1
        RootieTootie.Open_Lighthouse()
        march_time = RootieTootie.Lighthouse_Operation()

        if march_time >= 0:
            
            print(str(march_time) + " seconds until march returns to city")

            time.sleep(march_time - 4)


#testing events and bouncing between windows
else:

    for my_window in [Tootie, Tootin, Tootily, Leg]:

        open_window = Window_Finder.BlueStack_Window(my_window)

        open_window.window_to_foreground()

        open_window.open_events()

        open_window.lucky_wheel_chip_grab()

        open_window.backout()