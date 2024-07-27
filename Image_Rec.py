import pyautogui as p
import time

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl
import Reader
import Helper_Funcs as HF

#UI Navigation -----------------------------------------------------------
def Universal_Backout(x1, y1, W, L) -> None:
    p.moveTo(x1 + W*rl.Universal_Menu_Backout_x,
             y1 + L*rl.Universal_Menu_Backout_y)
    p.click()
    time.sleep(1)

#Events----------------------------------------------------------------
def go_to_events(x1, y1, W, L) -> None:
    event_icon = r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot\images\images_Events\main_event_menu.JPG"

    where_am_I = HF.check_location(x1, y1, W, L)

    if where_am_I == "Neither":
        error_int = 0
        while where_am_I == "Neither" and error_int < 5:
            error_int += 1
            Universal_Backout()
            where_am_I = HF.check_location(x1, y1, W, L)
    
    event_loc = HF.check_image(event_icon, x1, y1, W, L,
                               10)
    
    p.moveTo(event_loc)
    p.click()

def event_swipe(x1, y1, W, L, dir) -> None:
    HF.swipe(x1, y1, W, L, dir, starter_y = rl.Event_Slider[1])
            


#UI Navigation -----------------------------------------------------------

    
#City Navigation --------------------------------------------------------
def City_Swiper_PRS():
    """Naviates the screen to the portion of the city that contains
    the storehouse, petcage and research building"""

    pass
    # for _ in range(15):
    #     swipe("up")

    # for _ in range(5):
    #     test.swipe("down")

    # for _ in range(7):
    #     test.swipe("left")

def Online_Reward_Finder(x1, y1, W, L):
    online_reward_icon = HF.check_image(x1, y1, W, L, 
                                     r"images/images_City/Online_Reward_Icon.JPG",
                                     10, 0.7, "Online Rewards")
    
    def temp_point_grabies(coord, distance, W, L):
        new_coord = (coord[0] + distance, coord[1] + distance)

        print(new_coord)

        rel_coord = HF.relativexy(x1, y1, W, L, new_coord)

        return(rel_coord)
    
    dist = 100

    x3 = temp_point_grabies(online_reward_icon, -1 *  dist, W, L)[0]
    y3 = temp_point_grabies(online_reward_icon, -1 *  dist, W, L)[1]

    x4 = temp_point_grabies(online_reward_icon, dist, W, L)[0]
    y4 = temp_point_grabies(online_reward_icon, dist , W, L)[1]

    screenshot_name = "Online_Rewards"

    p.click(online_reward_icon)
    time.sleep(1)
    p.click()
    time.sleep(1)

    HF.screenshotter(x1, y1, W, L,
                  x3, y3, x4, y4,
                  screenshot_name)
    #I may regret not adding absolute directories here...
    #screw it
    screenshot_path = "Screenshots\\" + screenshot_name + "_temp.JPG"

    wait_time_text = Reader.text_reader_cv2(screenshot_path, 1)

    wait_time = Reader.time_reader(wait_time_text)

    return(wait_time)
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

    Where_am_I = HF.check_location(x1, y1, W, L)
    if Where_am_I == "City":
        p.moveTo(x1 + W*rl.Main_Menu_Map_Swap_x, 
                y1 + L*rl.Main_Menu_Map_Swap_y)
        p.click()

        time.sleep(2)
    elif Where_am_I == "Neither":
        error_int = 0
        while Where_am_I == "Neither" and error_int <= 10:
            error_int += 1
            Universal_Backout()
            where_am_I = HF.check_location(x1, y1, W, L)
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
        view_loc = HF.check_image(x1, y1, W, L,
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

        victory = HF.check_victory(x1, y1, W, L)

        if victory == 1:

            p.click()

    def tent_journey():
        
        view_locater(x1, y1, W, L)

        time.sleep(2)

        p.moveTo(x1 + W * rl.WorldMap_Tent_x,
                 y1 + L * rl.WorldMap_Tent_y)
        p.click()

        def check_for_tent():
            time.sleep(1)
            i = 0
            while True and i <= 20:
                i += 1
                try:
                    p.locateOnScreen(r"images/images_worldmap/tent_journey.JPG",
                                    region = (x1, y1, W/0.5, L),
                                    confidence= 0.5)
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


    
    
