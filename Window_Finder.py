import win32gui as w
import Helper_Funcs as HF
import os

#testing
import Image_Rec
import relative_locations as rel
import time
import pyautogui as p
import pandas as pd
from datetime import datetime as dt
import Map_Interact
import Data



#current_windows = Data.Bluestack_window_return()


class BlueStack_Window:

    def __init__(self, order):

        #remove this later
        self.polar_count = 0

        self.reaper_count = 0

        self.beast_count = 0

        self.march_time = None

        self.order = order

        self.rally_out = False
         
        def single_window_return(order):

            def enumHandler(hwnd, list):
                if ("BlueStacks App Player 1" == w.GetWindowText(hwnd) and
                order == "BlueStacks App Player 1"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 1])
                elif ("BlueStacks App Player 3" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 3"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 2])
                elif ("BlueStacks App Player 4" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player 4"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 3])
                elif ("BlueStacks App Player" == w.GetWindowText(hwnd)and
                      order == "BlueStacks App Player"):

                    
                    list.append([hwnd, w.GetWindowText(hwnd), w.GetWindowRect(hwnd), 0])

            window_list = []
            w.EnumWindows(enumHandler, window_list)

            for i in window_list:
                print(i[1])

            return(window_list[0][0])
        
        window_hwnd = single_window_return(order)
        
        temp_rect = w.GetWindowRect(window_hwnd)

        #commented out for testing. remove after confirm
        # def Window_lw(x1, y1, x2, y2):
        #     """finds the length and width of a rectangular
        #     box between two coordinates if the coordinates are
        #     located at the top left and bottom right corners of the rectangle"""

        #     l = y2 - y1
        #     w = x2 - x1

        #     return(w, l)
        
        x1, y1, x2, y2 = temp_rect

        temp_W_L = HF.Window_lw(x1, y1, x2, y2)

        w.MoveWindow(window_hwnd, x1, y1, 550, 951, True)

        self.rectangle = w.GetWindowRect(window_hwnd)

        x1, y1, x2, y2 = self.rectangle

        self.W_L = HF.Window_lw(x1, y1, x2, y2)

        self.hwnd = window_hwnd

        self.name =  w.GetWindowText(window_hwnd)

        

        path = os.path.dirname(__file__) + "Account_Config.csv"

        if os.path.isfile(path):

            config = pd.read_csv(path)

        else:

            raise("Account_Config file not found")
        
        self.config = config[config["Window_Name"] == self.name]




    def window_to_foreground(self):
        w.SetForegroundWindow(self.hwnd)

    def Open_Lighthouse(self) -> None:
        Image_Rec.Lighthouse_confirm_and_Open(self.rectangle[0],
                                              self.rectangle[1],
                                              self.W_L[0],
                                              self.W_L[1])
    
    
    def Lighthouse_Operation(self):

        march_time = Image_Rec.light_house_icon_Navigator(self.rectangle[0],
                                                    self.rectangle[1],
                                                    self.W_L[0],
                                                    self.W_L[1])
        return(march_time)
    
    #events functions need to be wrapped into something neater
    #current form is for testing
    def open_events(self):
        Image_Rec.go_to_events(self.rectangle[0],
                             self.rectangle[1],
                             self.W_L[0],
                             self.W_L[1])
        
    def lucky_wheel_chip_grab(self):
        Image_Rec.Lucky_Wheel_Chip_Grab(self.rectangle[0],
                                        self.rectangle[1],
                                        self.W_L[0],
                                        self.W_L[1])
        

    #temp set up for testing
    def backout(self):
        Image_Rec.Universal_Backout(self.rectangle[0],
                                    self.rectangle[1],
                                    self.W_L[0],
                                    self.W_L[1])

        
    
    def swipe(self, dir = "up", magnitude = 1, 
              starting_x = 0.5, starting_y = 0.5):
        
        HF.swipe(self.rectangle[0],
                 self.rectangle[1],
                 self.W_L[0],
                 self.W_L[1],
                 dir,
                 magnitude,
                 starting_x, starting_y)
        
    def vid(self):

        HF.stop_video_recording(self.rectangle[0],
                                self.rectangle[1],
                                self.W_L[0],
                                self.W_L[1])

if __name__ == '__main__':

    App = BlueStack_Window(order = "BlueStacks App Player")
    App_1 = BlueStack_Window(order = "BlueStacks App Player 1")
    App_3 = BlueStack_Window(order = "BlueStacks App Player 3")
    App_4 = BlueStack_Window(order = "BlueStacks App Player 4")

    schedule = Data.Window_Dataframe()


    x1, y1, x2, y2 = App.rectangle

    W, L = App.W_L

    my_time = Image_Rec.Preset_March_Sender(x1, y1, W, L, 1)

    print(my_time)
    

    




