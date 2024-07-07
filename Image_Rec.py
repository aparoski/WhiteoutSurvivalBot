

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
                                       region = (x1, y1, W, L),
                                       confidence= 0.7)
                return("World Map")
            except:
                pass
        else:
            try:
                img = p.locateOnScreen(r"images/Main_UI/world_map.JPG",
                                       region = (x1, y1, W, L),
                                       confidence= 0.7)
                return("City")
            except:
                pass
    if i >= 10:
        return("Neither")


check_lighthouse = 0

lighthouse_image_directory = r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot\images\images_Lighthouse"
#note - abspath connects using the current working directory so it may not get the correct path everytime
lighthouse_images = [lighthouse_image_directory + "\\" + i for i in os.listdir(lighthouse_image_directory)]

#Lighthouse 
    #check if we are in the world map
if check_lighthouse == 1:
    Where_am_I = check_location()
    if Where_am_I == "City":
        p.moveTo(x1 + W*rl.Main_Menu_Map_Swap_x, 
                y1 + L*rl.Main_Menu_Map_Swap_y)
        p.click()
    elif Where_am_I == "Neither":
        error_int = 0
        while Where_am_I == "Neither" and error_int <= 10:
            error_int += 1
            p.moveTo(x1 + W*rl.Universal_Menu_Backout_x, 
                    y1 + L*rl.Universal_Menu_Backout_y)
            p.click()
            time.sleep(1)
            where_am_I = check_location()
        if Where_am_I == "City":
            p.moveTo(x1 + W*rl.Main_Menu_Map_Swap_x, 
                y1 + L*rl.Main_Menu_Map_Swap_y)
            p.click()

        #now that we are in world map navigate to the lighthouse menu
    p.moveTo(x1 + W*rl.WorldMap_Lighthouse_x, 
            y1 + L*rl.WorldMap_Lighthouse_y)

    p.click()

    time.sleep(0.5)

def light_house_icon_finder(x1, y1, W, L):
    """Return the coordinates of a lighthouse icon
    must be within the lighthosue interface to work
    properly"""

    img = None
    for i, lighthouse in enumerate(lighthouse_images):
        print(lighthouse)
        try:
            img = p.locateCenterOnScreen(lighthouse,
                                            region = (x1, y1, W, L),
                                            confidence= 0.7)
            break
        except:
            pass
    if img == None:
        return(-100)
    
    else:

        return(img)

    
    
