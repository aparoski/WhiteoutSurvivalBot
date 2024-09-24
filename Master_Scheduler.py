import pandas as pd
import numpy as np
import time


import Window_Finder
import Reader
import Image_Rec
import Data
import Map_Interact

#temp for testing
import pyautogui as p
import Helper_Funcs as HF

polar_rally = "Polar_Rally"
beast_hunt = "Beast_Hunt"
Troop_Training = "Troop_Training" + "Troop_Type"
reaper = "reaper"

#polar Rally
#start with first function to iterate over each viewable window and send a rally march out
def send_march(accounts, type = "Polar") -> None:
    """iterates over Bluestack windows. sends a polar rally for each and
    assigns march time to teach window"""
    for app in accounts:
        
        x1, y1, x2, y2 = app.rectangle

        W, L = app.W_L

        #maybe have function to check for stamina?

        if type == "Polar":

            app.march_time = Map_Interact.polar_sender(x1, y1, W, L, account_polar_level_dict[app.name]) * 2
            
            #maybe keep? 
            app.polar_count += 1

            print(app.name, app.polar_count)

            app.rally_out = False

        elif type == "Beast":

            app.window_to_foreground()

            app.march_time = Map_Interact.Beast_Search(x1, y1, W, L, account_beast_level_dict[app.name]) * 2

            app.beast_count += 1

            print(app.name, app.beast_count)

            schedule.add(app.name, app.hwnd, beast_hunt, app.march_time, "s")

        elif type == "Reaper":

            #reducing delay slightly by amount of time it takes to
            #navigate through events interface (may need to make this value a variable...)
            app.march_time = Map_Interact.Reaper_Sender(x1, y1, W, L) * 2 - 18

            app.reaper_count += 1

            app.rally_out = False
        
#second function scans each window to determine when the rally has departed
#then adds the march time to the schedule
def check_all_rallies(accounts, type) -> None:
    for app in accounts:
        
        x1, y1, x2, y2 = app.rectangle

        W, L = app.W_L

        Rally_left = Map_Interact.check_rally_arrival(x1, y1, W, L)

        if type == "Polar":
            label = polar_rally
        if type == "Reaper":
            label = reaper

        if Rally_left and not app.rally_out:

            app.rally_out = True

            schedule.add(app.name, app.hwnd, label, app.march_time, "s")


#third function scans schedule for latest event and triggers related function
#this function will need to be expanded to deal with multiple event types
def schedule_check(accounts) -> None:

    latest_event = schedule.latest_event(True)

    if latest_event.shape[0] > 0:

        print(latest_event)

        #clear out the event so it does not trigger the check again

        schedule.df = schedule.df.drop(latest_event.index, axis = 0)

        for app in accounts:

            if latest_event["Window_Name"].iloc[0] == app.name:

        #polar rally logic
                if latest_event["Activity"].iloc[0] == polar_rally:
                    
                    #there is likely a better way by throwing the class
                    #itself into the dataframe? will mess around with that

                    send_march([app], type = "Polar")

                if latest_event["Activity"].iloc[0] == beast_hunt:

                    send_march([app], type = "Beast")

                if latest_event["Activity"].iloc[0] == reaper:

                    send_march([app], type = "Reaper")



        

#set the beast and polar counts

def Polar_Scheduler(accounts, limit = None, rally_type = "Polar") -> None:
#testing the polar scheduler 
    send_march(accounts, type = rally_type)

    time.sleep(0.5)

    error_int = 0


    #note failes to navigate to map when started within city 
    while error_int < 5000:

        #maybe keep to add limit to polar rallies? 
        if limit is None:
            pass
        elif len(accounts) > 0: 
            if rally_type == "Polar":
                accounts = [app for app in accounts if app.polar_count < limit]
            elif rally_type == "Reaper":
                accounts = [app for app in accounts if app.reaper_count < limit]

            if len(accounts) == 0:
                break
        else:
            break


        error_int += 1

        check_all_rallies(accounts, rally_type)

        schedule_check(accounts)

        time.sleep(1)

        if error_int % 15 == 0:
            print(schedule.df)

def Beast_Scheduler(accounts, limit = None):

    error_int = 0

    send_march(accounts, "Beast")

    #note failes to navigate to map when started within city 
    while error_int < 5000:

        if limit is None:
                pass
        elif len(accounts) > 0: 
            accounts = [app for app in accounts if app.beast_count < limit]

            if len(accounts) == 0:
                break
        else:
            break


        error_int += 1

        schedule_check(accounts)

        time.sleep(1)

        if error_int % 15 == 0:
            print(schedule.df)


if __name__ == '__main__':

    #Initialize Blue Stacks Windows. 
    # Tootie = "BlueStacks App Player"
    # Tootin = "BlueStacks App Player 1"
    # Tootily = "BlueStacks App Player 3"
    # Leg = "BlueStacks App Player 4"

    # schedule = Data.Window_Dataframe()

    

    # App = Window_Finder.BlueStack_Window(Tootie)
    # App1 = Window_Finder.BlueStack_Window(Tootin)
    # App3 = Window_Finder.BlueStack_Window(Tootily)
    # App4 = Window_Finder.BlueStack_Window(Leg)

    # #develop account config in the future which will contain these values
    # account_polar_level_dict = {Tootie : 7, Tootin : 5, Tootily : 4, Leg : 4}
    # account_beast_level_dict = {Tootie : 30, Tootin : 24, Tootily : 20, Leg : 20}

    # #in beginning we will need to instantiate the schedule
    # schedule = Data.Window_Dataframe()

    # active_windows = [App1, App4]  


    # polar = True

    # if polar == True:

    #     Polar_Scheduler(active_windows, 27)
    # else:

    #     Beast_Scheduler(active_windows, 22)

        






