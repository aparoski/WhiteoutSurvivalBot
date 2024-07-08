import pyautogui as p
import time

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl
import Reader

def check_location(x1, y1, W, L):
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

#March_UI
def Preset_March_Sender(x1, y1, W, L, Preset):
    if Preset == 1:
        p.moveTo(x1 + W*rl.March_Squad_1_x,
                 y1 + L*rl.March_Squad_1_y)
        p.click()
        time.sleep(0.5)
        p.moveTo(x1 + W*rl.March_Deploy_x,
                 y1 + W*rl.March_Deploy_y)
        
        p.screenshot("Screenshots\\March_time_temp.JPG", 
                     region = (x1 + W * rl.March_time_x1,
                               y1 + L * rl.March_time_y1,
                               x1 + W * rl.March_time_x1,
                               y1 + W * rl.March_time_y1))
        
        my_march_time = Reader.text_reader_cv2("Screenshots\\March_time_temp.JPG", 1)

        my_march_time_seconds = Reader.time_reader(my_march_time)

        return(my_march_time_seconds)



#Lighthouse functions
def Lighthouse_confirm_and_Open(x1, y1, W, L):

    Where_am_I = check_location(x1, y1, W, L)
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
            where_am_I = check_location(x1, y1, W, L)
        if Where_am_I == "City":
            p.moveTo(x1 + W*rl.Main_Menu_Map_Swap_x, 
                y1 + L*rl.Main_Menu_Map_Swap_y)
            p.click()

        #now that we are in world map navigate to the lighthouse menu
    p.moveTo(x1 + W*rl.WorldMap_Lighthouse_x, 
            y1 + L*rl.WorldMap_Lighthouse_y)
    
    #may need to adjust sleep time as time to load worldmap can vary
    time.sleep(2)

    p.click()

def lighthouse_icon_typer(x1, y1, W, L, path):
    def light_house_beast_attack():
        p.moveTo(x1 + W * rl.Lighthouse_BeastHunt_View_x,
                 y1 + L * rl.Lighthouse_BeastHunt_View_y)
        p.click()
        #give time for app to transition to the worldmap
        time.sleep(2)
        p.moveTo(x1 + W*rl.WorldMap_Beast_Attack_x,
                 y1 + L*rl.WorldMap_Beast_Attack_y)
        p.click()
        time.sleep(0.5)

        

    if "paw" in path: 
        light_house_beast_attack()
    elif "skull" in path:
        light_house_beast_attack()
    elif "swords" in path:
        return(2)
    elif "tent" in path:
        return(3)
    elif "Fire_Beast" in path:
        light_house_beast_attack()

def light_house_icon_Navigator(x1, y1, W, L):
    """Naviagte entire lighthouse operation. 
    Return time required for operation if relevant"""

    lighthouse_image_directory = r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot\images\images_Lighthouse"
    lighthouse_images = [lighthouse_image_directory + "\\" + i for i in os.listdir(lighthouse_image_directory)]

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
        #introduce an exit function here
    else:
        p.moveTo(img)
        time.sleep(0.5)
        p.click()
        time.sleep(0.5)

        #assumption here is that the last lighthouse variable passed in the for loop
        #is the one associated with the image that was found
        lighthouse_icon_typer(x1, y1, W, L, lighthouse)

        #assumption here is that the 1st preset is optimized
        #for beast marches
        #add catches for if this march has already been sent out
        march_time = Preset_March_Sender(x1, y1, W, L, 1)

        return(march_time)





    
    
