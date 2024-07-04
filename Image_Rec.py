

#on startup
#find game screen
#load images


#Continuous

#master scheduler

import win32gui as w

import time

import psutil

import pyautogui as p

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl

#Find the windows containing the game screen
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


#work within each Blue stack window / setup for testing right now
for i in window_list:
    print(i[2])
    print()
    print(i[1])
    print()
    print()


x1, y1, x2, y2 = window_list[0][1]

W, L = Window_lw(x1, y1, x2, y2)

p.moveTo(x1, y1)


#take screenshot of window
# first_shot = p.screenshot(region=[x1, y1, W, L])

# first_shot.save(r"Screenshots/test.png")

#navigate the lighthouse 
# check if game is at the world map screen

# Lx, Ly = p.locateCenterOnScreen(r"images/Main_UI/world_map.JPG",
#                                 region = (x1, x2, W, L),
#                                 confidence= 0.8)

# p.moveTo(Lx, Ly)

def check_location():
    """checks the UI to determine whether the game is in the world map,
    the City map, or neither.
    there has to be a better way than try/except..."""

    i = 0
    while True and i <= 10:
        i += 1
        if i % 2 == 0:

            try:
                img = p.locateOnScreen(r"images/Main_UI/City_door.JPG",
                                       region = (x1, x2, W, L),
                                       confidence= 0.7)
                return("World Map")
            except:
                pass
        else:
            try:
                img = p.locateOnScreen(r"images/Main_UI/world_map.JPG",
                                       region = (x1, x2, W, L),
                                       confidence= 0.7)
                return("City")
            except:
                pass
    if i >= 10:
        return("Neither")

check_lighthouse = 0

lighthouse_image_directory = r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot\images\images_Lighthouse"
#note - abspath connects using the current working directory so it may not get the correct path everytime
lighthouse_images = [os.path.abspath(i) for i in os.listdir(lighthouse_image_directory)]

for i in lighthouse_images:
    print(i)

#Lighthouse 
    #check if we are in the world map
if check_lighthouse == 1:
    Where_am_I = check_location()
    if Where_am_I == "City":
        p.moveTo(W*rl.Main_Menu_Map_Swap_x, 
                L*rl.Main_Menu_Map_Swap_y)
        p.click()
    elif Where_am_I == "Neither":
        error_int = 0
        while Where_am_I == "Neither" and error_int <= 10:
            error_int += 1
            p.moveTo(W*rl.Universal_Menu_Backout_x, 
                    L*rl.Universal_Menu_Backout_y)
            p.click()
            time.sleep(1)
            where_am_I = check_location()
        if Where_am_I == "City":
            p.moveTo(W*rl.Main_Menu_Map_Swap_x, 
                L*rl.Main_Menu_Map_Swap_y)
            p.click()

        #now that we are in world map navigate to the lighthouse menu
    p.moveTo(W*rl.WorldMap_Lighthouse_x, 
            L*rl.WorldMap_Beast_Attack_y)

    p.click()

    time.sleep(0.5)