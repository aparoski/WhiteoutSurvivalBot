import pyautogui as p
import time

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl
import Reader
import Helper_Funcs as HF
import Image_Rec

def map_search(x1, y1, L, W) -> None:
    """pull up the search pane in the world map"""
    Image_Rec.Navigate_to_cityormap(x1, y1, W, L, "World Map")

    p.moveTo(x1 + W * rl.WorldMap_Search[0],
             y1 + L * rl.WorldMap_Search[1])
    p.click()

    time.sleep(2)

def map_search_level_selection(x1, y1, W, L, level) -> None:
    """from within the search pane of world map. After the
    desired category has been selected. picks out the desired level
    for that category and starts search"""

    p.moveTo(x1 + W * rl.WorldMap_Search_Level_Selection[0],
             y1 + L * rl.WorldMap_Search_Level_Selection[1])
    
    p.click()

    time.sleep(1)

    p.hotkey('ctrl', 'a')

    p.press('backspace')

    time.sleep(0.5)

    p.write(str(level))

    p.press("enter")

    time.sleep(0.5)

    p.moveTo(x1 + W * rl.WorldMap_Search_Button[0],
             y1 + L * rl.WorldMap_Search_Button[1])
    
    p.click()

    time.sleep(2)

#rally functions----------------------------------------------

def polar_sender(x1, y1, L, W, level):
    
    map_search(x1, y1, L, W)

    HF.swipe(x1, y1, W, L, "left", 
             starting_y = rl.WorldMap_Search_Slider[1])
    
    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"
    
    terror_file = "images_worldmap\\search_polar_terror.JPG"

    teror_loc = HF.check_image(x1, y1, W, L, 
                               dir + terror_file,
                               message = " Polar Terror ")
    
    p.click(teror_loc)

    map_search_level_selection(x1, y1, W, L, level)

    
    
    

#rally functions----------------------------------------------