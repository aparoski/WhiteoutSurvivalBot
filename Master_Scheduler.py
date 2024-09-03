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

#Initialize Blue Stacks Windows. 
Tootie = "BlueStacks App Player"
Tootin = "BlueStacks App Player 1"
Tootily = "BlueStacks App Player 3"
Leg = "BlueStacks App Player 4"

schedule = Data.Window_Dataframe()

polar_rally = "Polar_Rally"
beast_hunt = "Beast_Hunt"
Troop_Training = "Troop_Training" + "Troop_Type"

beast_count = 0

App = Window_Finder.BlueStack_Window(Tootie)
App1 = Window_Finder.BlueStack_Window(Tootin)
App3 = Window_Finder.BlueStack_Window(Tootily)
App4 = Window_Finder.BlueStack_Window(Leg)

Windows_in_view = [App, App1, App3]

#develop account config in the future which will contain these values
account_polar_level_dict = {Tootie : 6, Tootin : 4, Tootily : 3, Leg : 3}

#in beginning we will need to instantiate the schedule
schedule = Data.Window_Dataframe()

#polar Rally
#start with first function to iterate over each viewable window and send a rally march out
def send_polars(accounts) -> None:
    """iterates over Bluestack windows. sends a polar rally for each and
    assigns march time to teach window"""
    for app in accounts:
        
        x1, y1, x2, y2 = app.rectangle

        W, L = app.W_L

        #maybe have function to check for stamina?

        app.march_time = Map_Interact.polar_sender(x1, y1, W, L, account_polar_level_dict[app.name]) * 2

        
#second function scans each window to determine when the rally has departed
#then adds the march time to the schedule
def check_all_rallies(accounts) -> None:
    for app in accounts:
        
        x1, y1, x2, y2 = app.rectangle

        W, L = app.W_L

        Rally_left = Map_Interact.check_rally_arrival(x1, y1, W, L)

        if Rally_left:

            schedule.add(app.name, app.hwnd, polar_rally, app.march_time, "s")


#third function scans schedule for latest event and triggers related function
#this function will need to be expanded to deal with multiple event types
def schedule_check(accounts) -> None:

    latest_event = schedule.latest_event()

    if latest_event.shape[0] > 0:

        print(latest_event)

        #polar rally logic
        if latest_event["Activity"].iloc[0] == polar_rally:
            
            #there is likely a better way by throwing the class
            #itself into the dataframe? will mess around with that
            for app in accounts:
                if latest_event["Window_Name"].iloc[0] == app.name:

                    send_polars([app])


        #clear out the event so it does not trigger the check again
        schedule.df = schedule.df.drop(latest_event.index, axis = 0)

#testing the polar scheduler 
send_polars(Windows_in_view)

time.sleep(0.5)

error_int = 0

while error_int < 5000:

    error_int += 1

    check_all_rallies(Windows_in_view)

    schedule_check(Windows_in_view)

    time.sleep(1)

    if error_int % 30 == 0:
        print(schedule.df)


                    




        






