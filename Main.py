

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

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

def Window_lw(x1, y1, x2, y2):
    """finds the length and width of a rectangular
    box between two coordinates if the coordinates are
    located at the top left and bottom right corners of the rectangle"""

    l = y2 - y1
    w = x2 - x1

    return(w, l)



def enumHandler(hwnd, list):
    if "BlueStacks App Player 1" in w.GetWindowText(hwnd):

        print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "second")
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
    elif "BlueStacks App Player 3" in w.GetWindowText(hwnd):

        print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "third")
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
    elif "BlueStacks App Player 4" in w.GetWindowText(hwnd):

        print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "fourth")
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
    elif "BlueStacks App Player" in w.GetWindowText(hwnd):

        print(hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), "main")
        list.append([w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])


window_list = []

w.EnumWindows(enumHandler, window_list)

for i in window_list:
    print(i[2])
    print()
    print(i[1])
    print()
    print()


x1, y1, x2, y2 = window_list[0][1]

W, L = Window_lw(x1, y1, x2, y2)

p.moveTo(x1, y1)


#note, to take screenshot the window must be in the foreground
first_shot = p.screenshot(region=[x1, y1, W, L])

def relative_coordinates(l, w)

x_lighthouse, y_lighthouse = x1 + 494, y1 + 677

print(x_l - x1, y_l - y1)

p.moveTo(x_lighthouse, y_lighthouse)

first_shot.save(r"Screenshots/test.png")