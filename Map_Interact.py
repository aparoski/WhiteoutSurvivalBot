import pyautogui as p
import time

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl
import Reader
import Helper_Funcs as HF
import Image_Rec

def map_search(x1, y1, W, L) -> None:
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

def rally_attack_button_findnpress(x1, y1, W, L, type = "Rally") -> None:

    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"

    rally_file = "images_worldmap\\Terror_Rally_Button.JPG"

    hold_a_rally_file = "images_worldmap\\hold_a_Rally.JPG"

    attack_file = "images_worldmap\\Beast_Attack_Button.JPG"

    if type == "Rally":

        button_loc = HF.check_image(x1, y1, W, L,
                                    dir + rally_file,
                                    message = " rally button ")
        
        p.moveTo(button_loc)

        p.click()

        time.sleep(1)

        hold_a_rally_button_loc = HF.check_image(x1, y1, W, L,
                                                dir + hold_a_rally_file,
                                                message = " hold a rally button ")

        p.moveTo(hold_a_rally_button_loc)

        p.click()

    else:
        
        button_loc = HF.check_image(x1, y1, W, L,
                                    dir + attack_file,
                                    message = " attack button ")
        
        p.moveTo(button_loc)

        p.click()


def check_rally_arrival(x1, y1, W, L):

    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"

    my_rally = "images_worldmap\\my_Rally.JPG"

    try:

        loc = HF.check_image(x1, y1, W, L, dir + my_rally, itterator = 2,
                            message = " checking if rally Icon is present ")

        return("False")

    except:

        return("True")
    

def polar_sender(x1, y1, W, L, level):

    """sends out march to a polar rally"""
    
    map_search(x1, y1, W, L)

    #swipe function uses 0.5 as base so it must be subtracted from any value
    #that is above 0.5...yes its ugly I know
    HF.swipe(x1, y1, W, L, "left", 
             starting_y = rl.WorldMap_Search_Slider[1])
    
    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"
    
    terror_file = "images_worldmap\\search_polar_terror.JPG"

    #delay is necessary before searching for image
    #after swipe slider bounces moving the icon about
    time.sleep(0.5)

    teror_loc = HF.check_image(x1, y1, W, L, 
                               dir + terror_file,
                               message = " Polar Terror ")
    
    p.click(teror_loc)

    map_search_level_selection(x1, y1, W, L, level)

    time.sleep(1)

    rally_attack_button_findnpress(x1, y1, W, L, "Rally")

    walk_time = Image_Rec.Preset_March_Sender(x1, y1, W, L, 1)

    return(walk_time)

def Reaper_Sender(x1, y1, W, L):
    Image_Rec.Hero_Mission(x1, y1, W, L)

    rally_attack_button_findnpress(x1, y1, W, L, " Reaper ")

    walk_time = Image_Rec.Preset_March_Sender(x1, y1, W, L, 1)

    return(walk_time)

# def Polar_Depature_check(x1, y1, W, L, windows):
    
#     """determines when a polar rally has departed the city"""

#     time.sleep(60)

#     error_int = 0

#     rally_ready = check_rally_arrival(x1, y1, W, L)

#     while rally_ready == "False" and error_int < 2000:

#         if error_int % 10 == 0:
#             print("rally wait " + str(error_int))
#             time.sleep(5)

#         error_int += 1

#         rally_ready = check_rally_arrival(x1, y1, W, L)

    




    
    

#rally functions----------------------------------------------
#Beast Functions ---------------------------------------------
def Beast_Search(x1, y1, W, L, level):
    map_search(x1, y1, W, L)

    #swipe function uses 0.5 as base so it must be subtracted from any value
    #that is above 0.5...yes its ugly I know
    
    HF.swipe(x1, y1, W, L, "left",starting_y = rl.WorldMap_Search_Slider[1])
    
    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"
    
    Beast_file = "images_worldmap\\search_beast.JPG"

    #delay is necessary before searching for image
    #after swipe slider bounces moving the icon about
    time.sleep(0.5)

    beast_loc = HF.check_image(x1, y1, W, L, 
                               dir + Beast_file,
                               message = " Beast ")
    
    p.click(beast_loc)

    map_search_level_selection(x1, y1, W, L, level)

    time.sleep(1)

    rally_attack_button_findnpress(x1, y1, W, L, "Attack")

    walk_time = Image_Rec.Preset_March_Sender(x1, y1, W, L, 1)

    return(walk_time)
#Beast Functions ---------------------------------------------