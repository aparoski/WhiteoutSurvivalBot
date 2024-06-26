

#on startup
#find game screen
#load images


#Continuous

#master scheduler

#take screen shot image of game screen
#check screen for images


import win32gui as w

import time

import psutil

import pyautogui as p

time.sleep(5)

Blue_stacks = w.GetActiveWindow()

w.GetWindowText(Blue_stacks)

#print(w.GetWindowRect(Blue_stacks))

def enumHandler(hwnd, lParam):
    print(hwnd, w.GetWindowText(hwnd))

    

# print(Blue_stacks)

# print(str(w.GetWindowText(w.GetForegroundWindow())))

# print("test")