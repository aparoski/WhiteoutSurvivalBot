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
    

#generalizing the check image oepration
#have it return object location center
def check_image(x1, y1, W, L, path, itterator, 
                confidence = 0.7, message = ""):
    i = 0
    while True and i <= itterator:
        i += 1
        try:
            image_loc = p.locateCenterOnScreen(path,
                                               region = (x1, y1, W, L),
                                               confidence= confidence)
            break
        except:
            print(message + "Check " + str)
            time.sleep(1)
            pass

    if i >= itterator:
        raise("Function to check " + message + " timed out")
    else:
        return(image_loc)
    
    
def check_victory(x1, y1, W, L):
    i = 0
    #20 seconds should be more than enough time for the battle to finish
    while True and i <= 20:
        i += 1
        try:
            victory = p.locateOnScreen(r"images/images_Events/misc/Victory_Screen.JPG",
                                    region = (x1, y1, W, L),
                                    confidence= 0.7)
            break
        except:
            time.sleep(1)
            pass

    if i >= 20:
        raise("Function to check Victory screen timed out")
    else:
        return(1)
    
def swipe(x1, y1, W, L, dir = "up") -> None:
    """direction refers to where the screen moves"""
    p.moveTo(x1 + W * 0.5,
                 y1 + L * 0.5)
    p.mouseDown(button = "left")
    if dir == "up":
        #place cursor in center of screen and swipe up
        p.moveTo(x1 + W * 0.5,
                 y1 + L,
                 duration = 0.2)
    elif dir == "down":
        p.moveTo(x1 + W * 0.5,
                 y1,
                 duration = 0.2)
    elif dir == "right":
        p.moveTo(x1,
                 y1 + L * 0.5,
                 duration = 0.2)
    elif dir =="left":
        p.moveTo(x1 + W,
                 y1 + L * 0.5,
                 duration = 0.2)
    time.sleep(0.1)
    p.mouseUp(button = "left")
    
#City Navigation --------------------------------------------------------


#March_UI
def Preset_March_Sender(x1, y1, W, L, Preset):
    if Preset == 1:
        p.moveTo(x1 + W*rl.March_Squad_1_x,
                 y1 + L*rl.March_Squad_1_y)
        p.click()
        time.sleep(0.5)
        p.moveTo(x1 + W*rl.March_Deploy_x,
                 y1 + W*rl.March_Deploy_y)
        
        print()

        #this stupid function will only take ints for its region
        x1_temp = round(x1 + W * rl.March_time_x1)
        y1_temp = round(y1 + L * rl.March_time_y1)
        x2_temp = round(x1 + W * rl.March_time_x2)
        y2_temp = round(y1 + L * rl.March_time_y2)
        W_temp = x2_temp - x1_temp
        L_temp = y2_temp - y1_temp

        print(W_temp, L_temp)

        p.screenshot("Screenshots\\March_time_temp.JPG", 
                     region = (x1_temp, y1_temp,
                               W_temp, L_temp))
        
        my_march_time = Reader.text_reader_cv2("Screenshots\\March_time_temp.JPG", 1)

        my_march_time_seconds = Reader.time_reader(my_march_time)

        #finally select the march sender and return the march time

        p.moveTo(x1 + W * rl.March_Deploy_x,
                 y1 + L * rl.March_Deploy_y)
        
        p.click()

        return(my_march_time_seconds)



#Lighthouse functions ---------------------------------------------------------------
def Lighthouse_confirm_and_Open(x1, y1, W, L):

    Where_am_I = check_location(x1, y1, W, L)
    if Where_am_I == "City":
        p.moveTo(x1 + W*rl.Main_Menu_Map_Swap_x, 
                y1 + L*rl.Main_Menu_Map_Swap_y)
        p.click()

        time.sleep(2)
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
            time.sleep(2)
        
        if error_int >= 10:
            raise("Error in exiting using universal backout")

        #now that we are in world map navigate to the lighthouse menu
    p.moveTo(x1 + W*rl.WorldMap_Lighthouse_x, 
            y1 + L*rl.WorldMap_Lighthouse_y)
    
    #may need to adjust sleep time as time to load worldmap can vary
    p.click()

