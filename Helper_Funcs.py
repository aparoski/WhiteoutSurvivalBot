import pyautogui as p
p.useImageNotFoundException()
import time


#General Funcs -------------------------------------------------------

def relativexy (x1, y1, W, L, position):
    pos_x, pos_y = position

    x_distance = pos_x - x1
    y_distance = pos_y - y1

    rel_x = x_distance / W
    rel_y = y_distance / L

    return(rel_x, rel_y)

def screenshotter(x1, y1, W, L,
                  locx1,
                  locy1,
                  locx2,
                  locy2,
                  save_name) -> None:
    """Takes screenshot and saves named item to screenshot
    directory"""
    
    x1_temp = round(x1 + W * locx1)
    y1_temp = round(y1 + L * locy1)
    x2_temp = round(x1 + W * locx2)
    y2_temp = round(y1 + L * locy2)
    W_temp = x2_temp - x1_temp
    L_temp = y2_temp - y1_temp

    print(W_temp, L_temp)

    p.screenshot("Screenshots\\" + save_name + "_temp.JPG", 
                region = (x1_temp, y1_temp,
                        W_temp, L_temp))
    
def check_image(x1, y1, W, L, path, itterator = 10, 
                confidence = 0.7, message = "",
                raise_error = True):
    print("checking image")
    i = 0
    while True and i <= itterator:
        i += 1
        print(i)
        try:
            image_loc = p.locateCenterOnScreen(path,
                                               region = (x1, y1, W, L),
                                               confidence= confidence)
            break
        except:
            print(message + "Check " + str(i))
            time.sleep(1)
            pass

    if raise_error:

        if i >= itterator:
            raise("Function to check " + str(message) + " timed out")
        else:
            return(image_loc)
        
    else:
        if i >= itterator:
            return(False)
        else:
            return(image_loc)

def swipe(x1, y1, W, L, dir = "up", magnitude = 1,
          starting_x = 0.5, starting_y = 0.5) -> None:
    """direction refers to where the screen moves"""

    if (starting_y + starting_y * magnitude > 1 or
        starting_x + starting_x * magnitude > 1 or
        starting_x > 1 or starting_y > 1 or magnitude > 1):
        raise("starting value or magnitude inapprorpiate")

    duration = magnitude * 0.4 

    p.moveTo(x1 + W * starting_x,
             y1 + L * starting_y)
    p.mouseDown(button = "left")
    if dir == "up":
        #place cursor in center of screen and swipe up
        p.moveTo(x1 + W * starting_x,
                 y1 + L * (starting_y + starting_y * magnitude),
                 duration = duration)
    elif dir == "down":
        p.moveTo(x1 + W * starting_x,
                 y1 + L * (starting_y - starting_y * magnitude),
                 duration = duration)
    elif dir == "right":
        p.moveTo(x1 + W * (starting_x - starting_x * magnitude),
                 y1 + L * starting_y,
                 duration = duration)
    elif dir =="left":
        p.moveTo(x1 + W * (starting_x + starting_x * magnitude),
                 y1 + L * starting_y,
                 duration = duration)
    elif dir == "bottomleft":
        p.moveTo(x1 + W * (starting_x + starting_x * magnitude),
                 y1 + L * (starting_y - starting_y * magnitude),
                 duration = duration * 2)
    elif dir == "bottomright":
        p.moveTo(x1 + W * (starting_x - starting_x * magnitude),
                 y1 + L * (starting_y - starting_y * magnitude),
                 duration = duration * 2)
    elif dir == "topleft":
        p.moveTo(x1 + W * (starting_x + starting_x * magnitude),
                 y1 + L * (starting_y + starting_y * magnitude),
                 duration = duration * 2)
    elif dir == "topright":
        p.moveTo(x1 + W * (starting_x - starting_x * magnitude),
                 y1 + L * (starting_y + starting_y * magnitude),
                 duration = duration * 2)
    time.sleep(0.1)
    p.mouseUp(button = "left")

#General Funcs -------------------------------------------------------
#Helpful Whiteout Funcs----------------------------------------------
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
    
def check_victory(x1, y1, W, L):
    print("checking for victory text")
    check_victory = check_image(x1, y1, W, L, r"images/images_Events/misc/Victory_Screen.JPG",
                                 20, confidence = 0.7, 
                                 message = "Victory_Screen")
    
    if check_victory:
        return(1)
#Helpful Whiteout Funcs----------------------------------------------
    
