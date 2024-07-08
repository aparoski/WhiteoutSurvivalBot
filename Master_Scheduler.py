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

time.sleep(5)

RootieTootie.Open_Lighthouse()

time.sleep(5)

RootieTootie.Lighthouse_Operation()