def lighthouse_icon_typer(x1, y1, W, L, path):
    
    def view_locater(x1, y1, W, L) -> None:
        view_loc = check_image(x1, y1, W, L,
                               "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\Main_UI\\View_Button.JPG",
                               5, 0.7, "View Button")
        p.moveTo(view_loc)
        p.click()
    
    def light_house_beast_attack():
        
        view_locater(x1, y1, W, L)

        #give time for app to transition to the worldmap
        time.sleep(2)
        p.moveTo(x1 + W*rl.WorldMap_Beast_Attack_x,
                 y1 + L*rl.WorldMap_Beast_Attack_y)
        p.click()
        time.sleep(0.5)

    def sword_battle():

        view_locater(x1, y1, W, L)

        time.sleep(2)

        p.moveTo(x1 + W * rl.WorldMap_Sword_Battle_x,
                 y1 + L * rl.WorldMap_Sword_Battle_y)
        p.click()

        print("Clicked world map battle")

        time.sleep(1)

        p.moveTo(x1 + W * rl.Sword_Fight_x,
                 y1 + L * rl.Sword_Fight_y)
        p.click()

        time.sleep(2)

        victory = check_victory(x1, y1, W, L)

        if victory == 1:

            p.click()

    def tent_journey():
        
        view_locater(x1, y1, W, L)

        time.sleep(2)

        p.moveTo(x1 + W * rl.WorldMap_Tent_x,
                 y1 + L * rl.WorldMap_Tent_y)
        p.click()

        def check_for_tent():
            i = 0
            while True and i <= 20:
                i += 1
                try:
                    p.locateOnScreen(r"images/images_worldmap/tent_journey.JPG",
                                    region = (x1, y1, W/0.5, L),
                                    confidence= 0.7)
                    print("Tent icon succesfully located {} times".format(str(i)))
                    time.sleep(0.5)
                except:
                    return(2)
            if i >= 20:
                raise("Function to check for Tent timed out")

        #once check for tent finishes runnining, the next operation is to open
        #lighthouse interface and select the checked tent icon    
        check_for_tent()


  
    if "paw" in path: 
        light_house_beast_attack()
        return(1)
    elif "skull" in path:
        light_house_beast_attack()
        return(1)
    elif "swords" in path:
        sword_battle()
        return(2)
    elif "tent" in path:
        tent_journey()
        return(3)
    elif "Fire_Beast" in path:
        light_house_beast_attack()
        return(1)

def light_house_icon_Navigator(x1, y1, W, L):
    """Navigate entire lighthouse operation. 
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
    else:
        p.moveTo(img)
        time.sleep(0.5)
        p.click()
        time.sleep(0.5)


        #assumption here is that the last lighthouse variable passed in the for loop
        #is the one associated with the image that was found
        lighthouse_icon = lighthouse_icon_typer(x1, y1, W, L, lighthouse)

        #assumption here is that the 1st preset is optimized
        #for beast marches
        #add catches for if this march has already been sent out
        if lighthouse_icon == 1:
            march_time = Preset_March_Sender(x1, y1, W, L, 1)
        elif lighthouse_icon == 2:
            march_time = -1
        else:
            march_time = -1


        #following section added at last minute because
        #I forgot to also add code to go back to lighthouse
        #and collect from the previous image position...
        Lighthouse_confirm_and_Open(x1, y1, W, L)

        time.sleep(march_time + 2)
        p.moveTo(img)
        p.click()

        p.moveTo(x1 + W * rl.Universal_Menu_Backout_x,
                 y1 + L * rl.Universal_Menu_Backout_y)
        time.sleep(0.5)
        p.click()
        time.sleep(2)
        p.click()
        #-------------------------------------------

        return(march_time)
#Lighthouse functions ---------------------------------------------------------------

#Pet Functions-------------------------------------------------------------------



if __name__ == '__main__':
    pass


    
    
