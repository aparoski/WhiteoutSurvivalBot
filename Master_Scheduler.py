import pandas as pd
import numpy as np
import time


import Window_Finder
import Reader
import Image_Rec

#temp for testing
import pyautogui as p

#Initialize Blue Stacks Windows. 
RootieTootie = Window_Finder.BlueStack_Window(0)

print(RootieTootie.rectangle)

print(RootieTootie.W_L)

march_time = None
error_int = 0
while march_time != -100 and error_int < 5:
    error_int += 1
    RootieTootie.Open_Lighthouse()
    march_time = RootieTootie.Lighthouse_Operation()

    if march_time >= 0:
        
        print(str(march_time) + " seconds until march returns to city")

        time.sleep(march_time - 4)