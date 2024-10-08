import pyautogui as p
import time

p.useImageNotFoundException()

import os 
os.chdir(r"A:\Data_Science\Projects\Whiteout_Survival\WoS Bot")

import relative_locations as rl
import Reader
import Helper_Funcs as HF
import Map_Interact

#UI Navigation -----------------------------------------------------------
def Universal_Backout(x1, y1, W, L) -> None:
    p.moveTo(x1 + W*rl.Universal_Menu_Backout_x,
             y1 + L*rl.Universal_Menu_Backout_y)
    p.click()
    time.sleep(1)

def Navigate_to_cityormap(x1, y1, W, L, location = "City",
                         iterator = 10) -> None:
    
    """function navigates through the UI to the selected location:
    either the city or map views"""

    print("Attempting to navigate to " + location)

    def switch_view() -> None:
        p.moveTo(x1 + W * rl.Main_Menu_Map_Swap_x,
                 y1 + L * rl.Main_Menu_Map_Swap_y)
        p.click()
        time.sleep(2)

    where_am_I = HF.check_location(x1, y1, W, L)

    if where_am_I == "Neither":
        print("Neither map or city viewed. attempting to back out")
        error_int = 0
        while where_am_I == "Neither" and error_int <= iterator:
            error_int += 1
            p.moveTo(x1 + W*rl.Universal_Menu_Backout_x, 
                    y1 + L*rl.Universal_Menu_Backout_y)
            p.click()
            time.sleep(1)
            print("Backout Navigation attempt number " + error_int)
            where_am_I = HF.check_location(x1, y1, W, L)

    else:
        error_int = 0
        if where_am_I == "City" and location == "City":
            pass
        elif where_am_I == "World Map" and location == "City":
            switch_view()
            move_check = HF.check_location(x1, y1, W, L)
            while move_check != "City" and error_int < 10:
                error_int += 1
                move_check = HF.check_location(x1, y1, W, L)
                time.sleep(0.5)
        elif where_am_I == "city" and location == "World Map":
            switch_view()
            move_check = HF.check_location(x1, y1, W, L)
            while move_check != "World Map" and error_int < 10:
                error_int += 1
                move_check = HF.check_location(x1, y1, W, L)
                time.sleep(0.5)
        elif where_am_I == "World Map" and location == "City":
            pass

#Events----------------------------------------------------------------
def go_to_events(x1, y1, W, L) -> None:
    
    """Opens the events UI then navigates over to the calendar as
    a starting position"""

    #city or map both have the events icon, so we will use the
    #default option here
    Navigate_to_cityormap(x1, y1, W, L)

    print("Opening Events UI")

    p.moveTo(x1 + W * rl.Events[0],
             y1 + L * rl.Events[1])
    p.click()
    time.sleep(1)

    #check if UI is in starting position: "Calendar" is visible
    #and in top left

    #swipe at the top
    #making this function dumb. just swipes a bunch until the scroller
    #is at the far left
    for i in range(5):
        HF.swipe(x1, y1, W, L, dir = "left", starting_y = 0.15)

    #check if UI is in starting position: "Calendar" is visible
    #and in top left

def event_return_to_start(x1, y1, W, L) -> None:
    for i in range(10):
        HF.swipe(x1, y1, W, L, dir = "left", starting_y = 0.15)

def find_event(x1, y1, W, L, path, message = "icon"):

    for i in range(10):

        icon = HF.check_image(x1, y1, W, L, path, message = message,
                              raise_error= False, itterator= 2)
        
        if icon:
            break

        HF.swipe(x1, y1, W, L, dir = "right", starting_y = 0.15, magnitude = 1,
                 manual_duration = 1)
        
        time.sleep(0.5)

    if icon:

        print(message + " found.")

        return(icon)
    else:

        print(message + " not found.")

        return(False)  

