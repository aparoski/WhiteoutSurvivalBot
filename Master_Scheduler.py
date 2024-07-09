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

RootieTootie.Open_Lighthouse()

march_time = RootieTootie.Lighthouse_Operation()

print(str(march_time * 2) + " seconds until march returns to city")

#time.sleep(march_time * 2)