def Hero_Mission(x1, y1, W, L) -> None:
    go_to_events(x1, y1, W, L)

    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\"

    hero_mission_icon = "images_Events\\Hero_Mission_Blue.JPG"
    reaper_button_icon = "images_Events\\Hero_Mission_Button.JPG"

    Hero_Mission_loc = find_event(x1, y1, W, L, dir + hero_mission_icon)
    #need to wait on slider to finish slipping...
    

    p.click(Hero_Mission_loc)

    reaper_button = HF.check_image(x1, y1, W, L, dir + reaper_button_icon)

    p.click(reaper_button)

def Lucky_Wheel_Chip_Grab(x1, y1, W, L) -> None:
    """A chip is collectable once after reset at 24:00 UTC"""

    dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_Events\\"

    chip_collect = dir + "Spin_Wheel_readytocollect.JPG"

    #check if lucky wheel is active
    Wheel_path_2 = dir + "Spin_Wheel_blue_back.JPG"


    Wheel = find_event(x1, y1, W, L, Wheel_path_2, "Wheel Icon")

    
    if Wheel:

        p.click(Wheel)

        print("Wheel event found. Collecting Chip")

        Chip_collect_img = HF.check_image(x1, y1, W, L, chip_collect,
                                        message = "Chip collect")

        p.moveTo(Chip_collect_img)
        p.click()

        Free_Button_path = dir + "Spin_Wheel_Free_Button.JPG"

        Free_Button  = HF.check_image(x1, y1, W, L, Free_Button_path,
                                      message = "Free Button")
        
        p.moveTo(Free_Button)
        p.click()

        time.sleep(1)

        p.click()

        p.moveTo(x1 + W*rl.Universal_Menu_Backout_x, 
                    y1 + L*rl.Universal_Menu_Backout_y)
        p.click()
        
        print("Chip successfully collected")
    
    else:
        print("Wheel event not found. Ending function")

    event_return_to_start(x1, y1, W, L)
    
    #return events tab to starting position
    

    


#Events Navigation----------------------------------------------------    
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

    wait_time = Reader.time_reader(wait_time_text, screenshot_path)

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
        
        time_TL = HF.time_w_clock_loc(x1, y1, W, L, 12, -10)

        HF.screenshotter(x1, y1, W, L,
                         time_TL[0],
                         time_TL[1],
                         rl.March_time_x2,
                         rl.March_time_y2,
                         "March_time")
        
        my_march_time = Reader.text_reader_cv2("Screenshots\\March_time_temp.JPG", 1)

        my_march_time_seconds = Reader.time_reader(my_march_time, "Screenshots\\March_time_temp.JPG")

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
        print("map or city icon not found using back navigation")
        error_int = 0
        while Where_am_I == "Neither" and error_int <= 10:
            error_int += 1
            Universal_Backout(x1, y1, W, L)
            time.sleep(1)
            Where_am_I = HF.check_location(x1, y1, W, L)
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

    time.sleep(1)

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
            """assumption here is that no other marches have completed
            so there should only be one check on the screen at a time"""
            
            Lighthouse_confirm_and_Open(x1, y1, W, L)

            where_am_I = HF.check_location(x1, y1, W, L)
    
            if where_am_I == "World Map":
                print("encountered error involving city return bubble in Tent_journey")
                Lighthouse_confirm_and_Open(x1, y1, W, L)
            
            dir = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_lighthouse_misc\\"
            check = "lighthouse_event_completion.JPG"
            tent_checked = HF.check_image(x1, y1, W, L, dir + check,
                                        20, confidence = 0.9,
                                        message = "tent journey completion")
            
            Universal_Backout(x1, y1, W, L)

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
                                            confidence= 0.8)
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

       #check if lighthouse was successfully open:
       #crude solution: if still on worldmap, open lighthouse again

        where_am_I = HF.check_location(x1, y1, W, L)
    
        if where_am_I == "World Map":
            print("encountered error involving city return bubble within Nav function")
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
    
    if True:
        print("apples")

    if False:
        print("banana")


    
    
